# Proyecto Data Analisys Pipiline:

![](./imagenes/Musica.jpeg)


En este proyecto vamos a analizar un csv de música.


## Limpiamos el csv:


Seleccionamos el csv llamado top50contry.csv.
Primero miramos las columnas que tiene par hacernos una idea de qué tenemos y qué vamos a utilizar. Miramos la cantidad de columna y el número de filas.
Eliminamos los duplicados.
Miramos los nulos que tienen y la suma de ellos con respecto a las columnas.
En la columna “top genre” cambiamos los nulos por el nombre del género. Elijo las columnas que voy a usar y renombro el data-frame a df_clean.
Coloco la tabla de mayor a menor con respecto a las columnas “title” y “artist”.
Elimino los nombre ilógicos de las filas, por ejemplo los que empiezan “<u+05...” . También los títulos incoherentes y algunos numéricos sin sentido.
Elimino los valores NaN de la columna val.
Cambio de flotante a entero el tipo de la columna val.
Guardo mi csv limpio en la carpeta csv como clean.csv.



## Usaremos la Api de Deezer:

Añadiremos desde la Api de Deezer la columna Albums que tendrá dentro el álbum de la canción con respecto al cantante.
Para ello sacaremos el token y después de identificarnos empezaremos a buscar los álbumes.
Para ello hago una prueba con uno en particular. A continuación, con la función “buscarAlbum”, creamos un json y extraemos el nombre exacto del álbum.
Ya que tengo la prueba de que funcionan mis funciones lo automatizo con las funciones “descargar” y la función “buscarAlbum”, así puedo hacer una columna nueva que nos da el álbum de cada artista y la canción que le metemos como parámetros.

Ahora que tenemos el data-frame miramos si tiene nulos en la nueva columna y los eliminamos.

## Reporte visual.

Imprimimos por pantalla un informe con los títulos la duración y la cantidad de veces que se ha repetido esa canción, lo que indica en que países fueron top esas canciones.
Imprimimos por pantalla un informe de los mínimos, máximos, etc… de la columna “dur”, que indica la duración de las canciones.

## Utilidad desde termina.

Por último guardo el dataframe en la carpeta de csv llamándolo “terminado”.
Ejecuto la función “argParse” desde la carpeta funciones.py, lo que nos hace que tengamos varios parámetros con los que podremos filtrar el csv desde el terminal.
Los parámetros que voy a usar son los siguientes:
-  Country     →   --pais, -p
-  Valoración  →   --valoracion, -v
-  Artista     →   --artista, -a
	