n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))
#print("a soma vale", n1+n2) pra apenas mostrar um valor na tela sem guardar em uma variavel (nao vai ser usado depois)
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma é {},\n o produto é {},\n a divisão é {},\n e a potencia é {}".format(s, m, d, e), end="") #forma de formatar a string
print("E a divisão inteira é {}".format(di))