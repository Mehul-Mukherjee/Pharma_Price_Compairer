class PriceEngine:
    def __init__(self, df):
        self.df = df

    def search_by_name(self, query):
        return self.df[self.df["name_norm"].str.contains(query.lower(), na=False)]

    def find_cheapest_alternatives(self, composition):
        return self.df[self.df["composition_norm"].str.contains(composition.lower(), na=False)] \
            .sort_values("price")