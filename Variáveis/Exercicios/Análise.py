#Criar uma base de dados para um dashboard de faturamento empresarial.
#1 Crie uma variável para o faturamento mensal (decimal).

#2 Crie uma variável para a quantidade de novos clientes no mês (inteiro).

#3 Crie uma variável que calcule o ticket médio (faturamento dividido pela quantidade de novos clientes).

#4Exiba uma mensagem usando f-string mostrando todos os dados.

faturamento_mental =  float(input("Digite o faturamento mensal: "))   #tipo de variável float, decimal
quantidade_novos_clientes = int(input("Digite a quantidade de novos clientes: "))   #tipo de variável int, inteiro

ticket_medio = faturamento_mental / quantidade_novos_clientes #tipo de variável float, decimal

print(f"Faturamento mensal: R$ {faturamento_mental:.2f}")
print(f"Quantidade de novos clientes: {quantidade_novos_clientes}")
print(f"Ticket médio: R$ {ticket_medio:.2f}")