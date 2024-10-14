import numpy as np
import pandas as pd

df_csv = pd.read_csv("E:\SoulCode\PythonOO\curso_python\PANDAS\IMPORTA_CSV\matriculas.csv",sep=";")

#print(df_csv['municipio_pessoa'].unique())
#print(df_csv['uf_pessoa'].value_counts())
#print(df_csv.groupby("uf_pessoa").mean("carga_horaria"))

#------------------------------------------------------------
df2 = df_csv.head()
#print(df2)
df3 = df2.replace({"esfera":{"Federal":np.nan}})
print(df3)
df4 = df3.dropna(subset=['esfera'])
print(df4)
