import pytest
from ac2 import (
    nome_do_pokemon,
    numero_do_pokemon,
    color_of_pokemon,
    cor_do_pokemon,
    tipos_do_pokemon,
    evolucao_anterior,
    evolucoes_proximas,
    nivel_do_pokemon,
)
from dependencies.errors import (
    PokemonJaCadastradoException,
    PokemonNaoCadastradoException,
    PokemonNaoExisteException,
    TreinadorNaoCadastradoException,
)


def test_error_nome_do_pokemon():
    with pytest.raises(PokemonNaoExisteException):
        assert nome_do_pokemon(0)
    with pytest.raises(PokemonNaoExisteException):
        assert nome_do_pokemon(-1)
    with pytest.raises(PokemonNaoExisteException):
        assert nome_do_pokemon(-2)
    with pytest.raises(PokemonNaoExisteException):
        assert nome_do_pokemon(-666)
    with pytest.raises(PokemonNaoExisteException):
        assert nome_do_pokemon(5000)
    with pytest.raises(PokemonNaoExisteException):
        assert nome_do_pokemon(10001)


def test_ok_nome_do_pokemon():
    assert nome_do_pokemon(1) == "bulbasaur"
    assert nome_do_pokemon(55) == "golduck"
    assert nome_do_pokemon(25) == "pikachu"
    assert nome_do_pokemon(700) == "sylveon"
    assert nome_do_pokemon(807) == "zeraora"