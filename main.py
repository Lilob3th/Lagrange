import streamlit as st

#1) crear las páginas
txts=st.Page("Paginas/textos.py", title="Textos")
inps=st.Page ("Paginas/inputs.py", title="Widges")
ejs= st.Page("Paginas/ejemplos.py", title="Ejemplos")

pg=st.navigation([txts, inps, ejs])
#pg=st.navegation()

pg.run()


