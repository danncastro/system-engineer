# Desenvolvendo as entradas de dados
# - Descrição do projeto
# - Total de horas estimadas
# - Valor da hora de trabalho
# - Prazo de entrega estimado

descricao_projeto = input("Descrição do projeto: ")
valor_horas_estimadas = input("Horas estimadas: ") 
valor_hora_trabalhada = input("Valor da hora trabalhada: ")
prazo_estimado = input("Prazo estimado: ")

# Criando o cálculo do valor total estimado
# - Cálculo: valor total estimado = total de horas estimadadas x valor da hora de trabalho

valor_total_estimado = int(valor_horas_estimadas) * int(valor_hora_trabalhada)
print(valor_total_estimado)

# Gerando o PDF com o orçamento
#   - Instalando a biblioteca
#       -  pip install fpdf

# importando a biblioteca
from fpdf import  FPDF

# Criando um arquivo PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

# Inserindo os dados no PDF
pdf.image("template_gerador_de_pdf.png", x=0, y=0)

# inserindo os dados do projeto
pdf.text(115, 145, descricao_projeto)
pdf.text(115, 160, valor_horas_estimadas)
pdf.text(115, 175, valor_hora_trabalhada)
pdf.text(115, 190, prazo_estimado)
pdf.text(115, 205, str(valor_total_estimado))

# Salvando o arquivo
pdf.output("orçamento.pdf")
print("Orçamento gerado com sucesso!")