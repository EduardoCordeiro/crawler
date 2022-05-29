import logging
from typing import Dict

import requests
from sqlalchemy.orm import Session

from app.database import Base, PokemonData

logger = logging.getLogger(__name__)


def display_pokemon(engine, name: str) -> Dict:
    # first try to find in the DB
    session = Session(engine)
    try:
        pokemon = (
            session.query(PokemonData)
            .filter(PokemonData.name == name)
            .one_or_none()
        )

        if pokemon is not None:
            logging.info("Got Pokemon via DB")
            return pokemon.to_dict()
    except Exception as e:
        logging.error(f"exception: {e}")
        pass

    # if not present, query API
    try:
        result = requests.get(
            url=f"https://pokeapi.co/api/v2/pokemon/{name}"
        ).json()
    except Exception as e:
        logging.error(e)
        raise Exception

    logging.info("Got Pokemon via API")

    Base.metadata.create_all(engine)
    with Session(engine) as session:
        pokemon_data = PokemonData(
            name=result["name"],
            height=result["height"],
            stats=result["stats"],
            abilities=result["abilities"],
        )

        session.add(pokemon_data)
        session.commit()

        logging.info(f"Stored Pokemon {result['name']} in DB")

        return pokemon_data.to_dict()
