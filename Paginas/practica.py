import streamlit as st

st.html("<center><h1> Evaluación de conocimientos </h1>")
st.markdown("**Instrucciones**: Selecciona la opción que consideres correcta para cada pregunta. Solo hay una respuesta correcta por pregunta.")

rta = st.selectbox("**1. ¿Cuál es el propósito principal del método de multiplicadores de Lagrange?**", options=["a) Resolver sistemas de ecuaciones diferenciales. ", "b) Encontrar los máximos y mínimos de una función con restricciones.", "c) Determinar el área bajo la curva.", "d) Resolver ecuaciones polinomiales de segundo grado."])

if rta[0] == "b":"La respuesta es correcta."
if rta[0] == "a":"La respuesta es incorrecta."
if rta[0] == "c":"La respuesta es incorrecta."
if rta[0] == "d":"La respuesta es incorrecta."

rta = st.selectbox("**2. ¿De donde fue heredado el nombre *Lagrange*?**", options=["a) De Pitagoras. ", "b) De Gauss.", "c) De Isaac.", "d) De Joseph-Louis."])

if rta[0] == "d":"La respuesta es correcta."
if rta[0] == "a":"La respuesta es incorrecta."
if rta[0] == "c":"La respuesta es incorrecta."
if rta[0] == "b":"La respuesta es incorrecta."

rta = st.selectbox("**3. ¿Qué es un gradiente?**", options=["a) Una integral indefinida. ", "b) Es un escalar que aparece en la ecuación que relaciona los gradienres de la funcion objetivo.", "c) Es un vector que apunta en la direccion de mayor tasa de cambio de una función."]) 

if rta[0] == "c":"La respuesta es correcta."
if rta[0] == "a":"La respuesta es incorrecta."
if rta[0] == "b":"La respuesta es incorrecta."

rta = st.selectbox("**4. ¿Cuál es el tercer paso para hallar los multiplicadores de Lagrange?**", options=["a)  Identifica las funciones involucradas.. ", "b)Forma la función Lagrangiana.", "c) Resolver el sistema de ecuaciones. ", "d) Calcula las derivadas parciales."]) 

if rta[0] == "d":"La respuesta es correcta."
if rta[0] == "a":"La respuesta es incorrecta."
if rta[0] == "c":"La respuesta es incorrecta."
if rta[0] == "b":"La respuesta es incorrecta."

rta = st.selectbox("**5. ¿De donde es la creadora de esta página?**", options=["a) Girón, Santander. ", "b)Cerrito, Santander", "c) San Andres, Santander. ", "d) Cucúta, Norte de Santander"]) 

if rta[0] == "b":"La respuesta es correcta."
if rta[0] == "a":"La respuesta es incorrecta."
if rta[0] == "c":"La respuesta es incorrecta."
if rta[0] == "d":"La respuesta es incorrecta."

st.text_input("**5. Explique con sus palabras en qué consiste el método de multiplicadores de Lagrange y respode: ¿para qué se utilizan?**") 

st.image("imagenes/motivacion.jpg")