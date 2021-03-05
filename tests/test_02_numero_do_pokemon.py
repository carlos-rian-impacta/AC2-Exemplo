from ac2 import numero_do_pokemon
from dependencies.errors import PokemonNaoExisteException
import pytest


def test_ok_numero_do_pokemon():
    assert numero_do_pokemon("eevee") == 133
    assert numero_do_pokemon("psyduck") == 54
    assert numero_do_pokemon("marill") == 183
    assert numero_do_pokemon("skitty") == 300
    assert numero_do_pokemon("zeraora") == 807


def test_error_numero_do_pokemon():
    with pytest.raises(PokemonNaoExisteException):
        assert numero_do_pokemon("dollynho")
    with pytest.raises(PokemonNaoExisteException):
        assert numero_do_pokemon("dobby")
    with pytest.raises(PokemonNaoExisteException):
        assert numero_do_pokemon("peppa-pigf")
    with pytest.raises(PokemonNaoExisteException):
        assert numero_do_pokemon("batman")
    with pytest.raises(PokemonNaoExisteException):
        assert numero_do_pokemon("spiderman")


def test_erro_nome_vazio_numero_do_pokemon():
    with pytest.raises(PokemonNaoExisteException):
        assert numero_do_pokemon("")