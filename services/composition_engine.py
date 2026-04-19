import re

class CompositionEngine:
    def extract(self, text):
        if not isinstance(text, str):
            return ""

        text = text.lower()

        # basic pharma pattern extraction (expandable)
        patterns = [
            r"\d+\s?mg",
            r"\d+\s?ml",
            r"\d+\s?mcg",
            r"[a-z]+(?:ine|ol|cin|mycin|pril|sartan)"
        ]

        matches = []
        for p in patterns:
            matches += re.findall(p, text)

        return " ".join(set(matches))