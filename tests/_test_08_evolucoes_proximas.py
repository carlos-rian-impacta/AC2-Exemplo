from dependencies.errors import PokemonNaoExisteException
from ac2 import evolucoes_proximas
import pytest


def test_ok_evolucoes_proximas():
    assert evolucoes_proximas("pikachu") == ["raichu"]
    assert evolucoes_proximas("pichu") == ["raichu"]
    assert evolucoes_proximas("togepi") == ["togekiss"]
    assert evolucoes_proximas("togetic") == ["togekiss"]
    assert evolucoes_proximas("tynamo") == ["eelektross"]
    assert evolucoes_proximas("eelektrik") == ["eelektross"]
    assert evolucoes_proximas("poliwhirl") == ["poliwrath", "politoed"]


def test_error_evolucoes_proximas():
    with pytest.raises(PokemonNaoExisteException):
        assert evolucoes_proximas("dollynho")
    with pytest.raises(PokemonNaoExisteException):
        assert evolucoes_proximas("dobby")
    with pytest.raises(PokemonNaoExisteException):
        assert evolucoes_proximas("peppa-pig")
    with pytest.raises(PokemonNaoExisteException):
        assert evolucoes_proximas("batman")
    with pytest.raises(PokemonNaoExisteException):
        assert evolucoes_proximas("spiderman")


def test_error_vazio_evolucao_anterio():
    with pytest.raises(PokemonNaoExisteException):
        assert evolucoes_proximas("")
