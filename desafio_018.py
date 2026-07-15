#faça um quadrado que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
angulo_graus = float(input("Digite o angulo em graus: "))
angulo_rad = math.radians(angulo_graus)
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)
print("O angulo de {} tem:\nSeno: {}\nCosseno: {}\nTangente: {}".format(angulo_graus, seno, cosseno, tangente))