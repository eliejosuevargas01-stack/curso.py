#crie um algoritmo que leia um numero e mostre o seu dobro, triplo e a raiz quadrada
n1 = int(input("Digite um numero: "))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)
print("O Dobro de {} é {}, \n o Triplo é {}, \n e a Raiz quadrada é {}".format(n1, d, t, r))