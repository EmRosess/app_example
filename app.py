import streamlit as st
from backend import calcular_potencia

st.title("Potencia electrica")

volt = st.number_input("Voltaje", min_value=0.0, value=200.0)
corriente = st.number_input("Corriente", min_value=0.0, value=1.0)

if st.button("Calcular"):
    potencia = calcular_potencia(volt, corriente)
    st.success(f"La potencia es: {potencia} W")