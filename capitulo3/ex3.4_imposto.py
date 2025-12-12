#escreva uma expressão para avaliar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que 5.000,00.
salario = float(input("Qual o seu salário R$: "))
if salario > 5000:
    print("paga imposto")
else:
    print("isento de imposto")