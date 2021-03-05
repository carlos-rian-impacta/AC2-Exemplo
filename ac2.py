from dependencies.errors import (
    PokemonJaCadastradoException,
    PokemonNaoCadastradoException,
    PokemonNaoExisteException,
    TreinadorNaoCadastradoException,
)
from requests import api
from dependencies.cache import cached

site_pokeapi = "http://pokeapi.co"

"""
caminhos da url que você pode usados.
# para pegar os dados de um pokemon, usando id ou nome
{site_pokeapi}/api/v2/pokemon/{id_pokemon or name}/

# para pegar a especie de um pokemon, usando id ou nome
{site_pokeapi}/api/v2/pokemon-species/{id_pokemon or name}/

# o id evolution não é o mesmo que o id_pokemon 
# essa url você encontra quando busca pokemon.
{site_pokeapi}/api/v2/evolution-chain/{id_evolution_chain}/ 

# para pegar a base experiência, o id_growth vai de 1 à 6
{site_pokeapi}/api/v2/growth-rate/{id_growth}/
"""

# Questão 1
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
    response = api.get(uri)
    if response.status_code != 200:
        raise PokemonNaoExisteException()
    return response.json()["name"]


# Questão 2
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


# Questão 3
@cached
def color_of_pokemon(nome):
    """
    3. Dado o nome de um pokémon, qual é o nome da cor (em inglês) predominante dele?

    Dica:
    As vezes ele pode dá erro quando usamos o nome então  use a função anterior
    para pegar o ID do pókemon, depois busque a cor usando a url abaixo.

    url: {site_pokeapi}/api/v2/pokemon-species/{id_pokemon or name}

    Observações:
    - Não se esqueça de verificar os casos onde o pokémon procurado não exista.
    """
    if not nome:
        raise PokemonNaoExisteException()

    id_pokemon = numero_do_pokemon(nome)
    url = f"{site_pokeapi}/api/v2/pokemon-species/{id_pokemon}/"
    response = api.get(url=url)
    if response.status_code != 200:
        raise PokemonNaoExisteException()
    return response.json()["color"]["name"]


# Questão 4
@cached
def cor_do_pokemon(nome):
    """
    4. Dado o nome de um pokémon, qual é o nome da cor (em português) predominante dele?

    Observações:
    - Os nomes de cores possíveis de pokémons em português são APENAS as
    ["marrom", "amarelo", "azul", "rosa", "cinza", "roxo", "vermelho", "branco", "verde" e "preto"]
    - No entanto, a pokeapi ainda não foi traduzida para o português! Como você pode dar um jeito nisso?

    Dicas:
    - O que os dicionários do python e os dicionários que você compra em livrarias têm em comum além do nome?
    - Faça uma invocação à função color_of_pokemon acima.
    - Não esqueça de verificar se o pokemon não existir.
    """
    raise Exception("Não implementado!")


# Questão 5
@cached
def tipos_do_pokemon(nome):
    """
    5. Dado o nome de um pokémon, quais são os tipos no qual ele se enquadra?
    Os nomes dos tipos de pokémons em português são:
    [
        "normal", "lutador", "voador", "veneno", "terra",
        "pedra", "inseto", "fantasma", "aço", "fogo", "água",
        "grama", "elétrico", "psíquico", "gelo", "dragão", "noturno" , "fada"
    ]
    Todo pokémon pode pertencer a um ou a dois tipos diferentes.
    caso o pokemon exista, você deve retornar uma lista contendo os tipos,
    mesmo que haja somente um tipo.
    Se houver dois tipos, a ordem não é importante.

    Observações:
    - Não se esqueça de verificar os casos onde o pokémon procurado não exista.
    - Assim como na função anterior que você precisou criar um dicionario,
      mapeando as cores, você também precisará mapears os tipor para português.
    Dica: no dict você pode criar um dict mais ou menos assim.
        types = {"dragon": "dragão", "ice": "gelo", "psychic":"psíquico" ...}
    """
    raise Exception("Não implementado!")


# Questão 6
@cached
def evolucao_anterior(nome):
    """
    6. Dado o nome de um pokémon, liste de qual pokémon ele evoluiu.
    Por exemplo, evolucao_anterior('venusaur') == 'ivysaur'
    Retorne None se o pokémon não tem evolução anterior. Por exemplo, evolucao_anterior('bulbasaur') == None

    Observações:
    - Não se esqueça de verificar os casos onde o pokémon procurado não exista e retorne a exceção
    Dica: A chave onde tem a evolução é "evolves_from_species"
    """
    raise Exception("Não implementado!")


# Nova Questão 7
def movimentos_pokemon(nome, qtde_mov):
    """
    7. Esta função recebe o nome de um pokemon e uma quantidade de movimentos que ele pode fazer.
    Então dado um nome de um pokemon, você deve retorne uma lista contendo os movimentos.
    Esta lista deve conter os movimentos do pokemon da posição 0 até a qtde_mov que é passada como parâmetro.
    Por exemplo:
        nome = "bulbasaur"
        qtde_mov = 5
        # Então eu devo consultar a api, e pegar os primeiros 5 movimentos.
        #                  mov1           mov2       mov3   mov4       mov5
        movimentos = ["razor-wind", "swords-dance", "cut", "bind", "vine-whip"]
    Observação:
        Não se esqueça de verificar os casos onde o pokémon procurado não exista.
        Caso a quantidade seja um número negativo ou menor que zero.
    """
    raise Exception("Não implementado!")


# Questão 8
@cached
def evolucoes_proximas(nome):
    """
    8. Dado o nome de um pokémon, liste para quais pokémons ele pode evoluiur.
    Por exemplo, evolucoes_proximas('ivysaur') == ['venusaur'].
    A maioria dos pokémons que podem evoluir, só podem evoluir para um único tipo de pokémon próximo.
    No entanto, há alguns que podem evoluir para dois ou mais tipos diferentes de pokémons.
    Se houver múltiplas possibilidades de evoluções, a ordem delas não importa.
    Por exemplo:
        evolucoes_proximas('poliwhirl') == ["poliwrath", "politoed"]
        evolucoes_proximas('poliwhirl') == ["raichu"]
        evolucoes_proximas('celebi') == []
    Se o pokémon não evolui, retorne uma lista vazia como no exemplo celebi.

    Observações:
    - Não se esqueça de verificar os casos onde o pokémon procurado não exista.

    Dicas:
    - Este é um item bônus de desafio e deve ser um dos exercícios mais difíceis deste AC.
      Isso significa que mesmo que você não consiga, ainda dá para tirar 10.
    - Se quiser desistir do bônus, basta colocar um "return []" como sendo o código disto.
    - Possivelmente o JSON que a API irá te devolver será um pouco mais complicado de analisar.
    - Possivelmente você terá que fazer 2 ou mais requisições aqui.

    - Porém caso queira, segue uma dica.
    - Para pegar a evolução do pokemon, você deve pegar primeiro a url que está na chave
     "evolution_chain" e depois fazer uma nova requisição.
      essa chave está nas species...
      O restante é por sua conta, boa sorte.
    # Caso queira testar sua função, altere o nome do arquivos
    # /tests/_test_08_evolucoes_proximas.py para /tests/test_08_evolucoes_proximas.py
    # Ou seja remova o underline!
    """
    raise Exception("Não implementado!")
