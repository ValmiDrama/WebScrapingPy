#------------------------------------------------------------------------------------------#
#                              Valmi Gomes Silva Junior
#------------------------------------------------------------------------------------------#
# 
# Este código é parte do processo seletivo, que consiste na realização de testes de 
# nivelamento básico. 
# Estes testes foram desenhados como versões simplificadas de tarefas realizadas no dia a 
# dia da empresa e têm como objetivo avaliar:

# Conhecimentos básicos de programação
# Organização do código
# Conhecimentos complementares de boas práticas de programação
#------------------------------------------------------------------------------------------#

import os

from zipfile import ZipFile
from os.path import basename

import requests

# Configurations:
list_files = [
    'Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf',
    'Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.xlsx',
    'Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536.pdf',
    'Anexo_III_DC_2021_RN_465.2021.v2.pdf',
    'Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf']
dirOrigini = "c:\\Users\\Valmi Junior\\Documents\\Rh Intuitive Care\\testes\\teste1\\local_data\\get_data_notas"
dirDistiny = "c:\\Users\\Valmi Junior\\Documents\\Rh Intuitive Care\\testes\teste1\\local_data\\output_to_zip"
#FUNCTIONS

    #Get documents from URL
def get_document_web(url, adress):
    response = requests.get(url)
    if response.status_code == requests.codes.OK:
        with open(adress, 'wb') as new_document:
            new_document.write(response.content)
        print("Donwload finalizado. Salvo em: {}".format(adress))
        print(" ")      
    else:
        response.raise_for_status()
        print('Erro, in get documents')

    #Convet from zip
def convertToZip():
    #Poderia chamar a lista e por para correr e converte os arquivos deacordo com a list de Downloads.    
    with ZipFile("local_data/get_data_notas/anexos.zip", "w") as myzip:
        myzip.write('local_data/get_data_notas/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf')
        myzip.write('local_data/get_data_notas/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.xlsx')
        myzip.write('local_data/get_data_notas/Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536.pdf')
        myzip.write('local_data/get_data_notas/Anexo_III_DC_2021_RN_465.2021.v2.pdf')
        myzip.write('local_data/get_data_notas/Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf')    
        print('Convertido com sucesso.')    

INPUT =list_files
print('Iniciando...')
if __name__ == "__main__":
   BASE_URL = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/{}'   
   OUTPUT_DIR = 'local_data\\get_data_notas'
   for i in range(0, 5):
       ARQUIVOX=INPUT[i];
       ducument_name = os.path.join(
           OUTPUT_DIR, ARQUIVOX)
       get_document_web(BASE_URL.format(ARQUIVOX), ducument_name)

convertToZip()
#Mapea diretorio para orientar o MOVEtoOutPut
os.chdir(dirOrigini)
documents_list = os.listdir()
print(documents_list)
print('###############################')
for document in documents_list:
    print("-------------------------")
    # if ".rar" in document:
    #     os.rename(document, dirDistiny + "\\" + document)
    #     print('Arquivo movido com sucesso.')
    if ".zip" in document:
        os.rename(document, '../output_to_zip/{}'.format(document))
        print('Arquivo movido com sucesso.')
    else:\
        print('...')
        
        
print('###############################')
print('Arquivos Arquivos movidos para output...')
print('Operação realizada com sucesso...')
