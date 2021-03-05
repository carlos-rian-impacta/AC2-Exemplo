from ac2 import evolucao_anterior
from dependencies.errors import PokemonNaoExisteException
import pytest


def test_ok_evolucao_anterior():
    assert evolucao_anterior("pikachu") == "pichu"
    assert evolucao_anterior("raichu") == "pikachu"
    assert evolucao_anterior("togetic") == "togepi"
    assert evolucao_anterior("togekiss") == "togetic"
    assert evolucao_anterior("eelektrik") == "tynamo"
    assert evolucao_anterior("eelektross") == "eelektrik"


def test_ok_sem_evolucao_anterior():
    assert evolucao_anterior("togepi") is None
    assert evolucao_anterior("tynamo") is None
    assert evolucao_anterior("pichu") is None


def test_error_evolucao_anterior():
    with pytest.raises(PokemonNaoExisteException):
        assert evolucao_anterior("dollynho")
    with pytest.raises(PokemonNaoExisteException):
        assert evolucao_anterior("dobby")
    with pytest.raises(PokemonNaoExisteException):
        assert evolucao_anterior("peppa-pig")
    with pytest.raises(PokemonNaoExisteException):
        assert evolucao_anterior("batman")
    with pytest.raises(PokemonNaoExisteException):
        assert evolucao_anterior("spiderman")


def test_error_vazio_evolucao_anterio():
    with pytest.raises(PokemonNaoExisteException):
        assert evolucao_anterior("")
