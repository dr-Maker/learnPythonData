import pandas as pd

pais = {
    "Chile": 10000,
    "Brasil": 20000,
    "Argentina": 30000,
    "Colombia": 40000,
}

# #Esto no lo puedo hacer si no es una serie
# print(pais["Chile":"Argentina"])


seriePais = pd.Series(pais)

print(seriePais["Chile":"Argentina"])