#faça um programa que leia a altura e largura de uma parede em metros, calcule a dua area e a quantidade de tinta necessaria para pintalo, sabendo que cada litro de tinta pinta uma area de 2m**2.
l = float(input("Largura da parede: "))
a = float(input("Altura da parede: "))
aq = l * a
t = 2 # inicialmente coloquei t = 2**2 pq não sabia como que referenciava que a o litro de tinta por metro quadrado em python, apos perguntar para o google no modo ia ele me respondeu que apenas precisava escrever t = 2
lt = aq / t
print("A parede tem {}m de largura, {}m de altura, {}m de area quadrada.\n e vc precisa de {} litros de tinta para poder pintar ela inteira".format(l, a, aq, lt))
