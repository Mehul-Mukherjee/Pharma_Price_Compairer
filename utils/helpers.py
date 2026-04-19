import pandas as pd
import re

def normalize_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    return re.sub(r"\s+", " ", text.lower()).strip()


def load_csv(path: str):
    return pd.read_csv(path)


def extract_composition(text: str):
    # simple heuristic (you can improve later with NLP)
    return normalize_text(text)