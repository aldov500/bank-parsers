# importing required modules
from code import InteractiveConsole
from posixpath import split
import PyPDF2
 
pdf_file = open('2022-04-25-BBVA-credito.pdf', 'rb')
pdf_page = [0,1,2]
pdf_read = PyPDF2.PdfFileReader(pdf_file)
pdf_cont = ''
pdf_list = list()

for page in pdf_page:
    pdf_cont += pdf_read.getPage(page).extractText()


pdf_list = pdf_cont.split('\n')
pdf_list_copy = pdf_list
pdf_list_record = list()
pdf_sep_char = "|"
pdf_index = 0
pdf_nextv = False

print("Operacion" + pdf_sep_char + "Liquidacion" + pdf_sep_char + "Descripcion" + pdf_sep_char + "Referencia" + pdf_sep_char + "Cargos" + pdf_sep_char + "Abonos")
for sentence in pdf_list:
    pdf_index += 1
    if "/" in sentence and len(sentence) == 6 and pdf_nextv == False:
        pdf_nextv = True
        print(pdf_list[pdf_index - 1] + pdf_sep_char + pdf_list[pdf_index] + pdf_sep_char + pdf_list[pdf_index + 1] + pdf_sep_char + pdf_list[pdf_index + 2] + pdf_sep_char + pdf_list[pdf_index + 3] + pdf_sep_char + pdf_list[pdf_index + 4])
    else:
        if pdf_nextv == True:
            pdf_nextv = False

pdf_file.close()

