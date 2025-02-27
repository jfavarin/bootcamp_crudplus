import requests
from pydantic import BaseModel

class PokemonSchema(BaseModel): #contrato de dados, schema de dados, view model
    name: str
    type: str

    class Config:
        orm_mode: True

def pegar_pokemon(id: int) -> PokemonSchema:
    URL =f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(URL)
    data = response.json()
    data_types = data['types']  # Supondo que 'data' é o dicionário com os dados do Pokémon
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    return PokemonSchema(name=data['name'],type=types)

if __name__ == "__main__":
    pokemon = pegar_pokemon(10)
    print(pokemon)