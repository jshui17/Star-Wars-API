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
and adds key value pair of specicies and name to dict.
(default dict is needed as opposed to a standard dict so no KeyError is raised when trying to access a key not already in the dict)
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
            species = retrieve_json(character['species'][0])['name'] if character['species'] else "Miscellaneous"
            characters_list[species].append(name)
        characters_url = data.get('next') 
    
    return characters_list

'''
This function loops through the characters_list dict's key value pairs.
Prints the key (species) followed by a new line of hypens and the values (names) that correspond
'''
def display_list(characters_list):
    for species, names, in characters_list.items():
        print(f"{species}: ")
        print("-" * (len(species)))
        for name in names:
            print(f"- {name}")
        print("\n")

if __name__ == "__main__":
    print(display_list(raw_characters()))