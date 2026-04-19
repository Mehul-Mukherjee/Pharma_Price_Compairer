# 💊 Pharma Price Comparator AI

An AI-powered **medicine price comparison system** that helps users find the cheapest and most suitable medicine based on composition, dosage, and pricing using **semantic search (FAISS) + LLM reasoning (Groq)**.

---

## 🚀 Features

- 🔍 Smart medicine search (e.g., *“Dolo 650 vs Calpol 650”*)
- 📊 Price comparison across brands
- 🧠 Semantic search using SentenceTransformers + FAISS
- 🤖 AI-generated explanations using Groq LLM
- ⚡ Fast API backend (FastAPI)
- 🖥️ Interactive UI (Streamlit dashboard)
- 📦 Large-scale dataset support (300K+ records)

---

## 🧠 System Architecture


User (Streamlit UI)
↓
FastAPI Backend (/chat endpoint)
↓
Vector Search (FAISS + SentenceTransformer)
↓
Relevant medicine data retrieval
↓
Groq LLM (analysis + explanation)
↓
Final structured response


---

## 🛠️ Tech Stack

- Python 3.11+
- FastAPI
- Streamlit
- FAISS (Facebook AI Similarity Search)
- SentenceTransformers (MiniLM model)
- Groq API (LLM inference)
- Pandas / NumPy

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pharma-price-comparator.git
cd Pharma_Price_Compairer
2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
# venv\Scripts\activate    # Windows
3. Install dependencies
pip install -r requirements.txt
4. Set environment variables

Create a .env file (DO NOT PUSH THIS TO GITHUB):

GROQ_API_KEY=your_groq_api_key_here

Or export directly:

export GROQ_API_KEY="your_key"
🚀 Run the Project
Step 1 — Start Backend (FastAPI)
PYTHONPATH=. uvicorn app.main:app --reload --port 8000

Backend runs at:

http://127.0.0.1:8000
Step 2 — Start Frontend (Streamlit)
PYTHONPATH=. streamlit run dashboard/app.py --server.port 8502

Frontend runs at:

http://localhost:8502
🧪 Example Queries

Try:

dolo 650
dolo 650 vs calpol 650
paracetamol 650 cheapest
ibuprofen vs paracetamol
⚙️ Key Improvements Made

This project went through several critical fixes:

🧠 Vector Store Fixes
Fixed FAISS index mismatch issues
Resolved Pandas indexing errors (KeyError)
Standardized metadata storage format
Added safe fallback handling for old cache files
⚡ Performance Fixes
Optimized embedding generation (one-time build)
Added FAISS persistent storage
Prevented re-embedding on every restart
🤖 AI Agent Fixes
Updated Groq model (removed deprecated models)
Fixed API errors due to decommissioned LLMs
Improved response structure for medicine comparison
🖥️ UI Fixes
Streamlit port conflict resolution
Stable backend/frontend separation
🔐 Security & GitHub Safety

This repository follows safe publishing practices:

❌ NOT included in repo:
.env (API keys protected)
data/faiss.index (optional large file exclusion if needed)
data/meta.pkl (can be regenerated)
personal keys or secrets
✅ Safe to include:
Codebase
Requirements
Dataset loader (if public-safe)
Model architecture
📁 Project Structure
Pharma_Price_Compairer/
│
├── app/
│   └── main.py
│
├── services/
│   ├── ai_agent.py
│   ├── vector_store.py
│   └── data_loader.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── (FAISS index + metadata - optional)
│
├── requirements.txt
├── README.md
└── .gitignore
🚧 Future Improvements
🔬 Dosage-aware comparison engine
💰 Price-per-mg normalization
🏥 Drug safety scoring system
📱 Mobile UI version
☁️ Deployment (AWS / Render / HuggingFace Spaces) 

📜 License

MIT License

👨‍💻 Author

Mehul Mukherjee

⭐ If you like this project

Give it a ⭐ on GitHub and contribute improvements!


---

