#faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
preco = float(input("Qual o preço do produto R$:"))
desconto = int(input("Qual o percentual de desconto: "))
novo_preco = preco - (preco * desconto / 100)
print(f"O produto que custava R${preco}, com desconto de {desconto}% ficará com o valor final de R${novo_preco}")
