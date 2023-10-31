n = int(input("tamanho matriz :"))
linha = [0] * n
matriz = [linha] * n

print(matriz)

for l in range(n):
    linha = [] # não precisava
    for c in range(n):
        numero = int(
            input(" digite o numero que ficara armazezanod0 {},{} :".format(l, c)))
        linha.append(numero)
    matriz[l] = linha

print(matriz)