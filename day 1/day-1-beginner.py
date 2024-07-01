# Day 1 - Beginner
# Trabalhando com variáveis em Python para gerenciar dados.

# A função print() é usada para imprimir texto na tela.
print("Hello World!")  # Exemplo básico de uso do print

# Modificadores de Print
# Para incluir aspas dentro de uma string, podemos usar várias abordagens:
print("Ela disse \"Oi\" e foi embora")  # Usando barras invertidas para escapar das aspas
print('Ela disse "Oi" e foi embora')  # Usando aspas simples para delimitar a string
print("Ela disse 'Oi' e foi embora")  # Usando aspas duplas para delimitar a string

# Manipulação de strings
# O \n é utilizado para quebrar linha dentro de uma string.
print("Oi!\nTudo bem?")  # "Oi!" será impresso em uma linha e "Tudo bem?" na linha seguinte

# O operador + é usado para concatenar (juntar) strings.
print("Meu nome é " + "Juliana")  # Resultado: "Meu nome é Juliana"

# A função input() é usada para receber dados do usuário.
name = input("What is your name? ")
print(name)  # Imprime o nome inserido pelo usuário

# Podemos combinar input e print em uma única linha.
print('Hello ' + input('Qual o seu nome? ') + "!")  # Pede o nome e imprime uma saudação

# A função len() retorna o comprimento de uma string (número de caracteres).
name = input("What is your name? ")  # Pede o nome do usuário
length = len(name)  # Calcula o comprimento do nome
print(length)  # Imprime o comprimento do nome

# Variáveis
# Uma variável é um objeto (frequentemente localizado na memória) que pode reter e representar uma expressão.
# Ela pode ser alterada ao longo do tempo, ou seja, é variável.

# Exemplos de restrições ao nomear variáveis:
# - Não podem começar com um número.
# - Não podem conter espaços em branco.
# - Não podem conter caracteres especiais como @, #, $, etc.
# - Não podem ser palavras reservadas do Python, como "print", "input", "if", etc.

# Exemplo de variável
name = "Juliana"  # Atribui o valor "Juliana" à variável name

# Variáveis globais e locais:
# - Variáveis globais podem ser acessadas em qualquer parte do código.
# - Variáveis locais só podem ser acessadas no bloco de código onde foram criadas.