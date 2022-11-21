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
!wget http://server01.labs.org.pe:2005/TB_CENTRO_VACUNACION.csv
pd.read_csv("TB_CENTRO_VACUNACION.csv")

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)
