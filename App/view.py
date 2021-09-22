"""
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
import ipdb
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

def ArtistSize(catalog):
    list_artists = catalog['artists']
    print("\nEl número total de artistas es: "+str(lt.size(list_artists)))

def ArtworkSize(catalog):
    list_artworks = catalog['artworks']
    print("El número total de obras de arte es: "+str(lt.size(list_artworks)))

def artistDates(catalog, anio_inicial, anio_final):
    return controller.artistDates(catalog, anio_inicial, anio_final)

def artworksDates(catalog, date_inicial, date_final):
    return controller.artworksDates(catalog, date_inicial, date_final)

def artist_technique(catalog, artist_name):
    return controller.artist_technique(catalog, artist_name)

def artworks_artistnationality(catalog):
    return controller.artworks_artistnationality(catalog)

def artworks_department(catalog, department):
    return controller.artworks_department(catalog, department)

# PRINT Functions

def printResultsArtworks(ord_list, sample = 3):
    size = lt.size(ord_list)
    if size > sample:
        print("Las primeras ", sample, "obras de arte ordenadas son: ")
        i = 1
        j = 0
        while i <= sample:
            artwork = lt.getElement(ord_list, i)
            const_ids = artwork["ConstituentID"]
            artists = controller.give_artists_byID(catalog, const_ids)
            print("Title: " + artwork["Title"] + ", Date: " + artwork["DateAcquired"] + ", Medio: " + artwork["Medium"] + ", Dimensiones: " + artwork["Dimensions"])
            print("Los artistas involucrados fueron: " + artists)
            i += 1
        print("----------------------------------------------------------------------------------")
        print("Las últimas ", sample, "obras de arte ordenadas son: ")
        while j < sample:
            artwork = lt.getElement(ord_list, size - j )
            print("Title: " + artwork["Title"] + ", Date: " + artwork["DateAcquired"] + ", Medio: " + artwork["Medium"] + ", Dimensiones: " + artwork["Dimensions"])
            print("Los artistas involucrados fueron: " + artists)
            j += 1

def printResultsArtists(ord_list, sample = 3):
    size = lt.size(ord_list)
    if size > sample:
        print("Los primeros ", sample, "artistas en el rango dado son: ")
        i = 1
        j = 0
        while i <= sample:
            artist = lt.getElement(ord_list, i)
            print("Nombre: " + artist["name"] + ", Nacimiento: " + artist["birth_date"] + ", Fallecimiento: " + artist["end_date"] + ", Nacionalidad: " + artist["nationality"] + ", Género: " + artist["gender"])
            i += 1
        print("----------------------------------------------------------------------------------")
        print("Los últimos ", sample, "artistas en el rango dado son: ")
        while j < sample:
            artist = lt.getElement(ord_list, size - j )
            print("Nombre: " + artist["name"] + ", Nacimiento: " + artist["birth_date"] + ", Fallecimiento: " + artist["end_date"] + ", Nacionalidad: " + artist["nationality"] + ", Género: " + artist["gender"])
            j += 1

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog(option=1)
        loadData(catalog)
        ArtistSize(catalog)
        ArtworkSize(catalog)

    elif int(inputs[0]) == 2:
        anio_inicial = int(input("Ingrese el año inicial: "))
        anio_final = int(input("Ingrese el año final: "))
        organized = artistDates(catalog, anio_inicial, anio_final)
        print("El número total de artistas para el rango dado es: " + str(lt.size(organized)))
        printResultsArtists(organized, sample=3)

    elif int(inputs[0]) == 3:
        date_inicial = input('Ingrese la fecha inicial de adquisición en el formato AAAA-MM-DD: ')
        date_final = input('Ingrese la fecha final de adquisición en el formato AAAA-MM-DD: ')
        organized, contador = artworksDates(catalog, date_inicial, date_final)
        print("El número total de obras en el rango cronológico es: " + str(lt.size(organized)))
        print("El número total de obras adquiridas por compra es: " + str(contador))
        printResultsArtworks(organized, sample=3)

    elif int(inputs[0]) == 4:
        name_artist = input("Ingrese el nombre del artista para clasificar sus obras por técnica: ")
        artworks, techniques = artist_technique(catalog, name_artist)
        print("El número total de obras para: " + name_artist + "son: " + str(lt.size(artworks)))
        print("El número total de técnicas utilizadas por " + name_artist + "son: " + str(len(techniques)))

    elif int(inputs[0]) == 5:
        #ipdb.set_trace()
        print(artworks_artistnationality(catalog))
        
    elif int(inputs[0]) == 6:
        department = input("Departamento del museo: ")
        artworks = artworks_department(catalog, department)
        print(artworks[0])
        print(artworks[1])

    elif int(inputs[0]) == 7:
        pass
    else:
        sys.exit(0)
sys.exit(0)