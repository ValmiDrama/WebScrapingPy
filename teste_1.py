from distutils.file_util import move_file
from lib2to3.pytree import convert
import os
from features.convert_to_zip import convertToZip

from features.get_document import get_documentc
from features.move_to_output import moveToOutput

#Configurations:
BASE_URL = 'https://math.mit.edu/classes/18.745/Notes/Lecture_{}_Notes.pdf'
OUTPUT_DIR = 'local_data/get_data_notas'

# Links
#BASE_URL = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/'
#/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf
#/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.xlsx
#/Anexo_II_DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536.pdf
#/Anexo_III_DC_2021_RN_465.2021.v2.pdf
#/Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf

#Get documents from URL
   # make request to server (whrite and bide)
if __name__ == "__main__":
    for i in range(1, 3):
        ducument_name = os.path.join(OUTPUT_DIR, 'nota_de_aula_{}.pdf'.format(i))
        get_documentc(BASE_URL.format(i), ducument_name)
#Convert documents from Zip
convertToZip()
#Move documents from output
moveToOutput()



