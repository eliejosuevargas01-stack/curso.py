#faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento
s = float(input("Digite seu salario para consultar o aumento a receber: "))
a = s * 0.15
sa = s + a
print("como seu salario é de R${:.2f}, o valor equivalente ao aumento de 15% é R${:.2f} e o seu salario fica em R${:.2f}".format(s, a, sa))