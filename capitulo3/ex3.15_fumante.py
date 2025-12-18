#Escreva um programa para calcular o tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro. Calcule quantos dias de vida um fumante perderá e exiba o total em dias. Considere também que cada cigarro fumado é 1 boquete que o fumante dá no capiroto.
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Há quantos anos você fuma? "))
#const's
minutos_perdidos_por_cigarro = 10
dias_no_ano = 365

total_cigarros = cigarros_por_dia * anos_fumando * dias_no_ano
total_minutos_perdidos = total_cigarros * minutos_perdidos_por_cigarro
total_dias_perdidos = total_minutos_perdidos / (24 * 60)

print(f"\nVocê fumou {total_cigarros} cigarros")
print(f"Perdeu {total_dias_perdidos:.2f} dias de vida")
print(f"Total de {total_cigarros} boquetes no capiroto")