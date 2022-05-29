import logging

from fastapi import FastAPI
from sqlalchemy import create_engine

from app.crawler import crawl_pokemons
from app.database import db_creation
from app.pokemon import display_pokemon

logger = logging.getLogger(__name__)

app = FastAPI(title="Pokemon Crawler")
engine = create_engine("sqlite:///:memory:", echo=True, future=True)


@app.on_event("startup")
def setup_application():
    db_creation(engine)
    try:
        crawl_pokemons(engine, "https://pokeapi.co/api/v2/pokemon/")
    except Exception as e:
        logging.error(e)


@app.get("/ping")
async def ping():
    return "Healthy"


@app.get("/pokemon/{name}")
async def pokemon(name):
    try:
        return display_pokemon(engine, name)
    except Exception as e:
        logger.error(e)
