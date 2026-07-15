import random
lista_alunos = []
print("Digite o nome dos alunos, quando terminar, digite 'fim' para sortear")
while True:
    nome = input("Digite o nome do aluno: ")
    if nome.lower() == 'fim':
        break
    lista_alunos.append(nome)
random.shuffle(lista_alunos)
print("A ordem escolhida é: {}".format(lista_alunos))