import requests
import pytest

host = 'https://api.pokemonbattle-stage.me:9101' # хост для покемонов
token = '3137ebadc9545dfea73e079512c06d6d'
def test_status_code():
    response = requests.get(f'{host}/trainers', params= {'trainer_id':1317})
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params= {'trainer_id':1317})
    assert response.json()['trainer_name'] == "Алёнка"  