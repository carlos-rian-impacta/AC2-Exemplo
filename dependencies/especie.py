from dataclasses import dataclass

"""
O que muitas pessoas não sabem é que no python, assim como no java, c#, etc
Nós também conseguimos criar o meu próprio tipo de dados, 
por exemplo a classe abaixo ela tem um decorador dataclass que torna a minha
classe em um tipo de dados, que vai receber alguns dados com seus respectivos
tipo, exemplo nome só aceita strings, se você passar um inteiro, terá um error.

Video para auxiliar:
    https://www.youtube.com/watch?v=1TFwgGE6qzI
"""


@dataclass(frozen=True)
class EspeciePokemon:
    """
    Essa classe cria um novo pokemon e valida os dados por meio do frozen
    quando você usa o decorador dataclass ele valida todo dado de entrada desde
    que você coloque o frozen como true.
    Ele não permitirá você passar um tipo invalido, por exemplo: nome = 1 isso
    dará err pois nome só aceita strings.

    Até agora, temos representado as espécies de pokemóns apenas como uma string,
    no entanto podemos representá-los com uma classe.
    Esta classe representa uma espécie de pokémon,
    e cada instância carrega dentro de si o nome de uma espécie de pokémon,
    a cor e as informações da evolução.
    """

    nome: str
    cor: str
    evoluiu_de: str
    evolui_para: list