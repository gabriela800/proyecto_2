# Alba Gabriela Yool Alvarado ________1990-19-15166
# Paula Yohana Hernandez Morales _____1990-19-17246
#_____________________________________________________________________________
#_____________________________________________________________________________

import json
import glob
import os

datos=[]
registro={}
print("")
print("RENUEVA NOMBRE DE ARCHIVOS DE UNA FORMA FACIL")
print("____________INGRESAR_____________ \n")

#Se ingresa el URL ejemplo:/home/personal/Escritorio en donde esta almacenados los archivos que se desea cambiar
print("Ingrese la Ruta")
ruta_carpeta = input(">>")    
os.system('clear')

#En esta opcion podemos visualizar los diferentes archivos que contiene la carpeta
print("Mostrando Vista previa de los Archivos de la Carpeta \n")
for item in os.listdir(ruta_carpeta):
    print(item)
print("")

#puede ingresar las diferentes extenciones que contiene su carpeta, por ejemplo: jpg,png,txt,py
print("Ingrese  el Tipo de Extencion que desee ")
extencion_archivo = input(">>")
print("")

#Genera un nuevo nombre a archivos, imagenes etc, existentes en  la carpeta.
print("Nuevo Nombre")
nuevo=input(">>")
numero=0
print("")
os.system('clear')
print("___________REGISTRO_______\n")

#Esta linea, se utiliza para llamar al archivo en dicha ruta dependiendo el tipo de extencion que ingresamos
original= sorted(glob.glob(ruta_carpeta + f'/*.{extencion_archivo}'))
datos=[]
for i in original:   

    #busca en la ruta ingresada y renueva el nombre del archivo
    cambio_nombre = ruta_carpeta + '/' + str(f'{nuevo}_{numero}') + f'.{extencion_archivo}' 
      
    #su funcion es enumerar desde 0 los archivos a generar, ejemplo: progra_0, progra_1, progra_2 etc.
    numero=numero+ 1
    nuevo_nombre = cambio_nombre
    os.rename(i , nuevo_nombre)#su funcion es trasladar el nombre Original a nombre Nuevo
    registro={}#almacena todos los datos obtenidos
    registro['Original']=i.split('/')[-1]
    registro['Nuevo']= nuevo_nombre.split('/')[-1]#su funcion es mostrar el nombre del archivo sin generar una ruta
    print(registro)
    datos.append(registro)#guarda todo
    print("")

#json (JavaScript Object Notation) es un formato ligero de intercambio de datos.
respuesta= input("Ingrese el nombre con que desee guardar el Json   > >   ")
respuesta1=respuesta+".json"
print(respuesta1)
direccion= input("Ingrese la ubicacion donde desea almacenar el archivo   > >  ")
#dir = 'C:/Pruebas'  # Tambien es valido 'C:\\Pruebas' o direccion de Desktop y de carpeta donde se va a almacenar.
		
with open(os.path.join(direccion, respuesta1),  'w') as archivo:
	json.dump(datos, archivo)
	print("")
	print("____________________Archivo exportado____________________")
	print("")
		