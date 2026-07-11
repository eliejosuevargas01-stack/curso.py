#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
m = float(input("Digite um valor em metros: "))
cm = m * 100
mm = m * 1000
print("{} metros contem {} centimetros e {} milimetros".format(m, cm, mm))