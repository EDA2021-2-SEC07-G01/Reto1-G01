"""
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
    aux = newArtist(artist['DisplayName'], artist['BeginDate'], artist['Nationality'], artist['Gender'])
    lt.addLast(catalog['artists'], aux)

def addArtwork(catalog, artwork):
    """
    Adiciona una obra de arte a la lista de obras de arte
    """
    t = newArtwork(artwork['Title'], artwork['DateAcquired'])
    lt.addLast(catalog['artworks'], t)

# Funciones para creacion de datos

def newArtist(name, birth_date, nationality, gender):
    """
    Esta estructura almancena los tags utilizados para marcar artistas.
    """
    artist = {'name': name, 'birth_date': birth_date, 'nationality': nationality, 'gender': gender}
    return artist

def newArtwork(name, date):
    """
    Esta estructura almancena las obras de arte.
    """
    artwork = {'Title': name, 'DateAcquired':date}
    return artwork

# Funciones de consulta
def Generate_sublist(catalog, sample):
    assert(sample <= lt.size(catalog['artworks'])), "Debe indicar un tamaño menor o igual a la cantidad de total de obras de arte"
    return lt.subList(catalog['artworks'],1,sample)

def artistDates(catalog, anio_inicial, anio_final):
    sorted_dict = {}
    for artist in catalog["artists"]:
        if artist["birth_date"] >= anio_inicial and artist["birth_date"] <= anio_final:
            sorted_dict # TODO
    return True

# Funciones utilizadas para comparar elementos dentro de una lista

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

def sortArtworks(subList, sorting_method):
    if sorting_method == 1:
        start_time = time.process_time()
        sorted_list = insertion.sort(subList, cmpArtworkByDateAcquired)
        stop_time = time.process_time()
    elif sorting_method == 2:
        start_time = time.process_time()
        sorted_list = shell.sort(subList, cmpArtworkByDateAcquired)
        stop_time = time.process_time()
    elif sorting_method == 3:
        start_time = time.process_time()        
        sorted_list = merge.sort(subList, cmpArtworkByDateAcquired)
        stop_time = time.process_time()
    elif sorting_method == 4:
        start_time = time.process_time()        
        sorted_list = quick.sort(subList, cmpArtworkByDateAcquired)
        stop_time = time.process_time()
    elapsed_time = (stop_time - start_time)*1000
    return elapsed_time, sorted_list

