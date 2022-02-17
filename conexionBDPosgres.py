#Conexion a BBDD Postgres

#pip install psycopg2 

import panda as pd
import psycopg2

#Conexion a la bbdd
conn_sql = psycopg2.connect(user = "user_name",
                            password = "password",
                            host = "xxx.xxx.xxx.xxx",
                            port = "5432",
                            database = "postgres_db_name")

#creacion de consulta a la bbdd
query_sql = '''
                select *
                from table_name
                limit 10
            '''

#generacion de dataframe conextada a la base de datos pasandole como argumentos la consulta y la contexion
df = pd.read_sql(query_sql, sql_conn)
print(df)