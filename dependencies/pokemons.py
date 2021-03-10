"""
No python é bastante comum você criar uma classe que tem N métodos.
O método é a mesma coisa que as funções, porém dentro de classes.

As funções são criadas para serem usadas diretamenta, 
já os métodos só podem ser usados quando a classe é instânciada(criada).

Nas classe nós podemos receber diversos parâmetros assim como na funções.
Para isso a gente especifica estes parâmetros no método "especial" __init__.

Este método é responsável por iniciar a classe. Onde o primeiro param você não precisa informar.
Por convenção, o self é um parâmetro default da classe, ou seja o self quer dizer que é a própria instância da classe.

Confuso né?

Vamos dá um exemplo. Imagine a classe pessoa, essa classe recebe o nome e idade de alguém.

class Pessoa:
    def __init__(self, nome, idade):
        # veja que eu não uso o self.self = self. Isso porque o self é a própria classe.
        # então o que eu faço é o seguinte, para cada parâmetro (nome, idade), eu crio um
        # objeto(variavel) dentro da minha classe, que só pode ser usado aqui dentro.
        self.nome = nome
        self.idade = idade
   
    # Vamos criar um método que retorna o nome de uma pessoa.
    # Veja que a gente só passa o argumento self no método.
    # Por quê? porque no __init__ a nós já pegamos o valor de nome e colocamos o mesmo dentro do self.nome. 
    def pegar_nome(self):
        # então podemos retornar desta forma.
        return self.nome

# Para testar
# crie uma variável que vai instânciar(criar) a classe
pessoa = Pessoa("João", 60)
# pegue o nome da pessoa
print(pessoa.pegar_nome())

Video para auxiliar: 
    https://www.youtube.com/watch?v=RLVbB91A5-8
    https://www.youtube.com/watch?v=j6B8shHXzks

"""


class Pokemon:
    """
    Agora, nós implementaremos alguns métodos desta classe (Pokemon).
    Não deve-se confundí-la com EspeciePokemon.
    Vamos supor que você tenha dois pokémons da espécie Ponyta.
    Para diferenciá-los, decida chamar um de "veloz" e o outro de
    "ligeirinho".
    Seu amigo também tem uma Ponyta, que ele chama de "quentinha".
    Nesse caso, "veloz", "ligeirinho" e "quentinha" são três Ponytas
    diferentes, pertencentes a dois treinadores diferentes.
    Além disso, esses diferentes pokémons, embora da mesma espécie,
    também podem ser de sexos diferentes e com diferentes quantidades
    de pontos de experiência.
    """

    def __init__(self, nome_treinador, apelido, tipo, experiencia, genero):
        if experiencia < 0:
            raise ValueError()
        self.__nome_treinador = nome_treinador
        self.__apelido = apelido
        self.__tipo = tipo
        self.__experiencia = experiencia
        self.__genero = genero

    # Não mexa nisso.
    def __setattr__(self, attr, value):
        if attr.find("__") == -1:
            raise AttributeError(attr)
        super().__setattr__(attr, value)

    @property
    def nome_treinador(self):
        return self.__nome_treinador

    @property
    def apelido(self):
        return self.__apelido

    @property
    def tipo(self):
        return self.__tipo

    @property
    def experiencia(self):
        return self.__experiencia

    @property
    def genero(self):
        return self.__genero