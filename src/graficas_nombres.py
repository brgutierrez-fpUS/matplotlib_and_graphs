# -*- coding: utf-8 -*-
'''
Created on 6 dic. 2021

@author: Belen Ramos
'''
import csv
from collections import namedtuple, defaultdict
from matplotlib import pyplot as plt

# EJERCICIO 1:
Registro = namedtuple('Registro', 'anyo, nombre, frecuencia, genero')


def leer_frecuencias_nombres(fichero):
    ''' Lee el fichero de registros y devuelve una lista de tuplas con nombre

    ENTRADA: 
       @param fichero: ruta del fichero csv que contiene los datos en codificación utf-8
       @type fichero: str
    SALIDA: 
       @return lista de registros 
       @rtype [Registro(int, str, int, str)]
    '''
    with open(fichero, 'r', encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        registros = [Registro(int(anyo), nombre, int(frecuencia), genero) for anyo, nombre, frecuencia, genero in lector]
    return registros


def calcular_frecuencia_por_anyo(registros, nombre):
    ''' Calcula una lista de tuplas (anyo, frecuencia) con las frecuencias de un nonmbre cada anyo

    ENTRADA: 
        @param registros: lista de registros 
        @type registros: [Registro(int, str, int, str)]
        @param nombre: nombre del que se hace la consulta 
        @type nombre: str
    SALIDA: 
       @return lista de tuplas (anyo, frecuencia) ordenanda por anyo  
       @rtype [(int, int)]

    En el caso de que un nombre se use para hombres y mujeres, se sumarán ambas frecuencias
    '''
    anyos = sorted(set(r.anyo for r in registros))
    frecuencia_por_anyo = []
    for anyo in anyos:
        frecuencia = sum(r.frecuencia for r in registros if r.anyo == anyo and r.nombre == nombre)
        frecuencia_por_anyo.append((anyo, frecuencia))
        
    return frecuencia_por_anyo


def mostrar_evolucion_por_anyo(registros, nombre):
    ''' Genera un gr�fico con la evolución de la frecuencia de un nombre

    ENTRADA: 
       @param registros: lista de registros 
        @type registros: [Registro(int, str, int, str)]
        @param nombre: nombre del que se hace la consulta 
        @type nombre: str
    SALIDA EN PANTALLA: 
       - curva con la evoluci�n de la frecuencia del nombre

    Se usar�n las siguientes instrucciones para generar la gráfica:
        plt.plot(anyos, frecuencias)
        plt.title("Evolución del nombre '{}'".format(nombre)
        plt.show()
    Donde 'anyos' y 'frecuencias' se extraen del resultado de la función
    'calcular_frecuencia_por_anyo'
    '''
    pass


def filtrar_por_genero(registros, genero):
    ''' Recibe una lista de tuplas y devuelve solo los registros del género recibido como parámetro

    ENTRADA: 
       @param registros: lista de registros 
       @type registros: [Registro(int, str, int, str)]
       @param genero: género del que se seleccionarán los registros 
       @type genero: str
    SALIDA: 
       @return lista de registros seleccionados 
       @rtype [Registro(int, str, int, str)]
    '''
    return [r for r in registros if r.genero == genero]


def calcular_nombres(registros, filtro=None):
    ''' Calcula el conjunto de nombres aplicando el filtro de género recibido como parámetro 

    ENTRADA: 
       @param registros: lista de registros 
       @type registros: [Registro(int, str, int, str)]
       @param filtro: 'Hombre', 'Mujer', o None si no se aplica filtro
       @type filtro: str
    SALIDA: 
       @return conjunto de nombres encontrados 
       @rtype {str}
    '''
    if filtro is not None:
        registros = filtrar_por_genero(registros, filtro)
    return set(r.nombre for r in registros)


def calcular_frecuencia_acumulada(registros, nombre):
    ''' Calcula la frecuencia acumulada de un nombre en todos los anyos

    ENTRADA: 
        @param registros: lista de registros 
        @type registros: [Registro(int, str, int, str)]
        @param nombre: nombre del que se hace la consulta 
        @type nombre: str
    SALIDA: 
       @return suma de las frecuencias del nombre en todos los anyos  
       @rtype int
    '''
    return sum(r.frecuencia for r in registros if r.nombre == nombre)


def calcular_frecuencias_por_nombre(registros):
    ''' Calcula un diccionario {nombre:frecuencia} con la frecuencia acumulada de cada nombre

    ENTRADA: 
        @param registros: lista de registros 
        @type registros: [Registro(int, str, int, str)]
    SALIDA: 
       @return diccionario con la frecuencia acumulada de cada nombre 
       @rtype {str:int}

    Hay dos posibles soluciones: (1) invocando a funciones que hemos implementado en los ejercicios anteriores y (2) haciendo uso de defaultdict, que en este caso es más eficiente

    '''
    frecuencias = defaultdict(int)
    nombres = calcular_nombres(registros)
    for nombre in nombres:
        frecuencias[nombre] = calcular_frecuencia_acumulada(registros, nombre)
    return frecuencias


def mostrar_frecuencias_nombres(registros, limite=10):
    ''' Genera un diagrama de barras con las frecuencias de los nombres más populares

    ENTRADA: 
        @param registros: lista de registros 
        @type registros: [Registro(int, str, int, str)]
        @param limite: número de nombres a mostrar 
        @type limite: int
    SALIDA EN PANTALLA: 
       - diagrama de barras con las frecuencias de los nombres más populares

    Se usarán las siguientes instrucciones para generar la gráfica:
        plt.bar(nombres, frecuencias)
        plt.xticks(rotation=80)
        plt.title("Frecuencia de los {} nombres más comunes".format(limite))
        plt.show()

    Donde 'nombres' y 'frecuencias' se extraen del resultado de la función
    'calcular_frecuencias_por_nombre'. El cálculo de los nombres más populares se puede
        realizar ordenando las claves del diccionario devuelto por 'calcular_frecuencias_por_nombre'
        en función de sus valores asociados.
    '''
    pass
