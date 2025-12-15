#faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento do novo salário
salario = float(input("Digite o valor do salário: "))
porcentagem = int(input("Digite o valor da porcentagem do aumento: "))
novo_salario = salario + (salario * porcentagem / 100)
print(f"O salario com o novo aumento de {aumento_salario}% é R${novo_salario}")