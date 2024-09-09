# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:37:25 2021

@author: David Alcázar Sánchez, Mariano Djemil Adelakum Nzang
"""

#________________________________________________________________________________________________________________
#FUNCIONES EUROMILLON


#Función utilizada para pedir números mediante una serie de inputs.
#Depende de variable externa 'listaNúmeros'.
def tuBoletoN(listaNumeros):

#La variable 'x' la utilizaremos como contador, y la variable 'auxiliar' la utilizaremos más tarde.    
    x = 0
    auxiliar = 0

#Mediante un bucle while, donde limitaremos el proceso a 5 para así poder elegir solo 5 números:    
    while x<5:
        seleccion = int(input("Elige un número entre 1 y 50: "))
#Este if lo utilizamos para limitar el rango entre 1 y 50.    
        if seleccion >= 1 and seleccion <= 50:
#El siguiente if lo utilizamos para comprobar si el número que hemos elegido ya lo habíamos elegido previamente,
#ya que si lo habíamos elegido, estará en la lista de números seleccionados.
                if seleccion in listaNumeros:
                    print("¡Ya has elegido ese número! Elige otro.")
#En cualquier otro caso, y siempre dentro del rango, se añadirá a la lista y se sumará 1 al contador.
#Nótese que situamos la comprobación en una línea superior, para que no haya errores con el contador.
                else:
                    listaNumeros += [seleccion]
                    x= x+1
#Por último, si elegimos un número fuera de rango, nos lanzará otro mensaje de error y nos pedirá otro número.
#Elegir un número fuera de rango tampoco aumentará el contador de límite de 5 números.                  
        elif seleccion < 1 or seleccion > 50:
            print("¡Has escogido un número fuera de rango! Elige otro.")

#Las siguientes líneas de código corresponden al método de ordenación en burbuja.
#Lo hemos introducido para ordenar en la propia consola de comandos los números, en caso de que el usuario 
#los introduzca de manera desordenada. Esto hará más cómoda la propia comprobación visual del usuario.
#Con un for dentro de otro for, recorremos toda la lista y, con la ayuda de la variable "auxiliar" declarada
#al principio de la función, colocaremos todos los números de la lista de menor a mayor.     
    for num in range(len(listaNumeros)-1, -1, -1):
        for recorrido in range(num):
            if listaNumeros[recorrido] > listaNumeros[recorrido + 1]:
                auxiliar = listaNumeros[recorrido]
                listaNumeros[recorrido] = listaNumeros [recorrido + 1]
                listaNumeros[recorrido +1] = auxiliar


#La función 'tuBoletoE' es exactamente igual que la función 'tuBoletoN', con la diferencia de que el limitador
#será de 2 (2 estrellas) y el rango a elegir número estará esta vez entre 1 y 12.  
#Depende de variable externa listaEstrellas.              
def tuBoletoE(listaEstrellas):
    
    y = 0
    auxiliar2 = 0
        
    while y<2:
        seleccion = int(input("Elige un número entre 1 y 12: "))
        if seleccion >= 1 and seleccion <= 12:
                if seleccion in listaEstrellas:
                    print("¡Ya has elegido esa estrella! Elige otra.")
                else:
                    listaEstrellas += [seleccion]
                    y= y+1
        elif seleccion < 1 or seleccion > 12:
            print("¡Has escogido una estrella fuera de rango! Elige otra.")
            
#De nuevo, el método de ordenación burbuja.    
    for num in range(len(listaEstrellas)-1, -1, -1):
        for recorrido in range(num):
            if listaEstrellas[recorrido] > listaEstrellas[recorrido + 1]:
                auxiliar2 = listaEstrellas[recorrido]
                listaEstrellas[recorrido] = listaEstrellas[recorrido + 1]
                listaEstrellas[recorrido +1] = auxiliar2

#La función 'boletoMarcado es una función que, modificando el print del boleto del enunciado en listas, compara 
#el boleto generado a través del input con las listas para sustituir los números coincidentes por 'X'. 
#Una vez repasadas y modificadas todas las listas, crearemos un nuevo print simulando el boleto generado.                
def boletoMarcado(listaNumeros, listaEstrellas):

    lista1 = [1, 10, 19, 28, 37, 46]  #-----> Las listas están diseñadas de forma 
    lista2 = [2, 11, 20, 29, 38, 47]          #que al pintar una detrás de otra simulen el boleto real.
    lista3 = [3, 12, 21, 30, 39, 48]
    lista4 = [4, 13, 22, 31, 40, 49]
    lista5 = [5, 14, 23, 32, 41, 50]
    lista6 = [6, 15, 24, 33, 42]
    lista7 = [7, 16, 25, 34, 43]
    lista8 = [8, 17, 26, 35, 44]
    lista9 = [9, 18, 27, 36, 45]
    
    listaE1 = [1, 5, 9]
    listaE2 = [2, 6, 10]
    listaE3 = [3, 7, 11]
    listaE4 = [4, 8, 12]

#Con un bucle for dentro de otro bucle for, recorreremos cada una de las listas (lista1, lista2...) comparando 
#cada numero en ellas con cada uno de los números generados.    
    for numero in listaNumeros:
        for numeroBoleto in lista1:
#Y en caso de que los números coincidan...
            if [numero] == [numeroBoleto]:
#Utilizando la función 'index' integrada en Python, guardamos en la variable "posición" el número coincidente
#como entero en vez de como campo... 
                posicion = lista1.index(numeroBoleto)
#Para poder sustituirlo en la lista correspondiente por una "X". De otra manera, estaríamos intentando añadir la "X" 
#en la posición del número coincidente, en vez de simplemente sustituir el valor.
                lista1[posicion] = "X"
#Este segundo if es simplemente para que, a la hora de pintar el boleto, no se descuadren las columnas 
#cuando haya que pintar la "X" donde antes había un número de dos dígitos.
                if numero >= 10:
                    lista1[posicion] = " X" # ---> Con un espacio antes de la X, solventamos el error del encuadre.
            
#Mismo procedimiento para las demás listas de números y estrellas:
    for numero in listaNumeros:
        for numeroBoleto in lista2:
            if [numero] == [numeroBoleto]:
                posicion = lista2.index(numeroBoleto)
                lista2[posicion] = "X"
                if numero >= 10:
                    lista2[posicion] = " X"
    
    for numero in listaNumeros:
        for numeroBoleto in lista3:
            if [numero] == [numeroBoleto]:
                posicion = lista3.index(numeroBoleto)
                lista3[posicion] = "X"
                if numero >= 10:
                    lista3[posicion] = " X"
                
    for numero in listaNumeros:
        for numeroBoleto in lista4:
            if [numero] == [numeroBoleto]:
                posicion = lista4.index(numeroBoleto)
                lista4[posicion] = "X"
                if numero >= 10:
                    lista4[posicion] = " X"
                
    for numero in listaNumeros:
        for numeroBoleto in lista5:
            if [numero] == [numeroBoleto]:
                posicion = lista5.index(numeroBoleto)
                lista5[posicion] = "X"
                if numero >= 10:
                    lista5[posicion] = " X"
    
    for numero in listaNumeros:
        for numeroBoleto in lista6:
            if [numero] == [numeroBoleto]:
                posicion = lista6.index(numeroBoleto)
                lista6[posicion] = "X"
                if numero >= 10:
                    lista6[posicion] = " X"
    
    for numero in listaNumeros:
        for numeroBoleto in lista7:
            if [numero] == [numeroBoleto]:
                posicion = lista7.index(numeroBoleto)
                lista7[posicion] = "X"
                if numero >= 10:
                    lista7[posicion] = " X"
                
    for numero in listaNumeros:
        for numeroBoleto in lista8:
            if [numero] == [numeroBoleto]:
                posicion = lista8.index(numeroBoleto)
                lista8[posicion] = "X"
                if numero >= 10:
                    lista8[posicion] = " X"
                
    for numero in listaNumeros:
        for numeroBoleto in lista9:
            if [numero] == [numeroBoleto]:
                posicion = lista9.index(numeroBoleto)
                lista9[posicion] = "X"
                if numero >= 10:
                    lista9[posicion] = " X"

    for numero in listaEstrellas:
        for numeroBoleto in listaE1:
            if [numero] == [numeroBoleto]:
                posicion = listaE1.index(numeroBoleto)
                listaE1[posicion] = "X"
                if numero >= 10:
                    listaE1[posicion] = " X"
                
    for numero in listaEstrellas:
        for numeroBoleto in listaE2:
            if [numero] == [numeroBoleto]:
                posicion = listaE2.index(numeroBoleto)
                listaE2[posicion] = "X"
                if numero >= 10:
                    listaE2[posicion] = " X"
                
    for numero in listaEstrellas:
        for numeroBoleto in listaE3:
            if [numero] == [numeroBoleto]:
                posicion = listaE3.index(numeroBoleto)
                listaE3[posicion] = "X"
                if numero >= 10:
                    listaE3[posicion] = " X"
                
    for numero in listaEstrellas:
        for numeroBoleto in listaE4:
            if [numero] == [numeroBoleto]:
                posicion = listaE4.index(numeroBoleto)
                listaE4[posicion] = "X"
                if numero >= 10:
                    listaE4[posicion] = " X"
                    
#Pintamos el boleto. Utilizaremos un asterisco justo antes de la lista para pintar la propia lista sin corchetes,
#comas o las comillas de las "X", para que quede más estético. Los demás elementos string del print del boleto 
#han sido colocados mediante pruebas en consola hasta que hemos quedado satisfechos con el resultado.                     
    print("--------------------")
    print ("|    ¡TU BOLETO!   |")
    print ("|__________________|")
    print ("|", *lista1, "|")
    print ("|", *lista2, "|")
    print ("|", *lista3, "|")
    print ("|", *lista4, "|")
    print ("|", *lista5, "|")
    print ("|", *lista6, "   |")
    print ("|", *lista7, "   |")
    print ("|", *lista8, "   |")
    print ("|", *lista9, "   |")
    print ("|__________________|")
    print ("| ESTRELLAS    |")
    print ("|______________|")
    print ("|", *listaE1, " |")
    print ("|", *listaE2, "|")
    print ("|", *listaE3, "|")
    print ("|", *listaE4, "|")
    print("----------")
        

#La función boletoGanador es muy similar a las funciones "tuBoletoN" y "tuBoletoE", con la diferencia de que 
#dentro de la propia función importamos el randomizador para que esta vez los números se generen aleatoriamente.
#Esta vez hemos introducido generador de estrellas y de números en la misma función, al ser más sencilla
#por no requerir de inputs externos.
#Depende de dos variables externas, númerosRandom y estrellasRandom.        
def boletoGanador(numerosRandom, estrellasRandom): 
    import random
    x = 0
    auxiliar = 0
#Esta vez, la selección la realizará un generador automático aleatorio al que hemos limitado a un rango, 
#por lo que no nos tendremos que preocupar de que se salga de ahí. El if que utilizabamos anteriormente para 
#limitar al rango ahora ya no es necesario. 
#Sin embargo, el randomizador puede generar dos números iguales, así que el if de comprobación SÍ es necesario.    
    while x<5:
        seleccion = random.randint(1,50)
        if seleccion in numerosRandom:
           seleccion = random.randint(1,50) 
        else:
            numerosRandom += [seleccion]
            x= x+1
            
#De nuevo, método de ordenación burbuja.       
    for num in range(len(numerosRandom)-1, -1, -1):
        for recorrido in range(num):
            if numerosRandom[recorrido] > numerosRandom[recorrido + 1]:
                auxiliar = numerosRandom[recorrido]
                numerosRandom[recorrido] = numerosRandom[recorrido + 1]
                numerosRandom[recorrido +1] = auxiliar

#Exactamente lo mismo para las estrellas, con el cambio en contadores y limitaciones que ya comentamos antes.                                   
    y = 0
    auxiliar2 = 0
    
    while y<2:
        seleccion = random.randint(1,12)
        if seleccion in estrellasRandom:
            seleccion = random.randint(1,50)
        else:
            estrellasRandom += [seleccion]
            y= y+1

#Ordenamos también esta lista.
    for num in range(len(estrellasRandom)-1, -1, -1):
        for recorrido in range(num):
            if estrellasRandom[recorrido] > estrellasRandom[recorrido + 1]:
                auxiliar2 = estrellasRandom[recorrido]
                estrellasRandom[recorrido] = estrellasRandom[recorrido + 1]
                estrellasRandom[recorrido +1] = auxiliar2
                

#La función boletoGanadorMarcado es exactamente la misma función que 'boletoMarcado', pero
#comparando las listas esta vez con los números y estrellas generados aleatoriamente.                
def boletoGanadorMarcado(numerosRandom, estrellasRandom):

    lista1 = [1, 10, 19, 28, 37, 46]
    lista2 = [2, 11, 20, 29, 38, 47]
    lista3 = [3, 12, 21, 30, 39, 48]
    lista4 = [4, 13, 22, 31, 40, 49]
    lista5 = [5, 14, 23, 32, 41, 50]
    lista6 = [6, 15, 24, 33, 42]
    lista7 = [7, 16, 25, 34, 43]
    lista8 = [8, 17, 26, 35, 44]
    lista9 = [9, 18, 27, 36, 45]
    
    listaE1 = [1, 5, 9]
    listaE2 = [2, 6, 10]
    listaE3 = [3, 7, 11]
    listaE4 = [4, 8, 12]

#Exactamente el mismo procedimiento, pero con las listas "numerosRandom" y "estrellasRandom".
    for numero in numerosRandom:
        for numeroBoleto in lista1:
            if [numero] == [numeroBoleto]:
                posicion = lista1.index(numeroBoleto)
                lista1[posicion] = "X"
                if numero >= 10:
                    lista1[posicion] = " X"
                
    for numero in numerosRandom:
        for numeroBoleto in lista2:
            if [numero] == [numeroBoleto]:
                posicion = lista2.index(numeroBoleto)
                lista2[posicion] = "X"
                if numero >= 10:
                    lista2[posicion] = " X"
    
    for numero in numerosRandom:
        for numeroBoleto in lista3:
            if [numero] == [numeroBoleto]:
                posicion = lista3.index(numeroBoleto)
                lista3[posicion] = "X"
                if numero >= 10:
                    lista3[posicion] = " X"
                
    for numero in numerosRandom:
        for numeroBoleto in lista4:
            if [numero] == [numeroBoleto]:
                posicion = lista4.index(numeroBoleto)
                lista4[posicion] = "X"
                if numero >= 10:
                    lista4[posicion] = " X"
                
    for numero in numerosRandom:
        for numeroBoleto in lista5:
            if [numero] == [numeroBoleto]:
                posicion = lista5.index(numeroBoleto)
                lista5[posicion] = "X"
                if numero >= 10:
                    lista5[posicion] = " X"
    
    for numero in numerosRandom:
        for numeroBoleto in lista6:
            if [numero] == [numeroBoleto]:
                posicion = lista6.index(numeroBoleto)
                lista6[posicion] = "X"
                if numero >= 10:
                    lista6[posicion] = " X"
    
    for numero in numerosRandom:
        for numeroBoleto in lista7:
            if [numero] == [numeroBoleto]:
                posicion = lista7.index(numeroBoleto)
                lista7[posicion] = "X"
                if numero >= 10:
                    lista7[posicion] = " X"
                
    for numero in numerosRandom:
        for numeroBoleto in lista8:
            if [numero] == [numeroBoleto]:
                posicion = lista8.index(numeroBoleto)
                lista8[posicion] = "X"
                if numero >= 10:
                    lista8[posicion] = " X"
                
    for numero in numerosRandom:
        for numeroBoleto in lista9:
            if [numero] == [numeroBoleto]:
                posicion = lista9.index(numeroBoleto)
                lista9[posicion] = "X"
                if numero >= 10:
                    lista9[posicion] = " X"

    for numero in estrellasRandom:
        for numeroBoleto in listaE1:
            if [numero] == [numeroBoleto]:
                posicion = listaE1.index(numeroBoleto)
                listaE1[posicion] = "X"
                if numero >= 10:
                    listaE1[posicion] = " X"
                
    for numero in estrellasRandom:
        for numeroBoleto in listaE2:
            if [numero] == [numeroBoleto]:
                posicion = listaE2.index(numeroBoleto)
                listaE2[posicion] = "X"
                if numero >= 10:
                    listaE2[posicion] = " X"
                
    for numero in estrellasRandom:
        for numeroBoleto in listaE3:
            if [numero] == [numeroBoleto]:
                posicion = listaE3.index(numeroBoleto)
                listaE3[posicion] = "X"
                if numero >= 10:
                    listaE3[posicion] = " X"
                
    for numero in estrellasRandom:
        for numeroBoleto in listaE4:
            if [numero] == [numeroBoleto]:
                posicion = listaE4.index(numeroBoleto)
                listaE4[posicion] = "X"
                if numero >= 10:
                    listaE4[posicion] = " X"

#Utilizamos el mismo print que en la otra función, simplemente cambiando el texto "¡TU BOLETO!"
#por "¡BOLETO GANADOR!" para diferenciar.                    
    print("--------------------")                               
    print ("| ¡BOLETO GANADOR! |")
    print ("|__________________|")
    print ("|", *lista1, "|")
    print ("|", *lista2, "|")
    print ("|", *lista3, "|")
    print ("|", *lista4, "|")
    print ("|", *lista5, "|")
    print ("|", *lista6, "   |")
    print ("|", *lista7, "   |")
    print ("|", *lista8, "   |")
    print ("|", *lista9, "   |")
    print ("|__________________|")
    print ("| ESTRELLAS    |")
    print ("|______________|")
    print ("|", *listaE1, " |")
    print ("|", *listaE2, "|")
    print ("|", *listaE3, "|")
    print ("|", *listaE4, "|")
    print("----------")

#Esta función es simplemente un input que utilizaremos para generar una pausa en la consola de comandos.
#Durante la creación del programa, nos fijamos que una vez introducidos los inputs requeridos, 
#la consola de comandos lanzaba el resto del programa sin ninguna pausa, y esto ocasinaba mucha incomodidad a 
#la hora de comprobar el desarrollo del programa. Mediante un input de un comando cualquiera, permitimos
#al usuario del programa el poder detenerse a leer la información lanzada hasta ese punto.
def comandoContinuar():
    comando = input("Presiona enter para continuar: ")
    
#La última función que utilizaremos se trata de "lanzaderaPremios", que utilizaremos tanto para almacenar la 
#información relativa a los premios como para comprobar los premios asignados (o no) nuestros aciertos 
#(operación expresada y explicada en el documento del código).
#La comprobación se realizará mediante distintos "if", donde en cada uno de ellos compararemos tuplas.    
def lanzaderaPremios(aciertosN, aciertosE):
    
    premio1 = (5,2) #-----> Cada uno de los premios se expresa en forma de tupla.
    premio2 = (5,1)
    premio3 = (5,0)
    premio4 = (4,2)
    premio5 = (4,1)
    premio6 = (4,0)
    premio7 = (3,2)
    premio8 = (3,1)       
    premio9 = (3,0)       
    premio10 = (2,2)        
    premio11 = (2,1)   
    premio12 = (2,0)  
    
    if premio1 == (aciertosN, aciertosE): #------> Comprobaremos la tupla asignada a cada premio con la tupla 
                                                   #de nuestros aciertos.
        print ("¡¡¡HAS ACERTADO TODO Y HAS GANADO EL EUROMILLON!!!")
        print ("¡¡¡ENHORABUENA!!!")
        print ("¡¡¡HAS GANADO 15.000.000€!!!")
        
    elif premio2 == (aciertosN, aciertosE):
        print (f"¡¡HAS ACERTADO {aciertosN} NÚMEROS Y {aciertosE} ESTRELLAS!!")
        print ("¡¡SEGUNDO PREMIO!!")
        print ("¡¡HAS GANADO 3.000.000€!!")
        
    elif premio3 == (aciertosN, aciertosE):
        print (f"¡¡HAS ACERTADO {aciertosN} NÚMEROS Y {aciertosE} ESTRELLAS!!")
        print ("¡TERCER PREMIO!")
        print ("¡¡HAS GANADO 1.500.000€!!")
        
    elif premio4 == (aciertosN, aciertosE):
        print (f"¡¡HAS ACERTADO {aciertosN} NÚMEROS Y {aciertosE} ESTRELLAS!!")
        print ("¡Cuarto premio!")
        print ("¡Has ganado 800.000€!")
        
    elif premio5 == (aciertosN, aciertosE):
        print (f"¡¡HAS ACERTADO {aciertosN} NÚMEROS Y {aciertosE} ESTRELLAS!!")
        print ("¡Quinto premio!")
        print ("¡Has ganado 500.000€!")
        
    elif premio6 == (aciertosN, aciertosE):
        print (f"¡¡HAS ACERTADO {aciertosN} NÚMEROS Y {aciertosE} ESTRELLAS!!")
        print ("¡Sexto premio!")
        print ("¡Has ganado 350.000€!")
        
    elif premio7 == (aciertosN, aciertosE):
        print (f"¡¡HAS ACERTADO {aciertosN} NÚMEROS Y {aciertosE} ESTRELLAS!!")
        print ("¡Séptimo premio!")
        print ("¡Has ganado 320.000€!")
        
    elif premio8 == (aciertosN, aciertosE):
        print (f"¡¡HAS ACERTADO {aciertosN} NÚMEROS Y {aciertosE} ESTRELLAS!!")
        print ("¡Octavo premio!")
        print ("¡Has ganado 300.000€!")
    
    elif premio9 == (aciertosN, aciertosE):
        print (f"¡¡HAS ACERTADO {aciertosN} NÚMEROS Y {aciertosE} ESTRELLAS!!")
        print ("¡Noveno premio!")
        print ("¡Has ganado 150.000€!")
        
    elif premio10 == (aciertosN, aciertosE):
        print (f"¡¡HAS ACERTADO {aciertosN} NÚMEROS Y {aciertosE} ESTRELLAS!!")
        print ("¡Décimo premio!")
        print ("¡Has ganado 50.000€!")
        
    elif premio11 == (aciertosN, aciertosE):
        print (f"¡¡HAS ACERTADO {aciertosN} NÚMEROS Y {aciertosE} ESTRELLAS!!")
        print ("¡Undécimo premio!")
        print ("¡Has ganado 10.000€!")
        
    elif premio12 == (aciertosN, aciertosE):
        print (f"¡¡HAS ACERTADO {aciertosN} NÚMEROS Y {aciertosE} ESTRELLAS!!")
        print ("¡Duodécimo premio!")
        print ("¡Has ganado 60€!")
    
    else:
        print("Lo sentimos, no coincide ningún número o la combinación coincidente no equivale a ningún premio. ¡Sigue intentándolo!")