import streamlit as st

#1) crear las páginas
txts= st.Page("Paginas/intro.py", title="Concepto")
inps= st.Page ("Paginas/lagrange.py", title="Joseph-Louis Lagrange")
ejs= st.Page("Paginas/explorar.py", title="Exploremos")
graphs= st.Page("Paginas/conceptos.py", title="Conceptos Importantes")
ejemp=st.Page("Paginas/ejemplo.py", title="Ejemplo")
paso=st.Page("Paginas/pasos.py", title="Paso a Paso")
pers=st.Page("Paginas/personal.py", title="Autora")
prac=st.Page("Paginas/practica.py", title="Práctica")
#pg=st.navigation([txts,inps,ejs])
pg=st.navigation({"Tamatica":[txts, inps, graphs,], "Aplicación": [ paso, ejemp, ejs], "Evaluemos":[prac], "Autora":[pers]})
#pg=st.navegation()

pg.run()


