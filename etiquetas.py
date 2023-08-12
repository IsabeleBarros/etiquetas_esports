nome_da_equipe = str
q_integrantes = int

nome_da_equipe = input("Qual o nome da sua equipe?")
q_integrantes = input("Quantos integrantes têm?")
i = 1
for i in range(int(q_integrantes)):
    print(nome_da_equipe, "-", i + 1)
    i = i + 1