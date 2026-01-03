soma = 0
contador = 0
print(f"Valor inicial: {soma}")
while True:
    n = int(input("Digite um a ser somado: (0 para parar a execução)"))
    if n == 0:
        break
    soma += n
    contador += 1

print(f"Total: {soma}\nQuantidade de números digitados:{contador}\n Média: {soma/contador}")