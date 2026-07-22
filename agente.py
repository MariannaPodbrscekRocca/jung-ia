"""
========================================================================================
PROYECTO: JUNG.IA - Sistema Inteligente de Reclutamiento y Diagnóstico Psicométrico
EMPRESA: Jung Tech Company | Versión Web Maestra Completa (Streamlit)
AUTORÍA / DESARROLLO: Marianna Podbrscek Rocca
========================================================================================
DESCRIPCIÓN TÉCNICA Y ARQUITECTURA GENERAL:
Este script maestro integra la totalidad de la lógica analítica, el procesamiento con Pandas
de los 16 arquetipos del modelo MBTI de Carl Jung, la gestión bilingüe de textos y un motor
conversacional web completo construido con Streamlit. Simula el flujo completo de reclutamiento
y evaluación técnica para Jung Tech Company.
========================================================================================
"""

import os
import sys
import random
import datetime
import streamlit as st
import pandas as pd

# // =====================================================================
# // MÓDULO 1: CONFIGURACIÓN E IMPORTACIÓN DE OPENAI (IA GENERATIVA)
# // =====================================================================
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# Configuración inicial de la página web en Streamlit
st.set_page_config(
    page_title="Jung.IA - Circo Digital de Personalidades (Versión Maestra)",
    page_icon="🎪",
    layout="centered"
)

# // =====================================================================
# // MÓDULO 2: CARGA DE HOJA DE ESTILOS CSS EXTERNA
# // =====================================================================
def cargar_estilos_css(ruta_css="styles.css"):
    if os.path.exists(ruta_css):
        with open(ruta_css, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

cargar_estilos_css()

# Encabezado principal del sistema
st.title("🎪 JUNG.IA: EL CIRCO DIGITAL DE LAS PERSONALIDADES 🎪")
st.markdown("### Etapa 1 del Proceso de Selección - Jung Tech Company")
st.markdown("---")

CSV_PATH = "matriz_personalidades.csv"

# // =====================================================================
# // MÓDULO 3: DICCIONARIO BILINGÜE NATIVO Y CONFIGURACIONES DE DATOS
# // =====================================================================
TEXTOS = {
    "ESP": {
        "bienvenida": "Hola, mi nombre es Jung.IA. Hoy voy a inspirarte en un proceso de selección fuera de este mundo.",
        "datos_personales": "Por favor, ingresa tus credenciales de contacto para formalizar tu postulación:",
        "lbl_nombre": "Nombres:",
        "lbl_apellido": "Apellidos:",
        "lbl_preferido": "¿Cómo prefieres que te llamemos?",
        "lbl_telefono": "Teléfono de contacto (con código de país):",
        "lbl_correo": "Correo electrónico institucional o personal:",
        "btn_continuar": "Confirmar Registro y Continuar 🚀",
        "error_campos": "⚠️ Por favor, completa los campos obligatorios para avanzar en el proceso.",
        "seleccion_serie": "Selecciona la producción audiovisual que deseas utilizar para tu análisis de arquetipos:",
        "pregunta_personaje": "¿Con qué personaje te identificas más dentro de esta selección?",
        "btn_diagnostico": "Ejecutar Diagnóstico Psicométrico con IA 🧠"
    },
    "ENG": {
        "bienvenida": "Hello, my name is Jung.IA. Today I am here to guide you through an out-of-this-world hiring process.",
        "datos_personales": "Please enter your contact details to formalize your application:",
        "lbl_nombre": "First Name(s):",
        "lbl_apellido": "Last Name(s):",
        "lbl_preferido": "Preferred Name:",
        "lbl_telefono": "Phone Number (with country code):",
        "lbl_correo": "Email Address:",
        "btn_continuar": "Confirm Registration & Continue 🚀",
        "error_campos": "⚠️ Please complete the mandatory fields to proceed.",
        "seleccion_serie": "Select the audiovisual production you wish to use for your archetype analysis:",
        "pregunta_personaje": "Which character do you identify with the most?",
        "btn_diagnostico": "Run Psychometric AI Diagnostic 🧠"
    }
}

SERIES_MAP = {
    "Harry Potter": "Serie_Harry_Potter_BOTH",
    "Arrested Development": "Serie_Arrested_Development_BOTH",
    "South Park": "Serie_South_Park_BOTH",
    "Breaking Bad": "Serie_Breaking_Bad_BOTH"
}

RESPUESTAS_CACHED_ESP = [
    "Comprendo perfectamente tu inquietud, {nombre}. La teoría de Carl Jung muestra que la función cognitiva asociada a tu perfil te ayuda a mantener la adaptabilidad y el balance analítico en tareas de desarrollo.",
    "Es una excelente pregunta, {nombre}. Apoyarte en tus fortalezas te permite procesar información compleja con mayor estructura en tus proyectos de software.",
    "En el entorno de Jung Tech Company, {nombre}, tu perfil opera como una herramienta estratégica que previene la sobrecarga cognitiva y optimiza tu rendimiento técnico."
]

# // =====================================================================
# // MÓDULO 4: CARGA DE LA MATRIZ DE PERSONALIDADES (PANDAS CON CACHÉ)
# // =====================================================================
@st.cache_data
def cargar_matriz_maestra():
    try:
        if os.path.exists(CSV_PATH):
            df = pd.read_csv(CSV_PATH)
            # Aseguramos un mínimo de 16 filas para el estándar MBTI
            if len(df) < 16:
                diferencia = 16 - len(df)
                cols = df.columns
                vacias = pd.DataFrame([[f"[Registro {i+len(df)+1}]" for _ in cols] for i in range(diferencia)], columns=cols)
                df = pd.concat([df, vacias], ignore_index=True)
            return df.iloc[0:16].copy().fillna("[Sin Datos]")
        else:
            return pd.DataFrame()
    except Exception as e:
        st.error(f"[ERROR CRÍTICO] Fallo en la lectura del archivo CSV: {e}")
        return pd.DataFrame()

df_matriz_maestra = cargar_matriz_maestra()

# // =====================================================================
# // MÓDULO 5: GESTIÓN DE ESTADOS DE SESIÓN (SESSION STATE)
# // =====================================================================
if "etapa" not in st.session_state:
    st.session_state.etapa = 1
if "idioma" not in st.session_state:
    st.session_state.idioma = "ESP"
if "usuario" not in st.session_state:
    st.session_state.usuario = {}
if "evaluacion" not in st.session_state:
    st.session_state.evaluacion = {}

# Selector global de idioma en barra lateral
idioma_sel = st.sidebar.selectbox("🌐 Seleccionar Idioma / Language", ["Español (ESP)", "English (ENG)"])
st.session_state.idioma = "ESP" if "Español" in idioma_sel else "ENG"
txt = TEXTOS[st.session_state.idioma]

# --------------------------------------------------------------------------
# ETAPA 1: SELECCIÓN DE IDIOMA Y REGISTRO DE DATOS PERSONALES
# --------------------------------------------------------------------------
if st.session_state.etapa == 1:
    st.markdown(f"### 📝 {txt['datos_personales']}")
    
    with st.form("form_maestro_registro"):
        nombres = st.text_input(txt["lbl_nombre"], placeholder="Ej. Marianna")
        apellidos = st.text_input(txt["lbl_apellido"], placeholder="Ej. Podbrscek Rocca")
        preferido = st.text_input(txt["lbl_preferido"], placeholder="Ej. Marianna")
        telefono = st.text_input(txt["lbl_telefono"], placeholder="+1 6184341558")
        correo = st.text_input(txt["lbl_correo"], placeholder="mariannapodbrscek@gmail.com")
        
        btn_submit = st.form_submit_button(txt["btn_continuar"])
        
        if btn_submit:
            if not nombres.strip() or not apellidos.strip() or not correo.strip():
                st.error(txt["error_campos"])
            else:
                st.session_state.usuario = {
                    "nombres": nombres.strip().title(),
                    "apellidos": apellidos.strip().title(),
                    "preferido": preferido.strip().title() if preferido else nombres.strip().title(),
                    "telefono": telefono.strip(),
                    "correo": correo.strip()
                }
                st.session_state.etapa = 2
                st.rerun()

# --------------------------------------------------------------------------
# ETAPA 2: FILTRO DE PRODUCCIONES Y SELECCIÓN DE ARQUETIPO MBTI
# --------------------------------------------------------------------------
elif st.session_state.etapa == 2:
    nombre_call = st.session_state.usuario["preferido"]
    st.success(f"¡Bienvenido/a al entorno interactivo, {nombre_call}!")
    
    st.markdown(f"### 🎬 {txt['seleccion_serie']}")
    serie_elegida = st.selectbox("Producción Audiovisual:", list(SERIES_MAP.keys()))
    col_serie = SERIES_MAP[serie_elegida]
    
    if not df_matriz_maestra.empty and col_serie in df_matriz_maestra.columns:
        personajes_disponibles = df_matriz_maestra[col_serie].dropna().tolist()
        personaje_sel = st.selectbox(txt["pregunta_personaje"], personajes_disponibles)
        
        if st.button(txt["btn_diagnostico"]):
            # Extracción estructurada del registro mediante Pandas
            fila_match = df_matriz_maestra[df_matriz_maestra[col_serie] == personaje_sel].iloc[0]
            
            st.session_state.evaluacion = {
                "serie": serie_elegida,
                "personaje": personaje_sel,
                "mbti": fila_match.get("MBTI_ESP" if st.session_state.idioma == "ESP" else "MBTI_ENG", "INTJ"),
                "descripcion_mbti": fila_match.get("MBTI_DESC_ESP" if st.session_state.idioma == "ESP" else "MBTI_DESC_ENG", ""),
                "funcion_dominante": fila_match.get("Funcion_Dominante_ESP" if st.session_state.idioma == "ESP" else "Funcion_Dominante_ENG", ""),
                "funcion_dominante_desc": fila_match.get("Funcion_Dominante_DESC_ESP" if st.session_state.idioma == "ESP" else "Funcion_Dominante_DESC_ENG", ""),
                "funcion_auxiliar": fila_match.get("Funcion_Auxiliar_ESP" if st.session_state.idioma == "ESP" else "Funcion_Auxiliar_ENG", ""),
                "funcion_auxiliar_desc": fila_match.get("Funcion_Auxiliar_DESC_ESP" if st.session_state.idioma == "ESP" else "Funcion_Auxiliar_DESC_ENG", ""),
                "funcion_terciaria": fila_match.get("Funcion_Terciaria_ESP" if st.session_state.idioma == "ESP" else "Funcion_Terciaria_ENG", ""),
                "funcion_inferior": fila_match.get("Funcion_inferior_ESP" if st.session_state.idioma == "ESP" else "Funcion_inferior_ENG", ""),
                "patron_loop": fila_match.get("Loops-ESP" if st.session_state.idioma == "ESP" else "Loops-ENG", ""),
                "area_ti": fila_match.get("Area_TI_Recomendada", "Desarrollo de Software y Arquitectura Cloud"),
                "razon_area": fila_match.get("razon_Area_ESP" if st.session_state.idioma == "ESP" else "razon_Area_ENG", "")
            }
            st.session_state.etapa = 3
            st.rerun()

# --------------------------------------------------------------------------
# ETAPA 3: REPORTE PSICOMÉTRICO MAESTRO Y CANAL CON IA REAL
# --------------------------------------------------------------------------
elif st.session_state.etapa == 3:
    ev = st.session_state.evaluacion
    usr = st.session_state.usuario["preferido"]
    
    st.markdown("### ✨ Reporte Diagnóstico Integral de Jung.IA")
    st.markdown(f"**Candidato/a:** {usr} ({st.session_state.usuario['correo']})")
    st.markdown(f"**Serie Analizada:** {ev['serie']} | **Personaje:** `{ev['personaje']}`")
    st.markdown(f"**Tipo Psicométrico MBTI:** `{ev['mbti']}`")
    st.markdown(f"**Función Dominante:** {ev['funcion_dominante']} — *{ev['funcion_dominante_desc']}*")
    st.markdown(f"**Área Tecnológica Recomendada:** `{ev['area_ti']}`")
    st.info(f"💡 **Fundamentación de Negocio:** {ev['razon_area']}")
    
    st.markdown("---")
    st.markdown("### 💬 Canal de Conversación Activa con el Agente Inteligente")
    st.markdown("Escribe tus consultas técnicas sobre funciones cognitivas, arquetipos o desarrollo de software:")
    
    # Campo de texto multilínea sin restricciones de longitud
    pregunta_libre = st.text_area("Mensaje para Jung.IA:", height=120, placeholder="Ej. Explícame cómo mi función auxiliar equilibra mi perfil bajo presión...")
    
    if st.button("Enviar Consulta 🚀"):
        if pregunta_libre.strip():
            if OPENAI_AVAILABLE and os.getenv("OPENAI_API_KEY"):
                try:
                    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
                    resp_api = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": f"Eres Jung.IA, la musa de reclutamiento de Jung Tech Company. Asesoras a {usr} con perfil {ev['mbti']} en el área de {ev['area_ti']}. Sé inspirador y técnico."},
                            {"role": "user", "content": pregunta_libre}
                        ]
                    )
                    st.success(f"**Jung.IA (ChatGPT):** {resp_api.choices[0].message.content}")
                except Exception as ex:
                    st.warning(f"[Aviso] No se pudo conectar con OpenAI ({ex}). Activando respaldo local:")
                    st.info(f"**Jung.IA (Fallback):** Comprendo tu inquietud, {usr}. Como perfil {ev['mbti']}, tu dominio en {ev['funcion_dominante']} optimiza notablemente tu desempeño en {ev['area_ti']}.")
            else:
                st.info(f"**Jung.IA (Modo Local):** Excelente perspectiva, {usr}. Tu estructura cognitiva {ev['mbti']} te otorga una ventaja competitiva excepcional en {ev['area_ti']}.")
        else:
            st.warning("⚠️ Por favor, ingresa una pregunta válida en el campo de texto.")
            
    st.markdown("---")
    if st.button("↺ Reiniciar Proceso de Evaluación"):
        st.session_state.etapa = 1
        st.rerun()