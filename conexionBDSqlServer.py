#Conexion a BBDD SQL Server

#pip install pyodbc 

import panda as pd
import pyodbc

#Conexion a la bbdd

driver = '{SQL Server}'
server_name = 'server_name'
db_name = 'database_name'
user = 'user'
password = 'password'
sql_conn = pyodbc.connect('''
DRIVER={};SERVER={};DATABASE={};UID={};PWD={};
Trusted_Connection=yes
'''.format(driver, server_name, db_name, user, password))

#creacion de consulta a la bbdd
query_sql = 'select * from table_name limit 10'

#generacion de dataframe conextada a la base de datos pasandole como argumentos la consulta y la contexion
df = pd.read_sql(query_sql, sql_conn)
print(df)