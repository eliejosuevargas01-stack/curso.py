#escreva um programa que pergunte a quantidade de kms percorridos por um carro alugado e a quantidade de dias pelos quais foi alugado, calcule o preço a pagar, sabendo que o carro custou 60 por dia e 0.15 por km rodado
d = int(input("Digite o numero de dias que vc ficou com o carro: "))
km = int(input("Escreva a quantidade de kms que vc rodou no carro nesse periudo: "))
vkm = 0.15
vd = 60
vpkm = vkm*km
vpd = vd*d
vt = vpkm+vpd
print("Voce ficou {} dias com o carro, oq corresponde a {}rs e foram {}kms rodados, oq corresponde a {}rs, o valor final é de {}rs".format(d, vpd, km, vpkm, vt))
#acabei colocando variaveis demais, deveria ter sido feito assim:
print("a conta funcionou, mas gastou mais memoria desnecessariamente\nVamos agora para uma alternativa que tambem funciona e é mais leve")
d1 = int(input("Digite o numero de dias que vc ficou com o carro: "))
km1 = int(input("Escreva a quantidade de kms que vc rodou no carro nesse periudo: "))
vtpd = d1*60
vtpkm = km1*0.15
vt1 = vtpd+vtpkm
print("Voce ficou {} dias com o carro, oq corresponde a {}rs e foram {}kms rodados, oq corresponde a {}rs, o valor final é de {}rs".format(d1, vtpd, km1, vtpkm, vt1))
#d== dias, km== kms, vkm== valor por km, vd== valor do dia, vpd== valor por dia, vpkm== valor por km, vt== valor total, vtpd== valor total por dias, vtpkm== valor total por kms