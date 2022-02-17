from importlib.resources import path
from operator import index
from xml.etree.ElementInclude import include
import pandas as pd

path="./data/Meteorite_Landings.csv"

df = pd.read_csv(path)

# print(df)

#imprimir los primeros 5 datos
# print(df.head())

# print(df.head(10))

#imprimir los ultimos 5 datos
# print(df.tail())


#mustra aleatorea de 1 dato
# print(df.sample())

#mustra aleatorea de indicando la cantidad de registros solicitados
# print(df.sample(10))


#numero de filas y columnas que tiene la base de datos
# print(df.shape)

#numero de datos que tiene la bd, filas por columnas
# print(df.size)

#estadisticas de las variables numericas de la bbd
pd.options.display.float_format = "{:,.1f}".format

# print(df.describe())

# print(df.describe(include="all"))


#informacion de las categorias
# print(df.info())

#tipo de la variable
# print(df.dtypes)
# print(df.convert_dtypes().dtypes)


# print(df.nunique())

# print(df[["fall", "nametype"]])

# df[["fall", "nametype"]]= df[["fall", "nametype"]].astype("category")

# print(df.dtypes)

# print(df["fall"].unique())

# print(df["fall"].value_counts())

# pd.get_dummies(df["fall"])

df["ones"] = 1

# df[["fell","found"]] = pd.get_dummies(df["fall"])

# print(df)


# print(df["year"])
# print(pd.to_datetime(df["year"], errors="coerce", format="%m/%d%Y %H: %M: %S %p"))

# print(df.convert_dtypes().dtypes)
#para cambiar el nombre a una columna se puede utilizar rename
# df.rename(columns={"mass (g)":"mass"}, inplace=True)

# print(df.convert_dtypes().dtypes)

#obtener los nombres de las columnas 
# print(list(df))

# print(df)

#remover una columna drop axis=0 for fila axis=1 for colunmna

# print(df.drop(["ones"], axis=1), inplace=True)


# print(df.drop([0,2,4,6]))
# print(list(df))

# print(df.drop( columns=["id", "recclass"], index=[0,2,4,6]))


#hacer una copia de un DataFrame

df_meteorites = df.copy(deep=True)
print(df_meteorites)
