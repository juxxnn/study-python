# Tipos de Dados (Data Types)

# String
# Uma string é uma sequência de caracteres.
print("Hello")  # Exemplo de uma string

# Para acessar um caractere específico de uma string, basta usar o índice do caractere entre colchetes.
print("Hello"[0])  # A resposta será H.

# Integer
# Um número inteiro é um número sem casas decimais.
print(5 + 5)  # 10

# Podemos usar underscores (_) para separar visualmente números grandes, mas eles não afetam o valor.
print(123_456_789)  # A resposta será 123456789

# Float
# Um número de ponto flutuante (float) é um número com casas decimais.
print(3.14)  # Exemplo de um float

# Boolean
# Um valor booleano é um dado que pode ser True (verdadeiro) ou False (falso).
print(True)
print(False)

# A função type() mostra o tipo de dados de uma variável ou valor.
num_char = len(input("Qual o seu nome? "))  # Pede o nome do usuário e calcula seu comprimento
print(type(num_char))  # Saída: <class 'int'>

# Comentário: print("Seu nome possui " + num_char + " caracteres.")
# No entanto, não podemos concatenar um número inteiro diretamente com uma string.
# Para resolver isso, podemos converter o número inteiro para uma string usando a função str().
new_num_char = str(num_char)
print("Seu nome possui " + new_num_char + " caracteres.")  # Saída correta

# Exemplo:
# Escreva um programa que soma os dígitos de um número de dois dígitos.
# Por exemplo, se a entrada for 35, a saída deve ser 3 + 5 = 8.
two_digit_number = input("Digite um número de dois dígitos: ")

# Antes de tudo, vamos verificar o tipo da entrada:
print(type(two_digit_number))  # Saída: <class 'str'>

# Convertendo cada dígito da string para inteiro
first_number = int(two_digit_number[0])
second_number = int(two_digit_number[1])

# Somando os dois dígitos
result = first_number + second_number
print(result)  # Exemplo: para entrada "35", a saída será 8

# Operações Matemáticas

print(3 + 5)  # Adição: 8
print(7 - 4)  # Subtração: 3
print(3 * 2)  # Multiplicação: 6
print(6 / 4)  # Divisão: 1.5 (A divisão em Python sempre retorna float.)
print(8 // 3)  # Divisão inteira: 2
print(2 ** 3)  # Exponenciação: 2 elevado a 3 é 8

# Para arredondar um número, podemos usar a função round()
print(8 / 3)  # Saída: 2.6666666666666665
print(round(8 / 3))  # Saída: 3
print(round(8 / 3, 2))  # Saída: 2.67 - arredondando para 2 casas decimais

# Operador de Atribuição com divisão
result = 4 / 2  # Resultado: 2.0
result /= 2  # Dividindo o resultado por 2; 2.0 / 2 = 1.0
print(result)  # Saída: 1.0

# Operador de Atribuição
score = 0
score += 1  # Incrementa score em 1; agora score é 1
print(score)  # Saída: 1

# f-String
# f-Strings permitem a inclusão de expressões dentro de strings.
score = 0
height = 1.8
isWinning = True

# O print abaixo não dará erro, mas a saída será em diferentes tipos de dados
print("Seus pontos são:", score)  # Saída: Seus pontos são: 0

# Para resolver isso de forma mais elegante, podemos usar f-Strings
print(f"Seus pontos são: {score}, sua altura é {height}, você está ganhando? {isWinning}")
# Saída: Seus pontos são: 0, sua altura é 1.8, você está ganhando? True