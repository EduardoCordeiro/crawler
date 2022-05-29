from typing import Dict, List

import requests
from sqlalchemy.orm import Session

from app.database import PokemonData


def crawl_pokemons(engine, url: str) -> None:
    """
    Query https://pokeapi.co/api/v2/pokemon/ and
    iterate over the results key until we have more
    pokemons to catch.
    """
    # Store all pokemon data and send to DB once
    all_pokemons = []

    response = requests.get(url=url).json()

    while True:
        try:
            response = requests.get(url=url).json()
            pokemon_data = create_pokemon_data(response["results"])
            all_pokemons.extend(pokemon_data)

            if response["next"] is None:
                break
        except Exception:
            raise Exception

        url = response["next"]

    # Save all Pokemons to DB
    with Session(engine) as session:
        session.add_all(all_pokemons)
        session.commit()


def create_pokemon_data(pokemons: List[Dict]) -> List[PokemonData]:
    return [get_pokemon_data(pokemon["name"]) for pokemon in pokemons]


def get_pokemon_data(name: str) -> PokemonData:
    print(f"Querying PokeAPI for {name}")
    # query PokeAPI to get the full information about this Pokemon
    try:
        result = requests.get(
            url=f"https://pokeapi.co/api/v2/pokemon/{name}"
        ).json()
    except Exception:
        raise Exception

    return PokemonData(
        name=result["name"],
        height=result["height"],
        stats=result["stats"],
        abilities=result["abilities"],
    )
