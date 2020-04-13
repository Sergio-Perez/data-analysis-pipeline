import requests
import json
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
import argparse
from cargarybuscar import buscarAlbum
from cargarybuscar import descargar
from funciones import argParse

#Cargo el dataframe limpio
df = pd.read_csv('./csv/clean.csv')

#Aqui uso la api de Deezer primero saco el token

apikey = os.getenv("apikey")
print("WE HAVE APIKEY") if apikey else print("NO APIKEY FOUND")

urlautentificador = f"https://api.deezer.com/user/{apikey}"

res = requests.get(urlautentificador)
res
#Probamos uno para sacar la formula para sacar el album
artists_url = "https://api.deezer.com/search?q=artist:'Arizona Zervas'"
artists_response = requests.get(artists_url)
album =artists_response.json()

# Elijo las columnas que voy a usar para descargar desde la Api
descargando = ["title","artist"]
df_descargar= df[descargando]

#Descargamos de la Api de Deezer usando la funcion descargar y hacemos una columna nueva
d_albunes = descargar(df_descargar)
df["albums"] = d_albunes

# Miramos los nulos y eliminamos esos registros.
df.drop(df[df.albums.isnull()].index, inplace=True) 
print(df)
#Sacamos un informe con los titulos, la duración 
#y la cantidad de veces que se ha repitido esa canción


df_group = df.groupby(['title', 'dur']).count()[["country"]]
print(df_group)


print(df.dur.describe())

#Creamos un DataFrame de estadisticas y hacemos un describe 
#con respecto a la duracion


df.to_csv('./csv/terminado.csv')

#Uso argaparse
argParse("./csv/terminado.csv")