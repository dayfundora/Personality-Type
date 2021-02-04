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

def prep_data(trait,dp, regression=False, model_comparison=False):
        df_status = dp.extract_text_from_corpus()
        X = df_status['STATUS']

        if regression:
            y_column = dp.trait_score_dict[trait]
        else:
            y_column = dp.trait_cat_dict[trait]
            
        y = df_status[y_column]

        return X, y
