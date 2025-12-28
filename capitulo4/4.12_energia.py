# escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências. I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela do livro.
consumo = int(input("Qual o consumo de energia elétrica mensal em kWh: "))
tipo = input("Qual o tipo de instalação?\nR para residências\nI para indústricas\nC para comércios\n:").upper()
if tipo not in ["R","I","C"]:
    print("Tipo de instalação inválido!")
    exit()
if tipo == "R" and consumo <= 500:
    custo = consumo * 0.40
elif tipo == "R" and consumo > 500:
    custo = consumo * 0.65
elif tipo == "C" and consumo <= 1000:
    custo = consumo * 0.55
elif tipo == "C" and consumo > 1000:
    custo = consumo * 0.60
elif tipo == "I" and consumo <= 5000:
    custo = consumo * 0.55
elif tipo == "I" and consumo > 5000:
    custo = consumo * 0.60
print(f"Tipo de instalação {tipo}.")
print(f"Custo total R${custo}")
