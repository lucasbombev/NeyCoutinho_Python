deposito_inicial = float(input("Depósito inicial: R$"))
taxa_juros = float(input("Taxa de juros mensal (%): "))

saldo = deposito_inicial
total_depositado = deposito_inicial
mes = 1

while mes <= 24:
    saldo += saldo * (taxa_juros / 100)
    print(f"{mes}° mês: R${saldo:.2f}")
    mes += 1

total_juros = saldo - total_depositado
print(f"Total de juros ganhos: R${total_juros:.2f}")