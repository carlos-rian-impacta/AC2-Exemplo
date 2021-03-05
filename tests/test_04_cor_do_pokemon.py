import pytest
from ac2 import cor_do_pokemon
from dependencies.errors import PokemonNaoExisteException


def test_ok_cor_do_pokemon():
    assert cor_do_pokemon("marill") == "azul"
    assert cor_do_pokemon("skitty") == "rosa"
    assert cor_do_pokemon("gastly") == "roxo"
    assert cor_do_pokemon("eevee") == "marrom"
    assert cor_do_pokemon("magneton") == "cinza"
    assert cor_do_pokemon("torterra") == "verde"
    assert cor_do_pokemon("ledyba") == "vermelho"
    assert cor_do_pokemon("psyduck") == "amarelo"
    assert cor_do_pokemon("togekiss") == "branco"
    assert cor_do_pokemon("xurkitree") == "preto"


def test_error_cor_do_pokemon():
    with pytest.raises(PokemonNaoExisteException):
        assert cor_do_pokemon("dollynho")
    with pytest.raises(PokemonNaoExisteException):
        assert cor_do_pokemon("dobby")
    with pytest.raises(PokemonNaoExisteException):
        assert cor_do_pokemon("peppa-pig")
    with pytest.raises(PokemonNaoExisteException):
        assert cor_do_pokemon("batman")
    with pytest.raises(PokemonNaoExisteException):
        assert cor_do_pokemon("spiderman")


def test_error_nome_vazio_cor_do_pokemon():
    with pytest.raises(PokemonNaoExisteException):
        assert cor_do_pokemon("")