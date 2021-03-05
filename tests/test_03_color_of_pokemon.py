from dependencies.errors import PokemonNaoExisteException
from ac2 import color_of_pokemon
import pytest


def test_ok_color_of_pokemon():
    assert color_of_pokemon("marill") == "blue"
    assert color_of_pokemon("togekiss") == "white"
    assert color_of_pokemon("magneton") == "gray"
    assert color_of_pokemon("eevee") == "brown"
    assert color_of_pokemon("psyduck") == "yellow"
    assert color_of_pokemon("skitty") == "pink"
    assert color_of_pokemon("gastly") == "purple"
    assert color_of_pokemon("ledyba") == "red"
    assert color_of_pokemon("torterra") == "green"
    assert color_of_pokemon("xurkitree") == "black"


def test_error_color_of_pokemon():
    with pytest.raises(PokemonNaoExisteException):
        assert color_of_pokemon("dollynho")
    with pytest.raises(PokemonNaoExisteException):
        assert color_of_pokemon("dobby")
    with pytest.raises(PokemonNaoExisteException):
        assert color_of_pokemon("peppa-pig")
    with pytest.raises(PokemonNaoExisteException):
        assert color_of_pokemon("batman")
    with pytest.raises(PokemonNaoExisteException):
        assert color_of_pokemon("spiderman")


def test_error_nome_vazio_color_of_pokemon():
    with pytest.raises(PokemonNaoExisteException):
        assert color_of_pokemon("")