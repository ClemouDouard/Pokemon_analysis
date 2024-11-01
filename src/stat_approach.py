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

    normal_poke = df.loc[(df.type_1 == "normal") | (df.type_2 == "normal")]
    fire_poke = df.loc[(df.type_1 == "fire") | (df.type_2 == "fire")]
    water_poke = df.loc[(df.type_1 == "water") | (df.type_2 == "water")]
    electric_poke = df.loc[(df.type_1 == "electric") | (df.type_2 == "electric")]
    grass_poke = df.loc[(df.type_1 == "grass") | (df.type_2 == "grass")]
    normal_poke = df.loc[(df.type_1 == "normal") | (df.type_2 == "normal")]
    ice_poke = df.loc[(df.type_1 == "ice") | (df.type_2 == "ice")]
    fighting_poke = df.loc[(df.type_1 == "fighting") | (df.type_2 == "fighting")]
    poison_poke = df.loc[(df.type_1 == "poison") | (df.type_2 == "poison")]
    ground_poke = df.loc[(df.type_1 == "ground") | (df.type_2 == "ground")]
    flying_poke = df.loc[(df.type_1 == "flying") | (df.type_2 == "flying")]
    psychic_poke = df.loc[(df.type_1 == "psychic") | (df.type_2 == "psychic")]
    bug_poke = df.loc[(df.type_1 == "bug") | (df.type_2 == "bug")]
    rock_poke = df.loc[(df.type_1 == "rock") | (df.type_2 == "rock")]
    ghost_poke = df.loc[(df.type_1 == "ghost") | (df.type_2 == "ghost")]