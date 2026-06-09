import requests

def fetch_data():

    url = "https://api.freeapi.app/api/v1/public/dogs/dog/random"
    response = requests.get(url)
    data = response.json()

    
