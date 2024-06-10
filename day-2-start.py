#Data Types

#String 

print("Hello")

#Para acessar um caractere específico de uma string, basta colocar o número correspondente ao caractere

print("Hello"[0])
#A resposta será H.

#Integer

print(5 + 5)

#Podemos usar _ para separar números grandes

print(123_456_789)
#A resposta será 123456789

#Float

#Números com casas decimais

print(3.14)

#Boolean

True
False

#A função type() irá mostrar o tipo de dados.

num_char = len(input("Qual o seu nome? "))

#  ---> print("Seu nome possui " + num_char + " caracteres.")

#Porém, nesse caso acima não é possível imprimir um número inteiro com uma string.
#Podemos usar str() para converter para string.

new_num_char = str(num_char)

print("Seu nome possui " + new_num_char + " caracteres.")

# Exemplo:
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input()

# Antes verificamos o type: 

print(type(two_digit_number))
first_number = int(two_digit_number[0])
second_number = int(two_digit_number[1])

two_digit_number = first_number + second_number
print(two_digit_number)

# Operações Matemáticas 

3 + 5
7 - 4
3 * 2
6 / 4 #A divisão em Python sempre retorna float.
8 // 3 #Para obter o resultado de número inteiro.
2 ** 3 #2 elevado a 3.

#Para arredondar um número podemos utilizar a função round()

print(8/3) #2.6666666666666665
print(round(8/3)) #3
print(round(8/3, 2)) #2.67 - nesse caso usamos após a vírgula a quantidade de casas decimais.

#Nesse caso abaixo, o '/=' irá dividir o resultado por 2
result = 4 / 2 #2.0
result /= 2 #2.0 / 2 = 1.0
print(result)

# Operador de Atribuição

score = 0 
score += 1 #O resultado é 1

#f-String

score = 0
height = 1.8
isWinning = True

# O print abaixo dará erro, pois não podemos imprimir string com int
print("Seus pontos são: ", score)

#Para resolver isso podemos usar o f-String

print(f"Seus pontos são: {score}, sua altura é {height}")
