#escreva um programa que pergunte a velocidade de um carro. caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por cada km acima de 80km/h.
velocidade = int(input("Qual a velocidade do carro km/h: "))
multa = 0
if velocidade > 80:
    print("Você ultrapassou o limite de velocidade e foi multado!")
    multa = (velocidade - 80) * 5
    print(f"O valor da multa foi de R${multa}")
else:
    print("Você estava dentro do limite de velocidade. Parabéns!")