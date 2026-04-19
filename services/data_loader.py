import pandas as pd
import os

class DataLoader:
    def __init__(self, path="data/India Medicines and Drug Info Dataset.csv"):
        self.path = path
        self.cache_path = "data/processed.parquet"

    def load(self):
        if os.path.exists(self.cache_path):
            print("Loading cached dataset...")
            df = pd.read_parquet(self.cache_path)
        else:
            print("Loading raw CSV dataset...")
            df = pd.read_csv(self.path)

        # 🔥 CRITICAL FIX (DO THIS ALWAYS)
        df.columns = df.columns.str.strip().str.lower()

        print("COLUMNS:", df.columns)

        # 🔥 SAFE TEXT BUILD (NO CRASH EVER)
        def safe(col):
            return df[col].astype(str) if col in df.columns else ""

        df["text_for_embedding"] = (
            safe("medicine name") + " | " +
            safe("composition") + " | " +
            safe("product name")
        )

        # cache only after clean
        df.to_parquet(self.cache_path, index=False)

        return df