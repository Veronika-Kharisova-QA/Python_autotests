import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
HEADER = {
    'Content-Type' : 'application/json',
    'trainer_token' : 'TOKEN'              
         }
TRAINER_ID = 'ID'



def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response.status_code==200, "Unexpected status code"


def test_trainer_id():
    response_get = requests.get(url = f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name']== 'NAME'