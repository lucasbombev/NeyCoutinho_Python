print(
    """
    Catálogo de Produtos
    Código '1' - R$0.50
    Código '2' - R$1.00
    Código '3' - R$4.00
    Código '5' - R$7.00
    Código '9' - R$8.00
    Digite '0' para sair!
    """)
total = 0
while True:
    produto = int(input("Código do produto desejado: "))
    if produto == 0:
        break
    if produto == 1:
        total += 0.50
    elif produto == 2:
        total += 1.00
    elif produto == 3:
        total += 4.00
    elif produto == 5:
        total += 7.00
    elif produto == 9:
        total += 8.00
    else:
        print("Código inválido. Tente novamente.")
    if produto in [1,2,3,5,9]:
        print("Produto Adicionado!")
print(f"Total a pagar: R$ {total:.2f}")