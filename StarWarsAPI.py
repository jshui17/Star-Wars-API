from collections import defaultdict
import requests

def retrieve_json(url):
    response=requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve json from {url}")
        return None

'''
This function loops through every character in the json file, 
checks if species is specified as first item in list struc, else label the character as "Miscellaneous", 
and adds key value pair of specicies and name to dictionary.
(default dict is needed so no KeyError is raised when trying to access a key not already in the dict)
'''
def raw_characters():
    characters_url="https://swapi.dev/api/people/"
    characters_list=defaultdict(list)
    while characters_url:
        data = retrieve_json(characters_url)
        if not data:
            break
        for character in data['results']:
            name = character['name']
            species = character['species'][0] if character['species'] else "Miscellaneous"
            characters_list[species].append(name)
        characters_url = data.get('next') 
    
    return characters_list

if __name__ == "__main__":
    print(raw_characters())