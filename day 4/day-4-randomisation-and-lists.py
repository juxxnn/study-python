#Modulo

# O módulo random fornece funções para gerar números aleatórios em Python.
# Importando o módulo random para gerar números aleatórios
import random

#Random

# Gera um número inteiro aleatório entre 1 e 10
# random.randint(1, 10): random é o módulo que importamos anteriormente. randint é uma função dentro do módulo random que gera números inteiros aleatórios. O primeiro argumento (1) é o menor valor possível que pode ser gerado, e o segundo argumento (10) é o maior valor possível que pode ser gerado. 
random_integer = random.randint(1, 10)
print(random_integer)

# Gera um número float aleatório entre 0.0 e 5.0
random_float = random.random() * 5
print(random_float) # Exibe o número float aleatório gerado

# Simula lançamento de uma moeda
random_number = random.randint(0, 1)

if random_number == 1:
  print("Heads")
else:
  print("Tails")

# Listas
# Listas possui ordem

fruits = ['banana', 'apple', 'strawberry']

print(fruits[2])  # Exibe o terceiro elemento da lista ('strawberry')
print(fruits[-1])  # Exibe o último elemento da lista ('strawberry')

#Append: Anexe o objeto ao final da lista.
fruits.append('kiwi')
print(fruits) #banana, apple, strawberry, kiwi

#Extend:  Estenda a lista anexando elementos do iterável. o método extend() em Python é específico para listas.
fruits.extend(['mango', 'lemon', 'orange'])
print(fruits) #banana, apple, strawberry, kiwi, mango, lemon, orange

# Len: Obtendo o comprimento (número de elementos) da lista
num_fruits = len(fruits)
print(num_fruits) #7 
# print(fruits[num_fruits]) #Dará erro, pois a contagem começa com 0-6, não existe 7, estará fora do intervalo

print(fruits[num_fruits - 1]) #Subtraindo por - 1, conseguimos acessar o sétimo item da lista que está na posição 6



# Escolhendo aleatoriamente um nome de uma lista de nomes fornecida pelo usuário
names_string = input("Enter names separated by comma: ")
# O método split(", ") é aplicado à string names_string. Ele divide a string em substrings sempre que encontra uma vírgula seguida por um espaço ", ", criando uma lista com os nomes fornecidos pelo usuário.
names = names_string.split(", ")  # Converte a string de nomes em uma lista

num_items = len(names) # Obtém o número de itens (nomes) na lista

random_choice = random.randint(0, num_items - 1)  # Escolhe aleatoriamente um índice da lista de nomes
print(f"{names[random_choice]} is going to buy the meal today!")  # Exibe o nome escolhido aleatoriamente


# Listas Aninhadas
# Uma lista aninhada em Python é uma lista que contém outras listas como seus elementos. 

# Definindo listas de frutas e vegetais
fruits_list = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables_list = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Criando uma lista aninhada que contém as listas de frutas e vegetais

dirty_dozen = [fruits_list, vegetables_list]
print(dirty_dozen) #Teremos 3 listas, 1 lista [] com 2 listas dentro [[] []]

# [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'], ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]


# Método lower()
# O método lower() é utilizado em strings para converter todos os caracteres para minúsculas.

# Exemplo do método lower()
message = "Olá Mundo"
lower_message = message.lower()
print(lower_message)  # Saída: "olá mundo"


# Método upper()
# O método upper() é usado para converter todos os caracteres de uma string em letras maiúsculas.

# Exemplo do método upper()
message = "olá mundo"
upper_message = message.upper()
print(upper_message)  # Saída: "OLÁ MUNDO"


# Método index()
# O método index() em Python é usado para encontrar a posição da primeira ocorrência de uma substring dentro de uma string. É como procurar a primeira vez que uma palavra específica aparece em um texto.

# Exemplo do método index()
sentence = "A casa é muito bonita e a vista é maravilhosa"
index_bonita = sentence.index("bonita")
print(index_bonita)  # Saída: 14 - Neste caso, "bonita" começa na posição 14 da string sentence.

# Método count()
# O método count() é usado para contar quantas vezes uma substring específica aparece dentro de uma string. É como contar quantas vezes uma palavra específica aparece em um texto.

# Exemplo do método count()
sentence = "A casa é muito bonita e a vista é maravilhosa"
count_a = sentence.count("a")
print(count_a)  # Saída: 6

# Diferença entre count() e len()
# count(): Conta quantas vezes uma substring específica ocorre dentro de uma string.
# len(): Retorna o número total de caracteres em uma string, ou o número total de elementos em uma lista.