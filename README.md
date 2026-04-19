# 💊 Pharma Price Comparator AI

An AI-powered **medicine price comparison system** that helps users find the cheapest and most suitable medicine based on composition, dosage, and pricing using **semantic search (FAISS) + LLM reasoning (Groq)**.

---

## 🚀 Features

- 🔍 Smart medicine search (e.g., “Dolo 650 vs Calpol 650”)
- 📊 Price comparison across brands
- 🧠 Semantic search using SentenceTransformers + FAISS
- 🤖 AI-generated explanations using Groq LLM
- ⚡ FastAPI backend
- 🖥️ Streamlit interactive dashboard
- 📦 Scales to 300K+ medicine records

---

## 📊 Dataset

This project uses the following dataset:

📦 **India Medicines and Drug Info Dataset**  
🔗 https://www.kaggle.com/datasets/apkaayush/india-medicines-and-drug-info-dataset

📜 License: **CC BY-NC-SA 4.0 (Creative Commons Attribution Non-Commercial ShareAlike 4.0)**

> ⚠️ This dataset is used strictly for educational and non-commercial purposes in accordance with its license.

---

## 🧠 System Architecture


User (Streamlit UI)
↓
FastAPI Backend (/chat endpoint)
↓
FAISS Vector Search (SentenceTransformers embeddings)
↓
Relevant medicine records retrieval
↓
Groq LLM reasoning layer
↓
Final structured response


---

## 🛠️ Tech Stack

- Python 3.11+
- FastAPI
- Streamlit
- FAISS
- SentenceTransformers (MiniLM)
- Groq API
- Pandas / NumPy

---

## 📦 Installation

### 1. Clone repository
```bash
git clone git@github.com:Mehul-Mukherjee/Pharma_Price_Compairer.git
cd Pharma_Price_Compairer
2. Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
3. Install dependencies
pip install -r requirements.txt
4. Set environment variables

Create .env file (DO NOT COMMIT):

GROQ_API_KEY=your_key_here

Or export:

export GROQ_API_KEY="your_key_here"
🚀 Run the Project
Start Backend (FastAPI)
PYTHONPATH=. uvicorn app.main:app --reload --port 8000

Backend:

http://127.0.0.1:8000
Start Frontend (Streamlit)
PYTHONPATH=. streamlit run dashboard/app.py --server.port 8502

Frontend:

http://localhost:8502
🧪 Example Queries
dolo 650
dolo 650 vs calpol 650
paracetamol cheapest alternative
ibuprofen vs paracetamol
⚙️ Key Fixes Implemented
🧠 Vector Search Fixes
Fixed FAISS index mismatch errors
Fixed Pandas indexing (KeyError issues)
Standardized metadata storage format
⚡ Performance Improvements
One-time embedding generation
Persistent FAISS index storage
Cached dataset loading
🤖 LLM Fixes
Updated deprecated Groq models
Fixed model decommission errors
Improved response formatting
🖥️ UI Fixes
Resolved Streamlit port conflicts
Clean backend/frontend separation
🔐 Security & GitHub Safety

This repository follows secure publishing practices:

❌ NOT included:
.env (API keys)
FAISS index files (faiss.index)
pickle metadata (meta.pkl)
any secrets or credentials
✅ Included:
Source code
Architecture
Dataset loader logic
Documentation
📁 Project Structure
Pharma_Price_Compairer/
│
├── app/
├── services/
├── dashboard/
├── utils/
├── models/
├── data/ (ignored in git)
├── requirements.txt
├── README.md
└── .gitignore
🚧 Future Improvements
Dosage-aware comparison engine
Price-per-mg normalization
Drug safety scoring system
Mobile UI version
Cloud deployment (Render / AWS / HF Spaces)
📜 License

MIT License (Project Code)

Dataset: CC BY-NC-SA 4.0 (Kaggle dataset license applies)

👨‍💻 Author

Mehul Mukherjee

⭐ If you like this project, give it a star on GitHub.