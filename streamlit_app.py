import streamlit as st

st.title("📋 Registro de Candidatos - BOCAPARDO AI")

# Inicializar la lista y control de formulario
if "candidatos" not in st.session_state:
    st.session_state.candidatos = []
if "mostrar_formulario" not in st.session_state:
    st.session_state.mostrar_formulario = True

# Mostrar formulario
if st.session_state.mostrar_formulario:
    with st.form("form_candidato"):
        nombre = st.text_input("Nombre")
        edad = st.number_input("Edad", min_value=0, step=1)
        tecnologia = st.text_input("Tecnología favorita")

        submit = st.form_submit_button("Registrar")

        if submit:
            if edad >= 18:
                nuevo = {"nombre": nombre, "edad": edad, "tecnologia": tecnologia}
                st.session_state.candidatos.append(nuevo)
                st.success(f"{nombre} ha sido registrado.")
                st.session_state.mostrar_formulario = False
            else:
                st.warning("Debes tener al menos 18 años para aplicar.")

# Botón para nuevo registro
if not st.session_state.mostrar_formulario:
    if st.button("➕ Ingresar otro candidato"):
        st.session_state.mostrar_formulario = True

# Botón para limpiar la lista
if st.button("🧹 Limpiar candidatos"):
    st.session_state.candidatos = []
    st.success("Lista de candidatos limpiada.")

# Mostrar la tabla
if st.session_state.candidatos:
    st.subheader("🧑‍💻 Candidatos registrados:")
    st.table(st.session_state.candidatos)
