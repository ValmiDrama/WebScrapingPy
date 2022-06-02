# Tarefas de código:

# Extrair do pdf do anexo I 
# Salvar dados em uma tabela em csv;
# e Zipar o csv num arquivo "Teste_{seu_nome}.zip".

import os
import pandas as pd
import tabula as tb
from tabula import read_pdf
from zipfile import ZipFile
from tabula import convert_into

#Funcoes salvas para futuras implementacoes:
#Funcao que converte para CSV:
def convert_into_csv(pagina):    
    tb.convert_into(pdf_path, 'tabela2.csv', output_format='csv', pages=pagina)

#Funcao de coletar uma tabela ate uma pagina espeficica.
def getTable(dataframes, endPag):    
    for tabela in range(endPag):
        dataframes[tabela].to_csv(f"tabela_{tabela}.csv")

#Funcao que converte para ZIP:        
def convertToZip():    
    with ZipFile("ValmiJunior.zip", "w") as myzip:
        myzip.write('tabela.csv')   
        print('Convertido com sucesso.')
        myzip.close()


# localizacao do arquivo (local/web)
dir = os.getcwd()
output_name = '{}\ValmiJunior'.format(dir)
# pdf_path='https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537.pdf'
pdf_path='arquivo.pdf'
table_file = r"arquivo.pdf"
output_csv = r"/file.csv"


#Verificar arquivo e tamnho (futuramente evitar erros de null e refatoramento)
listArquivo = tb.read_pdf(pdf_path, pages='all')
print(len(listArquivo))

# Extrair do pdf do anexo I 
# dfs = tb.read_pdf(pdf_path, encoding='utf-8', spreadsheet=True, pages='all')
# print(len(dfs))

# Salvar dados em uma tabela em CSV:
# dfs[0].to_csv("ValmiJunior.csv")

tb.convert_into(pdf_path, 'tabela.csv', output_format='csv', pages='all')

# e Zipar o csv num arquivo "Teste_{seu_nome}.zip".
# convertToZip(seu_nome='ValmiJunior')

convertToZip()

print('fim')