import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os
import pickle


class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.texts = []

    def build(self, df, text_column):
        os.makedirs("data", exist_ok=True)

        # ✅ load existing index safely
        if os.path.exists("data/faiss.index") and os.path.exists("data/meta.pkl"):
            print("✅ Loading FAISS index from disk...")

            self.index = faiss.read_index("data/faiss.index")

            with open("data/meta.pkl", "rb") as f:
                data = pickle.load(f)

            # ✅ FIX: backward compatibility
            if isinstance(data, dict):
                self.texts = data.get("texts", [])
            else:
                self.texts = data  # old format fallback (list)

            return

        print("🚀 Creating embeddings (ONE TIME ONLY)...")

        df = df.reset_index(drop=True)

        self.texts = df[text_column].fillna("").astype(str).tolist()

        embeddings = self.model.encode(self.texts, show_progress_bar=True)
        embeddings = np.array(embeddings).astype("float32")

        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)

        print("💾 Saving FAISS index + metadata...")

        faiss.write_index(self.index, "data/faiss.index")

        # ✅ ALWAYS save as dict (future-proof)
        with open("data/meta.pkl", "wb") as f:
            pickle.dump({
                "texts": self.texts
            }, f)

    def search(self, query, k=5):
        if self.index is None:
            raise ValueError("FAISS index not loaded. Run build() first.")

        query_vec = self.model.encode([query])
        query_vec = np.array(query_vec).astype("float32")

        D, I = self.index.search(query_vec, k)

        results = []

        for idx in I[0]:
            if idx < 0:
                continue

            try:
                results.append(str(self.texts[idx]))
            except Exception:
                continue

        return results