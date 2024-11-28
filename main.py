import streamlit as st

#1) crear las páginas
txts= st.Page("Paginas/intro.py", title="Concepto")
inps= st.Page ("Paginas/lagrange.py", title="Joseph-Louis Lagrange")
ejs= st.Page("Paginas/explorar.py", title="Exploremos")
graphs= st.Page("Paginas/conceptos.py", title="Conceptos Importantes")

#pg=st.navigation([txts,inps,ejs])
pg=st.navigation({"Tamatica":[txts, inps, graphs], "Aplicación": [ejs]})
#pg=st.navegation()

pg.run()


