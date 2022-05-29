import logging

import pytest

from app.conftest import engine
from app.pokemon import display_pokemon

logger = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "name, expected, location",
    [
        (
            "pikachu",
            "pikachu_data",
            "Got Pokemon via API",
        ),
        (
            "pikachu",
            "pikachu_data",
            "Got Pokemon via DB",
        ),
        (
            "this_is_not_a_pokemon",
            Exception,
            "Got Pokemon via API",
        ),
    ],
)
def test_display_pokemon(name, expected, location, caplog, request):
    with caplog.at_level(logging.INFO):
        if expected == Exception:
            with pytest.raises(Exception):
                display_pokemon(engine, name)
        else:
            pokemon = display_pokemon(engine, name)

            assert location in caplog.text
            assert pokemon == request.getfixturevalue(expected)
