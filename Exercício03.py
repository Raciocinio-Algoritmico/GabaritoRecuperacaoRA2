import math

def calculaAreaCirculo(raio):
    return math.pi * pow(raio, 2)

def calculaAreaQuadrado(lado):
    return math.pow(lado, 2)

def calculaAreaRetangulo(base, altura):
    return base * altura


############# PROGRAMA PRINCIPAL ############
opcao = 0

while(True):
    print("1. Calcular área do círculo")
    print("2. Calcular área do quadrado")
    print("3. Calcular área do retângulo")
    print("4. Sair")
    print()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        raio = float(input("Digite o tamanho do raio: "))
        areaCirculo = calculaAreaCirculo(raio)
        print(f"A área do círculo com raio {raio} é {areaCirculo}.")
        print()
    elif opcao == 2:
        lado = float(input("Digite o tamanho do lado: "))
        areaQuadrado = calculaAreaQuadrado(lado)
        print(f"A área do quadrado com lado {lado} é {areaQuadrado}.")
        print()
    elif opcao == 3:
        base = float(input("Digite o tamanho da base: "))
        altura = float(input("Digite o tamanho da altura: "))
        areaRetangulo = calculaAreaRetangulo(base, altura)
        print(f"A área do retângulo com base {base} e altura {altura} é {areaRetangulo}.")
        print()
    elif opcao == 4:
        print("Obrigada por utilizar nossa calculadora!")
        break
    else:
        print("Opção inválida! Digite uma opção entre 1 e 4.")
        print()