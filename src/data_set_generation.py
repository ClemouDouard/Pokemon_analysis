### THIS IS THE PY CODE TO GENERATE THE DATA SET

# libraries import
import requests
import pandas as pd
import seaborn as sns

# start of the url to use the api
base_url = "https://pokeapi.co/api/v2/"

# pokemon class
class Pokemon :
    def __init__(self, name) -> None:
        self.name = name

    def getName(self) -> str:
        return self.name

    # the correct url used with the api
    def url(self) -> str:
        return f"{base_url}/pokemon/{self.getName()}"
    
    # the general informations of the pokemon (gathered with the api)
    def info(self) :
        result = requests.get(self.url())

        if result.status_code == 200 : # the correct status_code
            return result.json()
        else :
            print(f"Failed to retrieve data : {result.status_code}")
            return None

# base list of all pokemon
pokemon_list = requests.get(f"{base_url}/pokemon?limit=100000&offset=0").json()

pokeNameUrl_list = pokemon_list["results"]
pokeName_list = [poke["name"] for poke in pokeNameUrl_list]

print(pokeName_list)