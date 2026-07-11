# -- Operações Aritmeticas --
# + == adição
# - == subtração
# * == multiplicação
# / == divisão
# // == divisão inteira
# ** == potência
# % == módulo (resto da divisão)

5+5 == 10
5-5 == 0
5*5 == 25
5/5 == 1
5//5 == 1
5**5 == 3125
5%5 == 0

# -- Ordem de Precedencia --
#a ordem de procedencia é a seguinte:
#1() parenteses
#2** potencia
#3*///% multiplicação, divisão, divisão inteira e módulo
#4+- adição e subtração

5 + 3 * 2 == 11 #a ordem neste caso é multiplicação e depois adição
3* 5 + 4 ** 2 == 31  #a ordem neste caso é potência, depois multiplicação e depois adição
3*(5 + 4) ** 2 == 243 #a ordem neste caso é parenteses, depois potência



