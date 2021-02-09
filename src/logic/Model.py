import pickle
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from .Datas_for_train import DataPrep
from sklearn.feature_extraction.text import TfidfVectorizer
from .liwc_vectorizer import LIWCVectorizer

class Model():
    def __init__(self, type='tfidf'):
        self.rfr = RandomForestRegressor(bootstrap=True,
         max_features='sqrt',
         min_samples_leaf=1,
         min_samples_split=2,
         n_estimators= 200)
        self.type = type         
        self.rfc = RandomForestClassifier(max_features='sqrt', n_estimators=110)
        self.tfidf = TfidfVectorizer(stop_words='english', strip_accents='ascii')
        self.liwc = LIWCVectorizer()

    def fit(self, X, y, regression=True):
        X = self.tfidf.fit_transform(X)

        self.rfc = self.rfc.fit(X, y)

    def predict(self, X, regression=True):
        X = self.tfidf.transform(X)

        return self.rfr.predict(X)
