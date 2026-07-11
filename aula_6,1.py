#n = input("digite um valor: ")
#print(n.is())

n1 = int(input(" numero 1: "))
n2 = int(input(" numero 2: "))
s = n1 + n2
print("A soma entre {} e {} é {}".format(n1, n2, s))
print(n1.isnumeric())
print(n2.isnumeric())
print(s.isnumeric())
# numero 1: 23
# numero 2: 32
# A soma entre 23 e 32 é 55
# Traceback (most recent call last):
#   File "/home/eliezer/Escritorio/scripts python/aula_6,1.py", line 8, in <module>
#     print(n1.isnumeric())
#           ^^^^^^^^^^^^
# AttributeError: 'int' object has no attribute 'isnumeric'