import pandas as pd
import sys
import argparse

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
    if any(vars(args).values()):
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