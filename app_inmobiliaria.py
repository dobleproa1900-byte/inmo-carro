import streamlit as st
import pandas as pd

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="InmoIA — Demo Inmobiliaria — InmoIA",
    page_icon="🏠",
    layout="wide"
)

# ==========================================
# LOGIN
# ==========================================
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

DEMO_USER = "inmoia"
DEMO_PASS = "demo2026"

if not st.session_state.autenticado:
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:center'>🏠 InmoIA — Demo Inmobiliaria</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align:center;color:gray'>Sistema Inteligente de Gestión Inmobiliaria</h4>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        with st.form("login_form"):
            usuario = st.text_input("Usuario:", placeholder="inmoia")
            clave = st.text_input("Contraseña:", type="password", placeholder="••••••••")
            st.caption("ℹ️ Demo: usuario `inmoia` / contraseña `demo2026`")
            if st.form_submit_button("Ingresar", type="primary"):
                if usuario == DEMO_USER and clave == DEMO_PASS:
                    st.session_state.autenticado = True
                    st.rerun()
                else:
                    st.error("❌ Usuario o contraseña incorrectos.")
    st.stop()

# ==========================================
# DATOS DE DEMO
# ==========================================
PROPIEDADES = [
    {"ID": "P001", "Tipo": "Venta", "Categoria": "Casa", "Titulo": "Casa amplia en el Centro", "Barrio": "Centro", "Direccion": "Av. Mitre 450, San Pedro", "Precio": 85000, "Moneda": "USD", "Ambientes": 4, "Superficie": 180, "Descripcion": "Hermosa casa con jardín, garage y patio. Ideal para familia. Cocina renovada, 3 dormitorios, 2 baños.", "Disponible": True, "Foto": "https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=600"},
    {"ID": "P002", "Tipo": "Alquiler", "Categoria": "Departamento", "Titulo": "Depto 2 amb. luminoso", "Barrio": "Centro", "Direccion": "Belgrano 320, San Pedro", "Precio": 180000, "Moneda": "ARS", "Ambientes": 2, "Superficie": 55, "Descripcion": "Departamento luminoso en planta alta, balcón con vista a la calle, cocina integrada, baño completo.", "Disponible": True, "Foto": "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=600"},
    {"ID": "P003", "Tipo": "Venta", "Categoria": "Terreno", "Titulo": "Terreno en zona residencial", "Barrio": "Las Casuarinas", "Direccion": "Calle Los Pinos 120, San Pedro", "Precio": 25000, "Moneda": "USD", "Ambientes": 0, "Superficie": 600, "Descripcion": "Terreno plano de 600m2 en barrio residencial tranquilo. Apto para construcción de vivienda familiar.", "Disponible": True, "Foto": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=600"},
    {"ID": "P004", "Tipo": "Alquiler", "Categoria": "Casa", "Titulo": "Casa 3 dorm. con patio", "Barrio": "Santa Lucía", "Direccion": "San Martín 780, San Pedro", "Precio": 250000, "Moneda": "ARS", "Ambientes": 3, "Superficie": 120, "Descripcion": "Casa con 3 dormitorios, living comedor, cocina, baño, patio y lavadero. Barrio tranquilo cerca de escuelas.", "Disponible": True, "Foto": "https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=600"},
    {"ID": "P005", "Tipo": "Venta", "Categoria": "Casa", "Titulo": "Casa con vista al río", "Barrio": "Costanera", "Direccion": "Av. Costanera 1200, San Pedro", "Precio": 120000, "Moneda": "USD", "Ambientes": 5, "Superficie": 250, "Descripcion": "Imponente propiedad frente al río Paraná. Quincho, pileta, 4 dormitorios, cochera doble. Una joya.", "Disponible": True, "Foto": "https://images.unsplash.com/photo-1613977257363-707ba9348227?w=600"},
    {"ID": "P006", "Tipo": "Alquiler", "Categoria": "Local Comercial", "Titulo": "Local comercial en peatonal", "Barrio": "Centro", "Direccion": "Peatonal Rivadavia 55, San Pedro", "Precio": 320000, "Moneda": "ARS", "Ambientes": 1, "Superficie": 80, "Descripcion": "Local comercial en pleno centro de San Pedro. Vidriera amplia, depósito trasero, baño. Alta circulación peatonal.", "Disponible": True, "Foto": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=600"},
    {"ID": "P007", "Tipo": "Venta", "Categoria": "Departamento", "Titulo": "Depto 3 amb. en edificio nuevo", "Barrio": "Centro", "Direccion": "Urquiza 210 Piso 3, San Pedro", "Precio": 65000, "Moneda": "USD", "Ambientes": 3, "Superficie": 85, "Descripcion": "Departamento en edificio de 5 años. Cochera, sum, lavadero. Excelente estado, cocina equipada.", "Disponible": False, "Foto": "https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=600"},
    {"ID": "P008", "Tipo": "Alquiler", "Categoria": "Casa", "Titulo": "Casa pequeña ideal pareja", "Barrio": "Bajo Tala", "Direccion": "Los Aromos 340, San Pedro", "Precio": 150000, "Moneda": "ARS", "Ambientes": 2, "Superficie": 70, "Descripcion": "Casa cómoda de 2 ambientes con patio. Perfecta para pareja o persona sola. Barrio tranquilo.", "Disponible": True, "Foto": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600"},
]

df = pd.DataFrame(PROPIEDADES)

# ==========================================
# HEADER
# ==========================================
col_titulo, col_logout = st.columns([5, 1])
with col_titulo:
    st.title("🏠 InmoIA — Demo Inmobiliaria")
    st.markdown("### *Sistema Inteligente de Gestión Inmobiliaria — Powered by IA*")
with col_logout:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚪 Cerrar sesión"):
        st.session_state.autenticado = False
        st.rerun()

st.markdown("---")

# ==========================================
# PESTAÑAS
# ==========================================
tab1, tab2, tab3 = st.tabs(["🏘️ Propiedades", "🤖 Consultor IA", "📊 Panel de Gestión"])

# ==========================================
# PESTAÑA 1: LISTADO DE PROPIEDADES
# ==========================================
with tab1:
    st.subheader("Propiedades disponibles")

    # Filtros
    col_f1, col_f2, col_f3, col_f4 = st.columns(4)
    with col_f1:
        tipo_filtro = st.selectbox("Operación:", ["Todas", "Venta", "Alquiler"])
    with col_f2:
        cat_filtro = st.selectbox("Categoría:", ["Todas", "Casa", "Departamento", "Terreno", "Local Comercial"])
    with col_f3:
        barrio_filtro = st.selectbox("Barrio:", ["Todos"] + sorted(df["Barrio"].unique().tolist()))
    with col_f4:
        solo_disponibles = st.checkbox("Solo disponibles", value=True)

    # Aplicar filtros
    df_filtrado = df.copy()
    if tipo_filtro != "Todas":
        df_filtrado = df_filtrado[df_filtrado["Tipo"] == tipo_filtro]
    if cat_filtro != "Todas":
        df_filtrado = df_filtrado[df_filtrado["Categoria"] == cat_filtro]
    if barrio_filtro != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Barrio"] == barrio_filtro]
    if solo_disponibles:
        df_filtrado = df_filtrado[df_filtrado["Disponible"] == True]

    st.caption(f"Mostrando {len(df_filtrado)} propiedades")

    # Grilla de propiedades
    cols = st.columns(3)
    for i, (_, prop) in enumerate(df_filtrado.iterrows()):
        with cols[i % 3]:
            with st.container(border=True):
                st.image(prop["Foto"], use_column_width=True)
                badge = "🟢 Disponible" if prop["Disponible"] else "🔴 No disponible"
                st.caption(f"{badge} · {prop['Tipo']} · {prop['Categoria']}")
                st.markdown(f"**{prop['Titulo']}**")
                st.caption(f"📍 {prop['Direccion']}")
                if prop["Ambientes"] > 0:
                    st.caption(f"🛏 {prop['Ambientes']} ambientes · 📐 {prop['Superficie']}m²")
                else:
                    st.caption(f"📐 {prop['Superficie']}m²")
                precio_fmt = f"${prop['Precio']:,} {prop['Moneda']}"
                st.markdown(f"### {precio_fmt}")
                with st.expander("Ver descripción"):
                    st.write(prop["Descripcion"])
                st.link_button(
                    "💬 Consultar por WhatsApp",
                    f"https://wa.me/5493329599250?text=Hola%20Carro%20Propiedades,%20me%20interesa%20la%20propiedad%20{prop['ID']}%20--%20{prop['Titulo']}",
                    use_container_width=True
                )

# ==========================================
# PESTAÑA 2: CONSULTOR IA
# ==========================================
with tab2:
    st.subheader("🤖 Consultor Inteligente de Propiedades")
    st.caption("Preguntame lo que necesitás saber sobre nuestras propiedades.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Mostrar historial
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Input del usuario
    pregunta = st.chat_input("Ej: ¿Tienen casas en alquiler en el Centro?")

    if pregunta:
        st.session_state.chat_history.append({"role": "user", "content": pregunta})
        with st.chat_message("user"):
            st.write(pregunta)

        # Lógica de respuesta basada en las propiedades
        pregunta_lower = pregunta.lower()
        respuesta = ""

        # Filtrar propiedades relevantes según la pregunta
        props_relevantes = df[df["Disponible"] == True].copy()

        if "alquiler" in pregunta_lower or "alquilar" in pregunta_lower:
            props_relevantes = props_relevantes[props_relevantes["Tipo"] == "Alquiler"]
        elif "venta" in pregunta_lower or "comprar" in pregunta_lower or "vender" in pregunta_lower:
            props_relevantes = props_relevantes[props_relevantes["Tipo"] == "Venta"]

        if "casa" in pregunta_lower:
            props_relevantes = props_relevantes[props_relevantes["Categoria"] == "Casa"]
        elif "depto" in pregunta_lower or "departamento" in pregunta_lower:
            props_relevantes = props_relevantes[props_relevantes["Categoria"] == "Departamento"]
        elif "terreno" in pregunta_lower:
            props_relevantes = props_relevantes[props_relevantes["Categoria"] == "Terreno"]
        elif "local" in pregunta_lower or "comercial" in pregunta_lower:
            props_relevantes = props_relevantes[props_relevantes["Categoria"] == "Local Comercial"]

        for barrio in df["Barrio"].unique():
            if barrio.lower() in pregunta_lower:
                props_relevantes = props_relevantes[props_relevantes["Barrio"] == barrio]

        if "precio" in pregunta_lower or "cuánto" in pregunta_lower or "cuanto" in pregunta_lower or "valor" in pregunta_lower:
            if len(props_relevantes) > 0:
                respuesta = "💰 **Precios de nuestras propiedades disponibles:**\n\n"
                for _, p in props_relevantes.iterrows():
                    respuesta += f"- **{p['Titulo']}**: ${p['Precio']:,} {p['Moneda']}\n"
            else:
                respuesta = "No encontré propiedades disponibles con esos criterios. ¿Querés que te contacte con el equipo?"

        elif "contacto" in pregunta_lower or "teléfono" in pregunta_lower or "llamar" in pregunta_lower or "hablar" in pregunta_lower:
            respuesta = "📞 Podés contactar a **InmoIA — Demo Inmobiliaria** por:\n\n- 💬 **WhatsApp:** +54 9 3329 599250\n- 📍 **Oficina:** San Pedro, Buenos Aires\n\n¡Te respondemos a la brevedad!"

        elif len(props_relevantes) > 0:
            respuesta = f"🏠 Encontré **{len(props_relevantes)} propiedad(es)** que puede(n) interesarte:\n\n"
            for _, p in props_relevantes.head(3).iterrows():
                respuesta += f"**{p['Titulo']}** ({p['Tipo']})\n"
                respuesta += f"📍 {p['Direccion']} · 💰 ${p['Precio']:,} {p['Moneda']}\n"
                if p['Ambientes'] > 0:
                    respuesta += f"🛏 {p['Ambientes']} amb · 📐 {p['Superficie']}m²\n"
                respuesta += "\n"
            respuesta += "¿Querés más detalles de alguna en particular?"
        else:
            respuesta = "No encontré propiedades disponibles con esos criterios en este momento. Te recomiendo contactarnos directamente por WhatsApp para ver opciones personalizadas: +54 9 3329 599250"

        st.session_state.chat_history.append({"role": "assistant", "content": respuesta})
        with st.chat_message("assistant"):
            st.write(respuesta)

# ==========================================
# PESTAÑA 3: PANEL DE GESTIÓN
# ==========================================
with tab3:
    st.subheader("📊 Panel de Gestión — Vista del Propietario")

    col_k1, col_k2, col_k3, col_k4 = st.columns(4)
    col_k1.metric("🏘️ Total Propiedades", len(df))
    col_k2.metric("🟢 Disponibles", len(df[df["Disponible"] == True]))
    col_k3.metric("🔴 Reservadas/Vendidas", len(df[df["Disponible"] == False]))
    col_k4.metric("💰 En Venta", len(df[df["Tipo"] == "Venta"]))

    st.markdown("---")

    col_g1, col_g2 = st.columns(2)
    with col_g1:
        import plotly.express as px
        tipo_counts = df["Tipo"].value_counts().reset_index()
        tipo_counts.columns = ["Tipo", "Cantidad"]
        fig = px.pie(tipo_counts, names="Tipo", values="Cantidad", hole=0.4, title="Venta vs Alquiler")
        st.plotly_chart(fig, use_container_width=True)

    with col_g2:
        cat_counts = df["Categoria"].value_counts().reset_index()
        cat_counts.columns = ["Categoría", "Cantidad"]
        fig2 = px.bar(cat_counts, x="Categoría", y="Cantidad", color="Cantidad",
                      color_continuous_scale="Blues", text_auto=True, title="Propiedades por Categoría")
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("📋 Listado completo")
    st.dataframe(
        df[["ID", "Tipo", "Categoria", "Titulo", "Barrio", "Precio", "Moneda", "Ambientes", "Superficie", "Disponible"]],
        use_container_width=True,
        hide_index=True
    )

    csv_export = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Exportar a CSV",
        data=csv_export,
        file_name="propiedades_inmoia.csv",
        mime="text/csv"
    )