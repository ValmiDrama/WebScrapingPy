import os

#Move document from output

#Documents Origin
dirOrigini = "c:\\Users\\Valmi Junior\\Documents\\Rh Intuitive Care\\Teste 1\\local_data\\get_data_notas"
#Documents Distinny
dirDistiny = "c:\\Users\\Valmi Junior\\Documents\\Rh Intuitive Care\\Teste 1\\local_data\\output_to_zip\\"


os.chdir(dirOrigini)
documents_list = os.listdir()

def moveToOutput():
        for document in documents_list:
                if ".rar" in document:
                         os.rename(document,dirDistiny +"\\"+ document)
                         print('Arquivo movido com sucesso.')
                if ".zip" in document:
                        os.rename(document,dirDistiny +"\\"+ document)
                        print('Arquivo movido com sucesso.')
                else:
                        print('...')