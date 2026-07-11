#desenvolva um programa que leia duas notas do aluno, calcule e mostre a media.
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
m = (n1 + n2) / 2 #oq esta nos parenteses é feito primeiro, depois a divisão
print("A sua media é {}".format(m))