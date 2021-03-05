"""
Esse arquivo contém todos os erros que serão usados durante o desenvolvimento
da AC.

Perceba que no python você pode criar sua própria classe de erro.
Por padrão o python tem a classe Exception, essa classe "pega" qualquer exceções.

Então se a gente herdar dela, a gente consegue criar nossas próprias exceções.
"""


class PokemonNaoExisteException(Exception):
    """Essa exceção será usada quando um pokemon não existir."""

    pass


class PokemonNaoCadastradoException(Exception):
    """Essa exceção será usada quando um pokemon não estiver cadastrado."""

    pass


class TreinadorNaoCadastradoException(Exception):
    """Essa exceção será usada quando um treinador não estiver cadastrado."""

    pass


class PokemonJaCadastradoException(Exception):
    """Essa exceção será usada quando um pokemon já estiver cadastrado."""

    pass