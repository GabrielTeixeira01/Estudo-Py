#estruturar uma nota de  texto que vários usuários podem colaborar ao mesmo tempo
# Criar uma variavel para o título da nota
#Crie uma variável para o número de usuários online lendo a nota.
#Crie uma variável booleana chamada em_edicao, que deve ser verdadeira.
#Mude o valor da variável de usuários online somando mais 1 (simulando que alguém entrou)
#Imprima o título e o número atualizado de usuários

nota_titulo = "Colaboração em Tempo Real"

usuarios_online = 0

em_edicao = True

usuarios_online += 1

print(f"Título da nota: {nota_titulo}")
print(f"Número de usuários online: {usuarios_online}")