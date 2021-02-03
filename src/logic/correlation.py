from Datas_for_train import DataPrep
from sklearn.feature_extraction.text import TfidfVectorizer
from liwc_vectorizer import LIWCVectorizer
from scipy.sparse.csr import csr_matrix
from scipy.stats import spearmanr, pearsonr
import matplotlib.pyplot as plt
import time, numpy
import pandas as pd
from info_gain import info_gain
from utils import write_to_xlsx

traits = ['OPN', 'CON', 'EXT', 'AGR', 'NEU']
dp = DataPrep()


def extract_vectorized_elements(tfidf_features):
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

