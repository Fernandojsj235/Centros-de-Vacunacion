#$ pip install streamlit --upgrade

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import urllib.request
import base64

st.title('Centros de vacunación')

st.markdown("""Esta tabla contiene la lista de los centros de vacunación programadas según 
entidad y ubicación geográfica a nivel nacional del territorio peruano.""")

from PIL import Image
image = Image.open('iamgenCV.jpg')
st.image(image, caption='Centro de vacunación en Lima', use_column_width=True)
        
st.header("Dataset MINSA")
@st.experimental_memo
def download_data():
   url=http://server01.labs.org.pe:2005/TB_CENTRO_VACUNACION.csv
   filename="TB_CENTRO_VACUNACION.csv"
   urllib.request.urlretrieve(url,filename)
   df=pd.read_csv('TB_CENTRO_VACUNACION.csv')
   return df
        
    
                
