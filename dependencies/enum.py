from enum import Enum, auto

""" 
Além do dataclass que está no arquivo de especie.py, temos também o enum.
O enum é usado em diversas linguagens para limitar um tipo de dado.
Imagine que você tem uma loja que só aceita 3 opções de pagamento.
Por exemplo: Débito, Crédito, Dinheiro. Ai você quer limitar seu sistema para
aceitar somente esses tipos, ao invés de vc fazer diversos IF para validar cada
tipo de pagamento, você pode criar um ENUM=Enumerate(Em pt-br Enumerar).
Ou seja eu posso especificar qual tipo eu aceito e o próprio python valida.
Por exemplo:

class Pagar(Enum):
    credito = "crédito"
    debito = "débito"
    dinheiro = "dinheiro"

# quando eu for pagar eu uso da seguinte forma

pagamento = Pagar.credito
pagamento = Pagar.debito
pagamento = Pagar.dinheiro

# se eu colocar qualquer outra coisa, por exemplo: Pagar.transferencia eu terei um erro.

Link para auxiliar:
    https://www.tutorialspoint.com/enum-in-python

"""


class Genero(Enum):
    """Essa classe irá verificar/limitar o genero dos pokemons.
    Ou seja, só tem dois generos de pokemons, feminino e masculino"""

    FEMININO = auto()
    MASCULINO = auto()

    @staticmethod
    def decodificar(valor):
        for g in Genero:
            if g.name.lower() == valor:
                return g
        raise ValueError()

    def __str__(self):
        return self.name.lower()