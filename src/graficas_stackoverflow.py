# -*- coding: utf-8 -*-
'''
Created on 6 dic. 2021

@author: Belen Ramos
'''

import csv
from collections import defaultdict, namedtuple, Counter
from itertools import groupby
from matplotlib import pyplot as plt

# EJERCICIO 1:
Pregunta = namedtuple('Pregunta', 'puntuacion, titulo, anyo, etiqueta')


def leer_preguntas(fichero):
    ''' Lee el fichero de registros y devuelve una lista de tuplas con nombre
    
    ENTRADA: 
       @param fichero: nombre del fichero de entrada
       @type fichero: str
    SALIDA: 
       @return: lista de preguntas (puntuacion, titulo, anyo, etiqueta)
       @rtype: [Pregunta(int, str, int, str)]
    '''
    with open(fichero, 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        preguntas = [Pregunta(int(puntuacion), titulo, int(anyo), etiqueta) for puntuacion, titulo, anyo, etiqueta in lector]
        return preguntas


def contar_etiquetas(preguntas):
    ''' Calcula las frecuencias de las etiquetas de una lista de preguntas
    
    ENTRADA: 
       @param preguntas: lista de preguntas (puntuacion, titulo, anyo, etiqueta)
       @type preguntas: [Pregunta(int, str, int, str)]
    SALIDA: 
       @return: diccionario cuyas claves son las etiquetas y los valores las frecuecias
       @rtype: {str: int}
    '''
    
    #===========================================================================
    # etiquetas = [p.etiqueta for p in preguntas]
    # frecuencias = dict()
    # for e in etiquetas:
    #     if e not in frecuencias.keys():
    #         frecuencias[e] = 1
    #     else:
    #         frecuencias[e] = frecuencias[e] + 1
    # return frecuencias
    #===========================================================================
    
    etiquetas = [p.etiqueta for p in preguntas]
    frecuencias = defaultdict(int)
    for e in etiquetas:
        frecuencias[e] += 1
         
    return frecuencias
    
    #===========================================================================
    # etiquetas = [p.etiqueta for p in preguntas]
    # frecuencias = Counter(etiquetas)
    # return dict(frecuencias)
    #===========================================================================


def agrupar_preguntas_por_anyo(preguntas):
    ''' Calcula un diccionario con una lista de preguntas por cada anyo
    
    ENTRADA: 
       @param preguntas: lista de preguntas (puntuacion, titulo, anyo, etiqueta)
       @type preguntas: [Pregunta(int, str, int, str)]
    SALIDA: 
       @return: diccionario cuyas claves son los anyos y los valores la lista de preguntas de cada anyo  
       @rtype: {int: [Pregunta(int, str, int, str)]}
    
    Hay tres alternativas: (1) usar dict, (2) usar dict y setfedault (3) usar groupby

    '''
    #===========================================================================
    # preguntas_por_anyo = dict()
    # for p in preguntas:
    #     if p.anyo not in preguntas_por_anyo.keys():
    #         preguntas_por_anyo[p.anyo] = [p]
    #     else:
    #         preguntas_por_anyo[p.anyo].append(p)
    # return preguntas_por_anyo
    #===========================================================================
    
    #===========================================================================
    # preguntas_ordenadas = sorted(preguntas, key=lambda x: x.anyo)
    # grupos = groupby(preguntas_ordenadas, key=lambda x:x.anyo)
    # #===========================================================================
    # # for g in grupos:
    # #     print(g)
    # #===========================================================================
    # preguntas_por_anyo = {k: [v_i for v_i in v] for k, v in grupos}
    # return dict(preguntas_por_anyo)
    #===========================================================================
    
    #===========================================================================
    # preguntas_por_anyo = defaultdict(list)
    # for p in preguntas:
    #     preguntas_por_anyo[p.anyo].append(p)
    # return preguntas_por_anyo
    #===========================================================================
    
    preguntas_por_anyo = dict()
    for p in preguntas:
        preguntas_por_anyo.setdefault(p.anyo, []).append(p)
    return preguntas_por_anyo


def mostrar_distribucion_etiquetas(preguntas, etiquetas):
    ''' Muestra un diagrama de tarta con la distribución de uso de varias etiquetas
    
    ENTRADA: 
       @param preguntas: lista de preguntas (puntuacion, titulo, anyo, etiqueta)
       @type preguntas: [Pregunta(int, str, int, str)]
       @param etiquetas: lista de etiquetas que se inlcuirán en la gráfica
       @type etiquetas: [str]
    SALIDA EN PANTALLA: 
       - gráfica con un diagrama de tarta con un sector por cada etiqueta recibida
    
    Se usarán las siguientes instrucciones para generar la gráfica:
        plt.pie(tamanyos, labels=etiquetas, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.legend()
        plt.show()

    Donde 'tamanyos' es una lista, alineada con la lista de etiquetas, con el número de preguntas para
    cada etiqueta.  
    '''
    pass


def mostrar_evolucion_etiquetas(preguntas, etiquetas):
    ''' Muestra la evolución del uso de etiquetas a lo largo del tiempo
    
    ENTRADA: 
       @param preguntas: lista de preguntas (puntuacion, titulo, anyo, etiqueta)
       @type preguntas: [Pregunta(int, str, int, str)]
       @param etiquetas: lista de etiquetas que se inlcuirán en la gráfica
       @type etiquetas: [str]
    SALIDA EN PANTALLA: 
       - gráfica con una línea para cada etiqueta con su evolución temporal
    
    Se usarán las siguientes instrucciones para generar la gráfica:
        for etiqueta, evolucion in zip(etiquetas, evoluciones):
            plt.plot(evolucion, label=etiqueta)
        plt.xticks(range(len(anyos)), anyos, rotation=80, fontsize=10)
        plt.legend()
        plt.show()

    Donde 'anyos' y 'evoluciones' son dos listas con la siguiente información:
       - anyos: lista de los anyos incluidos en la colección de preguntas, ordenados de menor a mayor
       - evoluciones: lista con la evolución de uso de cada etiqueta, alineada con la lista de etiquetas. 
                      Cada evolución consiste en una lista de frecuencias, alineada con la lista de anyos, 
                      correspondientes con el número de veces que la etiqueta ha sido usada cada anyo.   
    '''
    pass
    
