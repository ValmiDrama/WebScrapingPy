import os

from zipfile import ZipFile
from os.path import basename

import requests


# Configurations:
URL = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/'
OUTPUT = List_Arquivos = [
    'Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf',
    'Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.xlsx',
    'Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536.pdf',
    'Anexo_III_DC_2021_RN_465.2021.v2.pdf',
    'Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf']

print(OUTPUT)

# Move document from output
# Localde Extração:
#dirExtract = "c:\\Users\\Valmi Junior\\Documents\\"
# Documents Origin
dirOrigini = "c:\\Users\\Valmi Junior\\Documents\\Rh Intuitive Care\\Teste 1\\local_data\\get_data_notas"
# Documents Distinny
dirDistiny = "c:\\Users\\Valmi Junior\\Documents\\Rh Intuitive Care\\Teste 1\\local_data\\output_to_zip\\"


def get_document_web(url, adress):
    response = requests.get(url)
    if response.status_code == requests.codes.OK:
        with open(adress, 'wb') as new_document:
            new_document.write(response.content)
        print("Donwload finalizado. Salvo em: {}".format(adress))
    else:
        response.raise_for_status()
        print('Erro, in get documents')


def convertToZip():
    with ZipFile("local_data/get_data_notas/notas3.zip", "w") as myzip:
        myzip.write("nota_de_aula_1.pdf")
        print('Convertido com sucesso.')


def moveToOutput():
    for document in documents_list:
        if ".rar" in document:
            os.rename(document, dirDistiny + "\\" + document)
            print('Arquivo movido com sucesso.')
        if ".zip" in document:
            os.rename(document, dirDistiny + "\\" + document)
            print('Arquivo movido com sucesso.')
        else:
            print('...')


# print('Iniciado')
# Baixar arquivos
# if __name__ == "__main__":
#    BASE_URL = 'https://math.mit.edu/classes/18.745/Notes/Lecture_{}_Notes.pdf'
#    OUTPUT_DIR = 'local_data\\get_data_notas'
#    for i in range(1, 2):
#        ducument_name = os.path.join(
#            OUTPUT_DIR, 'nota_de_aula_{}.pdf'.format(i))
#        get_document_web(BASE_URL.format(i), ducument_name)
#
#print('Arquivos Baixados...')
#
# Converter
convertToZip()
print('Arquivos Convertidos...')

# Mover aquivos
os.chdir(dirOrigini)
documents_list = os.listdir()
moveToOutput()
print('Arquivos Arquivos movidos para output...')
