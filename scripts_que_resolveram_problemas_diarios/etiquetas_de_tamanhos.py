from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

# Configurações
LARGURA_A4, ALTURA_A4 = 200 * mm, 287 * mm
MARGEM_REGISTRO_X, MARGEM_REGISTRO_Y = 15 * mm, 15 * mm
LARGURA_UTIL, ALTURA_UTIL = 180 * mm, 260 * mm
DIAMETRO = 15 * mm
PASSO = 18 * mm
RAIO = DIAMETRO / 2

# 1. Abrimos o canvas APENAS UMA VEZ para o arquivo inteiro
nome_do_arquivo = "todos_os_numeros.pdf"
c = canvas.Canvas(nome_do_arquivo, pagesize=(LARGURA_A4, ALTURA_A4))

lista_numeros = [1, 2, 4, 6, 8, 10, 12, 14, 16]

for numero in lista_numeros:
    # Desenha o conteúdo da página atual
    nc = int(LARGURA_UTIL / PASSO)
    nl = int(ALTURA_UTIL / PASSO)

    for i in range(nc):
        for j in range(nl):
            pos_x = MARGEM_REGISTRO_X + (i * PASSO) + RAIO
            pos_y = MARGEM_REGISTRO_Y + (j * PASSO) + RAIO
            
            c.setLineWidth(0.2)
            c.circle(pos_x, pos_y, RAIO, stroke=1, fill=0)
            c.setFont("Helvetica-Bold", 30)
            c.drawCentredString(pos_x, pos_y - 3 * mm, str(numero))
    
    # 2. Comando vital: diz ao PDF para "virar a página"
    c.showPage()

# 3. Salva uma única vez no final de tudo
c.save()
print(f"Arquivo '{nome_do_arquivo}' gerado com sucesso!")