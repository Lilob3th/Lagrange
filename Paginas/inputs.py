import streamlit as st

st.title("paginas de inicio")

#pedir textos
nombre= st.text_input("Digite nombre:")
st.markdown(f"El nombre que ingeso es: {nombre}")


#para pedir numeros:
edad=st.number_input("Edad:", min_value=0, max_value=120, value=18)
st.markdown(f"La edadf ingresada es: {edad}")
st.markdown(f"Su edad en 10 años sera: {edad+10}")
if edad >18: 
    st.markdown("Es mayor de edad")
else:
    st.markdown("Es menor de edad")

rango= st.slider("Digite un valor:", min_value=1, max_value=10)
st.markdown(f"Valor seleccionado: {rango}")

ini, final= st.slider("Seleccione rangos", min_value=0, max_value=10, value=(2,4))
st.markdown(f"Valor de inicio: {ini}")
st.markdown(f"Valor final: {final}")

#seleccion
x=st.number_input("x:")
y=st.number_input("y:")
