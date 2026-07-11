#faça um programa que leia um numero qualquer e mostre na tela sua tabuada
n = int(input("Digite um numero ")) #usando for pq ja assisti uma aula de for e while e ja sei usar mais ou menos, mas poderia ser feito manualmente, o formato seria o seguintes: print("{} x 1 = {}".format(n, n*1)) e assim por diante, o for é mais pratico
for i in range(1, 11):
    print("{} x {} = {}".format(n, i, n*i))