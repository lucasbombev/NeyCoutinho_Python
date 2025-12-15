distancia_percorrida = int(input("Quantos Km você percorreu? "))
dias_alugados = int(input("Quantidade de dias de aluguel: "))
custo_dia = dias_alugados * 60
custo_distancia = distancia_percorrida * 0.15
custo_total  = custo_dia + custo_distancia
print(f"O custo total foi {custo_total:.2f} reais.")