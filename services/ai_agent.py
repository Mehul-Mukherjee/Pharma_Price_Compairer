from groq import Groq
import os

class PharmaAgent:
    def __init__(self, vector_store):
        self.vs = vector_store

        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("Missing GROQ_API_KEY in environment")

        self.client = Groq(api_key=api_key)

    def explain(self, query: str):
        # 🔍 get similar medicines
        docs = self.vs.search(query, k=5)

        # ✅ ensure proper formatting
        formatted_docs = []
        for d in docs:
            if isinstance(d, dict):
                formatted_docs.append(
                    f"{d.get('product name', '')} | {d.get('composition', '')} | ₹{d.get('price', '')}"
                )
            else:
                formatted_docs.append(str(d))

        context = "\n".join(formatted_docs)

        # 🤖 call LLM
        response = self.client.chat.completions.create(
           model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a pharma expert helping compare medicines."},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content.strip()