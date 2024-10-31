#---------------------------------------------------------------#
# BIBLIOTECAS
#---------------------------------------------------------------#

from pyproj import Transformer, CRS
import numpy as np
import math
import folium
from PIL import Image
import streamlit as st
from streamlit_folium import folium_static

#---------------------------------------------------------------#
# FUNÇÕES
#---------------------------------------------------------------#

# Função para transformar coordenadas GRAU, MINUTO, SEGUNDO para GRAUS DECIMAIS:
def gms_to_gd(grau, minuto, segundo, direcao):
    dd = grau + (minuto/60) + (segundo/3600)
    if direcao in ["S", "W"]:
        dd = -dd
    return dd

# Função para transformar coordenadas GRAU, MINUTO para GRAUS DECIMAIS:
def gm_to_gd(grau, minuto, direcao):
    dd = grau + (minuto/60)
    if direcao in ["S", "W"]:
        dd = -dd
    return dd

# Função que converte coordenadas em direferentes DATUM
def conversor_geo(epsg_entrada, epsg_saida, latitude, longitude):
    proj_entrada = CRS.from_epsg(epsg_entrada)
    proj_saida = CRS.from_epsg(epsg_saida)
    conversor = Transformer.from_crs(proj_entrada, proj_saida)
    lat_final, long_final = conversor.transform(latitude, longitude)
    return lat_final, long_final

# Função que calcula a distância entre dois pontos utilizando método de haversine
def haversine(coord1, coord2):
    # Raio da Terra em km
    R = 6371.0
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

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
    st.markdown("## Conversor de Coordenadas e Zonas UTM 🌎") 
    st.write("")
    
# Divisão de abas da página:
tab1, tab2, tab3 = st.tabs(["# Cartesiano para Grau Decimal", "# Cartesiano para UTM", "Mapa para Locação de Pontos"])


#--------------------------------------------------------------#
# CÓDIGO - ABA 1 - Conversão para Grau Decimal
#--------------------------------------------------------------#

with tab1:
    
# Input de dados

    with st.container():
        st.markdown("### Conversão de Coordenada Cartesiana em Grau Decimal:")
        st.write("Nesta aba, realiza-se conversões de coordenadas cartesianas em formato grau minuto e grau minuto segundo para grau decimal.")
        st.write("")
        st.markdown("##### Instruções:")
        st.text('I. No campo "Direção (N/S/E/W)" deve-se utilizar letras MAIUSCULAS;')
        st.text('II. Após preencher todos os campos, deve-se pressionar a tecla ENTER;')
        st.markdown("""---""")
        
    with st.container():
        st.markdown("#### Grau Minuto para Grau Decimal:")
        col1, col2, col3 = st.columns(3)

        with col1:
            grau_gm_lat = st.number_input("Grau (°): ")

        with col2:
            minuto_gm_lat = st.number_input("Minuto ('): ", format="%0.4f")

        with col3:
            direcao_gm_lat = st.text_input("Direção (N/S): ")
            
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            grau_gm_long = st.number_input("Grau (°):  ")

        with col2:
            minuto_gm_long = st.number_input("Minuto ('):  ", format="%0.4f")

        with col3:
            direcao_gm_long = st.text_input("Direção (E/W): ")
        st.markdown("")


    with st.container():
        st.markdown("#### Grau Minuto Segundo para Grau Decimal:")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            grau_gms_lat = st.number_input("Grau (°):   ")

        with col2:
            minuto_gms_lat = st.number_input("Minuto ('):   ", format="%0.4f")

        with col3:
            segundo_gms_lat = st.number_input("Segundo (''):   ", format="%0.4f")

        with col4:
            direcao_gms_lat = st.text_input("Direçao (N/S): ")
            
    with st.container():
        #st.markdown("#### Grau Minuto Segundo para Grau Decimal:")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            grau_gms_long = st.number_input("Grau (°):      ")

        with col2:
            minuto_gms_long = st.number_input("Minuto ('):      ", format="%0.4f")

        with col3:
            segundo_gms_long = st.number_input("Segundo (''):     ", format="%0.4f")

        with col4:
            direcao_gms_long = st.text_input("Direção (E/W):    ")
            

    with st.container():
        if grau_gm_lat and minuto_gm_lat and direcao_gm_lat and grau_gm_long and minuto_gm_long and direcao_gm_long:
            result_gm_to_gd_lat = gm_to_gd(grau_gm_lat, minuto_gm_lat, direcao_gm_lat)
            result_gm_to_gd_long = gm_to_gd(grau_gm_long, minuto_gm_long, direcao_gm_long)
            resultado = f"Grau Minuto para Grau Decimal - Latitude: {result_gm_to_gd_lat}, Longitude: {result_gm_to_gd_long}"
        
        elif grau_gms_lat and minuto_gms_lat and segundo_gms_lat and direcao_gms_lat and grau_gms_long and minuto_gms_long and segundo_gms_long and direcao_gms_long:
            result_gms_to_gd_lat = gms_to_gd(grau_gms_lat, minuto_gms_lat, segundo_gms_lat, direcao_gms_lat)
            result_gms_to_gd_long = gms_to_gd(grau_gms_long, minuto_gms_long, segundo_gms_long, direcao_gms_long)
            resultado = f"Grau Minuto Segundo para Grau Decimal - Latitude: {result_gms_to_gd_lat}, Longitude: {result_gms_to_gd_long}"
            
        else:
            resultado = "Nenhuma coordenada válida inserida."
            
        
        st.markdown("")
        st.markdown("")
        st.markdown("### Resultado da conversão:")
        st.text(resultado)
            
#--------------------------------------------------------------#
# CÓDIGO - ABA 2 - Conversão de DATUM
#--------------------------------------------------------------#
            
with tab2:
     
    with st.container():
        st.markdown("### Conversão de Cartesiano WGS84 para UTM SIRGAS2000:")
        st.write("Nesta aba, realiza-se conversão de DATUM transformando coordenadas cartesianas WGS84 para coordenadas UTM em SIRGAS2000 zona 23S e zona 24S.")
        st.write("")
        st.markdown("##### Instruções:")
        st.text('I. As coordenadas de entrada devem estar em formato cartesiano (GRAU DECIMAL);')
        st.text('II. Para indicar região S e W deve-se utilizar sinal NEGATIVO;')
        st.text('III. Após preencher todos os campos, deve-se pressionar a tecla ENTER;')
        st.markdown("""---""")
        
    with st.container():
        st.markdown("#### Cartesiano WGS84 para UTM SIRGAS2000 Zona 23S:")
        col1, col2 = st.columns(2)

        with col1:
            lat_entrada_23s = st.number_input("Latitude: ", format="%0.6f")
            
        with col2:
            long_entrada_23s = st.number_input("Longitude: ", format="%0.6f")
            
    with st.container():
        st.markdown("")
        st.markdown("#### Cartesiano WGS84 para UTM SIRGAS2000 Zona 24S:")
        col1, col2 = st.columns(2)

        with col1:
            lat_entrada_24s = st.number_input("Latitude ", format="%0.6f")

            
        with col2:
            long_entrada_24s = st.number_input("Longitude ", format="%0.6f")
            
    with st.container():
        if lat_entrada_23s and long_entrada_23s:
            lat_wgs_to_23s, long_wgs_to_23s = conversor_geo(4326, 31983, lat_entrada_23s, long_entrada_23s)
            lat_wgs_to_23s = np.round(lat_wgs_to_23s, 3)
            long_wgs_to_23s = np.round(long_wgs_to_23s, 3)
            resultado = f"Zona 23S - E: {lat_wgs_to_23s}, N: {long_wgs_to_23s}"
        
        elif lat_entrada_24s and long_entrada_24s:
            lat_wgs_to_24s, long_wgs_to_24s = conversor_geo(4326, 31984, lat_entrada_24s, long_entrada_24s)
            lat_wgs_to_24s = np.round(lat_wgs_to_24s, 3)
            long_wgs_to_24s = np.round(long_wgs_to_24s, 3)
            resultado = f"Zona 24S - E: {lat_wgs_to_24s}, N: {long_wgs_to_24s}"
        
        else:
            resultado = "Nenhuma coordenada válida inserida."
        
        st.markdown("")
        st.markdown("")
        st.markdown("### Resultado da conversão:")
        st.text(resultado)
            #st.text(f"N: {long_wgs_to_23s}")
            
        #with col2:
            #st.markdown("##### WGS84 para Zona 24S:")
            #st.text(f"E: {lat_wgs_to_24s}")
            #st.text(f"N: {long_wgs_to_24s}")
            
            
#--------------------------------------------------------------#
# CÓDIGO - ABA 3 - Mapa para locação de pontos
#--------------------------------------------------------------#

# Cabeçalho e informações da página

with tab3:
    with st.container():
        st.markdown("### Mapa para Locação de Pontos:")
        st.write("Nesta aba, temos o mapa mundi para plotar pontos e verificar distâncias horizontais.")
        st.write("")
        st.markdown("##### Instruções:")
        st.text('I. As coordenadas de entrada devem estar em formato cartesiano (GRAU DECIMAL);')
        st.text('II. Para indicar região S e W deve-se utilizar sinal NEGATIVO;')
        st.text('III. Após preencher todos os campos, deve-se pressionar a tecla ENTER;')
        st.markdown("""---""")

# Input coordenadas
    with st.container():
        st.markdown("#### Coordenadas P1:")
        col1, col2 = st.columns(2)

    with col1:
        lat_entrada_p1 = st.number_input("Latitude:  ", format="%0.6f")

    with col2:
        long_entrada_p1 = st.number_input("Longitude:  ", format="%0.6f")
        
    with st.container():
        st.write("")
        st.markdown("#### Coordenadas P2:")
        col1, col2 = st.columns(2)

    with col1:
        lat_entrada_p2 = st.number_input("Latitude:   ", format="%0.6f")

    with col2:
        long_entrada_p2 = st.number_input("Longitude:   ", format="%0.6f")
        
# Calculo entre distâncias (Método de HAVERSINE)
    with st.container():
        coord1 = (lat_entrada_p1, long_entrada_p1)
        coord2 = (lat_entrada_p2, long_entrada_p2)
        dist = haversine(coord1, coord2)
        dist = dist * 1000
        dist = np.round(dist, 2)
        
        st.markdown("""---""")
        st.markdown("#### Distância entre Pontos:")
        st.metric("", f"{dist} m")
        
# Criação do mapa
    with st.container():
        st.markdown("""---""")
        st.markdown("### Mapa:")
        mapa = folium.Map(location=[-17.5, -50.5], zoom_start=4, tiles="CartoDB positron")
        
        pontos = [
        {'local': 'P1', 'lat': lat_entrada_p1, 'lon': long_entrada_p1, 'cor': 'blue'},
        {'local': 'P2', 'lat': lat_entrada_p2, 'lon': long_entrada_p2, 'cor': 'red'}]

    # Adiciona marcadores no mapa para cada local
        for lugar in pontos:
            folium.Marker(
                location=[lugar['lat'], lugar['lon']],
                popup=[lugar['local'], lugar['lat'], lugar['lon']],
                icon=folium.Icon(color=lugar['cor']),
            ).add_to(mapa)

        folium_static(mapa, width = 700, height = 450)