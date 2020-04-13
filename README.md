##Proyecto Data Analisys Pipiline:

![](./imagenes/Musica.jpeg)


En este proyecto vamos a un csv de musica.
#Limpiamos el csv:
Seleccionamos el csv llamado top50contry.csv.
Primero miramos las columnas que tiene par hacernos una idea de que tenemos y que vamos a utilizar. Miramos la cantidad de columna y le número de filas.
Eliminamos los duplicados para no tener duplicados.
Miramos los nulos que tienen y la suma de ellos con respecto a las columnas.
En la columna “top genre” cambiamos los nulos por el nombre del genero. Elijo las columnas que voy a usar y renombro el data-frame a df_clean.
Coloco la tabla de mayor a menor con respecto a las columnas “title” y la columna “artist”.
Elimino los nombre ilógicos de las filas, por ejemplo los que empiezan “<u+05...” . También los titulos incoherentes y algunos numéricos sin sentido.
Elimino los valores NaN de la columna val.
Cambio de flotante a entero el tipo de la columna val.
Guardo mi csv limpio en la carpeta csv como clean.csv.



#Usaremos la Api de Deezer:

Añadiremos desde la Api de Deezer la columna Albums que tendrá dentro el álbum de la canción con respecto al cantante.
Para ello sacaremos el token y después de identificarnos empezaremos a buscar los álbumes.
Para ello hago una prueba con uno en particular. A continuación tenemos un json que busco con la función “buscarAlbum” el nombre exacto del álbum.
Ya que tengo la prueba de que funcionan mis funciones lo automatizo con las funciones “descargar” y la función “buscarAlbum”, así puedo hacer una columna nueva que nos da el álbum de cada artista y la canción que le metemos como parámetros.

Ahora que tenemos el data-frame miramos si tiene nulos y los eliminamos.
Sacamos un informe con los títulos la duración y la cantidad de veces que se ha repetido esa canción.
#Reporte visual.
Imprimimos por pantalla un reporte del los mínimos, máximos, etc… de la columna “dur”, que indica la duración de las canciones.
#Utilidad desde termina.
Por último guardo el dataframe en la carpeta de csv llamándolo “terminado”.
Y ejecuto la función “argParse” lo que nos hace que tengamos varios parámetros que podremos filtrar el csv desde la terminal.
Los parámetros que voy a usar son los siguientes:
-  Country     →   --pais, -a
-  Valoración →   --valoracion, -v
-  Artista        →   --artista, -a
	