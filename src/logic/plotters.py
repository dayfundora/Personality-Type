import pandas as pd
import time, os
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import learning_curve


def show(data, foobar, feature_id=None, verbose=0, solid=False, random_seed=43):
    """
    Show clusters of data using john as clusterer algorithm.
    """
    samples, features = data.shape
    
    if feature_id is None:
        feature_id = [i for i in range(features)]
        
    features = len(feature_id)
    
    clusterid = foobar.fit_predict(data)
    
    clusters = max(clusterid) + 1
    
    np.random.seed(43)
    colors = [ [np.random.random() for _ in range(3)]  for f in range(clusters)]
    colors.append("white") # Color -1
    
    if verbose >= 1:
        print("Samples:", samples)
        print("Features:", features)
        print("Clusters:", clusters)

    for i in range(features):
        for j in range(i + 1, features):
            fi, fj = feature_id[i], feature_id[j]
            for col in range(-1, clusters):
                value = data[clusterid==col]

                plt.subplot(features - 1,features - 1, i * (features-1) + j)


                
                if solid:
                    kwargs = {'color' : colors[col]}
                else:
                    kwargs = {'facecolor' : colors[col]}
                
                plt.scatter(value[:,fi], value[:,fj], **kwargs)     
    plt.show()

def plot_to2(X, y):
    to_plot = PCA(2).fit_transform(X)

    plt.scatter(to_plot[:,0], to_plot[:,1], c=y, cmap=plt.cm.Paired)
    plt.title('Actual labels')
    plt.show()