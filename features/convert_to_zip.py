from zipfile import *
#Convert documents from Zip or Rar
def convertToZip():    
    with ZipFile("./local_data/get_data_notas/notas.zip", "w") as myzip:
            myzip.write("local_data/get_data_notas/nota_de_aula_1.pdf")
            myzip.write("local_data/get_data_notas/nota_de_aula_2.pdf")
            return print('Sucefull')
