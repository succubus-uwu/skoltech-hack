from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier

class Validator:
    def __init__(self, init_df_osm: pd.DataFrame):
        X_train, X_valid, y_train, y_valid = train_test_split(init_df_osm['value'], init_df_osm['addr'], test_size=0.1, random_state=42)
        X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.3, random_state=42)

        # print(f"{len(X_train) = }")
        # print(f"{len(X_test) = }")
        # print(f"{len(X_valid) = }")

        self.sgd_ppl_clf = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('sgd_clf', SGDClassifier(random_state=42))])

        self.sgd_ppl_clf.fit(X_train, y_train)

    def predict(self, text: str):
        return self.sgd_ppl_clf.predict([text])

# if __name__ == '__main__':
#     df_osm = pd.read_csv('/Users/luzin/PycharmProjects/skoltech-hack/model/data/test.csv')
#
#     val = Validator(df_osm)
#
#     print(val.predict("ясногорский улица"))
