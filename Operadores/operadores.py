
# Aritméticos: +, -, *, /, // (divisão inteira), % (resto), ** (potência).
#Comparação: ==, !=, >, <, >=, <=.
#lógicos: and, or, not.
#atribuição: =, +=, -=, *=, /=, //=, %=, **=.

#Aritméticos
a = 20
b = 10

print(f"a + b = {a + b}") # Soma
print(f"a - b = {a - b}") # Subtração
print(f"a * b = {a * b}") # Multiplicação
print(f"a / b = {a / b}") # Divisão
print(f"a // b = {a // b}") # Divisão inteira
print(f"a % b = {a % b}") # Resto
print(f"a ** b = {a ** b}") # Potência

#Comparação

print(f"a == b: {a == b}") # Igualdade
print(f"a != b: {a != b}") # Diferença
print(f"a > b: {a > b}") # Maior que
print(f"a < b: {a < b}") # Menor que
print(f"a >= b: {a >= b}") # Maior ou igual
print(f"a <= b: {a <= b}") # Menor ou igual

#Lógicos

idade = 20
tem_carteira = True
print(f"idade >= 18 and tem_carteira: {idade >= 18 and tem_carteira}") 
# Verdadeiro se idade >= 18 e tem_carteira for True
print(f"idade >= 18 or tem_carteira: {idade >= 18 or tem_carteira}")
 # Verdadeiro se idade >= 18 ou tem_carteira for True  

print(f"not tem_carteira: {not tem_carteira}")
 # Verdadeiro se tem_carteira for False

#Atribuição

pontos = 10

pontos += 5 # pontos = pontos + 5
pontos -= 3 # pontos = pontos - 3
pontos *= 2 # pontos = pontos * 2

print(f"pontos: {pontos}") # Exibe o valor final de pontos