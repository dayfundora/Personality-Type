from .Model import Model, train_models
import pickle
import numpy as np
import os, sys

class Predictor():
    def __init__(self, vetorice='tfidf'):
        self.traits = ['OPN', 'CON', 'EXT', 'AGR', 'NEU']
        self.models = {}
        self.modelsreg = {}
        self.vetorice = vetorice        
        self.load_models()
        self.dicname = {'sOPN': " Score de Apertura ", 'cOPN': " Clasification de Apertura ", 'sCON': " Score de Conciencia ", 'cCON': " Clasification de Conciencia ", 
        'sEXT': " Score de Extraverión ", 'cEXT': " Clasification de Extraverión ", 'sAGR': " Score de Amabilidad ", 'cAGR': " Clasification de Amabilidad ", 
        'sNEU': " Score de Neurotimos ", 'cNEU': " Clasification de Neurotismo "

        }

    def load_models(self):
        r = ['categorical', 'regression']
        #M = Model(vetorice)
        #train_models(vetorice)
        for trait in self.traits:
            #for type_ in r:
                #SITE_ROOT = os.path.dirname(__file__)
                #filename = os.path.join(SITE_ROOT,'models/{1}_{0}_model_liwc.pkl'.format(type_, trait))
                #sys.path.append(r'filename')
            with open('logic/models/{1}_categorical_model_{0}.pkl'.format(self.vetorice, trait), 'rb') as f:
                self.models[trait] = pickle.load(f)
