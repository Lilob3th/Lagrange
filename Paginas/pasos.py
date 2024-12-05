import streamlit as st

st.html("<center><h1> Es importante seguir los siguientes pasos: </h1>")

with st.container(border=True):    
    st.subheader("1. Identifica las funciones involucradas:")
    st.markdown("""1. **Define la función objetivo** $f(x,y,z,...)$, que es la que deseas maximizar o minimizar.

2. Define la **restriccion** en forma de ecuacion $g(x,y,z,...)=0$""")

with st.container(border=True):    
    st.subheader("2. Forma la función Lagrangiana:")  
    st.markdown("""Contruye la función Lagrangiana. que incorpora tanto la funcion objetivo como las restricciones multilcadas por su respectivo multiplicador de lagrange \u03BB. """)

with st.container(border=True):    
    st.subheader("3. Calcula las derivadas parciales:")  
    st.markdown("""Encuentra lsa derivadas parciales con respecto a cada variable de la función $x,y,z,...$ y al multiplicador \u03BB.""")

with st.container(border=True):    
    st.subheader("4. Resolver el sistema de ecuaciones")  
    st.markdown("""Resuelve el sistema de ecuaciones simultáneas obtenido en el paso anterior. Este sistema incluye las ecuaciones derivadas con respecto a las variables y las ecuaciones de las restricciones. 
    Obtendrás los valores de las variables $x,y,x,...$ y el multiplicador \u03BB.""")

with st.container(border=True):    
    st.subheader("4. Analiza los resultados: ")  
    st.markdown("""1. Evalúa los puntos obtenidos en la función objetivo $f(x,y,z,...)$ para determinar si son máximos o minimos.
2. Si es necesario, compar los resultados obtenidos para identificar cuál cumple con los objetivos del profema. """)