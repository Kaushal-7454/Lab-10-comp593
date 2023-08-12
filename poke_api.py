'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_into() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    return

def get_pokemon_info(pokemon):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Clean the Pokemon name parameter by:
    # - Converting to a string object,
    # - Removing leading and trailing whitespace, and
    # - Converting to all lowercase letters
    pokemon = str(pokemon).strip().lower()

    # Check if Pokemon name is an empty string
    if pokemon == '':
        print('Error: No Pokemon name specified.')
        return

    # Send GET request for Pokemon info
    print(f'Getting information for {pokemon.capitalize()}...', end='')
    url = POKE_API_URL + pokemon
    resp_msg = requests.get(url)

    # Check if request was successful
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        # Return dictionary of Pokemon info
        return resp_msg.json()
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')

    # TODO: Define function that gets a list of all Pokemon names from the PokeAPI
def fetch_all_pokemon_name():
    """
    This function qill help to fetch all the names of the Pokemon names.

    Returns:
        Whole List: it will return list of pokemon names otherwise it will return 
        error message or enpty list.
    """
    whl_url = POKE_API_URL + "?limit=1000"
    response_msg = requests.get(whl_url)

    if response_msg.status_code = requests.code.ok:
        pokemon_data = response_msg.json()
        st_pokemon_name = [entry['NAME'] for entry in pokemon_data['results']]
    # TODO: Define function that downloads and saves Pokemon artwork
def save_pokemon_artwork(poke_name, store_path):
    poke_name = poke_name.strip().lower()

    if poke_name == '':
        print("Failed: pokemon name has not provided.")
        return False 
    poke_url = POKE_API_URL + f"{poke_name}/"
    response_msg = requests.get(poke_url)
if __name__ == '__main__':
    main()