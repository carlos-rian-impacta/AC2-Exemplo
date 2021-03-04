### Projeto Pókemon

Neste projeto iremos aprender a consultar API por meio da biblioteca requests e logo em seguida como usamos o framework flask para criarmos nossa propria API.

Nesta primeira parte nós iremos fazer alguns exercicios que serão para praticar e aprender um pouco mais sobre a biblioteca requests e testes automatizados usando Pytest.


### Configurando meu ambiente

1 - Entre na pasta [AC](AC/).

2 - Crie um ambiente virtual, usando o comando abaixo.
```sh
# esse comando irá criar uma pasta chamada .venv e dentro dela irá
# adicionar uma copia do seu python. O venv é muito util, pois você
# não precisa instalar as bibliotecas diretamente no seu python local.
python -m venv .venv
```
3 - Ative seu ambiente virtual.
```sh
# WINDOWS power shell
./.venv/Scripts/activate.psi

# Linux
source .venv/bin/activate

# Opcional atualize o gerenciador de pacotes.
pip install --upgrade pip
```

4 - Instale as dependências.
```sh
# esse comando irá instalar todas as libs que estão no arquivo requirements.txt
pip install -r requirements.txt
```

### Explicando Organização de Projeto

Nesse projeto temos duas pasta [dependencies](/dependencies) e [tests](/tests), perceba que dentro de dependencies tem alguns arquivos, em cada arquivo há um comentário explicando o que cada um faz e um link para te auxiliar em caso de dúvidas. Já na pasta tests há um arquivo chamado [tests.py](/tests/tests.py) nesse arquivo há todos os testes no qual o seu código precisa passar.

Quando você desenvolve algum software uma das preocupações é saber se o programa tem uma boa cobertura de código, isso é feito por meio de testes, ou seja, nós podemos enviar algumas informações para as funções e verificar se ela retorna o que de fato esperamos.

Por exemplo:
```python
# essa é uma função python que soma dois valores
def soma_dois_valores(valor1, valor2):
    return valor1 + valor2

# como podemos testa-la?
calculo = soma_dois_valores(5, 5)
# verifica se o retorno da função é igual ao valor esperado.
assert calculo == 10 # este teste irá passar, pois o retorno é igual a 10
# como testar com um caso de erro?
assert calculo == 11 # neste caso o código dará erro, pois calculo = 10 não é igual a 11.
```

Dentro da pasta raiz há o arquivo que de fato vai programar. Abra o arquivo [ac2.py](ac2.py) neste arquivo você vai seguir as instruções de como deve ser criada cada função.
Após você escrever uma função, você pode invocar ela chamando no próprio código ou executando os testes. Pois o que importa é ela passar nos testes! É por meio dos testes que eu irei verificar se seu código está ou não funcionando.

### Como executar os arquivos?

1 - Para executar seu código você pode digitar o comando abaixo.
```sh
python ac2.py
```

2 - Para executar os testes você pode digitar o comando abaixo.
```sh
pytest tests/
```
