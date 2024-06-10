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

