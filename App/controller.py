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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def initcatalog():
    catalog = model.initcatalog()
    return catalog

def intiCategoria():
    Categoria= model.intiCategoria()
    return Categoria

def loaddata(catalog,Categoria):
    cargardatoscat(Categoria)
    cargardatosvideoslarge(catalog)


def cargardatos(catalog):
    vfile = cf.data_dir + 'videos/videos-small.csv'
    input_file = csv.DictReader(open(vfile, encoding='utf-8'))
    for video in input_file:
        model.addvideo(catalog, video)

def cargardatoscat(Categoria):
    vfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(vfile, encoding='utf-8'))
    for categoria in input_file:
        model.addcatgories(Categoria, categoria)

def cargardatosvideoslarge(catalog):
    vfile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(vfile, encoding='utf-8'))
    for videol in input_file:
        model.addvideolarge(catalog, videol)

def requerimiento1(category_name,country,n,catalog,Categoria):
    return model.requerimiento1(category_name,country,n,catalog,Categoria)
def requerimiento2(catalog,country):
    return model.requerimiento2(catalog,country)



# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
