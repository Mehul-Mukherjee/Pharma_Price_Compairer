import streamlit as st
import requests

st.set_page_config(page_title="Pharma AI", layout="wide")

st.title("💊 Pharma Price Comparator AI")

# =========================
# INPUT
# =========================
query = st.text_input("Search medicine (e.g., dolo 650)")

# =========================
# BUTTON
# =========================
if st.button("Search"):

    if not query:
        st.warning("Please enter a medicine name")
    else:
        try:
            res = requests.get(
                "http://127.0.0.1:8000/chat",
                params={"q": query}
            )

            data = res.json()

            if "response" in data:
                st.markdown("### 🧠 AI Response")
                st.write(data["response"])
            else:
                st.error(data)

        except Exception as e:
            st.error(f"Error: {e}")