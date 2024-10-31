#---------------------------------------------------------------#
# BIBLIOTECAS
#---------------------------------------------------------------#

import streamlit as st
import math
import numpy as np
from PIL import Image
import os

#--------------------------------------------------------------#
# DIRETORIO
#--------------------------------------------------------------#

#os.chdir("C:/Users/Pedro Garcia/Desktop/Docs/scripts/Python/Survey")


#--------------------------------------------------------------#
# SIDEBAR STREAMLIT
#--------------------------------------------------------------#

st.set_page_config(page_title = "Survey Info", page_icon =  "🎯", layout = "centered")

# Sidebar
imagem = Image.open("lh2_foto.jpg")
st.sidebar.image(imagem, width=250)
st.sidebar.markdown("# Survey Info 🎯")
st.sidebar.markdown("### ")
st.sidebar.markdown("""---""")

# Sidebar (with CSS)
st.sidebar.markdown("""
<style>
    .sidebar-text {
        text-align: center;
        font-size: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown('<p class="sidebar-text">Powered by Pedro Garcia.</p>', unsafe_allow_html=True)


#--------------------------------------------------------------#
# CÓDIGO
#--------------------------------------------------------------#

# Cabeçalho

with st.container():
    st.markdown("## Área de cobertura e espaçamento entre linhas no Levamento Hidrográfico📱")
    st.markdown("""---""")
    
# Input de dados

with st.container():
    st.markdown("### Informe os seguintes parâmetros:")
    st.markdown("")

with st.container():
    col1, col2, col3 = st.columns(3)
    
    with col1:
        angulo = st.number_input("Ângulo de abertura do feixe (°): ")
    
    with col2:
        prof_min = st.number_input("Profundidade mínima (m): ")
        
    with col3:
        overlap = st.number_input("Sobreposição do LH (%): ")
        
        
# Calculo de cobertura

scan_area = (math.tan((angulo/2)*math.pi/180)*prof_min) * 2
scan_area = np.round(scan_area, 2)

# Calculo de distancia entre linhas do LH

dist_line = (math.tan((angulo/2)*math.pi/180)*prof_min) + (math.tan((angulo/2)*math.pi/180)*prof_min) * (1 - (overlap / 100))
dist_line = np.round(dist_line, 2)

# Cartões com respostas

with st.container():
    
    st.markdown("""---""")
    
    col1, col2 = st.columns(2)
    
    with col1:
        scan_area = f"{scan_area} m"
        st.markdown("### Área de varredura:")
        st.metric("", scan_area)
    
    with col2:
        dist_line = f"{dist_line} m"
        st.markdown("### Distância entre as linhas:")
        st.metric("", dist_line)

