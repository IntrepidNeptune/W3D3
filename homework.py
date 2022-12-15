# Create a python wrapper for the Pokemon API. It should take in a pokemon name and display the pokemon with its height and weight

# res = requests.get('https://pokeapi.co/api/v2/pokemon')
# data = res.json()
# data
# print (f'{data}')



class PokemonAPI:
    api_url = 'https://pokeapi.co/api/v2/pokemon'

    def __init__(self, pokemon_name):
        self.pokemon_name = pokemon_name
        self.pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
        self.pokeson = self.pokemon.json
        return f'{pokemon_name.capitalize()} is {pokeson[height]} and {pokeson[weight]}lbs'

PokemonAPI('charizard')