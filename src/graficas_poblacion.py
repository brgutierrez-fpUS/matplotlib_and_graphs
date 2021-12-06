# -*- coding: utf-8 -*-
'''
Created on 6 dic. 2021

@author: Belen Ramos
'''

import csv
from collections import namedtuple
from matplotlib import pyplot as plt

Poblacion = namedtuple('Poblacion', 'nombre, codigo, anyo, censo')


def lee_poblaciones(fichero):
    ''' Lee el fichero de entrada y devuelve una lista de tuplas poblaciones.
        Los tipos numéricos deben ser de tipo int.

    ENTRADA: 
        @param fichero: ruta del fichero csv que contiene los datos en codificación utf-8
        @type: fichero: str
    SALIDA: 
       @return lista de tuplas con la información de las poblaciones (nombre, código, anyo, censo)
       @rtype: [Poblacion(str,str,int,int)]
    '''
    poblaciones = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        for nombre, codigo, anyo, censo in lector:
            tupla = Poblacion(nombre, codigo, int(anyo), int(censo))
            poblaciones.append(tupla)
    return poblaciones


def filtra_por_pais(poblaciones, pais):
    '''A partir de la lista de poblaciones y del nombre o código de un país,  genera como salida
       una lista de tuplas con los datos de población del país dado por parámetro.  

    ENTRADA: 
        @param poblaciones: lista de tuplas Poblacion(nombre, código, año, censo) 
        @type: poblaciones: [Poblacion(str,str,int,int)]
        @param pais: nombre o código del país del que seleccionarán los registros
        @type: pais: str
    SALIDA: 
        @return lista de tuplas con la información de cada año y censo para el país dado (anyo, censo)
        @rtype: [(int,int)]
    '''
    poblaciones_filtradas = []
    for pais_i in poblaciones:
        if pais_i.nombre == pais or pais_i.codigo == pais:
            poblaciones_filtradas.append((pais_i.anyo, pais_i.censo))

    return poblaciones_filtradas


def muestra_evolucion_poblacion(poblaciones, pais):
    ''' Genera una curva con la evolución de la población de un país. El pais puede
    darse como su nombre completo o por su código.
    
    ENTRADA: 
       - poblaciones: lista de tuplas (nombre, código, año, censo) -> [(str, str, int, int)]
       - pais: del que se generará la gráfica -> str
    SALIDA EN PANTALLA: 
       - diagrama con la evolución del censo del país

    Toma como entrada una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    produce como salida un gráfico con la evolución de la población del país dado como
    parámetro a lo largo del tiempo. 
    
    Estas son las instrucciones 'matplotlib' para trazar el gráfico
    a partir una cadena con el título que se va a mostrar en el gráfico,
    una lista de años y otra lista con los número de habitantes (con el mismo orden):
        
        plt.title(titulo)
        plt.plot(l_anyos,l_habitantes)
        plt.show()
    '''
    pass


def filtra_por_paises_y_anyo(poblaciones, anyo, paises):
    ''' A partir de la lista de poblaciones, un año concreto y una lista de nombres de países,
    selecciona las tuplas correspondientes a un conjunto de paises de un año concreto

    ENTRADA: 
        @param poblaciones: lista de tuplas Poblacion(nombre, código, año, censo) 
        @type: poblaciones: [Poblacion(str,str,int,int)]
        @param anyo: año del que se buscan los datos de censo 
        @type: anyo: int
        @param paises: lista con los nombres de los países que se seleccionarán en los registros
        @type: pais: [str]
    SALIDA: 
        @return lista de tuplas con la el nombre de cada país y censo para el año dado (pais, censo)
        @rtype: [(str,int)]

    '''
    poblaciones_filtradas = []
    for p_i in poblaciones:
        if p_i.anyo == anyo and p_i.nombre in paises:
            poblaciones_filtradas.append((p_i.nombre, p_i.censo))

    return poblaciones_filtradas


def muestra_comparativa_paises_anyo(poblaciones, anyo, paises):
    ''' Genera una gráfica de barras en la que se muestra la comparativa de
    la población de varios países en un año concreto
    
    ENTRADA: 
       - poblaciones: lista de tuplas (nombre, código, año, censo) -> [(str, str, int, int)]
       - anyo: del que se generará la gráfica -> int
       - paises: de los que se generará la gráfica -> [str]
    SALIDA EN PANTALLA: 
       - diagrama de barras con la comparativa del censo por paises

    Toma como entrada una lista de tuplas (nombre_pais, cod_pais, anyo, num_habitantes) y 
    produce como salida un gráfico de barras con el número de habitantes de los paises 
    dados como parámetro en el año anyo.
    Cada barra corresponde a un pais.
    
    Estas son las instrucciones 'matplotlib' para trazar el diagrama de barras
    a partir de una cadena con el título del gráfico, 
    una lista de nombres paises y otra lista (con el mismo orden) de
    número de habitantes de esos países:
       
        plt.title(titulo)
        indice = range(len(l_paises))
        plt.bar(indice, l_habitantes)
        plt.xticks(indice, l_paises, fontsize=8)
        plt.show()
    '''
    pass
