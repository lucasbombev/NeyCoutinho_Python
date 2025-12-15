#Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
distancia = int(input("Qual a distância que será percorrida em Km: "))
velocidade_media = int(input("Qual a velocidade média esperada para a viagem Km/h?  "))
tempo = distancia / velocidade_media
print(f"De acordo com os dados que você me forneceu, você chegará ao destino em {tempo} horas.")