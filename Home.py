#---------------------------------------------------------------#
# BIBLIOTECAS
#---------------------------------------------------------------#

import streamlit as st
from PIL import Image

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
    st.markdown("## Bem vindo ao Survey Info 🎯") 
    st.write("")
    
with st.container():
        st.markdown("#### Aqui você conta com ferramentas para facilitar o dia a dia nas operações de Survey.")
        st.write("Caso tenha alguma sugestão, favor entrar em contato pelo email 'pedrogpb.ufes@gmail.com'.")