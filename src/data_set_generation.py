### THIS IS THE PY CODE TO GENERATE THE DATA SET

# libraries import
import requests
import pandas as pd
import seaborn as sns
import librosa
import numpy as np
import io

# start of the url to use the api
base_url = "https://pokeapi.co/api/v2/"

# pokemon class
class Pokemon :
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name
    
    def get_mfcc(self) -> list:
        response = requests.get(self.cries["latest"])
        audio_data = io.BytesIO(response.content)

        signal, sr = librosa.load(audio_data, sr= None)
        mfccs = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=13)
        return np.mean(mfccs.T, axis=0)
    
    def get_stats(self) -> dict:
        d = {}
        for stat in self.stats :
            d[stat["stat"]["name"]] = stat["base_stat"]
        
        return d
    
    def get_types(self) -> dict:
        d = {'type_1' : self.types[0]["type"]["name"]}
        if len(self.types) == 2 :
            d["type_2"] = self.types[1]["type"]["name"]
        else :
            d["type_2"] = "None"

        return d
    
    def get_dico(self) -> dict:
        return {'id' : self.id} | 

    # the correct url used with the api
    def url(self) -> str:
        return f"{base_url}/pokemon/{self.get_name()}"
    
    # the general informations of the pokemon (gathered with the api)
    def set_info(self) -> None :
        result = requests.get(self.url())

        if result.status_code == 200 : # the correct status_code
            self.info = result.json()
            return None
        else :
            print(f"Failed to retrieve data : {result.status_code}")
            return None

    # setters  
    def set_cries(self) -> None :
        self.cries = self.info["cries"]
    
    def set_height(self) -> None :
        self.height = self.info["height"]
    
    def set_id(self) -> None :
        self.id = self.info["id"]

    def set_sprites(self) -> None :
        self.sprites = self.info["sprites"]

    def set_stats(self) -> None :
        self.stats = self.info["stats"]
    
    def set_types(self) -> None :
        self.types = self.info["types"]

    def set_weight(self) -> None :
        self.weight = self.info["weight"]

    # general setter
    def set_all(self) -> None :
        self.set_info()
        self.set_cries()
        self.set_height()
        self.set_id()
        self.set_sprites()
        self.set_stats()
        self.set_types()
        self.set_weight()

# base list of all pokemon
#pokemon_list = requests.get(f"{base_url}/pokemon?limit=100000&offset=0").json()
#
#pokeNameUrl_list = pokemon_list["results"]
#pokeName_list = [poke["name"] for poke in pokeNameUrl_list]
#
#print(pokeName_list)

pikachu = Pokemon("pikachu")
pikachu.set_all()

print(pikachu.get_types())