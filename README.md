# brute_File_Carving
brute force file recovery PoC

Prueba de concepto de recuperacion de imagenes corruptas mediante tecnica de fuerza bruta

# Intrucciones:

* Se debe tener python 2.7.x instalado para ejecutar el script
* Descargar los archivos a cualquier carpeta del computador:
  brute_File_Carving.py
  Test_Image.jpg
* Ejecutar el script brute_File_Carving.py
* El script generará una serie de imagenes a partir de la imagen original "Test_Image.jpg"
* Si se desea se pueden modificar porciones del codigo o el nombre de la imagen y cmabiarla por otra para que el script la procese.

# Proceso adicional para crear animacion gif con las imagenes creadas, el resultado será un gif que muestra como se crea la imagen pixel a pixel:

* Se debe tener image magick instalado en la maquina http://www.imagemagick.org/script/binary-releases.php
* Se debe bajar la resolución de todas las imagenes jpg antes de crear el gif con ellas para que no quede muy pesado, se usa el   comando mogrify:
  C:\ImageMagick-6.8.8-10\mogrify -resample 72x72 -resize 256x256 *.JPG
* Ejecutar el comando convert de image magick con estos parametros para crear el gif:
  C:\ImageMagick-6.8.8-10\convert -delay 100 -loop 0 imagen*.jpg animation.gif


# Post con explicación detallada:
http://kr1shn4murt1.blogspot.com.co/2016/04/brutefilecarving-recuperacion-de.html

# Video mostrando la ejecución:
https://www.youtube.com/watch?v=1egeEnJmDXs
