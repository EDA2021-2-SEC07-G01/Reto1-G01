﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1 - Cargar información en el catálogo")
    print("2 - Listar cronológicamente los artistas")
    print("3 - Listar cronológicamente las adquisiciones")
    print("4 - Clasificar las obras de un artista por técnica")
    print("5 - Clasificar la obra por la nacionalidad de sus creadores")
    print("6 - Transportar obras de un departamento")
    print("7 - Proponer una nueva exposición en el museo")
    print("0 - Salir")

def initCatalog(option): # the option is for selecting the datastructure
    """
    Inicializa el catalogo de obras de arte
    """
    return controller.initCatalog(option)

def loadData(catalog):
    """
    Carga las obras de arte en la estructura de datos
    """
    controller.loadData(catalog)

def last3elements(catalog):
    artists = catalog['artists']['elements'][-3:]
    artworks = catalog['artworks']['elements'][-3:]
    last3_artist = ''
    last3_artworks = ''
    for i in range(0 , lt.size(artists)):
        artist_value = artists[i]['name']
        artwork_value = artworks[i]['Title']
        last3_artist += str(artist_value) + '\n'
        last3_artworks += str(artwork_value) + '\n'

    print("\nLos últimos tres artistas en el archivo son: \n"+str(last3_artist))
    print("Las últimas tres obras de arte en el archivo son: \n"+str(last3_artworks))

def ArtistSize(catalog):
    list_artists = catalog['artists']
    print("\nEl número total de artistas es: "+str(lt.size(list_artists)))

def ArtworkSize(catalog):
    list_artworks = catalog['artworks']
    print("El número total de obras de arte es: "+str(lt.size(list_artworks)))

def artistDates(catalog, anio_inicial, anio_final):
    list_artists = controller.artistDates(catalog, anio_inicial, anio_final)

def printSortResults(ord_list, sample = 12):
    size = lt.size(ord_list)
    if size > sample:
        print("Las primeras ", sample, "obras de arte ordenadas son: ")
        i = 1
        while i <= sample:
            artwork = lt.getElement(ord_list, i)
            print("Title: " + artwork["Title"] + "Date: " + artwork["DateAcquired"])
            i += 1

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Seleccione:") 
        opcion = int(input("El número 1 para usar la representación Array_List o 2 para Single_linked: \n"))
        print("Cargando información de los archivos ....")
        catalog = initCatalog(opcion)
        loadData(catalog)
        ArtistSize(catalog)
        ArtworkSize(catalog)
        #last3elements(catalog)

    elif int(inputs[0]) == 2:
        anio_inicial = input("Ingrese el año inicial: ")
        anio_final = input("Ingrese el año final: ")
        artistDates(catalog, anio_inicial, anio_final)

    elif int(inputs[0]) == 3:
        muestra = int(input("Elija el tamaño de la muestra: "))
        sublist = controller.Generate_sublist(catalog, muestra)
        sort_method = int(input("Seleccione un número para el algoritmo de ordenamiento: 1-Insertion, 2-Shell, 3-Merge, 4-Quick Sort \n"))
        artworks = controller.sortArtworks(sublist, int(sort_method)) # lista con tamaño de la muestra
        print("El tiempo de ordenamiento en milisegundos fue de: " + str(artworks[0]) + " para una muestra de tamaño " + str(muestra))
        printSortResults(artworks[1])

    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        pass
    elif int(inputs[0]) == 7:
        pass
    else:
        sys.exit(0)
sys.exit(0)
