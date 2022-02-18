import pandas as pd
import numpy as np

print(pd.__version__)

df_lmerged = pd.read_csv("./bicicleta/london_merged.csv")
# print(df_lmerged)

df_lmerged["timestamp"] = pd.to_datetime(df_lmerged["timestamp"])

# print(df_lmerged.dtypes)

df_lmerged["hour"] = df_lmerged["timestamp"].dt.hour
print(df_lmerged["hour"])

np.sin(df['wind_speed']**2) + 10

df['t1'].iloc[::3]-df['t2']

df['t1'].iloc[::3].sub(df['t2'], fill_value = 1000)


+    add()
-    sub(), subtract()
*    mul(), multiply()
/    truediv(), div(), divide()
//   floordiv()
%    mod()
**   pow()

df['t1']/df['t2']

df['t1'].dot(df['t1'])


def fun_1(x):
  y = x**2 + 1
  return y

  fun_1(10)

  np.arange(-5,6)

  np.arange(-5,6).shape

  fun_1(np.arange(-5,6))

  df['hour'].apply(fun_1)

  array([26, 17, 10,  5,  2,  1,  2,  5, 10, 17, 26])

  df['hour'].apply(fun_1)

  def fun_2(x, a=1, b=0):
  y = x**2 + a*x + b
  return y


  fun_2(10, a = 20, b= -100)

df['hour'].apply(fun_2, args = (20, -100))

df['hour'].apply(fun_2, a =20, b= -100)

df['t1'].apply(lambda x: x+273)

df.apply(lambda x: x.mean())

df.apply(lambda x: x.mean(), axis=1)

df.apply(lambda x: x.std(), axis=1)

df.apply(lambda x: x['t1']-x['t2'], axis=1)

df.applymap(lambda x: x/1000)

