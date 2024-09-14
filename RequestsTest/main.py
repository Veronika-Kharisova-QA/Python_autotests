import requests

URL = 'https://api.pokemonbattle.ru/v2'
HEADER ={
    'Content-Type' : 'application/json',
    'trainer_token' : 'TOKEN'              
         }
body = {

    "name": "NAME",
    "photo_id": 8
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body)
print(response)


import requests

URL = 'https://api.pokemonbattle.ru/v2'
HEADER ={
    'Content-Type' : 'application/json',
    'trainer_token' : 'NAME'              
         }
body = {
    "pokemon_id": "70065",
    "name": "NAME",
    "photo_id": 2
}
response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body)
print(response)



import requests

URL = 'https://api.pokemonbattle.ru/v2'
HEADER = {
    'Content-Type' : 'application/json',
    'trainer_token' : 'TOKEN'              
         }
body = {
    "pokemon_id": "ID"
}
response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body)
print(response)