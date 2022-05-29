from sqlalchemy import Column, Integer, PickleType, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


def db_creation(engine):
    Base.metadata.create_all(engine)


class PokemonData(Base):
    __tablename__ = "pokemon_data"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    height = Column(Integer)
    stats = Column(PickleType)
    abilities = Column(PickleType)

    def to_dict(self):
        return {
            "name": self.name,
            "height": self.height,
            "stats": self.stats,
            "abilities": self.abilities,
        }
