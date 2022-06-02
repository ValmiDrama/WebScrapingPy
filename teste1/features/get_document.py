import os
import requests



def get_document_web(url, adress):
    response = requests.get(url)
    if response.status_code == requests.codes.OK:
        with open(adress, 'wb') as new_document:
            new_document.write(response.content)
        print("Donwload finalizado. Salvo em: {}".format(adress))
    else:
        response.raise_for_status()
        print('Erro, in get documents')
        
if __name__ == "__main__":
    BASE_URL = 'https://math.mit.edu/classes/18.745/Notes/Lecture_{}_Notes.pdf'
    OUTPUT_DIR = 'local_data\\get_data_notas'
    for i in range(1, 2):
        ducument_name = os.path.join(
            OUTPUT_DIR, 'nota_de_aula_{}.pdf'.format(i))
        get_document_web(BASE_URL.format(i), ducument_name)