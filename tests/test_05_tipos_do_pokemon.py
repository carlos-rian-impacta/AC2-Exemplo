from ac2 import tipos_do_pokemon
from dependencies.errors import PokemonNaoExisteException
import pytest


def test_ok_tipos_do_pokemon():
    assert sorted(tipos_do_pokemon("klink")) == sorted(["aço"])
    assert sorted(tipos_do_pokemon("feebas")) == sorted(["água"])
    assert sorted(tipos_do_pokemon("dratini")) == sorted(["dragão"])
    assert sorted(tipos_do_pokemon("jynx")) == sorted(["psíquico", "gelo"])
    assert sorted(tipos_do_pokemon("archeops")) == sorted(["pedra", "voador"])
    assert sorted(tipos_do_pokemon("drapion")) == sorted(["veneno", "noturno"])
    assert sorted(tipos_do_pokemon("murkrow")) == sorted(["voador", "noturno"])
    assert sorted(tipos_do_pokemon("chinchou")) == sorted(["água", "elétrico"])
    assert sorted(tipos_do_pokemon("marshadow")) == sorted(["lutador", "fantasma"])
    assert sorted(tipos_do_pokemon("heracross")) == sorted(["lutador", "inseto"])


def test_error_cor_do_pokemon():
    with pytest.raises(PokemonNaoExisteException):
        assert tipos_do_pokemon("dollynho")
    with pytest.raises(PokemonNaoExisteException):
        assert tipos_do_pokemon("dobby")
    with pytest.raises(PokemonNaoExisteException):
        assert tipos_do_pokemon("peppa-pig")
    with pytest.raises(PokemonNaoExisteException):
        assert tipos_do_pokemon("batman")
    with pytest.raises(PokemonNaoExisteException):
        assert tipos_do_pokemon("spiderman")


def test_error_nome_vazio_cor_do_pokemon():
    with pytest.raises(PokemonNaoExisteException):
        assert tipos_do_pokemon("")
