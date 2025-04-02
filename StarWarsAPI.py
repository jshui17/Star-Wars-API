import requests

def retrieve_json(url):
    response=requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve json from {url}")
        return None

   

if __name__ == "__main__":
    retrieve_json("https://swapi.dev/api/planets/1/")