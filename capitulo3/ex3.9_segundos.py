#escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
all_in_second = segundos + (minutos * 60) + (horas * 3600) + (dias * 86400)
print(f"O total de tempo em segundos foi {all_in_second}")
