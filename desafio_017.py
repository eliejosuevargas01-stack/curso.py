#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento de hipotemusa
import math
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = math.hypot(co, ca)
print("O comprimento da hipotenusa é: {}".format(hipotenusa))
#odeio hipotenusaaaas