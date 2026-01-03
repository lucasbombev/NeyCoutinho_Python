divida_inicial = float(input("Digite o valor da dívida inicial: R$ "))
taxa_juros_mensal = float(input("Digite a taxa de juros mensal (em %): ")) / 100
pagamento_mensal = float(input("Digite o valor do pagamento mensal: R$ "))
meses = 0
total_juros = 0
while divida_inicial > 0:
    juros = divida_inicial * taxa_juros_mensal
    total_juros += juros
    divida_inicial += juros
    divida_inicial -= pagamento_mensal
    meses += 1
    if divida_inicial < 0:
        divida_inicial = 0
    print(f"Mês {meses}: Dívida restante: R$ {divida_inicial:.2f}")
print(f"\nDívida quitada em {meses} meses.")
print(f"Total de juros pago: R$ {total_juros:.2f}")