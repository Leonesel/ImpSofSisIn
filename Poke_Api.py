"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/132.png"

import requests
import shutil
import json

class Llamadanoseque:

    def coso_coso(self):
        r = requests.get(url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/132.png")
        print(r.content)
        print(r.status_code)

    def gogogo(self, url, file_name):
        res = requests.get(url,stream=True)
        
        if 200 == res.status_code:
            with open(file_name, "wb") as f:
                shutil.copyfileobj(res.raw,f)
            print("imagen descarga completamente")
        else:
            print("No se encontro nada")

    def cosos_coso(self,pokemon):
        r = requests.get(url="https://pokeapi.co/api/v2/pokemon/"+pokemon)
        obj = json.loads(r.content)
        return obj["sprites"]["front_shiny"]

pokemon = input("Escoge un pokemon: ")

yoyo = Llamadanoseque()
img = yoyo.cosos_coso(pokemon)
yoyo.gogogo(img, str(pokemon)+".png")