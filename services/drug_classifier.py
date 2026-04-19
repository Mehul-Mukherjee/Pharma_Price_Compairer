class DrugClassifier:
    def is_generic(self, name: str):
        generic_indicators = ["tablet", "capsule", "mg", "ml"]
        return any(x in name.lower() for x in generic_indicators)

    def classify(self, name: str):
        return "generic" if self.is_generic(name) else "brand"