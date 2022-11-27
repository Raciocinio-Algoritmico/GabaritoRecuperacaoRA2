alunos = []
notas = []

for i in range(5):
    alunos.append(input("Digite o nome do(a) aluno(a): "))

for aluno in alunos:
    notas.append(float(input(f"Digite uma nota de 0 a 10 para {aluno}: ")))

for j in range(5):
    if notas[j] >= 7:
        print(f"{alunos[j]} foi aprovado(a) com nota {notas[j]}")
    elif notas[j] >= 4 and notas[j] <= 6.9:
        print(f"{alunos[j]} está em recuperação com nota {notas[j]}")
    else:
        print(f"{alunos[j]} foi reprovado(a) com nota {notas[j]}")