#Funcionario vai emendar a sua licença paternidade com as férias e precisar saber o tempo total de afastamento.
#1 Crie uma variável para o tempo de licença paternidade (em dias)
#2 Crie uma variável para o tempo de férias (em dias)
#3 Crie uma variável para o tempo total de afastamento (em dias) que será a soma das duas variáveis anteriores.
#4 usando f strings, exiba na tela o tempo total de afastamento.

licenca_parternidade = int(input("Digite o tempo de licença paternidade (em dias): ")) #Int, inteiro

tempo_ferias = int(input("Digite o tempo de férias (em dias): ")) #Int, inteiro

tempo_total_afastamento = licenca_parternidade + tempo_ferias #Int, inteiro

print(f"O tempo total de afastamento é de {tempo_total_afastamento} dias.")