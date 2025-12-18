a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))
maior = a
if a > b and a > c:
    print(f"{a} é o maior valor.")
if b > a and b > c:
    print(f"{b} é o maior valor.")
if c > b and c > a:
    print(f"{c} é o maior valor.")
menor = a
if a < b and a < c:
    print(f"{a} é o menor valor.")
if b < a and b < c:
    print(f"{b} é o menor valor.")
if c < a and c < b:
    print(f"{c} é o menor valor.")
