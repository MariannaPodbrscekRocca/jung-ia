"""
================================================================================
PROYECTO: JUNG.AI: THE CIRCUS OF PERSONALITIES
AUTORA / DESIGNED BY: Marianna Podbrscek Rocca
CONTEXTO: Proyecto de Desarrollo Tecnológico para Alura Latam y Oracle Next.
================================================================================
"""

import os
import random
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
import streamlit as st

# Configuración de la página web en Streamlit
st.set_page_config(
    page_title="Jung.AI - The Circus of Personalities",
    page_icon="🎪",
    layout="wide"
)

# ------------------------------------------------------------------------------
# HOJA DE ESTILOS CSS PERSONALIZADA (ESTÉTICA DEL CIRCO DIGITAL)
# ------------------------------------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #12081c;
        color: #fce4ec;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1, h2, h3 {
        color: #ff007f !important;
        text-shadow: 0 0 15px rgba(255, 0, 127, 0.6);
        text-align: center;
    }
    .circus-terminal-box {
        background: linear-gradient(135deg, #1f1135 0%, #2a1b4e 100%);
        border: 3px solid #ff007f;
        border-radius: 16px;
        padding: 35px;
        margin-bottom: 25px;
        box-shadow: 0 0 25px rgba(255, 0, 127, 0.4);
    }
    .badge-candidato {
        background-color: #ffffff;
        color: #ff007f;
        padding: 8px 15px;
        border-radius: 8px;
        font-size: 1.15rem;
        font-weight: bold;
        display: inline-block;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.4);
        margin: 5px 0;
    }
    section[data-testid="stSidebar"] {
        color: #000000 !important;
    }
    section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] .stSelectbox div {
        color: #000000 !important;
        font-weight: 600 !important;
    }
    label, .stTextInput label, .stSelectbox label {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    .stButton>button[kind="primary"], div.stButton > button[data-baseweb="button"][kind="primary"] {
        background: linear-gradient(45deg, #ff007f, #ff5e00) !important;
        color: #ffffff !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        border: 2px solid #ffd700 !important;
        padding: 10px 22px !important;
        margin-top: 5px !important;
        margin-bottom: 5px !important;
        box-shadow: 0 0 20px rgba(255, 0, 127, 0.7) !important;
        transition: 0.3s ease;
    }
    .stButton>button[kind="primary"]:hover, div.stButton > button[data-baseweb="button"][kind="primary"]:hover {
        background: linear-gradient(45deg, #ff5e00, #ff007f) !important;
        color: #ffffff !important;
        transform: scale(1.03);
        box-shadow: 0 0 25px rgba(255, 215, 0, 0.9) !important;
    }
    .stButton>button {
        background-color: #ffffff !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        border: 2px solid #ffd700 !important;
        padding: 10px 22px !important;
        margin-top: 5px !important;
        margin-bottom: 5px !important;
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.3);
    }
    .stButton>button:hover {
        background: #f0f0f0 !important;
        color: #000000 !important;
        transform: scale(1.02);
    }
    input, textarea, div[data-baseweb="input"] {
        background-color: #ffffff !important;
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
    }
    input::placeholder {
        color: #555555 !important;
        opacity: 1 !important;
        font-weight: bold !important;
    }
    select {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 2px solid #ff007f !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }
    .subtitle-circus {
        color: #ffb3d1 !important;
        text-align: center;
        font-weight: 600;
        margin-bottom: 25px;
    }
    .instruction-fucsia {
        color: #ff80bf !important;
        font-size: 1.05rem;
        font-weight: bold;
        margin-top: 12px;
        margin-bottom: 6px;
    }
    .instruction-success {
        color: #00ffcc !important;
        font-size: 1.05rem;
        font-weight: bold;
        margin-top: 12px;
        margin-bottom: 6px;
    }
    .instruction-error {
        color: #ff4d4d !important;
        font-size: 1.05rem;
        font-weight: bold;
        margin-top: 12px;
        margin-bottom: 6px;
    }
    .box-opcion-1 {
        background: rgba(0, 255, 204, 0.12);
        border: 2px solid #00ffcc;
        border-radius: 12px;
        padding: 20px;
        margin-top: 15px;
        margin-bottom: 15px;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.3);
    }
    .box-opcion-2 {
        background: rgba(255, 215, 0, 0.12);
        border: 2px solid #ffd700;
        border-radius: 12px;
        padding: 20px;
        margin-top: 15px;
        margin-bottom: 15px;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.3);
    }
    .box-opcion-3 {
        background: rgba(255, 0, 127, 0.15);
        border: 2px solid #ff007f;
        border-radius: 12px;
        padding: 20px;
        margin-top: 15px;
        margin-bottom: 15px;
        box-shadow: 0 0 15px rgba(255, 0, 127, 0.4);
    }
    .alert-grande-roja {
        background-color: rgba(255, 0, 0, 0.2);
        border: 2px solid #ff0000;
        color: #ff4d4d;
        padding: 12px 18px;
        border-radius: 8px;
        font-size: 1.05rem;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 15px;
        line-height: 1.5;
    }
    .explicacion-bonita {
        background: linear-gradient(135deg, rgba(255, 0, 127, 0.2) 0%, rgba(18, 8, 28, 0.8) 100%);
        border: 2px solid #ff007f;
        border-radius: 14px;
        padding: 25px;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0 0 20px rgba(255, 0, 127, 0.4);
        font-size: 1.1rem;
        line-height: 1.6;
        color: #fce4ec;
    }
    .firma-footer {
        text-align: center;
        color: #ff80bf;
        font-size: 0.95rem;
        margin-top: 40px;
        border-top: 1px dashed rgba(255, 0, 127, 0.4);
        padding-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 3. GESTIÓN DE API KEY Y CARGA DE DATOS DESDE CSV
# ==============================================================================
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
if not OPENAI_API_KEY and "OPENAI_API_KEY" in st.secrets:
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

CSV_PATH = "matriz_personalidades.csv"

@st.cache_data
def cargar_matriz_completa():
    """Carga y procesa el archivo CSV local con Pandas asegurando la lectura íntegra de celdas."""
    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH).fillna("[Sin Nombre]")
        if len(df) < 16:
            dif = 16 - len(df)
            cols = df.columns
            vacias = pd.DataFrame([[f"[Personaje {i+len(df)+1}]" for _ in cols] for i in range(dif)], columns=cols)
            df = pd.concat([df, vacias], ignore_index=True)
        return df.iloc[0:16].copy()
    return pd.DataFrame()

df_matriz = cargar_matriz_completa()

LISTA_PREFIJOS = [
    ("EE. UU. / USA (+1)", "+1"), ("Perú (+51)", "+51"), ("México (+52)", "+52"), 
    ("Colombia (+57)", "+57"), ("Argentina (+54)", "+54"), ("Chile (+56)", "+56"), 
    ("Ecuador (+593)", "+593"), ("Venezuela (+58)", "+58")
]

LISTA_DOMINIOS_EMAIL = [
    ("@gmail.com", "@gmail.com"), ("@yahoo.com", "@yahoo.com"), 
    ("@outlook.com", "@outlook.com"), ("@icloud.com", "@icloud.com"), 
    ("@proton.me", "@proton.me"), ("@aol.com", "@aol.com"), 
    ("@zoho.com", "@zoho.com"), ("@mail.com", "@mail.com"), 
    ("@live.com", "@live.com"), ("@comcast.net", "@comcast.net"), 
    ("Otro proveedor", "OTRO")
]

LISTA_GENEROS_ESP = [
    ("Femenino", "Femenino"), 
    ("Masculino", "Masculino"), 
    ("Neutro / No binario u otro/a/e", "Neutro")
]

LISTA_GENEROS_ENG = [
    ("Female", "Femenino"), 
    ("Male", "Masculino"), 
    ("Neutral / Non-binary or other", "Neutro")
]

PRODUCCIONES_LISTA = ["• Harry Potter", "• Arrested Development", "• South Park", "• Breaking Bad"]

# ==============================================================================
# 4. DICCIONARIO BILINGÜE Y PREGUNTAS SUGERIDAS DINÁMICAS (POR FASE)
# ==============================================================================
TEXTOS = {
    "ESP": {
        "subtitulo": "Sistema Inteligente de Reclutamiento y Diagnóstico Psicométrico según el modelo de Carl Jung",
        "titulo_bienvenida": "🌟 ¡Bienvenidos a la primera fase para entrevista de trabajo con Jung Tech! 🌟",
        "bienvenida": (
            "Hola, mi nombre es Jung.AI. 🔮🧠\n\n"
            "Hoy voy a inspirarte a tener un proceso de selección fuera de este mundo bajo la gran carpa del circo digital.\n"
            "Este es un proceso de selección para el área de tecnología de la empresa Jung Tech Company 💻✨, "
            "y queremos marcar la diferencia en la forma de realizar nuestros procesos de contratación.\n"
            "Estamos interesados en que trabajes con nosotros, pero antes queremos ayudarte a "
            "postular al área más adecuada para ti utilizando los fascinantes test de personalidad de Carl Jung 🎪.\n\n"
            "Hoy realizaremos la primera etapa del proceso de selección. Te mostraremos personajes "
            "de series y películas, y tú nos dirás con cuál personaje te identificas más 🎭.\n"
            "En esta carpa digital contratamos mentes con diferentes arquetipos, así que no hay "
            "nada que temer. Lo único que queremos es ayudarte a encontrar el puesto perfecto 🚀.\n"
            "Solo te pedimos que seas completamente honesto/a. ¡Todos los tipos de personalidad son bienvenidos! 🌟"
        ),
        "btn_continuar": "🎪 Entrar a la Carpa Digital y Continuar 🎪",
        "confirmar_datos": "Registro del Candidato:",
        "input_nombres": "Nombres",
        "input_apellidos": "Apellidos",
        "input_preferido": "Nombre Preferido",
        "lbl_genero": "Género / Identificación:",
        "instruccion_nombres": "💡 Por favor llena este espacio con tu nombre completo.",
        "instruccion_apellidos": "💡 Por favor llena este espacio con tus apellidos.",
        "instruccion_preferido": "💡 Por favor llena este espacio con el nombre con el que prefieres que te llamemos (Opcional).",
        "instruccion_tel": "💡 Por favor ingresa tu número de teléfono sin código de país.",
        "instruccion_mail": "💡 Por favor escribe tu usuario de correo antes del símbolo '@'.",
        "msg_ok": "✅ ¡Campo completado correctamente!",
        "err_campo": "⚠️ El número de teléfono es obligatorio y solo acepta números.",
        "err_usr_mail": "⚠️ Debes escribir todo lo que va antes del '@', sin incluir el símbolo '@'.",
        "err_nombres": "⚠️ El nombre es obligatorio y no puede estar vacío.",
        "err_apellidos": "⚠️ Los apellidos son obligatorios y no pueden estar vacíos.",
        "err_tel": "⚠️ El número de teléfono solo puede contener números, sin letras.",
        "err_usr_mail_val": "⚠️ El usuario de correo es obligatorio y no puede contener el símbolo '@'.",
        "err_proveedor": "⚠️ Por el momento no tenemos soporte para este proveedor. Prueba con otro dominio de correo válido.",
        "lbl_prefijo": "Selecciona tu país / Prefijo:",
        "lbl_dominio": "Selecciona tu dominio:",
        "input_num_tel": "Número de teléfono (sin prefijo):",
        "input_usr_mail": "Usuario de correo (antes del @):",
        "btn_registrar": "Validate Credentials and Register",
        "btn_volver_inicio": "🌐 Volver a la Pantalla Inicial para Cambiar de Idioma",
        "err_vacio_ia": "⚠️ Por favor escribe una pregunta antes de hacer clic en Ask AI.",
        "intro_filtro_series": "Este es el inicio de tu entrevista de trabajo, elige una de estas películas o series para iniciar tu proceso de selección:",
        "lbl_selecciona_prod": "Selecciona una producción audiovisual:",
        "lbl_banco": "Banco de 16 Personalidades:",
        "btn_serie": "Confirmar Función y Ver Arquetipos 🎭",
        "btn_oops_datos": "😕 Oops, ingresé mal mis datos, quiero regresar al menú anterior",
        "pregunta_personaje": "{nombre}, ¿con qué personaje te identificas más dentro de la pista?",
        "btn_diagnostico": "✨ Revelar Diagnóstico Cognitivo y Arquetipo ✨",
        "btn_oops_serie": "😕 Oops, me equivoqué, quiero cambiar de película o serie",
        "btn_no_conozco": "😕 Oops, no conozco ninguna de estas películas o series",
        "msg_no_conozco": "¡No te preocupes! Esta prueba está diseñada exclusivamente para estas cuatro producciones actuales. Sin embargo, nos encantaría tomar tus datos para avisarte en cuanto abramos opciones para más series y películas. ¿Deseas registrar tus datos para futuras convocatorias?",
        "btn_aceptar_futuras": "Sí, registrar mis datos y finalizar",
        "btn_arrepinti": "😊 ¡Me arrepentí, ahora sí quiero tomar el test!",
        "gracias_cierre": "¡Muchas gracias! Tus datos han sido guardados exitosamente en nuestra base de datos de Jung Tech. Te notificaremos cuando tengamos nuevas series y películas disponibles. ¡Hasta pronto! 🎪✨",
        "btn_reiniciar_test": "🔄 Reiniciar Test / Restart Test",
        "btn_oops_reconexion": "😕 Oops, no siento que este perfil me describa como ser humano y como profesional, quiero volver a empezar el test",
        "btn_dom_1": "Opción 1: Si mi función es {f_val}, ¿cómo es mi personalidad en el día a día?",
        "btn_dom_2": "Opción 2: ¿Qué es el MBTI y cómo impacta en tu vida profesional?",
        "btn_dom_3": "Opción 3: ¿Cómo afecta esta función tu vida diaria y rendimiento?",
        "btn_siguiente_seccion": "➔ Siguiente Sección / Next Section",
        "instruccion_requisito": "💡 **Requisito del Circo Digital:** Debes hacer clic y explorar las opciones 1, 2 y 3 (en el orden que prefieras) para poder desbloquear el botón y pasar a la siguiente sección.",
        "err_falta_clicks": "⚠️ ¡Alto ahí! Te falta explorar alguna(s) de las opciones (1, 2, or/and 3) antes de continuar. Los botones que te falta presionar tienen un corazón roto (💔) al lado. Recuerda que en Jung Tech valoramos que nuestros empleados usen la IA y hagan preguntas. Si no comprendiste algo, ¡pregúntale a la IA! Este es un test laboral, dale rienda suelta a tu curiosidad. 🚀",
        "lbl_op1_sel": "Opción 1 Seleccionada",
        "lbl_op2_sel": "Opción 2 Seleccionada - Equipo de Reclutamiento",
        "lbl_op3_sel": "Opción 3 Seleccionada - Análisis IA",
        "badge_postulante": "Hola",
        "badge_personaje": "Personaje",
        "fase_1": "1. Función Dominante",
        "fase_2": "2. Función Auxiliar",
        "fase_3": "3. Función Terciaria",
        "fase_4": "4. Función Inferior",
        "fase_5": "5. Loop Cognitivo",
        "fase_6": "6. Arquetipo Digital",
        "titulo_resultado": "🎩✨ 7. Resultado Final y Diagnóstico en Jung Tech ✨🎩",
        "area_ti_lbl": "🎯 Área TI Recomendada",
        "rol_lbl": "permite liderar con propósito, conectando las necesidades humanas con la visión del producto.",
        "explicacion_bonita_txt": (
            "🌟 **Evaluación de Talento Jung Tech:**<br>"
            "A nuestro parecer y basándonos en tus respuestas, tu perfil cognitivo demuestra gran capacidad analítica y estratégica. "
            "Consideramos que encajarías perfectamente en nuestra área de <b>{area_ti}</b>, combinando resolución técnica con una visión humana e innovadora 🚀✨."
        ),
        "pregunta_envio_correo": "📩 Si estás de acuerdo con este diagnóstico, selecciona el idioma para el correo, elige una fecha tentativa para tu entrevista de Fase 2, y confirma tus datos:",
        "lbl_idioma_correo": "🌐 ¿En qué idioma deseas que te mandemos el correo?:",
        "lbl_fecha_fase2": "📅 Selecciona una fecha y hora tentativa para tu entrevista (Fase 2):",
        "btn_confirmar_y_enviar": "📤 Confirmar Datos, Idioma, Fecha y Enviar Email",
        "btn_oops_no_conforme": "😕 Oops, no estoy conforme con mi resultado (Resetear Test)",
        "msg_fin_sin_correo": "🎉 ¡Proceso finalizado con éxito! Gracias por participar en el circo digital de Jung Tech. 🚀🎪",
        "titulo_verificacion_datos": "🔍 Verificación y Confirmación de Datos del Postulante:",
        "msg_correo_enviado": "🎉 ¡Reporte y temario enviados con éxito a tu correo en el idioma solicitado! ⚠️ **¡POR FAVOR REVISA TU CARPETA DE SPAM!** Te esperamos en la entrevista de Fase 2. Fin del proceso. 🚀🎪",
        "label_improvisada": "💡 ¿Tienes dudas? Pregúntale a la IA:",
        "btn_enviar_improvisada": "Ask AI 🪄",
        "cargando_txt": "⏰ Cargando...",
        "orientacion_proceso": "💡 **Reclutamiento:** ¡Hola! Este es un proceso oficial de Jung Tech 🏢. Haz preguntas y explora los botones para conocerte a fondo 🧠✨.",
        "firma_autor": "Página web diseñada por: <b>Marianna Podbrscek Rocca</b>"
    },
    "ENG": {
        "subtitulo": "Intelligent Recruitment and Psychometric Diagnosis System according to Carl Jung's model",
        "titulo_bienvenida": "🌟 Welcome to the first phase for job interviews with Jung Tech! 🌟",
        "bienvenida": (
            "Hello, my name is Jung.AI. 🔮🧠\n\n"
            "Today, I am here to inspire you and guide you through a hiring process that is truly out of this world under the big top of the digital circus.\n"
            "This is the recruitment process for the Technology Department at Jung Tech Company 💻✨, "
            "and we want to make a difference in how we conduct our hiring processes.\n"
            "We are interested in having you work with us, but first, we want to help you "
            "apply to the most suitable area using Carl Jung's fascinating personality tests 🎪.\n\n"
            "Today, we will conduct the first stage of selection. We will show you characters "
            "from series and movies, and you will tell us which character you identify with the most 🎭.\n"
            "In this digital circus, we hire minds with different archetypes, so there is nothing to fear. "
            "Our only goal is to help you find the perfect position 🚀.\n"
            "We only ask you to be completely honest. Every single personality type is welcome here! 🌟"
        ),
        "btn_continuar": "🎪 Enter the Digital Big Top and Continue 🎪",
        "confirmar_datos": "Candidate Registration:",
        "input_nombres": "First Name",
        "input_apellidos": "Last Name",
        "input_preferido": "Preferred Name",
        "lbl_genero": "Gender / Identification:",
        "instruccion_nombres": "💡 Please fill this field with your full name.",
        "instruccion_apellidos": "💡 Please fill this field with your last name.",
        "instruccion_preferido": "💡 Please fill this field with your preferred name (Optional).",
        "instruccion_tel": "💡 Please enter your phone number without country code.",
        "instruccion_mail": "💡 Please type your email username before the '@' symbol.",
        "msg_ok": "✅ Field successfully completed!",
        "err_campo": "⚠️ Phone number is required and only accepts numbers.",
        "err_usr_mail": "⚠️ You must write everything before the '@', without including the '@' symbol.",
        "err_nombres": "⚠️ First name is required and cannot be empty.",
        "err_apellidos": "⚠️ Last name is required and cannot be empty.",
        "err_tel": "⚠️ Phone number can only contain numbers, no letters.",
        "err_usr_mail_val": "⚠️ Email username is required and cannot contain the '@' symbol.",
        "err_proveedor": "⚠️ We currently do not support this provider. Try another valid email domain.",
        "lbl_prefijo": "Select your country / Prefix:",
        "lbl_dominio": "Select your domain:",
        "input_num_tel": "Phone number (without country code):",
        "input_usr_mail": "Email username (before @):",
        "btn_registrar": "Validate Credentials and Register",
        "btn_volver_inicio": "🌐 Return to Home Screen to Change Language",
        "err_vacio_ia": "⚠️ Please type a question before clicking Ask AI.",
        "intro_filtro_series": "This is the beginning of your job interview, choose one of these movies or series to start your selection process:",
        "lbl_selecciona_prod": "Select an audiovisual production:",
        "lbl_banco": "Bank of 16 Personalities:",
        "btn_serie": "Confirm Show and View Archetypes 🎭",
        "btn_oops_datos": "😕 Oops, I entered my info incorrectly, I want to go back to the previous menu",
        "pregunta_personaje": "{nombre}, which character do you identify with the most under the circus tent?",
        "btn_diagnostico": "✨ Reveal Cognitive Diagnosis and Archetype ✨",
        "btn_oops_serie": "😕 Oops, my bad, I would like to change movie",
        "btn_no_conozco": "😕 Oops, I don't know any of these movies or series",
        "msg_no_conozco": "Don't worry! This test is exclusively designed for these four current productions. However, we would love to take your details to notify you as soon as we open options for more series and movies. Would you like to register your details for future calls?",
        "btn_aceptar_futuras": "Yes, register my details and finish",
        "btn_arrepinti": "😊 I changed my mind, now I want to take the test!",
        "gracias_cierre": "Thank you very much! Your data has been successfully saved in our Jung Tech database. We will notify you when new series and movies are available. See you soon! 🎪✨",
        "btn_reiniciar_test": "🔄 Restart Test",
        "btn_oops_reconexion": "😕 Oops, I don't feel like this profile describes me as a human and as a professional, I want to start the test over",
        "btn_dom_1": "Option 1: If my function is {f_val}, what is my personality like in daily life?",
        "btn_dom_2": "Option 2: What is the MBTI and how does it impact your professional life?",
        "btn_dom_3": "Option 3: How does this function affect your daily life and performance?",
        "btn_siguiente_seccion": "➔ Siguiente Sección / Next Section",
        "instruccion_requisito": "💡 **Digital Circus Requirement:** You must click and explore options 1, 2, and 3 (in any order you prefer) to unlock the button and move to the next section.",
        "err_falta_clicks": "⚠️ Hold on! You still need to explore some of the options (1, 2, or/and 3) before proceeding. The buttons you still need to press have a broken heart (💔) next to them. At Jung Tech, we value our employees using AI and asking questions. If you didn't understand something, ask the AI! Remember this is a job assessment test, so let your curiosity run wild. 🚀",
        "lbl_op1_sel": "Option 1 Selected",
        "lbl_op2_sel": "Option 2 Selected - Recruitment Team",
        "lbl_op3_sel": "Option 3 Selected - AI Analysis",
        "badge_postulante": "Hello",
        "badge_personaje": "Character",
        "fase_1": "1. Dominant Function",
        "fase_2": "2. Auxiliary Function",
        "fase_3": "3. Tertiary Function",
        "fase_4": "4. Inferior Function",
        "fase_5": "5. Cognitive Loop",
        "fase_6": "6. Digital Archetype",
        "titulo_resultado": "🎩✨ 7. Final Result and Diagnosis at Jung Tech ✨🎩",
        "area_ti_lbl": "🎯 Recommended IT Area",
        "rol_lbl": "allows connecting human needs with our company's vision",
        "explicacion_bonita_txt": (
            "🌟 **Jung Tech Talent Evaluation:**<br>"
            "In our view and based on your responses, your cognitive profile demonstrates strong analytical and strategic capacity. "
            "We consider that you would fit perfectly in our <b>{area_ti}</b> area, combining technical problem-solving with an innovative vision 🚀✨."
        ),
        "pregunta_envio_correo": "📩 If you agree with this diagnosis, select your preferred language for the email, choose a tentative date for your Phase 2 interview, and confirm your details:",
        "lbl_idioma_correo": "🌐 In which language would you like us to send the email?:",
        "lbl_fecha_fase2": "📅 Select a tentative date and time for your interview (Phase 2):",
        "btn_confirmar_y_enviar": "📤 Confirm Details, Language, Date and Send Email",
        "btn_oops_no_conforme": "😕 Oops, I don't agree with my result (Reset Test)",
        "msg_fin_sin_correo": "🎉 Process completed successfully! Thank you for participating in Jung Tech's digital circus. 🚀🎪",
        "titulo_verificacion_datos": "🔍 Verification and Confirmation of Candidate Details:",
        "msg_correo_enviado": "🎉 Report and preparation guide successfully sent to your email in the requested language! ⚠️ **PLEASE CHECK YOUR SPAM FOLDER!** We look forward to seeing you at your Phase 2 interview. End of process. 🚀🎪",
        "info_esp_txt": "This response was generated by our team of specialists. If you want a response completely tailored to you, please click the button below and our personalized AI will resolve any questions about our recruitment process or MBTI functions.",
        "label_improvisada": "💡 Any questions? Ask the AI:",
        "btn_enviar_improvisada": "Ask AI 🪄",
        "cargando_txt": "⏰ Loading...",
        "orientacion_proceso": "💡 **Recruitment:** Hello! This is an official Jung Tech hiring process 🏢. Ask questions and explore buttons to get to know yourself deeply 🧠✨.",
        "firma_autor": "Website designed by: <b>Marianna Podbrscek Rocca</b>"
    }
}

# Banco de preguntas contextuales y rotativas según la fase e idioma
PREGUNTAS_SUGERIDAS = {
    "ESP": {
        "funcion_dominante": "¿Cómo influye mi función dominante en mi toma de decisiones diaria?",
        "funcion_auxiliar": "¿De qué manera mi función auxiliar equilibra mis fortalezas técnicas?",
        "funcion_terciaria": "¿Cómo puedo integrar mi función terciaria para evitar bloqueos profesionales?",
        "funcion_inferior": "¿Qué nos enseña la función inferior sobre nuestras áreas de mejora?",
        "loop": "¿Cómo puedo salir saludablemente de este loop cognitivo en el trabajo?",
        "arquetipo": "¿Puedo trascender este arquetipo si en el futuro mi vocación cambia?"
    },
    "ENG": {
        "funcion_dominante": "How does my dominant function influence my daily decision-making?",
        "funcion_auxiliar": "In what way does my auxiliary function balance my technical strengths?",
        "funcion_terciaria": "How can I integrate my tertiary function to avoid professional burnout?",
        "funcion_inferior": "What does the inferior function teach us about our growth areas?",
        "loop": "How can I healthily break free from this cognitive loop at work?",
        "arquetipo": "Can I transcend this archetype if my vocation evolves in the future?"
    }
}

SERIES_MAP = {
    "Harry Potter": "Serie_Harry_Potter_BOTH",
    "Arrested Development": "Serie_Arrested_Development_BOTH",
    "South Park": "Serie_South_Park_BOTH",
    "Breaking Bad": "Serie_Breaking_Bad_BOTH"
}

# ==============================================================================
# 5. INICIALIZACIÓN DEL ESTADO DE LA APLICACIÓN (SESSION STATE)
# ==============================================================================
if "step" not in st.session_state:
    st.session_state.step = "bienvenida"
if "datos" not in st.session_state:
    st.session_state.datos = {}
if "eval" not in st.session_state:
    st.session_state.eval = {}
if "historial_interacciones" not in st.session_state:
    st.session_state.historial_interacciones = []
if "usadas_ia" not in st.session_state:
    st.session_state.usadas_ia = []
if "accion_activa" not in st.session_state:
    st.session_state.accion_activa = None
if "confirmar_regreso" not in st.session_state:
    st.session_state.confirmar_regreso = False
if "confirmar_reinicio" not in st.session_state:
    st.session_state.confirmar_reinicio = False
if "modo_no_conozco" not in st.session_state:
    st.session_state.modo_no_conozco = False
if "alerta_ia_vacia" not in st.session_state:
    st.session_state.alerta_ia_vacia = False
if "correo_enviado" not in st.session_state:
    st.session_state.correo_enviado = False

for campo in ["val_nombres", "val_apellidos", "val_preferido", "val_num_tel", "val_usr_mail", "verif_nombres", "verif_apellidos", "verif_tel", "verif_mail"]:
    if campo not in st.session_state:
        st.session_state[campo] = ""

if "errs_reg" not in st.session_state:
    st.session_state.errs_reg = {}
if "errs_verif" not in st.session_state:
    st.session_state.errs_verif = {}

st.title("🎪 JUNG.AI: THE CIRCUS OF PERSONALITIES 🎪")

def cambiar_idioma():
    """Reinicia los estados de error al cambiar de idioma."""
    st.session_state.errs_reg = {}
    st.session_state.errs_verif = {}
    for f in ["funcion_dominante", "funcion_auxiliar", "funcion_terciaria", "funcion_inferior", "loop", "arquetipo"]:
        if f"clics_{f}" in st.session_state:
            st.session_state[f"clics_{f}"] = set()

idioma_choice = st.sidebar.selectbox("🌐 Select Language / Seleccionar Idioma:", ["English", "Español"], on_change=cambiar_idioma)
current_idioma = "ESP" if idioma_choice == "Español" else "ENG"
txt = TEXTOS[current_idioma]

if "eval" in st.session_state and "personaje_idx" in st.session_state:
    idx_p = st.session_state.personaje_idx
    col_s = st.session_state.eval.get("serie_key", "Serie_Harry_Potter_BOTH")
    if not df_matriz.empty and idx_p < len(df_matriz):
        fila = df_matriz.iloc[idx_p]
        
        gen_val = st.session_state.datos.get("genero", "Neutro")
        if gen_val == "Femenino" or gen_val == "Female":
            arq_col = 'Arquetipos_F_ESP' if current_idioma == "ESP" else 'Arquetipos_F_ENG'
        elif gen_val == "Masculino" or gen_val == "Male":
            arq_col = 'Arquetipos_M_ESP' if current_idioma == "ESP" else 'Arquetipos_M_ENG'
        else:
            arq_col = 'Arquetipos_N_ESP' if current_idioma == "ESP" else 'Arquetipos_N_ENG'
            
        arq_desc_col = 'arquetipos_DESC_ESP' if current_idioma == "ESP" else 'arquetipos_DESC_ENG'
        f_inf_col = 'Funcion_inferior_ESP' if current_idioma == "ESP" else 'Funcion_inferior_ENG'
        f_inf_desc_col = 'Funcion_inferior_DESC_ESP' if current_idioma == "ESP" else 'Funcion_inferior_DESC_ENG'
        loop_col = 'Loops-ESP' if current_idioma == "ESP" else 'Loops-ENG'
        loop_desc_col = 'Loops_DESC_ESP' if current_idioma == "ESP" else 'Loops_DESC_ENG'
        
        st.session_state.eval.update({
            "mbti": fila.get('MBTI_ESP' if current_idioma == "ESP" else 'MBTI_ENG', 'INFJ'),
            "mbti_desc": fila.get('MBTI_DESC_ESP' if current_idioma == "ESP" else 'MBTI_DESC_ENG', ''),
            "f_dom": fila.get('Funcion_Dominante_ESP' if current_idioma == "ESP" else 'Funcion_Dominante_ENG', ''),
            "f_dom_d": fila.get('Funcion_Dominante_DESC_ESP' if current_idioma == "ESP" else 'Funcion_Dominante_DESC_ENG', ''),
            "f_aux": fila.get('Funcion_Auxiliar_ESP' if current_idioma == "ESP" else 'Funcion_Auxiliar_ENG', ''),
            "f_aux_d": fila.get('Funcion_Auxiliar_DESC_ESP' if current_idioma == "ESP" else 'Funcion_Auxiliar_DESC_ENG', ''),
            "f_ter": fila.get('Funcion_Terciaria_ESP' if current_idioma == "ESP" else 'Funcion_Terciaria_ENG', ''),
            "f_ter_d": fila.get('Funcion_Terciaria_DESC_ESP' if current_idioma == "ESP" else 'Funcion_Terciaria_DESC_ENG', ''),
            "f_inf": fila.get(f_inf_col, ''),
            "f_inf_d": fila.get(f_inf_desc_col, ''),
            "f_loop": fila.get(loop_col, ''),
            "f_loop_d": fila.get(loop_desc_col, ''),
            "arquetipo": fila.get(arq_col, ''),
            "arquetipo_d": fila.get(arq_desc_col, ''),
            "area_ti": fila.get('Area_TI_Recomendada', 'Desarrollo de Software'),
            "razon_ti": fila.get('razon_Area_ESP' if current_idioma == "ESP" else 'razon_Area_ENG', '')
        })

st.markdown(f"<p class='subtitle-circus'>{txt['subtitulo']}</p>", unsafe_allow_html=True)
st.markdown("---")

# ==============================================================================
# 6. FUNCIÓN DE CONSULTA A LA IA (CONSCIENCIA DUAL DE POSTULANTE + LUZ Y SOMBRA)
# ==============================================================================
def consultar_ia_orientada(nombre_usr, mbti_val, area_ti, func_nombre, func_desc, origen="equipo", pregunta_usuario=""):
    """
    Gestiona las consultas a la IA integrando la consciencia dual: se dirige al postulante 
    por su nombre pero analiza al personaje de la serie equilibrando su luz (light) y sombra (shadow), 
    evitando idealizaciones excesivas y abriendo la puerta a trascender arquetipos rígidos.
    """
    with st.spinner(txt["cargando_txt"]):
        resp_texto = ""
        
        personaje_actual = st.session_state.eval.get("personaje", "Desconocido")
        serie_actual = st.session_state.eval.get("serie_nombre", "producción seleccionada")

        q_lower = pregunta_usuario.lower()
        if "objetivo" in q_lower or "objective" in q_lower or "test" in q_lower:
            if current_idioma == "ESP":
                resp_texto = f"🎯 **[Objetivo del Test para ti, {nombre_usr}]:** Recordar que ningún arquetipo nos encierra; explorar tanto la luz como la sombra de {personaje_actual} nos permite elegir qué integrar y qué soltar 🚀."
            else:
                resp_texto = f"🎯 **[Test Objective for you, {nombre_usr}]:** Remember that no archetype traps us; exploring both the light and shadow of {personaje_actual} allows us to choose what to integrate and what to release 🚀."
        elif "character" in q_lower or "personaje" in q_lower or "quien soy" in q_lower or "who am i" in q_lower:
            if current_idioma == "ESP":
                resp_texto = f"🎭 **[Reflexión para {nombre_usr}]:** Estás dialogando con la esencia de **{personaje_actual}** (*{serie_actual}*), reconociendo su gran luz pero también su sombra oculta bajo el perfil **{mbti_val}** 🌟."
            else:
                resp_texto = f"🎭 **[Reflection for {nombre_usr}]:** You are engaging with the essence of **{personaje_actual}** (*{serie_actual}*), acknowledging both their brilliant light and hidden shadow through the **{mbti_val}** profile 🌟."

        if not resp_texto and OPENAI_AVAILABLE and OPENAI_API_KEY:
            try:
                client = OpenAI(api_key=OPENAI_API_KEY)
                sys_prompt = f"Eres Jung.AI, una presencia sabia y compasiva al estilo del Ánima/Ánimus 🔮✨. Te diriges al postulante por su nombre ('{nombre_usr}'), hablas del personaje ('{personaje_actual}') equilibrando su luz (light) y su sombra (shadow) sin idealizarlo excesivamente, en un solo párrafo completo y fluido. Responde en {'español' if current_idioma=='ESP' else 'inglés'}."
                if origen == "equipo":
                    prompt_completo = f"Dirigiéndote a {nombre_usr} en un solo párrafo, explica el impacto del MBTI y {func_nombre} en {area_ti}, analizando de forma equilibrada la luz y la sombra de {personaje_actual}."
                elif origen == "ia":
                    prompt_completo = f"Dirigiéndote a {nombre_usr} en un solo párrafo, analiza cómo ({func_nombre}: {func_desc}) moldea el rendimiento y los retos de {personaje_actual}, exponiendo tanto su destreza luminosa como su sombra."
                else:
                    prompt_completo = f"Postulante: {nombre_usr}. Personaje: {personaje_actual}. Concepto: {func_nombre}: {func_desc}. Pregunta: {pregunta_usuario}. Responde en un solo párrafo equilibrando luz y sombra."

                resp = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": sys_prompt},
                        {"role": "user", "content": prompt_completo}
                    ],
                    temperature=0.7,
                    max_tokens=250
                )
                resp_texto = resp.choices[0].message.content.strip()
            except Exception:
                pass

        if not resp_texto:
            if origen == "equipo":
                resp_texto = f"✨ Hola **{nombre_usr}**, al observar a **{personaje_actual}** (**{mbti_val}**), vemos su gran luz estratégica pero también su sombra aislante; en **{area_ti}**, integrar esta dualidad te hará un profesional más consciente y flexible 🚀."
            elif origen == "ia":
                resp_texto = f"🔮 Estimado/a **{nombre_usr}**, explorar **{func_nombre}** (*{func_desc}*) en el arquetipo de **{personaje_actual}** nos recuerda que toda luz proyecta una sombra, y aprender a abrazar ambas sin rigidez es la verdadera clave de tu evolución profesional 💡⚡."
            else:
                resp_texto = f"💡 Hola **{nombre_usr}**, analizando a **{personaje_actual}**, entendemos que **{func_nombre}** equilibra tus fortalezas luminosas y tus puntos ciegos (sombra) para tu rol en {area_ti}, demostrando que los arquetipos son herramientas que puedes adoptar o soltar libremente 💻."

        st.session_state.historial_interacciones.append({
            "tipo": origen,
            "pregunta": pregunta_usuario if origen == "libre" else f"Selección de {func_nombre}",
            "respuesta": resp_texto
        })
        return resp_texto

def generar_fechas_tentativas():
    """Genera 5 fechas hábiles futuras para la entrevista de Fase 2."""
    fechas = []
    actual = datetime.now() + timedelta(days=1)
    horas_disponibles = [10, 12, 15, 17, 19]
    while len(fechas) < 5:
        if actual.weekday() < 5:
            hora = random.choice(horas_disponibles)
            fecha_str = actual.replace(hour=hora, minute=0, second=0).strftime("%A, %d %b %Y - %I:00 %p")
            fechas.append(fecha_str)
        actual += timedelta(days=1)
    return fechas

def obtener_termino_genero(genero):
    """Retorna los sufijos gramaticales según el género."""
    if genero == "Femenino":
        return {"candidat": "candidata", "estimad": "Estimada"}
    elif genero == "Masculino":
        return {"candidat": "candidato", "estimad": "Estimado"}
    else:
        return {"candidat": "canditade", "estimad": "Estimadx"}

def enviar_correo_multilingue(fecha_seleccionada="", idioma_preferido="Español"):
    """Envía el correo SMTP traduciendo absolutamente todo al idioma elegido (Español o Inglés)."""
    datos_postulante = st.session_state.get("datos", {})
    correo_destino = datos_postulante.get("correo", "")
    nombre_postulante = datos_postulante.get("nombres", "Postulante")
    genero_postulante = datos_postulante.get("genero", "Neutro")
    mbti_postulante = st.session_state.eval.get("mbti", "INFJ")
    area_recomendada = st.session_state.eval.get("area_ti", "Desarrollo")
    personaje_elegido = st.session_state.eval.get("personaje", "N/A")

    if not correo_destino:
        return

    terms = obtener_termino_genero(genero_postulante)
    remitente = os.getenv("MAIL_USER", "jung.ai.tech@gmail.com")
    password = os.getenv("MAIL_PASSWORD", "")

    es_espanol = "Español" in idioma_preferido or "Spanish" in idioma_preferido

    if es_espanol:
        asunto = f"🎪 ¡Felicitaciones! Agenda Fase 2 - Jung Tech ({nombre_postulante})"
        cuerpo_html = f"""
        <html>
        <body style="background-color: #12081c; color: #fce4ec; font-family: Arial, sans-serif; padding: 20px;">
            <h2 style="color: #ff007f; text-align: center;">🎪 JUNG.AI: Reporte y Agenda de Entrevista (Fase 2) 🎪</h2>
            <p>{terms['estimad']} <b>{nombre_postulante}</b>,</p>
            <p>¡Felicitaciones por completar tu proceso psicométrico en la carpa digital de <b>Jung Tech</b>! Has avanzado a la segunda etapa como {terms['candidat']}.</p>
            <p><b>Personaje Seleccionado:</b> {personaje_elegido}</p>
            <p><b>Perfil MBTI Detectado:</b> {mbti_postulante}</p>
            <p><b>Área TI Asignada:</b> {area_recomendada}</p>
            <p><b>Horario Agendado para tu Entrevista (Fase 2):</b> <span style="color: #ff007f; font-weight: bold;">{fecha_seleccionada}</span></p>
            <hr style="border: 1px solid #ff007f;">
            <p style="color: #ff007f; font-weight: bold; font-size: 1.05rem;">⚠️ A PESAR DE QUE EL CANDIDATO PIDIÓ EL CORREO EN ESTE IDIOMA, EL RESUMEN DE PREGUNTAS Y RESPUESTAS REFLEJA EXACTAMENTE EL IDIOMA O LOS IDIOMAS QUE EL CANDIDATO USÓ DURANTE LA ENTREVISTA VIRTUAL.</p>
            <h3 style="color: #ff80bf;">📋 Resumen de tus conversaciones y reflexiones en la entrevista virtual:</h3>
            <ul>
        """
        for idx, item in enumerate(st.session_state.historial_interacciones, 1):
            cuerpo_html += f"<li><b>Conversación {idx} [{item['tipo'].upper()}]:</b><br><i>Pregunta/Acción:</i> {item['pregunta']}<br><i>Respuesta:</i> {item['respuesta']}<br><br></li>"
        cuerpo_html += f"""
            </ul>
            <p>Te esperamos puntualmente en el horario agendado (<b>{fecha_seleccionada}</b>) para nuestra entrevista de Fase 2. Fin del proceso.</p>
            <p style="color: #ff007f; font-weight: bold;">Atentamente, el equipo de reclutamiento de Jung.AI 🔮🤖</p>
        </body>
        </html>
        """
    else:
        asunto = f"🎪 Congratulations! Phase 2 Schedule - Jung Tech ({nombre_postulante})"
        cuerpo_html = f"""
        <html>
        <body style="background-color: #12081c; color: #fce4ec; font-family: Arial, sans-serif; padding: 20px;">
            <h2 style="color: #ff007f; text-align: center;">🎪 JUNG.AI: Interview Report and Schedule (Phase 2) 🎪</h2>
            <p>Dear <b>{nombre_postulante}</b>,</p>
            <p>Congratulations on successfully completing your psychometric process in <b>Jung Tech</b>'s digital big top! You have advanced to the second stage as our candidate.</p>
            <p><b>Selected Character:</b> {personaje_elegido}</p>
            <p><b>Detected MBTI Profile:</b> {mbti_postulante}</p>
            <p><b>Assigned IT Area:</b> {area_recomendada}</p>
            <p><b>Scheduled Time for your Interview (Phase 2):</b> <span style="color: #ff007f; font-weight: bold;">{fecha_seleccionada}</span></p>
            <hr style="border: 1px solid #ff007f;">
            <p style="color: #ff007f; font-weight: bold; font-size: 1.05rem;">⚠️ ALTHOUGH THE CANDIDATE REQUESTED THE EMAIL IN THIS LANGUAGE, THE SUMMARY OF QUESTIONS AND ANSWERS REFLECTS EXACTLY THE LANGUAGE OR LANGUAGES THE CANDIDATE USED DURING THE VIRTUAL INTERVIEW.</p>
            <h3 style="color: #ff80bf;">📋 Summary of your conversations and reflections in the virtual interview:</h3>
            <ul>
        """
        for idx, item in enumerate(st.session_state.historial_interacciones, 1):
            cuerpo_html += f"<li><b>Conversation {idx} [{item['tipo'].upper()}]:</b><br><i>Question/Action:</i> {item['pregunta']}<br><i>Respuesta:</i> {item['respuesta']}<br><br></li>"
        cuerpo_html += f"""
            </ul>
            <p>We look forward to seeing you promptly at your scheduled time (<b>{fecha_seleccionada}</b>) for your Phase 2 interview. End of process.</p>
            <p style="color: #ff007f; font-weight: bold;">Sincerely, the Jung.AI recruitment team 🔮🤖</p>
        </body>
        </html>
        """

    try:
        if password:
            msg = MIMEMultipart()
            msg['From'] = remitente
            msg['To'] = correo_destino
            msg['Subject'] = asunto
            msg.attach(MIMEText(cuerpo_html, 'html'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(remitente, password)
            server.sendmail(remitente, correo_destino, msg.as_string())
            server.quit()
    except Exception:
        pass

# ==============================================================================
# 7. RENDERIZADOR DE FASES COGNITIVAS (CONTROL DE CLICS OBLIGATORIOS)
# ==============================================================================
def renderizar_fase_cognitiva(titulo_fase, f_val, f_desc, clave_fase, siguiente_paso_tuple):
    """Renderiza las fases cognitivas exigiendo la exploración obligatoria de las 3 opciones."""
    ev = st.session_state.eval
    usr_completo = st.session_state.datos.get("preferido", "Postulante")
    usr = usr_completo.split()[0] if usr_completo else "Postulante"
    
    key_clics = f"clics_{clave_fase}"
    if key_clics not in st.session_state:
        st.session_state[key_clics] = set()

    st.markdown(f'<div class="circus-terminal-box">', unsafe_allow_html=True)
    st.subheader(f"🎩✨ {titulo_fase} ✨🎩")
    st.info(txt["orientacion_proceso"])
    
    label_personaje = "Personaje" if current_idioma == "ESP" else "Character"
    st.markdown(
        f'<div style="text-align: center; margin-bottom: 20px;">'
        f'<span class="badge-candidato">{txt["badge_postulante"]}, {usr}</span> &nbsp;&nbsp;|&nbsp;&nbsp; '
        f'<span class="badge-candidato">{label_personaje}: {ev.get("personaje")}</span>'
        f'</div>',
        unsafe_allow_html=True
    )
    
    st.markdown(f"### {titulo_fase}: `{f_val}`")
    st.markdown("---")
    
    st.markdown(f"<p class='instruction-fucsia'>{txt['instruccion_requisito']}</p>", unsafe_allow_html=True)
    
    c1_indicator = " ✅" if "opcion_1" in st.session_state[key_clics] else " 💔"
    c2_indicator = " ✅" if "opcion_2" in st.session_state[key_clics] else " 💔"
    c3_indicator = " ✅" if "opcion_3" in st.session_state[key_clics] else " 💔"

    b1 = txt["btn_dom_1"].format(f_val=f_val) + c1_indicator
    b2 = txt["btn_dom_2"] + c2_indicator
    b3 = txt["btn_dom_3"] + c3_indicator
    
    def toggle_accion(nombre_accion):
        id_completo = f"{clave_fase}_{nombre_accion}"
        if st.session_state.accion_activa == id_completo:
            st.session_state.accion_activa = None
        else:
            st.session_state.accion_activa = id_completo
            st.session_state[key_clics].add(nombre_accion)

    key_lang = "ESP" if current_idioma == "ESP" else "ENG"
    pregunta_sugerida_actual = PREGUNTAS_SUGERIDAS[key_lang].get(clave_fase, "What is my selected character?")
    
    # Opción 1 (Conectada a la IA)
    if st.button(b1, key=f"{clave_fase}_b1", type="primary" if "opcion_1" in st.session_state[key_clics] else "secondary"):
        toggle_accion("opcion_1")
    if st.session_state.accion_activa == f"{clave_fase}_opcion_1":
        resp_ia_op1 = consultar_ia_orientada(usr, ev.get('mbti'), ev.get('area_ti'), f_val, f_desc, origen="ia")
        st.markdown(f"<div class='box-opcion-1'><b>[{txt['lbl_op1_sel']}]:</b><br>{resp_ia_op1}</div>", unsafe_allow_html=True)
        
        col_ia1_1, col_ia1_2 = st.columns([3, 1])
        with col_ia1_1:
            pregunta_libre_1 = st.text_input(txt["label_improvisada"], placeholder=pregunta_sugerida_actual, key=f"{clave_fase}_lib_1", label_visibility="collapsed")
        with col_ia1_2:
            st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
            btn_enviar_ia1 = st.button(txt["btn_enviar_improvisada"], key=f"{clave_fase}_btn_lib_1", type="primary")

        if st.session_state.get(f"{clave_fase}_alerta_vacia_1", False):
            st.markdown(f"<div class='alert-grande-roja'>{txt['err_vacio_ia']}</div>", unsafe_allow_html=True)

        if btn_enviar_ia1:
            texto_a_enviar = pregunta_libre_1.strip() if pregunta_libre_1.strip() else pregunta_sugerida_actual
            st.session_state[f"{clave_fase}_alerta_vacia_1"] = False
            resp_libre = consultar_ia_orientada(usr, ev.get('mbti'), ev.get('area_ti'), f_val, f_desc, origen="libre", pregunta_usuario=texto_a_enviar)
            st.info(f"**Jung.AI:** {resp_libre}")

    # Opción 2 (Conectada a la IA)
    if st.button(b2, key=f"{clave_fase}_b2", type="primary" if "opcion_2" in st.session_state[key_clics] else "secondary"):
        toggle_accion("opcion_2")
    if st.session_state.accion_activa == f"{clave_fase}_opcion_2":
        resp_ia_extra = consultar_ia_orientada(usr, ev.get('mbti'), ev.get('area_ti'), f_val, f_desc, origen="equipo")
        st.markdown(f"<div class='box-opcion-2'><b>[{txt['lbl_op2_sel']}]:</b><br>{resp_ia_extra}</div>", unsafe_allow_html=True)
        
        col_ia2_1, col_ia2_2 = st.columns([3, 1])
        with col_ia2_1:
            pregunta_libre_2 = st.text_input(txt["label_improvisada"], placeholder=pregunta_sugerida_actual, key=f"{clave_fase}_lib_2", label_visibility="collapsed")
        with col_ia2_2:
            st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
            btn_enviar_ia2 = st.button(txt["btn_enviar_improvisada"], key=f"{clave_fase}_btn_lib_2", type="primary")

        if st.session_state.get(f"{clave_fase}_alerta_vacia_2", False):
            st.markdown(f"<div class='alert-grande-roja'>{txt['err_vacio_ia']}</div>", unsafe_allow_html=True)

        if btn_enviar_ia2:
            texto_a_enviar = pregunta_libre_2.strip() if pregunta_libre_2.strip() else pregunta_sugerida_actual
            st.session_state[f"{clave_fase}_alerta_vacia_2"] = False
            resp_libre = consultar_ia_orientada(usr, ev.get('mbti'), ev.get('area_ti'), f_val, f_desc, origen="libre", pregunta_usuario=texto_a_enviar)
            st.info(f"**Jung.AI:** {resp_libre}")

    # Opción 3 (Conectada a la IA)
    if st.button(b3, key=f"{clave_fase}_b3", type="primary" if "opcion_3" in st.session_state[key_clics] else "secondary"):
        toggle_accion("opcion_3")
    if st.session_state.accion_activa == f"{clave_fase}_opcion_3":
        resp_ia_ia = consultar_ia_orientada(usr, ev.get('mbti'), ev.get('area_ti'), f_val, f_desc, origen="ia")
        st.markdown(f"<div class='box-opcion-3'><b>[{txt['lbl_op3_sel']}]:</b><br>{resp_ia_ia}</div>", unsafe_allow_html=True)
        
        col_ia3_1, col_ia3_2 = st.columns([3, 1])
        with col_ia3_1:
            pregunta_libre_3 = st.text_input(txt["label_improvisada"], placeholder=pregunta_sugerida_actual, key=f"{clave_fase}_lib_3", label_visibility="collapsed")
        with col_ia3_2:
            st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
            btn_enviar_ia3 = st.button(txt["btn_enviar_improvisada"], key=f"{clave_fase}_btn_lib_3", type="primary")

        if st.session_state.get(f"{clave_fase}_alerta_vacia_3", False):
            st.markdown(f"<div class='alert-grande-roja'>{txt['err_vacio_ia']}</div>", unsafe_allow_html=True)

        if btn_enviar_ia3:
            texto_a_enviar = pregunta_libre_3.strip() if pregunta_libre_3.strip() else pregunta_sugerida_actual
            st.session_state[f"{clave_fase}_alerta_vacia_3"] = False
            resp_libre = consultar_ia_orientada(usr, ev.get('mbti'), ev.get('area_ti'), f_val, f_desc, origen="libre", pregunta_usuario=texto_a_enviar)
            st.info(f"**Jung.AI:** {resp_libre}")

    st.markdown("---")

    if st.session_state.get(f"{clave_fase}_alerta_clicks", False):
        st.markdown(f"<div class='alert-grande-roja'>{txt['err_falta_clicks']}</div>", unsafe_allow_html=True)

    col_inf_1, col_inf_2 = st.columns([3, 1])
    
    with col_inf_1:
        if st.button(txt["btn_siguiente_seccion"], type="primary", key=f"{clave_fase}_btn_sig"):
            if {"opcion_1", "opcion_2", "opcion_3"}.issubset(st.session_state[key_clics]):
                st.session_state[f"{clave_fase}_alerta_clicks"] = False
                sig_step, sig_nombre = siguiente_paso_tuple
                st.session_state.step = sig_step
                st.session_state.accion_activa = None
                st.rerun()
            else:
                st.session_state[f"{clave_fase}_alerta_clicks"] = True
                st.rerun()

    with col_inf_2:
        st.markdown('<div class="btn-secundario-pequenito">', unsafe_allow_html=True)
        if st.button(txt["btn_oops_reconexion"], key=f"{clave_fase}_oops_btn"):
            st.session_state.step = "seleccion_serie"
            st.session_state.accion_activa = None
            st.session_state[key_clics] = set()
            st.session_state.historial_interacciones = []
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
                
    st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# 8. MÁQUINA DE ESTADOS PRINCIPAL (FLUJO PASO A PASO DE LA APLICACIÓN)
# ==============================================================================

# Estado 1: Pantalla de Bienvenida inicial
if st.session_state.step == "bienvenida":
    st.markdown('<div class="circus-terminal-box">', unsafe_allow_html=True)
    st.markdown(f"### {txt['titulo_bienvenida']}")
    st.write(txt["bienvenida"])
    
    if st.button(txt["btn_continuar"], type="primary"):
        st.session_state.step = "captura_datos"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# Estado 2: Captura de Datos del Candidato
elif st.session_state.step == "captura_datos":
    st.markdown('<div class="circus-terminal-box">', unsafe_allow_html=True)
    st.subheader(txt["confirmar_datos"])

    errs = st.session_state.get("errs_reg", {})
    val_nombres = st.session_state.get("val_nombres", "")
    val_apellidos = st.session_state.get("val_apellidos", "")
    val_tel = st.session_state.get("val_num_tel", "")
    val_mail = st.session_state.get("val_usr_mail", "")

    with st.form("form_reg"):
        if errs.get("nombres"):
            st.markdown(f"<p class='instruction-error'>{errs['nombres']}</p>", unsafe_allow_html=True)
        elif val_nombres.strip():
            st.markdown(f"<p class='instruction-success'>{txt['msg_ok']}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p class='instruction-fucsia'>{txt['instruccion_nombres']}</p>", unsafe_allow_html=True)
        nombres = st.text_input(txt["input_nombres"], value=val_nombres, label_visibility="collapsed")
        
        if errs.get("apellidos"):
            st.markdown(f"<p class='instruction-error'>{errs['apellidos']}</p>", unsafe_allow_html=True)
        elif val_apellidos.strip():
            st.markdown(f"<p class='instruction-success'>{txt['msg_ok']}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p class='instruction-fucsia'>{txt['instruccion_apellidos']}</p>", unsafe_allow_html=True)
        apellidos = st.text_input(txt["input_apellidos"], value=val_apellidos, label_visibility="collapsed")
        
        st.markdown(f"<p class='instruction-fucsia'>{txt['instruccion_preferido']}</p>", unsafe_allow_html=True)
        preferido = st.text_input(txt["input_preferido"], value=st.session_state.get("val_preferido", ""), label_visibility="collapsed")
        
        st.markdown(f"<p class='instruction-success'>✅ Género seleccionado correctamente / Gender successfully selected</p>", unsafe_allow_html=True)
        lista_generos_actual = LISTA_GENEROS_ESP if current_idioma == "ESP" else LISTA_GENEROS_ENG
        genero_sel = st.selectbox(txt["lbl_genero"], [g[0] for g in lista_generos_actual], label_visibility="collapsed")

        c1, c2 = st.columns(2)
        with c1:
            prefijo = st.selectbox(txt["lbl_prefijo"], [p[0] for p in LISTA_PREFIJOS])
            if errs.get("num_tel"):
                st.markdown(f"<p class='instruction-error'>{errs['num_tel']}</p>", unsafe_allow_html=True)
            elif val_tel.strip() and val_tel.isdigit():
                st.markdown(f"<p class='instruction-success'>{txt['msg_ok']}</p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p class='instruction-fucsia'>{txt['instruccion_tel']}</p>", unsafe_allow_html=True)
            num_tel = st.text_input(txt["input_num_tel"], value=val_tel, label_visibility="collapsed")
            
        with c2:
            if errs.get("usr_mail"):
                st.markdown(f"<p class='instruction-error'>{errs['usr_mail']}</p>", unsafe_allow_html=True)
            elif val_mail.strip() and "@" not in val_mail:
                st.markdown(f"<p class='instruction-success'>{txt['msg_ok']}</p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p class='instruction-fucsia'>{txt['instruccion_mail']}</p>", unsafe_allow_html=True)
            usr_mail = st.text_input(txt["input_usr_mail"], value=val_mail, label_visibility="collapsed")
            
            if errs.get("prov_msg"):
                st.markdown(f"<p class='instruction-error'>{errs['prov_msg']}</p>", unsafe_allow_html=True)
            dom_mail = st.selectbox(txt["lbl_dominio"], [d[0] for d in LISTA_DOMINIOS_EMAIL])
            
        btn_enviar = st.form_submit_button(txt["btn_registrar"], type="primary")
        
        if btn_enviar:
            st.session_state.val_nombres = nombres
            st.session_state.val_apellidos = apellidos
            st.session_state.val_preferido = preferido
            st.session_state.val_num_tel = num_tel
            st.session_state.val_usr_mail = usr_mail

            new_errs = {}
            has_error = False

            if not nombres.strip():
                new_errs["nombres"] = txt["err_nombres"]
                has_error = True
            if not apellidos.strip():
                new_errs["apellidos"] = txt["err_apellidos"]
                has_error = True
            if not usr_mail.strip():
                new_errs["usr_mail"] = txt["err_usr_mail"]
                has_error = True
            elif "@" in usr_mail:
                new_errs["usr_mail"] = txt["err_usr_mail"]
                has_error = True
            
            if dom_mail == "Otro proveedor":
                new_errs["prov_msg"] = txt["err_proveedor"]
                has_error = True

            if not num_tel.strip():
                new_errs["num_tel"] = txt["err_campo"]
                has_error = True
            elif not num_tel.isdigit():
                new_errs["num_tel"] = txt["err_tel"]
                has_error = True

            if has_error:
                st.session_state.errs_reg = new_errs
                st.rerun()
            else:
                st.session_state.errs_reg = {}
                prefix_val = next(p[1] for p in LISTA_PREFIJOS if p[0] == prefijo)
                dom_val = next(d[1] for d in LISTA_DOMINIOS_EMAIL if d[0] == dom_mail)
                
                lista_generos_mapeo = LISTA_GENEROS_ESP if current_idioma == "ESP" else LISTA_GENEROS_ENG
                genero_val = next(g[1] for g in lista_generos_mapeo if g[0] == genero_sel)
                
                st.session_state.datos = {
                    "nombres": nombres.strip().title(),
                    "apellidos": apellidos.strip().title(),
                    "preferido": preferido.strip().title() if preferido else nombres.strip().title(),
                    "genero": genero_val,
                    "telefono": f"{prefix_val} {num_tel}",
                    "correo": f"{usr_mail.replace('@', '')}{dom_val}"
                }
                st.session_state.step = "seleccion_serie"
                st.rerun()

    st.markdown("---")
    if st.button(txt["btn_volver_inicio"]):
        st.session_state.step = "bienvenida"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# Estado 3: Selección de la Producción Audiovisual (Series / Películas)
elif st.session_state.step == "seleccion_serie":
    usr_completo = st.session_state.datos.get("preferido", "Postulante")
    usr = usr_completo.split()[0] if usr_completo else "Postulante"
    st.markdown('<div class="circus-terminal-box">', unsafe_allow_html=True)
    st.markdown(f"### 🎪 {txt['badge_postulante']}, `{usr}`")
    st.subheader(txt["intro_filtro_series"])
    for prod in PRODUCCIONES_LISTA:
        st.markdown(f"**{prod}**")
        
    serie_sel = st.selectbox(txt["lbl_selecciona_prod"], list(SERIES_MAP.keys()))
    
    col_ss1, col_ss2, col_ss3 = st.columns([2, 2, 2])
    with col_ss1:
        if st.button(txt["btn_serie"], type="primary"):
            st.session_state.eval["serie_key"] = SERIES_MAP[serie_sel]
            st.session_state.eval["serie_nombre"] = serie_sel
            st.session_state.step = "seleccion_personaje"
            st.rerun()
    with col_ss2:
        if st.button(txt["btn_oops_datos"]):
            st.session_state.step = "captura_datos"
            st.rerun()
    with col_ss3:
        if st.button(txt["btn_no_conozco"]):
            st.session_state.modo_no_conozco = True
            st.rerun()

    if st.session_state.modo_no_conozco:
        st.warning(txt["msg_no_conozco"])
        col_nc1, col_nc2 = st.columns(2)
        with col_nc1:
            if st.button(txt["btn_aceptar_futuras"], type="primary"):
                st.success(txt["gracias_cierre"])
                if st.button(txt["btn_reiniciar_test"]):
                    st.session_state.clear()
                    st.rerun()
        with col_nc2:
            if st.button(txt["btn_arrepinti"], type="primary"):
                st.session_state.modo_no_conozco = False
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# Estado 4: Selección del Personaje del Banco del CSV
elif st.session_state.step == "seleccion_personaje":
    usr_completo = st.session_state.datos.get("preferido", "Postulante")
    usr = usr_completo.split()[0] if usr_completo else "Postulante"
    col_s = st.session_state.eval.get("serie_key", "Serie_Harry_Potter_BOTH")
    st.markdown('<div class="circus-terminal-box">', unsafe_allow_html=True)
    
    if st.session_state.modo_no_conozco:
        st.warning(txt["msg_no_conozco"])
        col_nc1, col_nc2 = st.columns(2)
        with col_nc1:
            if st.button(txt["btn_aceptar_futuras"], type="primary"):
                st.success(txt["gracias_cierre"])
                if st.button(txt["btn_reiniciar_test"]):
                    st.session_state.clear()
                    st.rerun()
        with col_nc2:
            if st.button(txt["btn_arrepinti"], type="primary"):
                st.session_state.modo_no_conozco = False
                st.rerun()
    else:
        pregunta_formato = txt.get("pregunta_personaje", "{nombre}, ¿con qué personaje te identificas más?:")
        st.subheader(pregunta_formato.format(nombre=usr))
        
        if not df_matriz.empty and col_s in df_matriz.columns:
            personajes = df_matriz[col_s].dropna().tolist()
            per_sel = st.selectbox(txt["lbl_banco"], personajes)
            
            col_b_izq, col_b_der, col_b_ter = st.columns([1, 1, 1])
            with col_b_izq:
                if st.button(txt["btn_diagnostico"], type="primary"):
                    idx_p = personajes.index(per_sel)
                    st.session_state.personaje_idx = idx_p
                    fila = df_matriz[df_matriz[col_s] == per_sel].iloc[0]
                    
                    gen_val = st.session_state.datos.get("genero", "Neutro")
                    if gen_val == "Femenino" or gen_val == "Female":
                        arq_col = 'Arquetipos_F_ESP' if current_idioma == "ESP" else 'Arquetipos_F_ENG'
                    elif gen_val == "Masculino" or gen_val == "Male":
                        arq_col = 'Arquetipos_M_ESP' if current_idioma == "ESP" else 'Arquetipos_M_ENG'
                    else:
                        arq_col = 'Arquetipos_N_ESP' if current_idioma == "ESP" else 'Arquetipos_N_ENG'
                        
                    arq_desc_col = 'arquetipos_DESC_ESP' if current_idioma == "ESP" else 'arquetipos_DESC_ENG'
                    f_inf_col = 'Funcion_inferior_ESP' if current_idioma == "ESP" else 'Funcion_inferior_ENG'
                    f_inf_desc_col = 'Funcion_inferior_DESC_ESP' if current_idioma == "ESP" else 'Funcion_inferior_DESC_ENG'
                    loop_col = 'Loops-ESP' if current_idioma == "ESP" else 'Loops-ENG'
                    loop_desc_col = 'Loops_DESC_ESP' if current_idioma == "ESP" else 'Loops_DESC_ENG'
                    
                    st.session_state.eval.update({
                        "personaje": per_sel,
                        "mbti": fila.get('MBTI_ESP' if current_idioma == "ESP" else 'MBTI_ENG', 'INFJ'),
                        "mbti_desc": fila.get('MBTI_DESC_ESP' if current_idioma == "ESP" else 'MBTI_DESC_ENG', ''),
                        "f_dom": fila.get('Funcion_Dominante_ESP' if current_idioma == "ESP" else 'Funcion_Dominante_ENG', ''),
                        "f_dom_d": fila.get('Funcion_Dominante_DESC_ESP' if current_idioma == "ESP" else 'Funcion_Dominante_DESC_ENG', ''),
                        "f_aux": fila.get('Funcion_Auxiliar_ESP' if current_idioma == "ESP" else 'Funcion_Auxiliar_ENG', ''),
                        "f_aux_d": fila.get('Funcion_Auxiliar_DESC_ESP' if current_idioma == "ESP" else 'Funcion_Auxiliar_DESC_ENG', ''),
                        "f_ter": fila.get('Funcion_Terciaria_ESP' if current_idioma == "ESP" else 'Funcion_Terciaria_ENG', ''),
                        "f_ter_d": fila.get('Funcion_Terciaria_DESC_ESP' if current_idioma == "ESP" else 'Funcion_Terciaria_DESC_ENG', ''),
                        "f_inf": fila.get(f_inf_col, ''),
                        "f_inf_d": fila.get(f_inf_desc_col, ''),
                        "f_loop": fila.get(loop_col, ''),
                        "f_loop_d": fila.get(loop_desc_col, ''),
                        "arquetipo": fila.get(arq_col, ''),
                        "arquetipo_d": fila.get(arq_desc_col, ''),
                        "area_ti": fila.get('Area_TI_Recomendada', 'Desarrollo de Software'),
                        "razon_ti": fila.get('razon_Area_ESP' if current_idioma == "ESP" else 'razon_Area_ENG', '')
                    })
                    st.session_state.accion_activa = None
                    st.session_state.historial_interacciones = []
                    for f in ["funcion_dominante", "funcion_auxiliar", "funcion_terciaria", "funcion_inferior", "loop", "arquetipo"]:
                        st.session_state[f"clics_{f}"] = set()
                    st.session_state.step = "funcion_dominante"
                    st.rerun()
            with col_b_der:
                if st.button(txt["btn_oops_serie"]):
                    st.session_state.step = "seleccion_serie"
                    st.rerun()
            with col_b_ter:
                if st.button(txt["btn_no_conozco"]):
                    st.session_state.modo_no_conozco = True
                    st.rerun()

        if st.session_state.modo_no_conozco:
            st.warning(txt["msg_no_conozco"])
            col_nc1, col_nc2 = st.columns(2)
            with col_nc1:
                if st.button(txt["btn_aceptar_futuras"], type="primary"):
                    st.success(txt["gracias_cierre"])
                    if st.button(txt["btn_reiniciar_test"]):
                        st.session_state.clear()
                        st.rerun()
            with col_nc2:
                if st.button(txt["btn_arrepinti"], type="primary"):
                    st.session_state.modo_no_conozco = False
                    st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# Estados de Fases Cognitivas
elif st.session_state.step == "funcion_dominante":
    ev = st.session_state.eval
    renderizar_fase_cognitiva(txt["fase_1"], ev.get('f_dom', 'N/A'), ev.get('f_dom_d', 'N/A'), "funcion_dominante", ("funcion_auxiliar", txt["fase_2"]))

elif st.session_state.step == "funcion_auxiliar":
    ev = st.session_state.eval
    renderizar_fase_cognitiva(txt["fase_2"], ev.get('f_aux', 'N/A'), ev.get('f_aux_d', 'N/A'), "funcion_auxiliar", ("funcion_terciaria", txt["fase_3"]))

elif st.session_state.step == "funcion_terciaria":
    ev = st.session_state.eval
    renderizar_fase_cognitiva(txt["fase_3"], ev.get('f_ter', 'N/A'), ev.get('f_ter_d', 'N/A'), "funcion_terciaria", ("funcion_inferior", txt["fase_4"]))

elif st.session_state.step == "funcion_inferior":
    ev = st.session_state.eval
    renderizar_fase_cognitiva(txt["fase_4"], ev.get('f_inf', 'N/A'), ev.get('f_inf_d', 'N/A'), "funcion_inferior", ("loop", txt["fase_5"]))

elif st.session_state.step == "loop":
    ev = st.session_state.eval
    renderizar_fase_cognitiva(txt["fase_5"], ev.get('f_loop', 'N/A'), ev.get('f_loop_d', 'N/A'), "loop", ("arquetipo", txt["fase_6"]))

elif st.session_state.step == "arquetipo":
    ev = st.session_state.eval
    renderizar_fase_cognitiva(txt["fase_6"], ev.get('arquetipo', 'N/A'), ev.get('arquetipo_d', 'N/A'), "arquetipo", ("resultado", txt["titulo_resultado"]))

# Estado 11: Resultado Final y Envío de Correo SMTP
elif st.session_state.step == "resultado":
    ev = st.session_state.eval
    usr_completo = st.session_state.datos.get("preferido", "Postulante")
    usr = usr_completo.split()[0] if usr_completo else "Postulante"
    
    st.markdown('<div class="circus-terminal-box">', unsafe_allow_html=True)
    st.subheader(txt["titulo_resultado"])
    
    label_personaje = "Personaje" if current_idioma == "ESP" else "Character"
    st.markdown(
        f'<div style="text-align: center; margin-bottom: 20px;">'
        f'<span class="badge-candidato">{txt["badge_postulante"]}, {usr}</span> &nbsp;&nbsp;|&nbsp;&nbsp; '
        f'<span class="badge-candidato">{label_personaje}: {ev.get("personaje")}</span>'
        f'</div>',
        unsafe_allow_html=True
    )
    st.markdown(f"### {txt['area_ti_lbl']}: `{ev.get('area_ti')}`")
    st.info(f"**Description / Rol:** {txt['rol_lbl']}")
    
    explicacion_HTML = txt["explicacion_bonita_txt"].format(area_ti=ev.get('area_ti'))
    st.markdown(f'<div class="explicacion-bonita">{explicacion_HTML}</div>', unsafe_allow_html=True)
    st.markdown("---")

    st.markdown(f"### {txt['titulo_verificacion_datos']}")
    
    errs_v = st.session_state.get("errs_verif", {})
    opciones_fechas = generar_fechas_tentativas()

    with st.form("form_verif_correo_completo"):
        if errs_v.get("nombres"):
            st.markdown(f"<p class='instruction-error'>{errs_v['nombres']}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p class='instruction-fucsia'>{txt['input_nombres']}:</p>", unsafe_allow_html=True)
        nombres_val = st.text_input(txt["input_nombres"], value=st.session_state.get("verif_nombres", ""), label_visibility="collapsed")
        
        if errs_v.get("apellidos"):
            st.markdown(f"<p class='instruction-error'>{errs_v['apellidos']}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p class='instruction-fucsia'>Apellidos / Last Name:</p>", unsafe_allow_html=True)
        apellidos_val = st.text_input("Apellidos", value=st.session_state.get("verif_apellidos", ""), label_visibility="collapsed")
        
        st.markdown(f"<p class='instruction-fucsia'>{txt['input_preferido']}:</p>", unsafe_allow_html=True)
        preferido_val = st.text_input(txt["input_preferido"], value=usr, label_visibility="collapsed")
        
        st.markdown(f"<p class='instruction-fucsia'>{txt['lbl_genero']}</p>", unsafe_allow_html=True)
        genero_actual = st.session_state.datos.get("genero", "Neutro")
        
        lista_generos_verif = LISTA_GENEROS_ESP if current_idioma == "ESP" else LISTA_GENEROS_ENG
        genero_label_idx = 0 if genero_actual == "Femenino" else (1 if genero_actual == "Masculino" else 2)
        genero_val_sel = st.selectbox("Género:", [g[0] for g in lista_generos_verif], index=genero_label_idx, label_visibility="collapsed")

        c_tel1, c_tel2 = st.columns(2)
        with c_tel1:
            prefijo_sel = st.selectbox(txt["lbl_prefijo"], [p[0] for p in LISTA_PREFIJOS])
            if errs_v.get("num_tel"):
                st.markdown(f"<p class='instruction-error'>{errs_v['num_tel']}</p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p class='instruction-fucsia'>{txt['input_num_tel']}</p>", unsafe_allow_html=True)
            num_tel_val = st.text_input(txt["input_num_tel"], value=st.session_state.get("verif_tel", ""), label_visibility="collapsed")
            
        with c_tel2:
            if errs_v.get("usr_mail"):
                st.markdown(f"<p class='instruction-error'>{errs_v['usr_mail']}</p>", unsafe_allow_html=True)
            else:
                st.markdown(f"<p class='instruction-fucsia'>{txt['input_usr_mail']}</p>", unsafe_allow_html=True)
            correo_usr_val = st.text_input(txt["input_usr_mail"], value=st.session_state.get("verif_mail", ""), label_visibility="collapsed")
            
            if errs_v.get("prov_msg"):
                st.markdown(f"<p class='instruction-error'>{errs_v['prov_msg']}</p>", unsafe_allow_html=True)
            dominio_sel = st.selectbox(txt["lbl_dominio"], [d[0] for d in LISTA_DOMINIOS_EMAIL], label_visibility="collapsed")
        
        st.markdown(f"<p class='instruction-fucsia'>{txt['lbl_idioma_correo']}</p>", unsafe_allow_html=True)
        idioma_correo_sel = st.selectbox("Idioma del correo:", [
            "Español (Spanish)", 
            "Inglés (English)"
        ], label_visibility="collapsed")
        
        st.markdown(f"<p class='instruction-fucsia'>{txt['lbl_fecha_fase2']}</p>", unsafe_allow_html=True)
        fecha_elegida = st.selectbox("Seleccione horario:", opciones_fechas, label_visibility="collapsed")
        
        st.markdown(f"<p class='instruction-fucsia'>{txt['pregunta_envio_correo']}</p>", unsafe_allow_html=True)
        
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            btn_confirma_envio = st.form_submit_button(txt["btn_confirmar_y_enviar"], type="primary")
        with col_f2:
            btn_reset_test = st.form_submit_button(txt["btn_oops_no_conforme"])
            
        if btn_confirma_envio:
            st.session_state.verif_nombres = nombres_val
            st.session_state.verif_apellidos = apellidos_val
            st.session_state.verif_tel = num_tel_val
            st.session_state.verif_mail = correo_usr_val

            new_errs_v = {}
            has_error_v = False

            if not nombres_val.strip():
                new_errs_v["nombres"] = txt["err_nombres"]
                has_error_v = True
            if not apellidos_val.strip():
                new_errs_v["apellidos"] = txt["err_apellidos"]
                has_error_v = True
            if not correo_usr_val.strip():
                new_errs_v["usr_mail"] = txt["err_usr_mail"]
                has_error_v = True
            elif "@" in correo_usr_val:
                new_errs_v["usr_mail"] = txt["err_usr_mail"]
                has_error_v = True
            
            if dominio_sel == "Otro proveedor":
                new_errs_v["prov_msg"] = txt["err_proveedor"]
                has_error_v = True

            if not num_tel_val.strip():
                new_errs_v["num_tel"] = txt["err_campo"]
                has_error_v = True
            elif not num_tel_val.isdigit():
                new_errs_v["num_tel"] = txt["err_tel"]
                has_error_v = True

            if has_error_v:
                st.session_state.errs_verif = new_errs_v
                st.rerun()
            else:
                st.session_state.errs_verif = {}
                prefix_val = next(p[1] for p in LISTA_PREFIJOS if p[0] == prefijo_sel)
                dom_val = next(d[1] for d in LISTA_DOMINIOS_EMAIL if d[0] == dominio_sel)
                
                lista_generos_mapeo = LISTA_GENEROS_ESP if current_idioma == "ESP" else LISTA_GENEROS_ENG
                genero_val = next(g[1] for g in lista_generos_mapeo if g[0] == genero_val_sel)
                
                st.session_state.datos = {
                    "nombres": nombres_val.strip().title(),
                    "apellidos": apellidos_val.strip().title(),
                    "preferido": preferido_val.strip().title() if preferido_val else nombres_val.strip().title(),
                    "genero": genero_val,
                    "telefono": f"{prefix_val} {num_tel_val.strip()}",
                    "correo": f"{correo_usr_val.strip().replace('@', '')}{dom_val}"
                }
                
                enviar_correo_multilingue(fecha_seleccionada=fecha_elegida, idioma_preferido=idioma_correo_sel)
                st.session_state.correo_enviado = True
                st.rerun()
            
        if btn_reset_test:
            st.session_state.confirmar_reinicio = True
            st.rerun()

    if st.session_state.get("confirmar_reinicio", False):
        st.warning("⚠️ ¿Estás segura de que deseas reiniciar el test y borrar todo el progreso?")
        col_r1, col_r2 = st.columns(2)
        with col_r1:
            if st.button("Sí, reiniciar / Yes, restart", type="primary"):
                st.session_state.clear()
                st.rerun()
        with col_r2:
            if st.button("No, continuar / No, continue"):
                st.session_state.confirmar_reinicio = False
                st.rerun()

    if st.session_state.get("correo_enviado", False):
        st.success(txt["msg_correo_enviado"])
        
    st.markdown('</div>', unsafe_allow_html=True)

# Firma bilingüe con la autoría de la autora
st.markdown(
    f"<div class='firma-footer'>"
    f"{txt['firma_autor']}"
    f"</div>",
    unsafe_allow_html=True
)