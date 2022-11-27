def retornaPares(valores):
    pares = []
    for valor in valores:
        if valor % 2 == 0:
            pares.append(valor)

    return pares


def retornaImpares(valores):
    impares = []
    for valor in valores:
        if valor % 2 != 0:
            impares.append(valor)

    return impares


############### PROGRAMA PRINCIPAL #################
numeros = []

for i in range(10):
    numeros.append(int(input("Digite um numero inteiro: ")))


print("---- PARES ----")
for par in retornaPares(numeros):
    print(par)

print("---- IMPARES ----")
for impar in retornaImpares(numeros):
    print(impar)