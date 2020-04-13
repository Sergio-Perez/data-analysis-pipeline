import requests
import json
import pandas as pd
import os

from dotenv import load_dotenv
load_dotenv()


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
