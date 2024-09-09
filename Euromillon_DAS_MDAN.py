# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:56:00 2021

@author: David Alcázar Sánchez, Mariano Djemil Adelakum Nzang
"""
#_________________________________________________________________________________________________________________
#CÓDIGO EUROMILLON

#Este documento comentaremos por qué motivo llamamos a las funciones.
#Se pueden encontrar los comentarios relativos al funcionamiento de la propia función en la librería.
#Antes de tirar cualquier línea de código, vamos a importar la biblioteca con nuestras funciones.
import LibEuromillon_DAS_MDAN

print("  ¡VAMOS A JUGAR A  ")
print("   EL EUROMILLÓN!")
print("--------------------")
print("| 1 10 19 28 37 46 |")
print("| 2 11 20 29 38 47 |")
print("| 3 12 21 30 39 48 |")
print("| 4 13 22 31 40 49 |")
print("| 5 14 23 32 41 50 |")
print("| 6 15 24 33 42    |")
print("| 7 16 25 34 43    |")
print("| 8 17 26 35 44    |")
print("| 9 18 27 36 45    |")
print("--------------------")
print("| 1 5 9  |")
print("| 2 6 10 |")
print("| 3 7 11 |")
print("| 4 8 12 |")
print("----------\n") 

print ("Para empezar a jugar, tienes que escoger cinco números entre el 1 y el 50 y dos estrellas entre el 1 el 12.")

#Agregamos las listas vacías que llenaremos después tanto con los campos seleccionados
#como con los generados automáticamente.
listaNumeros = []
listaEstrellas = []
numerosRandom =[]
estrellasRandom =[]

#Llamamos a la función "tuBoletoN" para lanzar los inputs que elegirán los números de la lista.
#Estos inputs llenarán la lista listaNumeros.
LibEuromillon_DAS_MDAN.tuBoletoN(listaNumeros)

print(f"\n\nLa lista de números que has escogido es {listaNumeros}. \n\n")
print("Escoge ahora dos estrellas de la lista.")

#Hacemos exactamente lo mismo con las estrellas mediante la función "tuBoletoE". 
#Esta serie de inputs llenarán la lista listaEstrellas.
LibEuromillon_DAS_MDAN.tuBoletoE(listaEstrellas)

#Con el siguiente print podremos ver la selección completa del boleto.
print(f"\n\nLas estrellas que has escogidos son {listaEstrellas}. \n\n")
print(f"El boleto con el que vas a participar es:\n\n{listaNumeros}\n{listaEstrellas}\n\n")

#Llamamos a la función "boletoMarcado" para que nos pinte una representación digital del boleto físico con
#las "X" sustituyendo los números y estrellas elegidos.
LibEuromillon_DAS_MDAN.boletoMarcado(listaNumeros, listaEstrellas)

#Pausamos el programa para que el usuario pueda analizar los datos lanzados en consola y continuar con los siguientes.
LibEuromillon_DAS_MDAN.comandoContinuar()

print("\n\n\n\nSe va a generar el boleto ganador..............")
print("\n¡Este es el boleto ganador del sorteo!:\n\n")

#Llamamos a la función "boletoGanador", que se encargará de generar tanto los números como las estrellas
#de un nuevo boleto aleatorio, que será la referencia como boleto ganador.
LibEuromillon_DAS_MDAN.boletoGanador(numerosRandom, estrellasRandom)

print(numerosRandom)
print(estrellasRandom)
print()
print()

#Llamamos a la función ''boletoGanadorMarcado para que nos pinte la representación digital del boleto físico ganador,
#sustituyendo las "X" por los números y estrellas ganadores.
LibEuromillon_DAS_MDAN.boletoGanadorMarcado(numerosRandom, estrellasRandom)

#Una nueva pausa para que el usuario analice la información en pantalla antes de continuar.
LibEuromillon_DAS_MDAN.comandoContinuar()

#Esta es la poca parte de código que hemos decidido no incluir en una función, puesto que depende de
#muchos elementos relativos al propio programa.
#Creamos las variables "aciertosN" y "aciertosE" como contador de coincidencias, y mediante el uso de
#un bucle for dentro de otro bucle for, recorreremos las listas del boleto seleccionado y del ganador 
#generado aleatoriamente para ir sumando coincidencias a los contadores.
aciertosN = 0
aciertosE = 0

for valor1 in listaNumeros:
    for valor2 in numerosRandom:
        if valor1 == valor2:
            aciertosN = aciertosN + 1

#El mismo procedimiento para las estrellas, que guardaremos en la variable "aciertosE"            
for valor1 in listaEstrellas:
    for valor2 in estrellasRandom:
        if valor1 == valor2:
            aciertosE = aciertosE + 1

#Pintamos el número de aciertos totales...            
print (f"\n\n\nHas acertado {aciertosN} número(s) y {aciertosE} estrella(s).")

#Y pausamos de nuevo para que el usuario vuelva a leer la información antes de continuar.
LibEuromillon_DAS_MDAN.comandoContinuar()

print()
#Por último, llamamos a la función "lanzaderaPremios" para que nos lance un mensaje acorde al resultado obtenido.
LibEuromillon_DAS_MDAN.lanzaderaPremios(aciertosN, aciertosE)

