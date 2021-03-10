from functools import wraps

""" 
No python nós conseguimos criar uma função que guarda cache.
Mas primeiro, o que é um cache? O cache é uma forma mais rápida de buscar um valor
Se a entrada é a mesma.

Por exemplo: Imagine que eu tenho uma função que recebe sempre um parâmetro.

# se a gente mandar chamar essa função 10 vezes com o mesmo valor, você concorda
# que a resposta é a mesma? tipo se eu passar 10 então eu recebo 11.
def adicione_mais_1(numero):
    return numero + 1

O cache ele faz o seguinte, ele armazena sempre a entrada e a saida da função.
Pois caso você já tenha enviado 10 uma vez e vai te retornar 11.
Para isso a gente usa uma variavel do tipo dict que armazena a entra e saida.
sendo a entrada a chave e a saida o valor.

Por exemplo: cache = {10: 11} ai toda vez que ele for entrar na função, 
ele verifica se o 10 (número) já existe no dict.

Video para auxiliar:
    https://www.youtube.com/watch?v=AyZbZAzaJIs

"""


def cached(what):
    cache = {}

    @wraps(what)
    def caching(n):
        if n not in cache:
            cache[n] = what(n)
        return cache[n]

    return caching