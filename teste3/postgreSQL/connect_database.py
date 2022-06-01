from multiprocessing import connection
import numpy as np
import pandas as pd
import psycopg2

# Códgo que permite acesso ao Banco de dados Postegrees
# Obs.: Refatorar aplicando SOLID

try:
    print('Iniciando conecão...')
    connection = psycopg2.connect(
        host='localhost',
        database='newdb',
        user='db_user',
        password='StrongPassword!'
    )

    print('Conectado.')
    cursor = connection.cursor()
    cursor.execute("SELECT version()")
    versionDb = cursor.fetchone()
    print(versionDb)
    cursor.execute("SELECT * FROM trimes2021_1")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
finally:
    connection.close()
