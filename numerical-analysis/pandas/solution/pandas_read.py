import pandas as pd


DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/breast-cancer.csv'

column_names = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
                'mean smoothness', 'mean compactness', 'mean concavity',
                'mean concave points', 'mean symmetry', 'mean fractal dimension',
                'radius error', 'texture error', 'perimeter error', 'area error',
                'smoothness error', 'compactness error', 'concavity error',
                'concave points error', 'symmetry error',
                'fractal dimension error', 'worst radius', 'worst texture',
                'worst perimeter', 'worst area', 'worst smoothness',
                'worst compactness', 'worst concavity', 'worst concave points',
                'worst symmetry', 'worst fractal dimension', 'label']

labels = ['malignant', 'benign']

df = pd.read_csv(DATA, skiprows=1, names=column_names)

df['label'].replace(
    to_replace=dict(enumerate(labels)),  # {0: 'malignant', 1: 'benign'}
    inplace=True
)
