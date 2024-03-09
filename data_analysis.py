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
data_directory = './datasets/' 

# Read CSV file into DataFrame 
df = pd.read_csv(f'{data_directory}/data.csv')

# Read Excel file into DataFrame
df = pd.read_excel(f'{data_directory}/data.xlsx') 

# List all CSV files in directory
csv_files = [f for f in os.listdir(data_directory) if f.endswith('.csv')]

# Read specific CSV file into DataFrame 
for f in csv_files:
    df = pd.read_csv(f'{data_directory}/{f}')

# Read all Excel files into DataFrames
excel_files = [f for f in os.listdir(data_directory) if f.endswith('.xlsx')]
df_dict = {}
for f in excel_files:
    df_dict[f] = pd.read_excel(f'{data_directory}/{f}')


# Calculate metrics


# Visualize results
