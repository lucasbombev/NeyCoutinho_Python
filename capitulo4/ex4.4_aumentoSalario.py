#estamos usando apenas if pois o else ainda não foi ensinado
salario = float(input("Digite o salário R$"))
aumento = 0
if salario > 1250:
    aumento = salario + (salario * 0.10)
    print(f"com o salário de {salario} e o aumento de 10% seu novo salário é {aumento:.2f}")
if salario <= 1250:
    aumento = salario + (salario * 0.15)
    print(f"com o salário de {salario} e o aumento de 15% seu novo salário é {aumento:.2f}")
