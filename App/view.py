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

def initCatalog():
    """
    Inicializa el catalogo de obras de arte
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga las obras de arte en la estructura de datos
    """
    controller.loadData(catalog)


def printAuthorData(author):
    if author:
        print('Autor encontrado: ' + author['name'])
        print('Promedio: ' + str(author['average_rating']))
        print('Total de libros: ' + str(lt.size(author['books'])))
        for book in lt.iterator(author['books']):
            print('Titulo: ' + book['title'] + '  ISBN: ' + book['isbn'])
    else:
        print('No se encontro el autor')


def printBestBooks(books):
    size = lt.size(books)
    if size:
        print(' Estos son los mejores libros: ')
        for book in lt.iterator(books):
            print('Titulo: ' + book['title'] + '  ISBN: ' +
                  book['isbn'] + ' Rating: ' + book['average_rating'])
    else:
        print('No se encontraron libros')

def last3elements(catalog):
    artists = catalog['artists']['elements'][-3:]
    artworks = catalog['artworks']['elements'][-3:]
    print(catalog['artworks']['elements'][0:19])
    last3_artist = ''
    last3_artworks = ''
    for i in range(0 , len(artists)):
        artist_value = artists[i]['name']
        artwork_value = artworks[i]['name']
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

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        ArtistSize(catalog)
        ArtworkSize(catalog)
        last3elements(catalog)

    elif int(inputs[0]) == 2:
        pass
    elif int(inputs[0]) == 3:
        pass
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
