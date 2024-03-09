import pandas as pd
from matplotlib import pyplot as plt
import scipy as sp
import numpy as np

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.datasets import load_iris

import os

# LOAD DATA

# Set data directory
data_directory = './datasets'
training_csv = 'adult_tr.csv'
testing_csv = 'adult_ts.csv'

df_train = pd.read_csv(f'{data_directory}/{training_csv}')
df_test = pd.read_csv(f'{data_directory}/{testing_csv}')

print(df_train)


# Calculate metrics


# Visualize results



print('Done.')


'''


# Read CSV file into DataFrame 
df = pd.read_csv(f'{data_directory}/data.csv')

# Read Excel file into DataFrame
df = pd.read_excel(f'{data_directory}/data.xlsx') 


# List all CSV files in directory
csv_files = [f for f in os.listdir(data_directory) if f.endswith('.csv')]

# Read specific CSV file into DataFrame 
for f in csv_files:
    df = pd.read_csv(f'{data_directory}/{f}')


'''
