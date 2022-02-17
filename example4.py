import pandas as pd
import numpy as np
# print(pd.__version__)

# dict_data = {
#     "CO": 300,
#     "MX": 400,
#     "CH": 200,
# }
# print(dict_data)

# print(pd.Series(dict_data))

# dict_data2 = {
#     "CH": [100, 800, 200],
#     "CO": [100, 200, 300],
#     "MX": [300, 500, 400],
# }

# df = pd.DataFrame(dict_data2)
# print(df)

dict_data3 = {
    'edad': [10,9,13,14,12,11,12],
    'cm': [115,110,130,155,125,120,125],
    'pais':['co','mx','co','mx','mx','ch','ch'],
    'genero':['M','F','F','M','M','M','F'],
    'Q1':[5,10,8,np.nan,7,8,3],
    'Q2':[7,9,9,8,8,8,9]
}


# df2 = pd.DataFrame(dict_data3)

#definir los indices del DataFrame

df2 = pd.DataFrame(dict_data3, index=["ana", "benito", "camilo", "daniel", "erika", "fabian", "gabriela"])


# #obtener el indice del dataFrame
# print(df2.index)

# #obtener la columna del dataFrame
# print(df2.columns)

# #obtener el valor del dataFrame
# print(df2.values)

# # print(df2)

#obtener un conjunto de datos por columna o columnas

# print(df2["pais"])

# print(df2[["pais","cm","edad"]])

#obtener un conjunto de datos fila, obtner todos las caracteristicas de las columnas

# print(df2.loc["ana"])

#obtener una fila con eligiendo las caracteristicas que se quieren visualizar

# print(df2.loc["ana",["edad", "genero", "pais"]])


#obtener con conjunto de fila con eligiendo las caracteristicas que se quieren visualizar

# print(df2.loc[["ana","camilo"],["edad", "genero", "pais"]])


#funcion iloc

# print(df2)
# print(df2.iloc[2,1])
# print(df2.iloc[3:])


#data condicional
#se pone la condicion boleeana que desaamos cumplir con la columna
# print(df2[df2["edad"] >= 12])


# print(df2[(df2["edad"] >= 12) & (df2["pais"] == "mx") & (df2["cm"] >= 150) ])


print(df2.query("edad > 12"))