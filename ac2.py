from dependencies.errors import (
    PokemonJaCadastradoException,
    PokemonNaoCadastradoException,
    PokemonNaoExisteException,
    TreinadorNaoCadastradoException,
)
from requests import api
from dependencies.cache import cached

site_pokeapi = "http://pokeapi.co"


@cached
def nome_do_pokemon(numero):
    """
    1. Dado o número de um pokémon, qual é o nome dele?

    Observações:
    - Presuma que nunca irá existir mais do que 5000 pokémons
    diferentes.
    - Também não existe pokémon de número zero ou negativo.
    - Assim sendo, nem precisa fazer a requisição nesses casos.
    - Se o pokémon não existir, lance uma PokemonNaoExisteException.
    """
    if numero < 1 or numero >= 5000:
        raise PokemonNaoExisteException()
    uri = f"{site_pokeapi}/api/v2/pokemon/{numero}"
    data = api.get(uri)
    if data.status_code != 200:
        raise PokemonNaoExisteException()
    return data.json()["name"]


@cached
def numero_do_pokemon(nome):
    """
    2. Dado o nome de um pokémon, qual é o número dele?

    Observações:
    - Não se esqueça de verificar os casos onde o pokémon procurado não exista (PokemonNaoExisteException).
    """
    if not nome:
        raise PokemonNaoExisteException()
    uri = f"{site_pokeapi}/api/v2/pokemon/{nome}"
    data = api.get(uri)
    if data.status_code != 200:
        raise PokemonNaoExisteException()
    return data.json()["id"]


@cached
def color_of_pokemon(nome):
    """
    3. Dado o nome de um pokémon, qual é o nome da cor (em inglês) predominante dele?

    Observações:
    - Não se esqueça de verificar os casos onde o pokémon procurado não exista.
    """
    raise Exception("Não implementado.")


@cached
def cor_do_pokemon(nome):
    """
    4. Dado o nome de um pokémon, qual é o nome da cor (em português) predominante dele?

    Observações:
    - Os nomes de cores possíveis de pokémons em português são APENAS as "marrom", "amarelo", "azul", "rosa", "cinza", "roxo", "vermelho", "branco", "verde" e "preto".
    - No entanto, a pokeapi ainda não foi traduzida para o português! Como você pode dar um jeito nisso?

    Dicas:
    - O que os dicionários do python e os dicionários que você compra em livrarias têm em comum além do nome?
    - Faça uma invocação à função color_of_pokemon acima.
    """
    raise Exception("Não implementado.")


@cached
def tipos_do_pokemon(nome):
    """
    5. Dado o nome de um pokémon, quais são os tipos no qual ele se enquadra?
    Os nomes dos tipos de pokémons em português são "normal", "lutador", "voador", "veneno", "terra", "pedra", "inseto", "fantasma", "aço", "fogo", "água", "grama", "elétrico", "psíquico", "gelo", "dragão", "noturno" e "fada".
    Todo pokémon pode pertencer a um ou a dois tipos diferentes. Retorne uma lista (ou um set ou uma tupla ou coisa similar, se preferir) contendo os tipos, mesmo que haja somente um.
    Se houver dois tipos, a ordem não é importante.

    Observações:
    - Não se esqueça de verificar os casos onde o pokémon procurado não exista.
    """
    raise Exception("Não implementado.")


@cached
def evolucao_anterior(nome):
    """
    6. Dado o nome de um pokémon, liste de qual pokémon ele evoluiu.
    Por exemplo, evolucao_anterior('venusaur') == 'ivysaur'
    Retorne None se o pokémon não tem evolução anterior. Por exemplo, evolucao_anterior('bulbasaur') == None

    Observações:
    - Não se esqueça de verificar os casos onde o pokémon procurado não exista.
    """
    raise Exception("Não implementado.")


@cached
def evolucoes_proximas(nome):
    """
    7. Dado o nome de um pokémon, liste para quais pokémons ele pode evoluiur.
    Por exemplo, evolucoes_proximas('ivysaur') == ['venusaur'].
    A maioria dos pokémons que podem evoluir, só podem evoluir para um único tipo de pokémon próximo. No entanto, há alguns que podem evoluir para dois ou mais tipos diferentes de pokémons.
    Se houver múltiplas possibilidades de evoluções, a ordem delas não importa. Por exemplo:
    evolucoes_proximas('poliwhirl') == ['poliwrath', 'politoed']
    Note que esta função dá como resultado somente o próximo passo evoluitivo. Assim sendo, evolucoes_proximas('poliwag') == ['poliwhirl']
    Se o pokémon não evolui, retorne uma lista vazia. Por exemplo, evolucoes_proximas('celebi') == []

    Observações:
    - Não se esqueça de verificar os casos onde o pokémon procurado não exista.

    Dicas:
    - Este é um item bônus de desafio e deve ser um dos exercícios mais difíceis deste AC. Isso significa que mesmo que você não consiga, ainda dá para tirar 10.
    - Se quiser desistir do bônus, basta colocar um "return []" como sendo o código disto.
    - Possivelmente o JSON que a API irá te devolver será algo bem complicado de analisar.
    - Possivelmente você terá que fazer 2 ou mais requisições aqui.
    - Uma forma de resolver este exercício inclui utilizar recursão.
    """
    raise Exception("Não implementado.")


def nivel_do_pokemon(nome, experiencia):
    """
    8. A medida que ganham pontos de experiência, os pokémons sobem de nível.
    É possível determinar o nível (1 a 100) em que um pokémon se encontra com base na quantidade de pontos de experiência que ele tem.
    Entretanto, cada tipo de pokémon adota uma curva de level-up diferente (na verdade, existem apenas 6 curvas de level-up diferentes).
    Assim sendo, dado um nome de pokémon e uma quantidade de pontos de experiência, retorne o nível em que este pokémon está.
    Valores negativos de experiência devem ser considerados inválidos.

    Observações:
    - Não se esqueça de verificar os casos onde o pokémon procurado não exista.
    - Lance uma exceção ValueError para os casos onde o valor da experiência é negativo.
    - Não realize os cálculos diretamente nesta função implementando nela alguma fórmula matemática. Utilize a API para fazer os cálculos.
    """
    raise Exception("Não implementado.")
