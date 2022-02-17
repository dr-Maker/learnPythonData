import pandas as pd
import numpy as np

dict_data = {
    'edad': [10,9,13,14,12,11,12],
    'cm': [115,110,130,155,125,120,125],
    'pais':['co','mx','co','mx','mx','ch','ch'],
    'genero':['M','F','F','M','M','M','F'],
    'Q1':[5,10,8,np.nan,7,8,3],
    'Q2':[7,9,9,8,8,8,9]
}

df = pd.DataFrame(dict_data)

path = "./panda/{}"

#variable opcional sheet_name="nombre de la hoja excel"
df.to_json(path.format("JSON.json"))

df_import = pd.read_json(path.format("JSON.json"))
print(df_import)
