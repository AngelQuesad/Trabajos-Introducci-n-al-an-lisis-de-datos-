# -*- coding: utf-8 -*-
"""Laboratorio1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KDpKFbV5hkKg7nblQ1d6d3-PLlRXZg4u
"""

#Laboratorio 1
#Introducción al Análisis de Datos
#07/08/2023

#Derek Espinach
#Adrian Morales
#Montserrat Castillo
#Ángel Quesada

from statistics import mode
import math
import numpy as np
print("Promedio de los elementos del vector")
suma= 0
media= 0
Visitas=[]
N= int (input("Ingrese la cantidad de personas preguntadas: "))
for i in range(N):
  cantidad=int(input("Cantidad de visitas: "))
  Visitas.append(cantidad)
  suma=suma+Visitas[i]
  moda = mode(Visitas)
media=suma/N
print(media)

def ord_burbuja(Visitas):
    n = len(Visitas)

    for i in range(n-1):
        for j in range(n-1-i):
            if Visitas[j] > Visitas[j+1]:
                Visitas[j], Visitas[j+1] = Visitas[j+1], Visitas[j]

print("Ordenamiento ascendente...")
mitad=N/2
mitadF=int(mitad)
mediana=Visitas[mitadF]
print("Mediana: ",mediana)

print("Moda: ",moda)

def desviacion():
  sumatoria=0
  for i in range(N):
    sumatoria =(Visitas[i]+sumatoria-media)**2

  fraccion=sumatoria/N
  raiz_cuadrada=math.sqrt(fraccion)
  print("La desviacion estandar es: ",raiz_cuadrada)
  Varianza=raiz_cuadrada**2
  print("Varianza: ",Varianza)

print(desviacion())

