import requests

def fetch_data():

    url = "https://api.freeapi.app/api/v1/public/dogs/dog/random"
    response = requests.get(url)
    data = response.json()

    if data["statusCode"] == 200 and data["success"]:
        dog_data = data["data"]
        dog_details = f"Name : {dog_data["name"]} \nBread for : {dog_data["bred_for"]} \nBreed Group : {dog_data["breed_group"]} \nLife Span : {dog_data["life_span"]} \nTemperament{dog_data["temperament"]}"

        print(f"- > Dog Details < - \n{dog_details}")

    else:
        print("Request could not complete")

def main():

    try:    
        fetch_data()
    except Exception as e:
        print(f"Error occured : {e}")

if __name__ == "__main__":
    main()

