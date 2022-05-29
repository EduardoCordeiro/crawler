import pytest
from sqlalchemy import create_engine

engine = create_engine("sqlite:///:memory:", echo=True, future=True)


@pytest.fixture
def pikachu_data():
    return {
        "name": "pikachu",
        "height": 4,
        "stats": [
            {
                "base_stat": 35,
                "effort": 0,
                "stat": {
                    "name": "hp",
                    "url": "https://pokeapi.co/api/v2/stat/1/",
                },
            },
            {
                "base_stat": 55,
                "effort": 0,
                "stat": {
                    "name": "attack",
                    "url": "https://pokeapi.co/api/v2/stat/2/",
                },
            },
            {
                "base_stat": 40,
                "effort": 0,
                "stat": {
                    "name": "defense",
                    "url": "https://pokeapi.co/api/v2/stat/3/",
                },
            },
            {
                "base_stat": 50,
                "effort": 0,
                "stat": {
                    "name": "special-attack",
                    "url": "https://pokeapi.co/api/v2/stat/4/",
                },
            },
            {
                "base_stat": 50,
                "effort": 0,
                "stat": {
                    "name": "special-defense",
                    "url": "https://pokeapi.co/api/v2/stat/5/",
                },
            },
            {
                "base_stat": 90,
                "effort": 2,
                "stat": {
                    "name": "speed",
                    "url": "https://pokeapi.co/api/v2/stat/6/",
                },
            },
        ],
        "abilities": [
            {
                "ability": {
                    "name": "static",
                    "url": "https://pokeapi.co/api/v2/ability/9/",
                },
                "is_hidden": False,
                "slot": 1,
            },
            {
                "ability": {
                    "name": "lightning-rod",
                    "url": "https://pokeapi.co/api/v2/ability/31/",
                },
                "is_hidden": True,
                "slot": 3,
            },
        ],
    }
