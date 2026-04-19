from fastapi import FastAPI
from services.data_loader import DataLoader
from services.vector_store import VectorStore
from services.ai_agent import PharmaAgent
import os
import traceback

app = FastAPI()

# =========================
# LOAD DATA
# =========================
loader = DataLoader()
df = loader.load()

print("COLUMNS:", df.columns)

# =========================
# VECTOR STORE
# =========================
vs = VectorStore()
vs.build(df, text_column="text_for_embedding")

# =========================
# AI AGENT (lazy)
# =========================
agent = None

@app.on_event("startup")
def startup():
    global agent
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY missing")
    agent = PharmaAgent(vs)

# =========================
# ROUTES
# =========================
@app.get("/")
def home():
    return {"status": "Pharma AI running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/chat")
def chat(q: str):
    try:
        result = agent.explain(q)
        return {"response": result}
    except Exception as e:
        return {
            "error": str(e),
            "trace": traceback.format_exc()
        }