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
   url= "https://raw.githubusercontent.com/Fernandojsj235/Centros-de-Vacunacion/main/TB_CENTRO_VACUNACION%20(5).csv"
   filename="TB_CENTRO_VACUNACION%20(5).csv"
   urllib.request.urlretrieve(url,filename)
   df=pd.read_csv('TB_CENTRO_VACUNACION%20(5).csv')
   return df

download_data()
st.dataframe(download_data())

#st.map(data=None, zoom=None, use_container_width=True)
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)

        
    
                
