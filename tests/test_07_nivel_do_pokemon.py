from ac2 import movimentos_pokemon
from dependencies.errors import PokemonNaoExisteException
import pytest


def test_ok_movimentos_pokemon():
    assert movimentos_pokemon("bulbasaur", 4) == [
        "razor-wind",
        "swords-dance",
        "cut",
        "bind",
    ]
    assert movimentos_pokemon("pikachu", 3) == ["mega-punch", "pay-day", "thunder-punch"]
    assert movimentos_pokemon("togepi", 4) == [
        "mega-punch",
        "mega-kick",
        "headbutt",
        "body-slam",
    ]
    assert movimentos_pokemon("togetic", 2) == ["mega-punch", "fly"]
    assert movimentos_pokemon("tynamo", 5) == [
        "tackle",
        "thunder-wave",
        "spark",
        "magnet-rise",
        "charge-beam",
    ]


def test_error_movimentos_pokemon():
    with pytest.raises(PokemonNaoExisteException):
        assert movimentos_pokemon("dollynho", -1)
    with pytest.raises(PokemonNaoExisteException):
        assert movimentos_pokemon("dobby", 4)
    with pytest.raises(PokemonNaoExisteException):
        assert movimentos_pokemon("peppa-pig", 0)
    with pytest.raises(PokemonNaoExisteException):
        assert movimentos_pokemon("batman", 3)
    with pytest.raises(PokemonNaoExisteException):
        assert movimentos_pokemon("spiderman", 4)


def test_error_vazio_evolucao_anterio():
    with pytest.raises(PokemonNaoExisteException):
        assert movimentos_pokemon("", 4)
