# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zZZoqXYfKLisTogYiLonGveek-YTGXZq
"""

importar  streamlit  como  st
importar  pandas  como  pd
importar  numpy  como  np
desde  fechahora hora  de importación 
importar  fecha y hora
import pandas as pd
!wget http://server01.labs.org.pe:2005/TB_CENTRO_VACUNACION.csv
pd.read_csv("TB_CENTRO_VACUNACION.csv")

st . title ( "Proyecto de Programación Avanzada 2022-2" )