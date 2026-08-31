#Um servidor (ou módulo hardware) retorna o tempo que está ligado em segundos totais.
#  Você precisa converter isso para um formato legível.

#1 criar uma varial total_segundos = 10000
#2 Calcule quantas horas inteiras cabem nesses segundos (use //).
#3 calcule quantos minutos inteiros sobram 
#4 calcule quantos segundos sobram no final.
#imprima no formato: x horas, y minutos e z segundos

total_segundos = 10000

horas = int(total_segundos // 3600)

minutos = int((total_segundos % 3600) // 60) #calcula os minutos restantes após as horas

segundos_finais = int(total_segundos % 60) #calcula os segundos restantes após as horas e minutos

print(f"{horas} horas, {minutos} minutos e {segundos_finais} segundos") 