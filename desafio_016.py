#crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
import math
n = float(input("DIgite um numero real qualquer"))
inteiro = math.trunc(n)
print("O numero {} tem as parte inteira {}".format(n, inteiro))