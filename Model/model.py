import numpy as np
import pandas as pd
import joblib

df = pd.read_csv("Mental Stress Detection Using Machine Learning.csv")
X = df.iloc[:, 0:24]
Y = df.iloc[:, 25]

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify=Y, random_state=2)
"""
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
"""
"""
from sklearn.metrics import accuracy_score
from sklearn import metrics"""

"""from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, Y_train)"""
"""from sklearn.ensemble import RandomForestClassifier
rfmodel = RandomForestClassifier()
rfmodel.fit(X_train,Y_train)"""
"""from sklearn.svm import SVC
smodel = SVC()
smodel.fit(X_train,Y_train)"""
"""from sklearn.neighbors import KNeighborsClassifier
kmodel = KNeighborsClassifier()
kmodel.fit(X_train,Y_train)"""
"""from sklearn.tree import DecisionTreeClassifier
dt_clf = DecisionTreeClassifier()
dt_clf.fit(X_train, Y_train)"""
"""from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, Y_train)"""
"""from sklearn.ensemble import GradientBoostingClassifier
gmodel = GradientBoostingClassifier()
gmodel.fit(X_train,Y_train)"""

from sklearn.neighbors import KNeighborsClassifier
kmodel = KNeighborsClassifier()
kmodel.fit(X_train,Y_train)
from sklearn.metrics import accuracy_score
from sklearn import metrics

prediction = kmodel.predict(X_test)
score = metrics.accuracy_score(Y_test, prediction)
print("\nAccuracy:   %0.3f" % score)

#save the model to disk

filename = 'finalized_model.sav'
joblib.dump(kmodel, filename)