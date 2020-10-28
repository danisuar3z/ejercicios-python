# -*- coding: utf-8 -*-

# clasificadores.py
# Dani Suarez - suarezdanieltomas@gmail.com

# Machine Learning con sklearn

import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


ds = load_iris()
df = pd.DataFrame(ds.data, columns=ds.feature_names)

knn_pred, clf_pred, rfc_pred = [], [], []


# %%

def main(N=50):
    for _ in range(N):
        x_train, x_test, y_train, y_test = train_test_split(
            ds.data, ds.target)

        # Initialize
        knn = KNeighborsClassifier()
        clf = DecisionTreeClassifier()
        rfc = RandomForestClassifier()

        # Training
        knn.fit(x_train, y_train)
        clf.fit(x_train, y_train)
        rfc.fit(x_train, y_train)

        # Testing
        knn_pred.append(knn.score(x_test, y_test))
        clf_pred.append(clf.score(x_test, y_test))
        rfc_pred.append(rfc.score(x_test, y_test))

def table(l1, l2, l3):
    print('\n' + '*'*39)
    print(f'{"Modelo":^15} | {"Promedio scores (%)":24}')
    print('-'*39)
    for model, l in zip(['Near. Neigh.', 'Tree', 'Random Forest'],
                        [l1, l2, l3]):
        print(f'{model:15} | {np.mean(l)*100:^24.2f}')
        print('-'*39)

# %%

if __name__ == '__main__':
    main()  # N=50 default
    table(knn_pred, clf_pred, rfc_pred)

'''
# Out:
***************************************
    Modelo      | Promedio scores (%)     
---------------------------------------
Near. Neigh.    |          94.74          
---------------------------------------
Tree            |          93.68          
---------------------------------------
Random Forest   |          93.68          
---------------------------------------
'''
