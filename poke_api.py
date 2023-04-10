'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def get_pokemon_info(pokemon):
    """Gets information about a specified pokemon from the PokeAPI.

    Args:
        pokemon (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise 
        none.
    """
    # Clean the pokemon name parameter by:
    # - Converting to a string object,
    # - Removing leading a trailing whitespace, and
    # - Converting to all lowercase letters
    pokemon = str(pokemon).strip().lower()

    # Check if pokemon name is an empty string
    if pokemon == '':
        print('Error: No Pokemon name specified.')
        return 
    
    # Send GET request for Pokemon info
    print(f'Getting information for {pokemon}...', end='')
    url = POKE_API_URL + pokemon
    resp_msg = requests.get(url)

    # Check if request was successful 
    if resp_msg.status_code == requests.code.ok:
        print('success')
        # Return ductionary of Pokemon info
        return resp_msg.json()
    else:
        print('failure')
        print(f'Respones code: {resp_msg.status_code} ({resp_msg.reason})')
        return
