### THIS IS A FILE TO EXPLORE AND MAKE VISUALIZATIONS ON THE SIMPLE DATASET

# libraries import
import requests
import pandas as pd
import seaborn as sns
import librosa
import numpy as np
import io

if __name__ == "__main__" :

    # extraction of the data set previously created
    df = pd.read_csv('data/pokemon_data_1stgen.csv', index_col=0)
    print(df.head())