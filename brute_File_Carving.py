#autor: @kr1shn4murt1
#fecha: Nov 20 - 2012
# Proposito del script: Prueba de concepto de recuperacion de 
# imagenes corruptas mediante tecnica de fuerza bruta
# https://github.com/kr1shn4murt1/brute_File_Carving
# Video mostrando ejecución: https://www.youtube.com/watch?v=1egeEnJmDXs
# Info detallada: http://kr1shn4murt1.blogspot.com.co/2016/04/brutefilecarving-recuperacion-de.html
# PAra mas informacion leer archivo README.md https://github.com/kr1shn4murt1/brute_File_Carving/blob/master/README.md
#!/usr/bin/env python
#-*-coding:utf-8-*-

#Para manipular el contenido binario y hexadecimal del archivo
import binascii 

#Para controlar cuanto demora la ejecucion del script
import time 


horaInicio= time.time()
print '\n \t Hora de inicio del script: ',time.ctime(horaInicio)

"""Imagen de prueba que se descompondra en bytes para luego ser reensamblada
   por partes"""
imagen = 'Test_Image.jpg' 

with open(imagen, 'rb') as f:
	"""Lectura imagen es la correcta representacion del contenido hexadecimal
	al imprimir solo imprime algunos caracteres, no todos"""
	lecturaImagen = f.read()

"""lecturaHex es la representacion humanamente visible 
	del codigo hexadecimal al copiarlo de manera exacta a
	un archivo ejm una imagen no queda bien la imagen, hay
	que hacerle una transformacion antes"""
lecturaHex = (binascii.hexlify(lecturaImagen))

"""Asi se transforma para generar el archivo con el codigo
	hexadecimal"""
hexSecundario=binascii.a2b_hex(lecturaHex) 

print "\n \t Hex reconstruido: ",hexSecundario,"\n"

print "\t Tamano del codigo hex a hacerle carving: ",len(lecturaHex),"\n"
print "\t Tuplas del codigo hex + el footer \n"

#en el caso de ffd9 es una imagen jpg
footerArchivo="ffd9" 

j=1

"""Numero de unidades de bytes en los que se quiere descomponer el archivo, un numero 
	mas pequenho requerira mas tiempo de procesamiento, si es una imagen muy pequenha de 
	aprox 4,2 KB usar 1, si la imagen es grande, 1 MB o mas usar un numero grande como un
	millon por que dependiendo del numero que usen se creara de manera proporcional el 
	mismo numero de imagenes en la carpeta desde donde lo ejecuten"""

numeroBytes=32

numeroBytes=numeroBytes*2
data = lecturaHex

"""Este bloque divide el codigo hexadecimal en el numero
	de bytes escogido para luego insertar despues de cada 
	uno de ellos el footer del tipo de archivo deseado para
	intentar la recuperacion o carving del archivo mediante 
	fuerza bruta"""        			
for i,item in enumerate(data[::numeroBytes]):

    tupla=str(data[:(i*numeroBytes)+numeroBytes:])
    tupla+=footerArchivo
    print "Tupla numero: ",j
    print 'Valores: ',tupla,'\n'
    j+=1

    nombreImagenGenerada="imagen"+str(j)+".jpg"
    imagenes=open(nombreImagenGenerada,'wb')
    imagenes.write(binascii.a2b_hex(tupla))
    imagenes.close()

print '\n \t Numero total de tuplas',j

horaFin= time.time()
print '\n\t Hora de inicio del script: ',time.ctime(horaInicio)
print '\t Hora de finalizacion del script: ',time.ctime(horaFin)
tiempoEjecucion= horaFin-horaInicio
print '\n \t La ejecucion tomo %s segundos\n\n'%str(tiempoEjecucion)
