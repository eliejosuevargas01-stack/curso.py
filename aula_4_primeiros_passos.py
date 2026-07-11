import time

nome = input("qual seu nome? ")
print(f"Seu nome é {nome}")

peso = float(input("e o seu peso é qual? "))
print(f"seu peso é {peso}kg ")

# O .replace garante que se ele digitar 1,75 vire 1.75 e não quebre o código
altura_input = input("qual a sua altura mesmo? ")
altura = float(altura_input.replace(",", "."))
print(f"então sua altura é {altura}m, né?")

input("Sim ou não? ")
time.sleep(2)
print("otimo, então vamos calcular seu imc")
imc = peso / (altura ** 2)
time.sleep(1)
print("calculando...")
time.sleep(1)
print("calma cabaço, espera um pouco, isso não é tão rapido assim")
time.sleep(1)
print("...")
time.sleep(1)
print("acho que eu perdi a aula de calcular imc... :'/")
time.sleep(1)
print(f"kkkkkkk se assustou né?, eu sei sim calcular, seu imc é: {imc:.2f}")
time.sleep(1)
input("agora, vc quer saber se está obeso de acordo com as categorias do imc? acho que ainda me lembro como ver isso...")
time.sleep(1)
print("vamos lá, eu nem preciso fazer esse calculo, eu sei que vc está OBESO, O-BE-SO, KKKKKKK, mas tá, tô calculando aqui...")
time.sleep(1)

# Usando a estrutura limpa de if/elif (evita falhas de intervalo)
if imc < 18.5:
    print("magrelo do carai, vc está abaixo do peso, mas não se preocupe, vc ainda pode engordar um pouco, vai malhar e comer mais, mas não muito, senão vc vai engordar demais")
    time.sleep(1)
elif imc < 25:
    print("vc está no peso ideal, parabéns, mas não se empolgue, se ficar comendo demais vai engordar bem rapido")
    time.sleep(1)
elif imc < 30:
    print("iih, parece que alguem andou comendo demais por ai, vai malhar desgraça, tá com sobrepeso!!!")
    time.sleep(2)
elif imc < 35:
    print(f"{nome}, vai malhar caraio... aah, ja deve ter esquecido oq significa malhar né? kkkk, Obesidade Grau I cara, cuida essa boca")
    time.sleep(2)
elif imc < 40:
    print("... ˢᵉ ᵉˡᵉ ᶠᶦᶻᵉʳ ᵐᵃᶦˢ ᵘᵐᵃ ᑫᵘᵉʳʸ ᵉˢˢᵉ ˢᵉʳᵛᶦᵈᵒʳ ᶜᵃᶦ ...")
    time.sleep(1.5)
    print("... ᵖˢˢᵗ, ᵒˡʰᵃ ᵒ ᴵᴹᶜ ᵈᵒ ᶜᵃʳᵃ, ᵐᵉᵘ ᵈᵉᵘˢ ...")
    time.sleep(2)
    print("""
[SISTEMA]: Ops! Opa, você já tá aí? Nem te vi! 
Resultado do cálculo: Opa... é... deu Obesidade Grau 2. Tchau! *desliga o terminal na sua cara*
""")
    time.sleep(1)
else:
    print("INFORMAMOS QUE GRAÇAS AO SEU PESO, O NOSSO SERVIDOR CAIU, MAS AINDA CONSEGUIU TE DEIXAR UM RECADO, VC ESTÁ COM OBESIDADE GRAU 3, VAI MALHAR DESGRAÇA, E NÃO É SÓ MALHAR NÃO, TEM QUE PARAR DE COMER TANTA MERDA, SEU GORDO!!!")