#Conexion a BBDD My SQL

#pip install sqlalchemy

import panda as pd
import sqlalchemy as sql
database_type = 'mysql'


#Conexion a la bbdd

user = 'user_name'
password = 'password'
host = 'xxx.xxx.xxx.xxx:port'
database = 'database_name'

conn_string = '{}://{}:{}@{}/{}'.format(
database_type, user, password, host, database)

sql_conn = sql.create_engine(conn_string)

#creacion de consulta a la bbdd
query_sql = 'select * from table_name limit 10'

#generacion de dataframe conextada a la base de datos pasandole como argumentos la consulta y la contexion
df = pd.read_sql(query_sql, sql_conn)
print(df)