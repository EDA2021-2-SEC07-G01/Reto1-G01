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


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def initCatalog():
    """
    Inicializa el catálogo de obras del MoMA. Crea una lista vacia para guardar
    todos los artistas y las obras de arte. Retorna el catalogo inicializado.
    """
    catalog = {'artists': None,
               'artworks': None,}

    catalog['artists'] = lt.newList(datastructure="ARRAY_LIST", cmpfunction= compareArtists)
    catalog['artworks'] = lt.newList(datastructure="ARRAY_LIST")

    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    """
    Adiciona un artista a la lista de artistas
    """
    aux = newArtist(artist['DisplayName'])
    lt.addLast(catalog['artists'], aux)

def addArtwork(catalog, artwork):
    """
    Adiciona una obra de arte a la lista de obras de arte
    """
    t = newArtwork(artwork['Title'])
    lt.addLast(catalog['artworks'], t)

# Funciones para creacion de datos

def newArtist(name):
    """
    Esta estructura almancena los tags utilizados para marcar artistas.
    """
    name_artist = {'name': name}
    return name_artist

def newArtwork(name):
    """
    Esta estructura almancena las obras de arte.
    """
    name_artwork = {'name': name}
    return name_artwork

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def compareArtists(authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1

# Funciones de ordenamiento