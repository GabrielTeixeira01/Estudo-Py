#Você está programando o código de um microcontrolador (como um módulo ESP32) e precisa guardar as
#leituras dos  sensores em  variáveis.

#1 Crie uma variável para o modelo da placa (texto)
#2 crie uma vairave para o nivel da bateria em porcentagem (inteiro)
#3 Crie uma variável booleana indicando se o dispositivo precisa ser recarregado 
# (True se a bateria for menor que 20%, caso contrário, False).
#4 exista status final na tela 

modelo_placa = input("Digite o modelo da placa: ") #String, texto

nível_bateria = int(input("Digite o nível da bateria em porcentagem: ")) #Int, inteiro

if nível_bateria <20:
    precisa_recarregar = True
else:
    precisa_recarregar = False

print(f"Modelo da placa: {modelo_placa}, Nível da bateria: {nível_bateria}%, Precisa ser recarregado: {precisa_recarregar}")