import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

data = pd.read_csv("flowers.csv", sep=",", header=None)
data.columns =  ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'species']

print(data.head())


print("Summary:")
summary = data.describe()
summary = summary.transpose()
print(summary.head())

seto = data[data['species'] == 'Iris-setosa']
vers = data[data['species'] == 'Iris-versicolor']
virg = data[data['species'] == 'Iris-virginica']

### Sepal length plot:
### sepal_length.png
# plt.hist(data['sepal length (cm)'])
# plt.title('Sepal Length')
# plt.xlabel('height (cm)')
# plt.ylabel('number')
#plt.show()


### Sepal Length vs Width

#
# x_axis = data['sepal length (cm)']
# y_axis = data['sepal width (cm)']
# colors = {'Iris-setosa': 'blue', 'Iris-versicolor': 'red', 'Iris-virginica': 'green'}
# se = plt.scatter(seto['sepal length (cm)'], seto['sepal width (cm)'], color = 'b')
# ve = plt.scatter(vers['sepal length (cm)'], vers['sepal width (cm)'], color = 'g')
# vi = plt.scatter(virg['sepal length (cm)'], virg['sepal width (cm)'], color = 'r')
#
# plt.legend((se, ve, vi), ('Setosa', 'Versicolor', 'Virginica'), scatterpoints=1)
#
# plt.title('Sepal Length vs Width')
# plt.xlabel('Sepal Length (cm)')
# plt.ylabel('Sepal Width (cm)')
# plt.show()


###Box plot of Flower Attributes by species
# data.boxplot(by='species')
# plt.show()
#
# ##Box plot of flower attributes
# data.plot(kind="box", subplots=True, layout=(2,2), sharex=False, sharey=False, title="Length of each Attribute")
# plt.show()
#
# ##histogram of each attributes
# data.hist()
# plt.show()

##multivariate analysis
scatter_matrix(data)
plt.show()
