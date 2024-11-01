# THIS PY FILE MAKES A LINEAR REGRESSION ON THE DATA

# libraries import
import requests
import pandas as pd
import seaborn as sns
import librosa
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

if __name__ == "__main__" :

    # extraction of the data set previously created
    df = pd.read_csv('data/pokemon_data_1stgen.csv', index_col=0)
