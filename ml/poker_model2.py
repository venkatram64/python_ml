import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer


features = ['card1 suit', 'card1 rank', 'card2 suit', 'card2 rank', 'card3 suit', 'card3 rank', 'card4 suit',\
            'card4 rank','card5 suit', 'card5 rank','poker hand']

train_data = pd.read_csv("poker_hand_train.csv", names=features)
test_data = pd.read_csv("poker_hand_train.csv", names=features)


data = pd.concat([train_data, test_data])

print(data)

categoryVarLabelList = ['card1 suit', 'card1 rank', 'card2 suit', 'card2 rank', 'card3 suit', 'card3 rank',
                        'card4 suit', 'card4 rank', 'card5 suit', 'card5 rank']

for var in categoryVarLabelList:
    data[var] = data[var].astype('float64')


imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputedData = imp.fit_transform(data)

clusters = range(1,11)
meandist = []

for k in clusters:
    model=KMeans(n_clusters=k)
    model.fit(imputedData)
    clusassign = model.predict(imputedData)
    meandist.append(sum(np.min(cdist(imputedData, model.cluster_centers_,'euclidean'), axis=1))/imputedData.shape[0])


plt.plot(clusters, meandist)
plt.xlabel('Number of clusters')
plt.ylabel('Average distance')
plt.title("Selcting k with elbow method")

mode2Clusters=KMeans(n_clusters=2)
mode2Clusters.fit(imputedData)
preds = mode2Clusters.predict(imputedData)

pca_2 = PCA(2)
plot_columns = pca_2.fit_transform(imputedData)
plt.scatter(x=plot_columns[:, 0], y=plot_columns[: ,1], c=mode2Clusters.labels_,)
plt.xlabel('Canonical varibale 1')
plt.ylabel('Canonical varibale 2')
plt.title("Scatterplot of Canonical varibales for 2 clusters")
plt.show()