#Em um sistema de banco de dados, precisa inverter os valores de duas variáveis.
#1 crie x = 10 e y = 99
#2 O desafio: Faça o valor de x passar a ser 99 e o de y passar a ser 10, sem digitar os números 10 e 99 de novo.
#(Dica: Você pode criar uma terceira variável temporária ou usar um truque exclusivo do Python).

x = 10 
y = 99

x, y = y, x # Invertendo os valores
print(f"Valor de x: {x}, Valor de y: {y}")