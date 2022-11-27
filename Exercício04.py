matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

soma = 0

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input("Digite um valor inteiro: "))

maior = matriz[0][0]
menor = matriz[0][0]

for linha in matriz:
    print(linha)

for i in range(0, 3):
    for j in range(0, 3):
        if i == j:
            soma += matriz[i][j]

            if matriz[i][j] > maior:
                maior = matriz[i][j]

            if matriz[i][j] < menor:
                menor = matriz[i][j]

print(f"A soma dos valores da diagonal principal é {soma}")
print(f"O maior valor da diagonal principal é {maior}")
print(f"O menor valor da diagonal principal é {menor}")