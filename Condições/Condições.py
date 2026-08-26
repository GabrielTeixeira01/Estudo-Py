#Estruturas Condicionais
#If, else, elif
#if , condição verdadeira, executa o bloco de código.
#else , condição falsa, executa o bloco de código.
#elif , condição intermediária, executa o bloco de código.

nota = float(input("digite sua nota: "))

if nota >=  9.0:
    print("Execelente")

elif nota >= 7.0:
    print("Aprovado")

else:
    print("Reprovado")