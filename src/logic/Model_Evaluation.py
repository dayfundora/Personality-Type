import pandas as panda
import numpy as np
from Datas_for_train import DataPrep
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge, SGDRegressor
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import cross_validate
from sklearn.metrics import f1_score, mean_squared_error
from sklearn.model_selection import GridSearchCV
from liwc_vectorizer import LIWCVectorizer
import warnings
warnings.filterwarnings("ignore")

class Model_Evaluation():
    def __init__(self, X, Y, trait):
        self.X = X
        self.Y = Y
        self.trait = trait
        self.model_dic = {
            'LogisticRegression': LogisticRegression(),
            'RandomForestClassifier': RandomForestClassifier(max_features='sqrt', n_estimators=110),
            'MultinomialNB': MultinomialNB(),
            'GradientBoostingClassifier': GradientBoostingClassifier(),
            'SVC': SVC(),
            'LinearRegression': LinearRegression(),
            'RandomForestRegressor' : RandomForestRegressor(
                 bootstrap=True,
                 # max_depth=50,
                 max_features='sqrt',
                 min_samples_leaf=1,
                 min_samples_split=2,
                 n_estimators= 200),
            'Ridge': Ridge(),
            'SGDRegressor': SGDRegressor(),
        }
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, Y, test_size=0.34, random_state=32)

        self.models = [
            ('LogisticRegression', False), 
            ('RandomForestClassifier', False), 
            ('MultinomialNB',False), 
            ('GradientBoostingClassifier',False), 
            ('SVC', False), ('LinearRegression', True), 
            ('RandomForestRegressor', True), 
            ('Ridge', True), 
            ('SGDRegressor', True)
            ]
    
    def compare_scores(self, save):
        
        accuracy_scores = []
        f1_scores = []

        for model_name, regression in self.models:
            model = self.model_dic[model_name]
            model.fit(self.X_train, self.y_train)

            if regression:
                y_pred = model.predict(self.X_test)
                y_true = self.y_test
                mse = -np.mean(cross_validate(model, self.X_test, self.y_test, scoring='neg_mean_squared_error', cv=10)['test_score'])
            else:
                accuracy_score = np.mean(cross_validate(model, self.X_test, self.y_test, cv=10)['test_score'])
                accuracy_scores.append(accuracy_score)

                f_score = np.mean(cross_validate(model, self.X_test, self.y_test, scoring='f1', cv=10)['test_score'])
                f1_scores.append(f_score)

        best_accuracy_score = max(accuracy_scores)
        best_accuracy_model, d = self.models[accuracy_scores.index(best_accuracy_score)]

def prep_data(trait,dp, regression=False, model_comparison=False):
        df_status = dp.extract_text_from_corpus()
        X = df_status['STATUS']

        if regression:
            y_column = dp.trait_score_dict[trait]
        else:
            y_column = dp.trait_cat_dict[trait]
            
        y = df_status[y_column]

        return X, y

def extract_vectorized_elements(dp, tfidf_features= False):
    
    corpus = dp.extract_text_from_corpus()['STATUS']

    mx = None
    features = None
    xlabel = None

    if tfidf_features:
        tfidf = TfidfVectorizer(stop_words='english', strip_accents='ascii')
        mx = tfidf.fit_transform(corpus).toarray()
        features = tfidf.get_feature_names()
        xlabel = 'Tfidf_features'
    else:
        liwc = LIWCVectorizer()
        mx = liwc.vectorize_docs(corpus)
        features = liwc.features
        xlabel = 'LIWC_features'

    return mx, features, xlabel

