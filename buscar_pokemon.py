import requests
import json

url = 'https://pokeapi.co/api/v2/pokemon/'

def buscarPokemon(num):
    peticion = requests.get(url + str(num) )
    respuesta = json.loads(peticion.content)
    print(respuesta['name'])

buscarPokemon(4)