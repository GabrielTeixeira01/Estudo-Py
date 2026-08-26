#while , for, break, continue, pass

# While , loop de repetição, enquanto a condição for verdadeira, ele vai executar o bloco de código.
# for , loop de repetição, para cada elemento da sequência, ele vai executar o bloco de código.
# break , sai do loop.
# continue , pula para a próxima iteração do loop.
# pass , não faz nada, é um placeholder.

numero = 1

while numero <= 10:
    print(numero)
    numero += 1
    #ENQUANTO numero for menor ou igual a 5 → continue repetindo.


    for numero in range(1, 11):
        print(numero)
        #PARA cada numero de 1 a 10 → continue repetindo.

        for numero in range(1, 11):

            if numero == 5:
                break
                #SE numero for igual a 5 → saia do loop.

            print(numero)



for numero in range(1, 11):

    if numero == 5:
        continue
        #SE numero for igual a 5 → pule para a próxima iteração do loop.

    print(numero)



    

    idade = 18

    if idade < 18:
        pass
        #SE idade for menor que 18 → não faça nada.
