# -*- coding: utf-8 -*-
'''
Created on 6 dic. 2021

@author: Belen Ramos
'''

from graficas_poblacion import lee_poblaciones, muestra_evolucion_poblacion, muestra_comparativa_paises_anyo
from graficas_nombres import leer_frecuencias_nombres, mostrar_evolucion_por_anyo, mostrar_frecuencias_nombres
from graficas_stackoverflow import leer_preguntas, mostrar_distribucion_etiquetas, mostrar_evolucion_etiquetas


def mostrar_numerado(coleccion):
    i = 0
    for p in coleccion:
        i = i + 1
        print(i, p)


#===============================================================================
# POBLACIONES
#===============================================================================
def test_lee_poblaciones(poblaciones):
    print("Leídos ", len(poblaciones), "datos de población mundial")
    mostrar_numerado(poblaciones[:10])

    
def test_muestra_evolucion_poblacion(poblaciones):
    muestra_evolucion_poblacion(poblaciones, "Spain")


def test_muestra_comparativa_paises_anyo(poblaciones):
    muestra_comparativa_paises_anyo(poblaciones, 2016, ["Spain", "Portugal", "France", "Mexico", "China"])


#===============================================================================
# NOMBRES
#===============================================================================
def test_lee_nombres(nombres):
    print("\nLeídos ", len(nombres), "datos de población mundial")
    mostrar_numerado(nombres[:10])


def test_mostrar_evolucion_por_anyo(registros):
    print("TEST de 'mostrar_evolucion_por_anyo'")
    nombre = 'IKER'
    mostrar_evolucion_por_anyo(registros, nombre)
    print()


def test_mostrar_frecuencias_nombres(registros):
    print("TEST de 'mostrar_frecuencias_nombres'")
    mostrar_frecuencias_nombres(registros, 20)
    print()

#===============================================================================
# STACKOVERFLOW
#===============================================================================

def test_leer_preguntas(preguntas):
    print("\nTEST de 'leer_preguntas'")
    print(f'Se han leído {len(preguntas)} preguntas')
    mostrar_numerado(preguntas[:10])


def test_mostrar_distribucion_etiquetas(preguntas):
    print("\nTEST de 'mostrar_distribucion_etiquetas'\n")
    etiquetas = ['list', 'file', 'string']
    mostrar_distribucion_etiquetas(preguntas, etiquetas)

    
def test_mostrar_evolucion_etiquetas(preguntas):
    print("\nTEST de 'mostrar_evolucion_etiquetas'\n")
    etiquetas = ['list', 'file', 'string']
    mostrar_evolucion_etiquetas(preguntas, etiquetas)


if __name__ == '__main__':
    #===========================================================================
    # POBLACIONES
    #===========================================================================
    poblaciones = lee_poblaciones('../data/population.csv')
    test_lee_poblaciones(poblaciones)
    test_muestra_evolucion_poblacion(poblaciones)
    test_muestra_comparativa_paises_anyo(poblaciones)
    #===========================================================================
    # NOMBRES
    #===========================================================================
    nombres = leer_frecuencias_nombres('../data/frecuencias_nombres.csv')
    test_lee_nombres(nombres)
    test_mostrar_evolucion_por_anyo(nombres)
    test_mostrar_frecuencias_nombres(nombres)
    #===========================================================================
    # STACKOVERFLOW
    #===========================================================================
    preguntas = leer_preguntas('../data/stackoverflow_python_questions.csv')
    test_leer_preguntas(preguntas)
    test_mostrar_distribucion_etiquetas(preguntas)
    test_mostrar_evolucion_etiquetas(preguntas)
