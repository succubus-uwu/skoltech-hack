from sklearn.model_selection import train_test_split
import pandas as pd

df_osm = pd.read_csv('/Users/luzin/PycharmProjects/skoltech-hack/model/data/buildings_addr_list_drop_trash_2.csv')

print(list(set(df_osm["addr"].to_list())))
print(df_osm)

X_train, X_valid, y_train, y_valid = train_test_split(df_osm['value'], df_osm['addr'], test_size=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.3, random_state=42)

print(f"{len(X_train) = }")
print(f"{len(X_test) = }")
print(f"{len(X_valid) = }")

from sklearn.pipeline import Pipeline
# pipeline позволяет объединить в один блок трансформер и модель, что упрощает написание кода и улучшает его читаемость
from sklearn.feature_extraction.text import TfidfVectorizer
# TfidfVectorizer преобразует тексты в числовые вектора, отражающие важность использования каждого слова из некоторого набора слов (количество слов набора определяет размерность вектора) в каждом тексте
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
# линейный классификатор и классификатор методом ближайших соседей
from sklearn import metrics
# набор метрик для оценки качества модели
from sklearn.model_selection import GridSearchCV
# модуль поиска по сетке параметров

sgd_ppl_clf = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('sgd_clf', SGDClassifier(random_state=42))])
knb_ppl_clf = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('knb_clf', KNeighborsClassifier(n_neighbors=10))])
sgd_ppl_clf.fit(X_train, y_train)
knb_ppl_clf.fit(X_train, y_train)

X_test = ["БЦ Вивальди Плаза Летниковская улица, 2 ст1 1 этаж"]
predicted_sgd = sgd_ppl_clf.predict(X_test)
print(predicted_sgd)
# print(metrics.classification_report(predicted_sgd, y_test))

predicted_knb = knb_ppl_clf.predict(X_test)
print(predicted_knb)
# print(metrics.classification_report(predicted_knb, y_test))
