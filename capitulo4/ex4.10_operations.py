#Escreva um prqograma que leia dois nmeros inteiros e exiba a soma, subtrao, multiplicao e divisao dos dois nmeros. 
n1 = int(input("Digite o primeiro número a ser operado: "))
n2 = int(input("Digite o segundo número a ser operado: "))
operation = input("Digite a operação que deseja realizar:\nsoma(+)\nsubtração(-)\nmultiplicação(*)\ndivisão(/)\n")
if operation == "+":
    print(f"A soma entre {n1} e {n2} é igual a: {n1 + n2}")
elif operation == "-":
    print(f"A subtração entre {n1} e {n2} é igual a: {n1 - n2}")
elif operation == "*":
    print(f"A multiplicação entre {n1} e {n2} é igual a: {n1 * n2}")
elif operation == "/":
    print(f"A divisão entre {n1} e {n2} é igual a: {n1 / n2}")
else:
    print("Operação inválida!")
