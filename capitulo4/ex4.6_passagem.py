# escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 km e R$0,45 para viagens mais longas.
distancia = int(input("Qual será a distância percorrida em Km: "))
viagem_curta = distancia * 0.50
viagem_longa = distancia * 0.45
if distancia > 200:
    print(f"Sua viagem é longa e você receberá um pequeno desconto por Km rodado.\ncom a distância percorrida de {distancia} o valor da sua passagem fica R${viagem_longa:.2f}")
else:
    print(f"Sua viagem é curta e você receberá o valor cheio por km rodado.\ncom a distância percorrida de {distancia} o valor da sua passagem fica R${viagem_curta:.2f} ")