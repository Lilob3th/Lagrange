import streamlit as st

st.title("Lilibeth Andrea Correa Ramírez")
st.caption("Soy estudiante de Licenciatura en Matemáticas")
st.caption("Otro mensaje.")

st.title("Titulo de nivel 1")
st.header("Titulo de nivel 2")
st.subheader("Titulo de nivel ")

#textos
st.markdown("""
En una etiqueta tipo markdoen pueden poner cualquier texto en el formato markdown.
podemos poner un texto en **negrilla**, en *italica* o en ***ambas***

Esto es otra linea. 

enumeraciones
1. primer item
2. segundo item
3. tercer item

items:
+ Item 1
+ item 2
+ item 3

Podemos dar color al texto, por ejemplo :blue[Lilo]

""")

#ecuaciones 
st.latex("a2+b2=c2")

st.image("https://pymstatic.com/18793/conversions/frases-pitagoras-wide_webp.webp")
st.video("...")

