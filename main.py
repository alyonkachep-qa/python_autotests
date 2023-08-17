import requests
token = '3137ebadc9545dfea73e079512c06d6d'
host = 'https://api.pokemonbattle-stage.me:9101' # хост для покемонов
'''response = requests.post('https://api.pokemonbattle-stage.me:9101/pokemons', json = {
    "name": "Душка",
    "photo": "https://dolnikov.ru/pokemons/createthumb.php?filename=albums/030.png&size=200"
}, headers={'Content-Type':'application/json', 'trainer_token': token})
print(response.text)'''

'''response_change_name_pokemon = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "1587",
    "name": "Диего",
}, headers={'Content-Type':'application/json', 'trainer_token': token})
print(response_change_name_pokemon.text)'''

response_pokemons_in_pokeball = requests.post(f'{host}/trainers/add_pokeball', json ={
    "pokemon_id": "1587",
    "photo": "https://dolnikov.ru/pokemons/createthumb.php?filename=albums/004.png&size=200"
}, headers={'Content-Type':'application/json', 'trainer_token': token})
print(response_pokemons_in_pokeball.text)