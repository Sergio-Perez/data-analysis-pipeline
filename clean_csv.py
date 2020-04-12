import pandas as pd

#Cargamos el csv
df = pd.read_csv('./csv/top-50-spotify-songs-by-each-country/top50contry.csv',encoding="latin1'")
df.head()

#Miramos las columnas del csv 
df.columns

#Miramos las columnas y rows de la tabla
df.shape

#Vamos a eliminar duplicados
df.drop_duplicates().shape

#Veamos los nulos que tienen
df.isnull().head()
df.isnull().sum()

df[df["top genre"].isnull()][["title","year"]]

#Cambiamos los null de top genre por "otros"
df["top genre"] = df["top genre"].replace("None", "Other")
df.loc[df["top genre"].isnull(), "top genre"] = list("Other" for e in range(0,15))

#Voy a legir las columnas que voy a usar
eleccion = ["title","artist","top genre","year", "country","val","dur"] 
df_clean = df[eleccion]
df_clean.head()

#Coloco la tabla por title y artist por valor ascendente
df_clean.sort_values(["title", "artist"], axis=0, 
                 ascending=True, inplace=True)
df_clean

#Miro los valores de title
list(df_clean.title)

#Elimino todos los nombre iligico con "<u+05" etc..
df_clean.drop(df_clean[df_clean.title.str.contains("<U+")].index, inplace=True)  
df_clean.title

print((df_clean.title.loc[124]).isdigit())

#Elimino los titulos incoherentes o numericon sin sentido.
df_clean.title2= df_clean["title"].str.replace(".", "") 
df_clean.drop(df_clean[df_clean.title2.str.isdigit() == True].index, inplace=True)
df_clean.drop(df_clean[df_clean.title.str.len() == 1].index, inplace=True)

#Elimino el valor NaN de la columna val.
df_clean.val.isnull().sum()
df_clean.drop(df_clean[df_clean.val.isnull()].index, inplace=True)  

#Cambio de flotante a int el type de la columna
df_clean.val = df_clean.val.astype(int)

#Copio la tabla a un csv
df_clean.to_csv('./csv/clean.csv')
 
print(df_clean)