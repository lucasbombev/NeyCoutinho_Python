# Escreva um programa para aprovar um emprestimo bancário para compra de uma casa. o programa deve perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação como sendo o valor da casa dividido pelo número de meses que o comprador vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário mensal.
valor_casa = float(input("Digite o valor do imóvel R$"))
salario = float(input("Digite o valor do salário R$"))
anos_pagar = int(input("Em quantos anos a casa será paga: "))
meses = anos_pagar * 12
prestacao = valor_casa / meses

if prestacao > (salario * 0.30):
	print("Empréstimo negado!")
else:
	print("Empréstimo aprovado!")
	print(f"O valor da prestação será fixado em R$ {prestacao:.2f}")
