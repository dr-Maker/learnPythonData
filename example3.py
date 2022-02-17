import pandas as pd
import numpy as np
# print(pd.Series([10,9,8,7,6]))

#serie con columna de indexacion 
sr = pd.Series([10,9,8,7,6])

# print(sr)


# #para visualizarlo como array
# print(sr.values)

# #para obtener un resumen desde los indices
# print(sr.index)

# #dimensionalidad del objeto
# print(sr.shape)


# #para seleccionar un elemento 
# print(sr[3])

# #para seleccionar distintos elementos, estos se mostraran segun la seleccion del indice
# print(sr[[0,4,2]])

# sr = pd.Series([10,9,8,7,6], index=["a","b","c","d","e"])

# # print(sr)

# #seleccion de rangos
# print(sr["a":"c"])


###------------ DICCIONARIO ------------###
dictionario = {
    "CO": 100,
    "MX": 200,
    "AR": 300,
    "CL": 400,
}

# # print(dictionario)

# #keys del diccionario
# print(dictionario.keys())

# #values del diccionario
# print(dictionario.values())


sr = pd.Series(dictionario, index=["CO","MX","PE"])
# print(sr)


#funciones
#isnull()
#notnull()

np.nan

print(sr.isnull())
