# -*- coding: utf-8 -*-
"""Laboratorio#3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PKeAZkgWkYw2VARTGHkL8iRv_kG94aTx
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/content/CSVInvestigation.csv')
data= pd.DataFrame(df)
print(data)

#data=
dataFilteres2018= data.loc[(data['Year']==2018)]
print(dataFilteres2018)

# 5 países con mayor indice de criminalidad
dataFiltered= data.loc[(data['Series']=="Intentional homicide rates per 100,000")]
print(dataFiltered.sort_values(by=['Value'],ascending=False)[['Country','Value']].head(5))

# 5 países con menor indice de criminalidad
dataFiltered= data.loc[(data['Series']=="Intentional homicide rates per 100,000")]
print(dataFiltered.sort_values(by=['Value'],ascending=True)[['Country','Value']].head(5))

#El crimen más repetido por país en el año 2018
print(dataFilteres2018['Series'].value_counts())

#El crimen con el porcentaje más alto de CR en el año 2005
dataFilteredCR=data.loc[(data['Country']=="Costa Rica")&(data['Year']==2005)]
print(dataFilteredCR)
print(dataFilteredCR.sort_values(by=['Value'],ascending=False)[['Country','Series','Value']])

#Compativa entre CR,Nicaragua,Panamá por medio de la tasa
registro=df.loc[(df["Country"]=="Costa Rica")|(df["Country"]=="Panama")|(df["Country"]=="Nicaragua")]
print(registro)

registro=df["Year"]
annio=registro.mode()
print(annio)

from pandas.core.groupby import groupby
#Género más afecta en crimenes en promedio en el año 2018
print()
print()
print('H-Geneo mas afectado en crimenes en promedio en el año 2018')
dataFilteredByGender=dataFilteres2018.loc[((dataFilteres2018['Series']=="Percentage of male and female intentional homidice victims, Male")|
 (dataFilteres2018['Series']=="Percentage of male and female intentional homidice victims, Female"))].groupby('Series')['Value']
print(dataFilteredByGender.mean())