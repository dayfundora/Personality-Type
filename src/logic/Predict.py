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

