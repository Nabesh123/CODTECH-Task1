import pandas as pd
data = pd.read_csv('/content/Mall_Customers.csv')
data.head()
data.tail()
data.shape
print("number of row ",data.shape[0])
print("number of columns",data.shape[1])
data.info()
data.isnull().sum()
data.describe()
data.columns
x=data[['Annual Income (k$)', 'Spending Score (1-100)*]]
from sklearn.cluster import KMeans
k_means KMeans()
k_means.fit(x)
k_means KMeans (n_clusters=5)
k_means.fit_predict(x)
wcss=[]
for i in range(1,11):
k_means KMeans(n_clusters=i)
k_means.fit_predict(x)
wcss.append(k_means.inertia_)
import matplotlib.pyplot as plt
plt.plot(range (1,11), wcss)
plt.title("elbow method").
plt.xlabel("number of clusters")
plt.ylabel("wcss")
plt.show()
x=data[['Annual Income (k$)', 'Spending Score (1-100)]]
k_means = KMeans(n_clusters=5, random_state=42)
Y_means =k_means.fit_predict(x)
plt.scatter(x.iloc[Y_means==0,0],x.iloc[Y_means==0,1], s = 1theta*theta c='red', label='cluster1
plt.scatter(x.iloc[Y_means z = 1, theta ] x.iloc[Y_means z = 1, 1 ], s=100, c='yellow', label='clust plt.scatter(x.iloc[Y_means z = 2, 0 ] x.iloc[Y_means z = 2, 1 ], s = 1theta*theta c='blue', label='cluster
plt.scatter(x.iloc[Y_means==3,0],x.iloc[Y_means z = 3, 1 ], s = 1theta*theta c='green', label='cluste
plt.scatter(x.iloc[Y_means==4,0],x.iloc[Y_means==4,1], s = 1theta*theta c='black', label='cluste
plt.scatter(k_means.cluster_centers_[:,0],k_means.cluster_centers_[:,1],s=200, c='cs
plt.title("customer segmentation")
plt.xlabel("annual income")
plt.ylabel("spending score")
plt.legend()
plt.show()
k_means.predict([[15,39]])
