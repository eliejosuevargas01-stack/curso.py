print ("Hello World from arquivo1.py    ")
print("este é meu priemiro arquivo em python da faculdade")
while True:

    resposta = input("digite aqui se vc acredita que eu vou conseguir aprender python (sim/não): ").lower()


    print(f"vc disse: {resposta}")
    if resposta == "sim" or resposta == "não" or resposta == "nao":
            break

    print("obrigado por acreditar em mim")

    valor = input("digite quanto eu vou tirar na proxima prova:")
    print(f"vc disse: {valor}")
    if valor >= 7:
        print("é uma nota boa pra quem quase não estuda sobre teoria kkk")
    elif valor >= 5:
        print("tá, tbm não esculacha, eu vou tirar mais do que isso tá? ;´^(")
    else:
        print("obrigado por não acreditar em mim, isso me motiva a aprender mais")