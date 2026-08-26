#perguntar se tem carteira de motorista, se for menor de idade, informar que não pode tirar carteira, se for maior de idade, informar que pode tirar carteira.

idade = int(input("Qual é a sua idade?"))

if idade < 18:
    print("Você não pode tirar carteira de motorista.")

else:
    print("Você pode tirar carteira de motorista.")

