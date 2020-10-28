# -*- coding: utf-8 -*-

# iris_seaborn.py
# Dani Suarez - suarezdanieltomas@gmail.com
# Ejercicio 11.10: Seaborn

import pandas as pd
import seaborn as sns

from sklearn.datasets import load_iris

def main():
    iris_ds = load_iris()
    
    iris_df = pd.DataFrame(iris_ds.data, columns=iris_ds.feature_names)
    
    iris_df['target'] = iris_ds.target
    
    sns.pairplot(iris_df, hue='target', palette='colorblind')

if __name__ == '__main__':
    main()