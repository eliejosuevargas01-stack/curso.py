#um professor quer sortear um dos seus quatro alunos para apagar o quadro, faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido
#aqui usamos random
import random
lista_de_alunos = []
print("Digite o nome dos alunos, quando terminar, digite 'fim' para sortear")
while True:
    nome = input("Digite o nome do aluno: ")
    if nome.lower() == 'fim':
        break
    lista_de_alunos.append(nome)
escolhido = random.choice(lista_de_alunos)
print("O aluno escolhido foi {}".format(escolhido))