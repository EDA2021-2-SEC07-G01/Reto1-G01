﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import subList
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import mergesort as merge 
from DISClib.Algorithms.Sorting import quicksort as quick
import datetime
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def initCatalog(option):
    """
    Inicializa el catálogo de obras del MoMA. Crea una lista vacia para guardar
    todos los artistas y las obras de arte. Retorna el catalogo inicializado.
    """
    catalog = {'artists': None,
               'artworks': None,}
    if option == 1:
        catalog['artists'] = lt.newList(datastructure="ARRAY_LIST", cmpfunction= compareArtists)
        catalog['artworks'] = lt.newList(datastructure="ARRAY_LIST", cmpfunction= cmpArtworkByDateAcquired)
    elif option == 2:
        catalog['artists'] = lt.newList(datastructure="SINGLE_LINKED", cmpfunction= compareArtists)
        catalog['artworks'] = lt.newList(datastructure="SINGLE_LINKED", cmpfunction= cmpArtworkByDateAcquired)
    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    """
    Adiciona un artista a la lista de artistas
    """
    aux = newArtist(artist['DisplayName'], artist['BeginDate'], artist['EndDate'], artist['Nationality'], artist['Gender'], artist['ConstituentID'])
    lt.addLast(catalog['artists'], aux)

def addArtwork(catalog, artwork):
    """
    Adiciona una obra de arte a la lista de obras de arte
    """
    t = newArtwork(artwork['Title'], artwork['DateAcquired'], artwork['CreditLine'], artwork['ConstituentID'], artwork['Date'], artwork['Medium'], artwork['Dimensions'])
    lt.addLast(catalog['artworks'], t)

# Funciones para creacion de datos

def newArtist(name, birth_date, end_date, nationality, gender, const_id):
    """
    Esta estructura almancena los tags utilizados para marcar artistas.
    """
    artist = {'name': name, 'birth_date': birth_date, 'end_date': end_date, 'nationality': nationality, 'gender': gender, 'const_id': const_id}
    return artist

def newArtwork(name, date_acqu, credit, artist, date, medium, dimensions):
    """
    Esta estructura almancena las obras de arte.
    """
    artwork = {'Title': name, 'DateAcquired':date_acqu, 'CreditLine':credit, 'ConstituentID': artist, 'Date': date, 'Medium': medium, 'Dimensions': dimensions}
    return artwork

# Funciones de consulta

def artistDates(catalog, anio_inicial, anio_final):
    artist_year_list = lt.newList(datastructure="ARRAY_LIST", cmpfunction= compareArtistsDates)
    for artist in catalog["artists"]["elements"]:
        try:
            if int(artist["birth_date"]) >= anio_inicial and int(artist["birth_date"]) <= anio_final:
                lt.addLast(artist_year_list, artist)
        except:
            pass
    sorted_list = sortArtistDates(artist_year_list)
    return sorted_list

def artworksDates(catalog, date_inicial, date_final):
    artworks_list = lt.newList(datastructure="ARRAY_LIST", cmpfunction= cmpArtworkByDateAcquired)
    for artwork in catalog["artworks"]["elements"]:
        try:
            artwork_date = artwork["DateAcquired"].split("-")
            initial = date_inicial.split("-")
            final = date_final.split("-")
            if (datetime.datetime(int(artwork_date[0]), int(artwork_date[1]), int(artwork_date[2])) >= 
            (datetime.datetime(int(initial[0]), int(initial[1]), int(initial[2])))) and (datetime.datetime(int(artwork_date[0]), int(artwork_date[1]), int(artwork_date[2])) <= 
            (datetime.datetime(int(final[0]), int(final[1]), int(final[2])))):
                lt.addLast(artworks_list, artwork)
        except:
            pass
    sorted_list = sortArtworksDates(artworks_list)
    return sorted_list

def artist_technique(catalog, artist_name):
    for artist in catalog["artists"]["elements"]:
        if artist["name"] == artist_name:
            const_id = artist["const_id"]
            break
    assert(const_id != None, "Debe ingresar el nombre de un artista válido para la base de datos" )
    artworks = lt.newList(datastructure='ARRAY_LIST')
    for artwork in catalog["artworks"]["elements"]:
        if const_id in (artwork["ConstituentID"][1:-1].split(",")):
            lt.addLast(artworks, artwork)
    return artworks


# Funciones utilizadas para comparar elementos dentro de una lista

def compareArtistsDates(artist1, artist2):
    try:
        if int(artist1["birth_date"]) <= int(artist2["birth_date"]):
            return True
        else:
            return False
    except:
        pass

def compareArtists(authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1

def cmpArtworkByDateAcquired(artwork1, artwork2): #Formato = año-mes-día
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menor que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    try:
        d1 = artwork1["DateAcquired"].split("-")
        d1 = [int(date) for date in d1]
        d2 = artwork2["DateAcquired"].split("-")
        d2 = [int(date) for date in d2]
        if (datetime.datetime(d1[0], d1[1], d1[2]) < datetime.datetime(d2[0], d2[1], d2[2])): #debido al formato
            return True
        else:
            return False
    except:
        pass

# Funciones de ordenamiento

def sortArtistDates(list):
    return merge.sort(list, compareArtistsDates)

def sortArtworksDates(list):
    return merge.sort(list, cmpArtworkByDateAcquired)

# ---
def Generate_sublist(catalog, sample):
    assert(sample <= lt.size(catalog['artworks'])), "Debe indicar un tamaño menor o igual a la cantidad de total de obras de arte"
    return lt.subList(catalog['artworks'],1,sample)