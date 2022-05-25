import requests

def get_documentc(url, adress): 
    response = requests.get(url)
    if response.status_code == requests.codes.OK:
        with open(adress, 'wb') as new_document:
            new_document.write(response.content)
        print("Donwload finalizado. Salvo em: {}".format(adress))
        
    else:
        response.raise_for_status()
        print('Erro, in get documents')

