# Condição if/else
# A estrutura if em Python permite executar um bloco de código se uma condição for verdadeira. Se a condição não for verdadeira, o bloco de código dentro do else é executado (se existir).

print("Welcome to the rollercoaster!")
height = int(input("What is our height in cm? "))

# Verifica se a altura é maior que 120 cm
if height > 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  
  # Verifica a idade para determinar o preço do ingresso
  if age <= 18:
      print("Please pay $7.")  # Se idade <= 18, paga $7
  else:
      print("Please pay $12.")  # Se idade > 18, paga $12
else:
    print("Sorry, you have to grow taller before you can ride.")  # Se altura <= 120 cm


# Condição elif
# A estrutura elif (abreviação de "else if") é usada para verificar múltiplas condições sequencialmente após um if. Se a condição anterior for falsa, ele verifica a próxima condição elif.

# Verifica se a altura é maior que 120 cm
if height > 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
    
  # Verifica a idade para determinar o preço do ingresso
  if age < 12:
      print("Please pay $5.")  # Se idade < 12, paga $5
  elif age <= 18:
      print("Please pay $7.")  # Se idade <= 18, paga $7
  else:
      print("Please pay $12.")  # Se idade > 18, paga $12
else:
    print("Sorry, you have to grow taller before you can ride.")  # Se altura <= 120 cm


# Operadores de Comparação 
# Os operadores de comparação são utilizados para comparar valores. Eles retornam um valor booleano (True ou False) dependendo da condição.

# > maior que
# < menor que
# >= maior ou igual
# <= menor ou igual
# == é igual
# != é diferente

# Exemplo de uso:
number = int(input("Digite um número: "))
if number % 2 == 0:
  print("O número é par.")
else:
  print("O número é ímpar.")


# Múltiplos if
# Múltiplos if permitem verificar várias condições independentes em um programa.

print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

bill = 0

# Verifica o tamanho da pizza para determinar o preço base
if size == 'S':
  bill = 15
elif size == 'M':
  bill = 20
elif size == 'L':
  bill = 25

# Verifica se o usuário quer adicionar pepperoni e ajusta o preço se necessário
if add_pepperoni == 'Y':
  if size == 'S':
    bill += 2
  else:
    bill += 3

# Verifica se o usuário quer adicionar queijo extra e ajusta o preço se necessário
if extra_cheese == 'Y':
  bill += 1

print(f"Your final bill is: ${bill}.")

# Operadores Lógicos
# Os operadores lógicos (and, or, not) são usados para combinar condições booleanas.


# Exemplos de operadores lógicos
# and (e): retorna True se ambas as condições forem verdadeiras
# or (ou): retorna True se pelo menos uma das condições for verdadeira
# not (não): inverte o valor booleano de uma expressão

# Exemplo de uso:

number = 5
if number > 0 and number <= 10:
  print("O número está entre 1 e 10.")

if not (number > 0 and number <= 10):
  print("O número não está entre 1 e 10.")
