import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_url = "https://pokeapi.co/api/v2/"

class Pokemon :
    def __init__(self, name) -> None:
        self.name = name

    def getName(self) -> str:
        return self.name

    def url(self) -> str:
        return f"{base_url}/pokemon/{self.getName()}"
    
    def info(self) :
        result = requests.get(self.url())

        if result.status_code == 200 :
            return result.json()
        else :
            print(f"Failed to retrieve data : {result.status_code}")
            return None
    
pikachu = Pokemon("pikachu")
print(pikachu.info())
