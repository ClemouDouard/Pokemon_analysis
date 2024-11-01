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
    
    # stats for each type

    types = ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost"]

    stat = []

    for type in types :
        stat.append(
            {
                'type' : type,
                'mean-height' : df.loc[(df.type_1 == type) | (df.type_2 == type)]['height'].mean(),
                'mean-weight' : df.loc[(df.type_1 == type) | (df.type_2 == type)]['weight'].mean(),
                'mean-hp' : df.loc[(df.type_1 == type) | (df.type_2 == type)]['hp'].mean(),
                'mean-attack' : df.loc[(df.type_1 == type) | (df.type_2 == type)]['attack'].mean(),
                'mean-defense' : df.loc[(df.type_1 == type) | (df.type_2 == type)]['defense'].mean(),
                'mean-special-attack' : df.loc[(df.type_1 == type) | (df.type_2 == type)]['special-attack'].mean(),
                'mean-special-defense' : df.loc[(df.type_1 == type) | (df.type_2 == type)]['special-defense'].mean(),
                'mean-speed' : df.loc[(df.type_1 == type) | (df.type_2 == type)]['speed'].mean()
            }
        )
    
    type_df = pd.DataFrame(stat)
    type_df.set_index('type', inplace=True)

    type_df.to_csv('data/type_data_1stgen.csv', index=False)