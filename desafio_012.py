#faça um algoritmo que leia o preço do produto e de um desconto de 5%
p = float(input("O Valor do produto é de R$: "))
d = p * 0.05
pf = p-d
print("O novo valor com desconto de 5% é de R${:.2f}".format(pf))