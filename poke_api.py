import requests

def get_pokemon_info(pokemon_name_or_id):
    """
    Fetches information for a specified Pokémon from the PokéAPI.

    Args:
        pokemon_name_or_id (str/int): The name or PokéDex number of the Pokémon.

    Returns:
        dict: A dictionary containing Pokémon information if successful, None otherwise.
    """
    url = f'https://pokeapi.co/api/v2/pokemon/{str(pokemon_name_or_id).strip().lower()}'
    
    print(f"Getting information for {pokemon_name_or_id}...")
    response = requests.get(url)
    
    if response.status_code == 200:
        print("Information fetched successfully!")
        return response.json()
    else:
        print("Failed to fetch Pokémon information.")
        return None
