import requests
import json
import pandas as pd
import os
import sys
from dotenv import load_dotenv
load_dotenv()
import argparse
def buscarAlbum(albunes):    
    if albunes["total"] != 0:
        for elemento in albunes.items():    
            for elem in elemento:
                if type(elem) == list:                   
                    for x,y in elem[0].items():
                        if x =="album":
                             for el,busco in y.items():
                                    if el == 'title':
                                        return  busco
    else:    
        return None

def descargar(df):
    albunes = []
    for index,row in df.iterrows():
        titulo = row.title
        artista = row.artist
        artists_url = f"https://api.deezer.com/search?q=artist:'{artista}' track:'{titulo}'"
        artists_response = requests.get(artists_url)
        album =artists_response.json()
        try:
            albunes.append(buscarAlbum(album))
        except:
            albunes.append(None)

    return albunes


def argParse(archivo):
    df = pd.read_csv(archivo)
    parser = argparse.ArgumentParser(description= "Lee el dataframe y lo devuelve por los valores filtrados")
    parser.add_argument('--artista', '-a', help = 'Nombre del artista por el que se quiere filtrar')
    parser.add_argument('--pais', '-p', help = 'Nombre del pais por el que se quiere filtrar')
    parser.add_argument('--valoracion', '-v', type = int,help = 'Valoracion por la que quieres filtar. Debe ser un número entero entre 0 y 100 ')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if args.artista != None: # tengo artista
        if args.valoracion == None:
            if args.pais == None:
                print(df[df["artist"].str.lower() == args.artista.lower()])
            
            else: # tengo pais
                print(df[(df["country"].str.lower() == args.pais.lower()) & (df["artist"].str.lower() == args.artista.lower())])

        else: # tengo valoración
            if args.valoracion < 0 or args.valoracion > 100:
                print(f"ErrorValoracion: La valoración tiene que ser un número entre 0 y 100")
            
            else:    
                if args.pais == None:
                    print(df[(df["val"] == args.valoracion) & (df["artist"].str.lower() == args.artista.lower())])
            
                else: # tengo pais
                    print(df[(df["val"] == args.valoracion) & (df["artist"].str.lower() == args.artista.lower()) & (df["country"].str.lower() == args.pais.lower())])
    else: # no tengo artista
        
        if args.valoracion == None:
            if args.pais == None:
                print(df)
            
            else: # tengo pais
                print(df[df["country"].str.lower() == args.pais.lower()]) 

        else: # tengo valoración
            if args.valoracion < 0 or args.valoracion > 100:
                print(f"ErrorValoracion: La valoración tiene que ser un número entre 0 y 100")
            else:
                if args.pais == None:
                    print(df[(df["val"] == args.valoracion)])
            
                else: # tengo pais
                    print(df[(df["val"] == args.valoracion) & (df["country"].str.lower() == args.pais.lower())])