frase = "Curso em Video Python"#[c][u][r][s][o][ ][e][m][ ][v][i][d][e][o][ ][p][y][t][h][o][n] 
frase[1]#pega desde o numero 1, se eu colocar "frase[] oq estiver dentro do colchete é o numero da lista ao qual ele vai iniciar"
frase[1:10]#agora ele começa no primeiro numero, e vai até o ultimo numero, por exemplo, não considera o 10 neste caso, ele pega até o 9 e no 10 para de contar
frase[1:10:4]#a mesma logica, porem o ultimo numero significa as casas que ele vai contar, por exemplo, neste caso ele vai começar no numero 1, vai até o 10 e vai contar de 4 em 4, pegando o numero 1, o numero 5 e o numero 9
frase[:9]#como não tem numero pra começar,ele começa desde a casa 0 e vai até a casa que esta no numero depois dos dois pontos
frase[2:]#aqui é o mesmo, porem como não tem numero pra finalizar, ele conta desde o numero de inicio até o numero final
frase[2::3]#agora ele começa com o primeiro numero definido no colchete, que seria neste caso o 2, vai até o ultimo numero e conta de 2 em 2
#analise
len(frase)#qual o cumprimento da frase str
frase.count('o')#conte quantas o minusculos tem na frase
frase.count('o, 0, 13')#fatia a primeira o apartir do 0 até o caractere 13
frase.find('deo')#indica onde encontrou a palavra deo em caracteres, neste exemplo ele encontra no 11
frase.find('Android')#se ele enão encontrar o objeto entre aspas, ele retorna -1
'Curso' in frase#existe curso em frase? Sim/Não
#transformação
frase.replace('Python', 'Android')#substitui o item 1 pelo item 2, no caso ele substitui Python por Android se encontrar na frase
frase.upper()#transforma em maiusculo
frase.lower()#transforma tudo pra minusculo
frase.capitalize()#apenas o primeiro caractere permanece em maiusculo, todos os outros caracteres que não forem o primeiro e forem maiusculos vão ficar em minusculo
frase.title()#capitaliza a frase por palavra, todas as primieras letras da frase ficam em maiuscula
#frase = "   Aprenda Python   "
frase.strip()#elimina espaços no inicio e no fim da frase pra manter a string limpa
frase.rstrip()#remove apenas os ultimos espaços, os espaços no final da frase
frase.lstrip()#remove apenas os espaços da esquerda, do inicio da frase
#divisão de str
frase.split()#faz uma divisão na str considerando os espaços [esta frase] viraria [esta] [frase], por padrão é o espaço, mas da pra usar basicamentr qualquer letra
'-'.jois(frase)#junta as palavras e coloca o traço '-' no lugar do espaço, ou vice versa, u da pra mudar o traço por qualquer outro caractere (acho)
print("""Principais UsosLíngua Portuguesa: Serve para inserir anotações, explicações ou correções feitas por quem está transcrevendo um texto, diferenciando-as do autor original.Matemática: Organiza a ordem das operações, sendo usado geralmente "fora" dos parênteses, como em: \(2 \times [3 + (5 - 1)]\). Também serve para representar intervalos numéricos.Programação: Usado na criação e manipulação de listas ou matrizes (arrays) na maioria das linguagens de código.""")
#pra printar paragrafos sem ter que dar print para cada linha