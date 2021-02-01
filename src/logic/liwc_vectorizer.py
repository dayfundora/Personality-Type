from liwc.liwc import Liwc
import pandas as pd
import time 

class LIWCVectorizer:
    def __init__(self):
        self.liwc = Liwc('logic/data/LIWC2007_English100131.dic')
        self.features = list(self.liwc.categories.values())
        self.featuresidx = dict([(f,i) for i,f in enumerate(self.features)])

    def vectorize(self, doc):
        doc = doc.lower().split(' ')
        parse = self.liwc.parse(doc)
        vector = [0]*len(self.features)
        for v in parse:
            vector[self.featuresidx[v]] = parse[v]/len(doc)
            #print('feature = {0}   value = {1}'.format(v,vector[self.featuresidx[v]]))
        return vector

