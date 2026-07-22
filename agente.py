"""
================================================================================
PROYECTO: Jung.IA - Agente de Reclutamiento Interactivo (Versión Maestra Original)
AUTORA: Marianna Podbrscek Rocca
CONTEXTO: Proyecto de Desarrollo Tecnológico para Alura Latam y Oracle Next.
================================================================================
"""

import os
import sys
import random
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
import inquirer

# Intentar importar la librería oficial de OpenAI
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# ------------------------------------------------------------------------------
# CONFIGURACIÓN DE LLAVE DE API Y SERVIDOR DE CORREO (SMTP)
# ------------------------------------------------------------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "") 

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "mariannapodbrscek@gmail.com" 
SENDER_PASSWORD = "TU_APP_PASSWORD_AQUI" 

CSV_PATH = "matriz_personalidades.csv"

LISTA_PREFIJOS = [
    ("EE. UU. / USA (+1)", "+1"),
    ("Perú (+51)", "+51"),
    ("México (+52)", "+52"),
    ("Colombia (+57)", "+57"),
    ("Argentina (+54)", "+54"),
    ("Chile (+56)", "+56"),
    ("Ecuador (+593)", "+593"),
    ("Guatemala (+502)", "+502"),
    ("Bolivia (+591)", "+591"),
    ("Costa Rica (+506)", "+506"),
    ("Panamá (+507)", "+507"),
    ("República Dominicana (+1-809)", "+1-809"),
    ("República Dominicana (+1-829)", "+1-829"),
    ("República Dominicana (+1-849)", "+1-849"),
    ("Uruguay (+598)", "+598"),
    ("Venezuela (+58)", "+58")
]

LISTA_DOMINIOS_EMAIL = [
    ("@gmail.com", "@gmail.com"),
    ("@hotmail.com", "@hotmail.com"),
    ("@outlook.com", "@outlook.com"),
    ("@yahoo.com", "@yahoo.com"),
    ("@icloud.com", "@icloud.com"),
    ("@live.com", "@live.com"),
    ("@msn.com", "@msn.com"),
    ("@aol.com", "@aol.com"),
    ("@protonmail.com", "@protonmail.com"),
    ("@proton.me", "@proton.me"),
    ("Otro proveedor / Other domain", "OTRO")
]

PRODUCCIONES_LISTA = [
    "• Harry Potter",
    "• Arrested Development",
    "• South Park",
    "• Breaking Bad"
]

TEXTOS = {
    "ESP": {
        "bienvenida": (
            "Hola, mi nombre es Jung.IA.\n\n"
            "Hoy voy a inspirarte a tener un proceso de selección fuera de este mundo.\n"
            "Este es un proceso de selección para el área de tecnología de la empresa Jung Tech Company, "
            "y queremos marcar la diferencia en la forma de realizar nuestros procesos de contratación.\n"
            "Estamos interesados en que trabajes en nuestra empresa, pero antes queremos ayudarte a "
            "postular al área más adecuada para ti utilizando los test de personalidad de Carl Jung.\n\n"
            "Hoy realizaremos la primera etapa del proceso de selección. Te mostraremos personajes "
            "de series y películas, y tú nos dirás con cuál personaje te identificas más.\n"
            "En esta empresa contratamos empleados con diferentes tipos de personalidad, así que no hay "
            "nada que temer. Lo único que queremos es ayudarte a encontrar el puesto que mejor se adapte a ti.\n"
            "Solo te pedimos que seas completamente honesto/a. Aunque creas que tu personalidad se parece "
            "a la de Darth Sidious o Lord Voldemort, todos los tipos de personalidad son bienvenidos."
        ),
        "confirmar_datos": "Por favor, ingresa tus datos personales de contacto:",
        "nota_nombres": "(Nota: Puedes ingresar uno o más nombres y uno o más apellidos)",
        "input_nombres": "Nombres (1 o más): ",
        "input_apellidos": "Apellidos (1 o más): ",
        "input_preferido": "¿Cómo prefieres que te llamemos?: ",
        "err_campo_vacio": "[!] Este campo no puede estar vacío. Por favor, ingresa una respuesta válida.",
        "err_solo_letras": "[!] Por favor, solo ingresar letras.",
        "err_solo_numeros": "[!] Solo se permiten números (sin letras, espacios ni símbolos). Por favor, intenta de nuevo.",
        "nota_cobertura_tel": "(Por el momento solo aceptamos números telefónicos de EE. UU. y Latinoamérica)",
        "input_prefijo": "Selecciona tu país:",
        "input_num_tel": "Número de teléfono (sin prefijo): ",
        "input_usr_mail": "Usuario de correo (antes del @): ",
        "input_dom_mail": "Selecciona tu dominio:",
        "nota_correo_otro": (
            "Por el momento solo aceptamos postulaciones con correos de los proveedores listados.\n"
            "Por favor, selecciona uno de los dominios disponibles."
        ),
        "pregunta_datos_correctos": "¿Todos tus datos están correctos?",
        "opt_datos_ok": "Sí, todo está correcto",
        "opt_datos_edit": "No, quiero corregir algún dato",
        "lbl_nom": "Nombres",
        "lbl_ape": "Apellidos",
        "lbl_pref": "Nombre Preferido",
        "lbl_tel": "Teléfono",
        "lbl_mail": "Correo",
        "menu_corregir": "¿Qué dato te gustaría corregir?",
        "opt_edit_nom": "Corregir Nombres / Apellidos / Preferido",
        "opt_edit_tel": "Corregir Teléfono (Prefijo / Número)",
        "opt_edit_mail": "Corregir Correo (Usuario / Dominio)",
        "opt_edit_todo": "Corregir TODO de nuevo",
        "intro_filtro_series": "Las producciones audiovisuales disponibles en esta evaluación son:",
        "filtro_series": "{nombre}, ¿has visto alguna de estas películas o series?:",
        "opt_si": "Sí",
        "opt_no": "No",
        "no_series": (
            "Estimado/a {nombre}, por el momento este modelo de inteligencia artificial solo está diseñado "
            "para evaluar a candidatos a través de las siguientes producciones: Harry Potter, Arrested Development, "
            "South Park y Breaking Bad.\n\n"
            "Sin embargo, en Jung Tech Company estamos muy interesados en tu perfil y nos encantaría considerar tu postulación."
        ),
        "pregunta_correo_inmediato": (
            "{nombre}, ¿nos autorizas a enviarte un correo electrónico EN ESTE MOMENTO para confirmar que tenemos "
            "tu información correctamente registrada en nuestro sistema?"
        ),
        "opt_auth_mail_si": "Sí, autorizo el correo ahora",
        "opt_auth_mail_no": "No por el momento",
        "correo_confirmacion_enviado": (
            "¡Perfecto, {nombre}! Te hemos enviado un correo de confirmación de recepción de datos.\n"
            "Más adelante nos pondremos en contacto contigo nuevamente con fechas tentativas para agendar "
            "tus posibles entrevistas en el área de tecnología."
        ),
        "consentimiento_no": "Entendido, {nombre}. Respetamos tu decisión y mantendremos tus datos resguardados de forma confidencial.",
        "pregunta_personaje": "{nombre}, ¿con qué personaje te identificas más? ¿Cuál se parece (en personalidad) a ti?:",
        "confirmar_personaje": "{nombre}, ¿tu personaje es '{personaje}'?",
        "cambiar_serie": "Cambiar de serie o película",
        "btn_reiniciar_prueba": "↺ Volver al Inicio de la Prueba (Seleccionar otra serie)",
        "btn_reiniciar_todo_datos": "Oops, me equivoqué: Quiero empezar TODO desde cero (no puse bien mis datos)",
        "btn_reiniciar_test_personaje": "Oops, no seleccioné bien mi personaje / no me resuenan los resultados: Quiero volver a empezar el test",
        "sospecha_texto": "{nombre}, sospecho que eres un {mbti} + {desc}.",
        "pregunta_mbti_confirmar": "¿Crees que esta descripción representa tu personalidad?",
        "diagnostico_base": "Entonces {nombre}, eres un: {personaje}.\nPresiento que tienes {mbti_desc}.\nTu función dominante es {fun_dom}.\nSABES {fun_dom_desc}.",
        "pregunta_genero": "{nombre}, para la siguiente etapa necesitamos que nos digas tu género:",
        "arquetipo_intro": (
            "Un arquetipo es un patrón universal de personalidad según Carl Gustav Jung.\n\n"
            "{nombre}, elegiste el personaje {personaje} (Tipo MBTI: {mbti})."
        ),
        "arquetipo_cierre": "Recuerda que los arquetipos son patrones universales para comprender el mundo y tomar decisiones más auténticas.",
        "area_ideal": (
            "Según la información recopilada, {nombre}, el área de tecnología ideal para ti dentro de Jung Tech Company es: "
            "{area}, {razon}."
        ),
        "gusto_resultado": "{nombre}, ¿te gustó tu resultado?",
        "test_de_nuevo": "¿Quieres tomar el test de nuevo?",
        "prompt_final": (
            "{tratamiento} postulante {nombre}, has superado la primera etapa de nuestro proceso de selección. "
            "Por favor, confirma tus datos antes de enviar el correo con los detalles de tu postulación."
        ),
        "correo_enviado": "El correo ha sido enviado exitosamente a {correo}. Gracias por participar, {nombre}.",
        "info_correcta": "Sí, toda la información es correcta",
        "modificar_datos": "Corregir un dato",
        "gracias": "Gracias por tu tiempo, {nombre}.",
        "press_enter": "\nPresiona Enter para continuar...",
        "press_enter_arquetipos": "\nPresiona Enter para avanzar a Arquetipos...",
        "press_enter_area": "\nPresiona Enter para ver tu área recomendada...",
        "press_enter_inicio": "\nPresiona Enter para volver al inicio...",
        "select_una_produccion": "{nombre}, selecciona una producción audiovisual para tu evaluación:",
        "datos_verificar": "\nResumen de tus datos de contacto:",
        "fechas_enviadas": "\n[Fechas tentativas enviadas a tu correo para entrevistas (Posteriores al 1 de Agosto de 2026)]:",
        "canal_conversacion_titulo": " CANAL DE CONVERSACIÓN CON JUNG.IA ",
        "canal_conversacion_sub": "Escribe tus dudas sobre tus resultados, puesto o datos registrados..."
    },
    "ENG": {
        "bienvenida": (
            "Hello, my name is Jung.IA.\n"
            "(Note: \"IA\" stands for \"Inteligencia Artificial\", which is Artificial Intelligence in Spanish)\n\n"
            "Today, I am here to inspire you and guide you through a hiring process that is truly out of this world.\n"
            "This is the recruitment process for the Technology Department at Jung Tech Company.\n\n"
            "Today, we will conduct the first stage using Carl Jung's personality framework.\n"
            "We only ask you to be completely honest. Every single personality type is welcome here."
        ),
        "confirmar_datos": "Please enter your personal contact details:",
        "nota_nombres": "(Note: You may enter one or more first names and last names)",
        "input_nombres": "First Name(s) (1 or more): ",
        "input_apellidos": "Last Name(s) (1 or more): ",
        "input_preferido": "What would you prefer us to call you?: ",
        "err_campo_vacio": "[!] This field cannot be empty. Please enter a valid response.",
        "err_solo_letras": "[!] Please enter letters only.",
        "err_solo_numeros": "[!] Only numbers are allowed (no letters, spaces, or symbols). Please try again.",
        "nota_cobertura_tel": "(At the moment we only accept phone numbers from USA and Latin America)",
        "input_prefijo": "Select your country code:",
        "input_num_tel": "Phone number (without country code): ",
        "input_usr_mail": "Email username (before @): ",
        "input_dom_mail": "Select your domain:",
        "nota_correo_otro": (
            "At the moment we only accept applications with email accounts from the listed providers.\n"
            "Please select one of the available domains."
        ),
        "pregunta_datos_correctos": "Is all your information correct?",
        "opt_datos_ok": "Yes, all information is correct",
        "opt_datos_edit": "No, I want to edit an item",
        "lbl_nom": "First Names",
        "lbl_ape": "Last Names",
        "lbl_pref": "Preferred Name",
        "lbl_tel": "Phone",
        "lbl_mail": "Email",
        "menu_corregir": "Which item would you like to edit?",
        "opt_edit_nom": "Edit First / Last / Preferred Names",
        "opt_edit_tel": "Edit Phone (Country Code / Number)",
        "opt_edit_mail": "Edit Email (Username / Domain)",
        "opt_edit_todo": "Edit EVERYTHING again",
        "intro_filtro_series": "The available audiovisual productions for this assessment are:",
        "filtro_series": "{nombre}, have you watched any of these movies or series?:",
        "opt_si": "Yes",
        "opt_no": "No",
        "no_series": (
            "Dear {nombre}, at the moment this AI model is specifically designed to evaluate candidates "
            "through the following productions: Harry Potter, Arrested Development, South Park, and Breaking Bad.\n\n"
            "However, at Jung Tech Company we are genuinely interested in your profile."
        ),
        "pregunta_correo_inmediato": (
            "{nombre}, do you authorize us to send you an email RIGHT NOW to confirm that we have your "
            "information correctly registered in our system?"
        ),
        "opt_auth_mail_si": "Yes, authorize email now",
        "opt_auth_mail_no": "No for now",
        "correo_confirmacion_enviado": (
            "Great, {nombre}! We have sent you a data receipt confirmation email.\n"
            "We will contact you again later with tentative dates to schedule your potential tech interviews."
        ),
        "consentimiento_no": "Understood, {nombre}. We respect your decision and will keep your data confidential.",
        "pregunta_personaje": "{nombre}, which character do you identify with the most?:",
        "confirmar_personaje": "{nombre}, is your character '{personaje}'?",
        "cambiar_serie": "Change series or movie",
        "btn_reiniciar_prueba": "↺ Return to Start of Test (Select another series)",
        "btn_reiniciar_todo_datos": "Oops, I made a mistake: I want to restart EVERYTHING from scratch (incorrect data)",
        "btn_reiniciar_test_personaje": "Oops, wrong character selection / results don't resonate: I want to restart the test",
        "sospecha_texto": "{nombre}, I suspect you are a {mbti} + {desc}.",
        "pregunta_mbti_confirmar": "Do you believe this description represents your personality?",
        "diagnostico_base": "So {nombre}, you are a: {personaje}.\nI sense that you have {mbti_desc}.\nYour dominant function is {fun_dom}.\nYOU KNOW {fun_dom_desc}.",
        "pregunta_genero": "{nombre}, for the next stage, please select your gender:",
        "arquetipo_intro": (
            "An archetype is a universal pattern of personality according to Carl Jung.\n\n"
            "{nombre}, you chose {personaje} (MBTI: {mbti})."
        ),
        "arquetipo_cierre": "Remember that archetypes help us understand ourselves and make more authentic decisions.",
        "area_ideal": (
            "Based on all gathered information, {nombre}, your ideal technology area at Jung Tech Company is: "
            "{area}, {razon}."
        ),
        "gusto_resultado": "{nombre}, did you like your result?",
        "test_de_nuevo": "Do you want to take the test again?",
        "prompt_final": (
            "Dear applicant {nombre}, you have passed stage 1. Please confirm your details before sending the summary email."
        ),
        "correo_enviado": "The email has been sent successfully to {correo}. Thank you, {nombre}.",
        "info_correcta": "Yes, all information is correct",
        "modificar_datos": "Edit an item",
        "gracias": "Thank you for your time, {nombre}.",
        "press_enter": "\nPress Enter to continue...",
        "press_enter_arquetipos": "\nPress Enter to move to Archetypes...",
        "press_enter_area": "\nPress Enter to view recommended area...",
        "press_enter_inicio": "\nPress Enter to return to start...",
        "select_una_produccion": "{nombre}, select one audiovisual production:",
        "datos_verificar": "\nSummary of your contact details:",
        "fechas_enviadas": "\n[Tentative interview dates sent to your email (After August 1, 2026)]:",
        "canal_conversacion_titulo": " OPEN CONVERSATION CHANNEL WITH JUNG.IA ",
        "canal_conversacion_sub": "Type any questions regarding your results, job placement, or contact details..."
    }
}

SERIES_MAP = {
    "Harry Potter": "Serie_Harry_Potter_BOTH",
    "Arrested Development": "Serie_Arrested_Development_BOTH",
    "South Park": "Serie_South_Park_BOTH",
    "Breaking Bad": "Serie_Breaking_Bad_BOTH"
}

RESPUESTAS_UNICAS_ESP = [
    "Comprendo perfectamente tu inquietud, {nombre}. La teoría de Carl Jung muestra que la función {nombre_funcion} ({codigo_funcion}) te ayuda a mantener la adaptabilidad y el balance analítico en tareas de {area}.",
    "Es una excelente pregunta, {nombre}. Como {tratamiento}, apoyarte en la función {nombre_funcion} te permite procesar información compleja con mayor estructura en tus proyectos de software.",
    "En el contexto laboral, {nombre}, la función {nombre_funcion} opera como una herramienta estratégica que previene la sobrecarga cognitiva y optimiza tu rendimiento en {area}.",
    "Qué buena observación, {nombre}. La integración práctica de {codigo_funcion} te brinda un marco claro para tomar decisiones objetivas sin actuar por impulso.",
    "Esa función en particular ({nombre_funcion}), {nombre}, aporta una perspectiva complementaria fundamental que equilibra tu perfil {mbti} dentro del equipo de tecnología."
]

RESPUESTAS_UNICAS_ENG = [
    "I completely understand your question, {nombre}. Carl Jung's framework shows that the function {nombre_funcion} ({codigo_funcion}) provides adaptability and analytical balance for {area}.",
    "That is a great question, {nombre}. As a {tratamiento}, relying on {nombre_funcion} helps you process complex information with better structure in software projects.",
    "In a workplace setting, {nombre}, the function {nombre_funcion} acts as a strategic tool that prevents cognitive overload and optimizes your performance in {area}.",
    "Insightful observation, {nombre}. The practical integration of {codigo_funcion} gives you a clear framework to make objective decisions under pressure.",
    "That specific function ({nombre_funcion}), {nombre}, brings a crucial complementary perspective that balances your {mbti} profile within the tech team."
]

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def formatear_nombre(texto):
    return texto.strip().title() if texto else ""

def es_solo_letras(texto):
    if not texto:
        return False
    texto_sin_espacios = texto.replace(" ", "")
    return texto_sin_espacios.isalpha()

def pedir_solo_letras(prompt_texto, txt_error_vacio, txt_error_letras, obligatorio=True):
    while True:
        entrada = input(prompt_texto).strip()
        if not entrada:
            if obligatorio:
                print(txt_error_vacio)
                continue
            else:
                return ""
        if es_solo_letras(entrada):
            return entrada
        else:
            print(txt_error_letras)

def generar_fechas_tentativas(idioma="ESP"):
    if idioma == "ESP":
        return [
            "Lunes, 3 de Agosto de 2026 - 10:00 AM",
            "Miércoles, 5 de Agosto de 2026 - 03:00 PM",
            "Viernes, 7 de Agosto de 2026 - 11:00 AM"
        ]
    else:
        return [
            "Monday, August 3, 2026 - 10:00 AM",
            "Wednesday, August 5, 2026 - 03:00 PM",
            "Friday, August 7, 2026 - 11:00 AM"
        ]

def enviar_correo_real(destinatario, nombre, resumen_texto, fechas_list, idioma="ESP"):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = destinatario
        asunto = f"Jung Tech Company - Resumen de Postulación de {nombre}" if idioma == "ESP" else f"Jung Tech Company - Application Summary for {nombre}"
        msg['Subject'] = asunto
        fechas_html = "".join([f"<li><b>{f}</b></li>" for f in fechas_list])
        if idioma == "ESP":
            body_html = f"<html><body style='font-family: Arial, sans-serif; color: #333;'><h2>Jung Tech Company</h2><p>Hola <b>{nombre}</b>,</p><p>Resumen: {resumen_texto}</p><ul>{fechas_html}</ul></body></html>"
        else:
            body_html = f"<html><body style='font-family: Arial, sans-serif; color: #333;'><h2>Jung Tech Company</h2><p>Hello <b>{nombre}</b>,</p><p>Summary: {resumen_texto}</p><ul>{fechas_html}</ul></body></html>"
        msg.attach(MIMEText(body_html, 'html'))
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, destinatario, msg.as_string())
        server.quit()
        return True
    except Exception:
        return False

def mostrar_cabecera(serie=None, nombre_usuario=None, idioma="ESP", genero="N"):
    print("=======================================================================")
    if idioma == "ENG":
        print("  Stage 1 of the Selection Process for Jung Tech Company  ")
        print("         In collaboration with the AI Agent: Jung.IA        ")
    else:
        print(" Etapa 1 del Proceso de Selección para la empresa de tecnología Jung Tech Company")
        print("         Con la colaboración del agente de IA: Jung.IA             ")
    print("=======================================================================")
    print("                           [ JUNG TECH COMPANY ]                       ")
    if nombre_usuario:
        print(f" Postulante / Candidate: {formatear_nombre(nombre_usuario)}")
    print("=======================================================================")
    if serie:
        if idioma == "ENG":
            print(f" * Movie or series used for the applicant's personality analysis: {serie} *")
        else:
            art = "del" if genero == "M" else ("de la" if genero == "F" else "de le")
            print(f" * Película o serie que se usó para hacer el análisis de personalidad {art} postulante: {serie} *")
    print("-----------------------------------------------------------------------\n")

def capturar_datos_completos(idioma):
    txt = TEXTOS[idioma]
    print(f"{txt['confirmar_datos']}\n{txt['nota_nombres']}")
    nombres_raw = pedir_solo_letras(txt["input_nombres"], txt["err_campo_vacio"], txt["err_solo_letras"], obligatorio=True)
    apellidos_raw = pedir_solo_letras(txt["input_apellidos"], txt["err_campo_vacio"], txt["err_solo_letras"], obligatorio=True)
    preferido_raw = pedir_solo_letras(txt["input_preferido"], txt["err_campo_vacio"], txt["err_solo_letras"], obligatorio=False)
    
    nombres = formatear_nombre(nombres_raw)
    apellidos = formatear_nombre(apellidos_raw)
    preferido = formatear_nombre(preferido_raw) if preferido_raw else (nombres.split()[0] if nombres.split() else nombres)
    
    print(f"\n{txt['nota_cobertura_tel']}")
    prefijo = inquirer.prompt([inquirer.List('prefijo', message=txt["input_prefijo"], choices=LISTA_PREFIJOS)])['prefijo']
    
    while True:
        numero_local = input(txt["input_num_tel"]).strip()
        if not numero_local:
            print(txt["err_campo_vacio"])
        elif not numero_local.isdigit():
            print(txt["err_solo_numeros"])
        else:
            break
            
    telefono = f"{prefijo} {numero_local}"
    
    while True:
        usr_mail = input(f"\n{txt['input_usr_mail']}").strip().replace("@", "")
        if not usr_mail:
            print(txt["err_campo_vacio"])
            continue
            
        dom_mail = inquirer.prompt([inquirer.List('dom', message=txt["input_dom_mail"], choices=LISTA_DOMINIOS_EMAIL)])['dom']
        if dom_mail == "OTRO":
            print(f"\n[!]{txt['nota_correo_otro']}\n")
            continue
            
        correo = f"{usr_mail}{dom_mail}"
        break
        
    return {
        "nombres": nombres,
        "apellidos": apellidos,
        "preferido": preferido,
        "telefono": telefono,
        "correo": correo
    }

def verificar_y_editar_datos(datos, idioma, genero="N"):
    txt = TEXTOS[idioma]
    while True:
        limpiar_pantalla()
        mostrar_cabecera(nombre_usuario=datos['preferido'], idioma=idioma, genero=genero)
        print(txt["datos_verificar"])
        print(f" 1. {txt['lbl_nom']}: {datos['nombres']}")
        print(f" 2. {txt['lbl_ape']}: {datos['apellidos']}")
        print(f" 3. {txt['lbl_pref']}: {datos['preferido']}")
        print(f" 4. {txt['lbl_tel']}: {datos['telefono']}")
        print(f" 5. {txt['lbl_mail']}: {datos['correo']}")
        print("-" * 60)
        
        pregunta_ok = [
            inquirer.List('ok', message=txt["pregunta_datos_correctos"], choices=[(txt["opt_datos_ok"], "SI"), (txt["opt_datos_edit"], "NO")])
        ]
        if inquirer.prompt(pregunta_ok)['ok'] == "SI":
            return datos
            
        opciones_edicion = [
            (txt["opt_edit_nom"], "NOMBRES"),
            (txt["opt_edit_tel"], "TEL"),
            (txt["opt_edit_mail"], "EMAIL"),
            (txt["opt_edit_todo"], "TODO")
        ]
        campo_elegido = inquirer.prompt([inquirer.List('campo', message=txt["menu_corregir"], choices=opciones_edicion)])['campo']
        
        if campo_elegido == "NOMBRES":
            raw_nom = pedir_solo_letras(f"\n{txt['input_nombres']}", txt["err_campo_vacio"], txt["err_solo_letras"], obligatorio=True)
            raw_ape = pedir_solo_letras(txt["input_apellidos"], txt["err_campo_vacio"], txt["err_solo_letras"], obligatorio=True)
            raw_pref = pedir_solo_letras(txt["input_preferido"], txt["err_campo_vacio"], txt["err_solo_letras"], obligatorio=False)
            datos['nombres'] = formatear_nombre(raw_nom)
            datos['apellidos'] = formatear_nombre(raw_ape)
            datos['preferido'] = formatear_nombre(raw_pref) if raw_pref else (datos['nombres'].split()[0] if datos['nombres'].split() else datos['nombres'])
        elif campo_elegido == "TEL":
            prefijo = inquirer.prompt([inquirer.List('prefijo', message=txt["input_prefijo"], choices=LISTA_PREFIJOS)])['prefijo']
            while True:
                num = input(txt["input_num_tel"]).strip()
                if not num:
                    print(txt["err_campo_vacio"])
                elif not num.isdigit():
                    print(txt["err_solo_numeros"])
                else:
                    break
            datos['telefono'] = f"{prefijo} {num}"
        elif campo_elegido == "EMAIL":
            while True:
                usr_mail = input(f"\n{txt['input_usr_mail']}").strip().replace("@", "")
                if not usr_mail:
                    print(txt["err_campo_vacio"])
                    continue
                dom_mail = inquirer.prompt([inquirer.List('dom', message=txt["input_dom_mail"], choices=LISTA_DOMINIOS_EMAIL)])['dom']
                if dom_mail == "OTRO":
                    print(f"\n[!] {txt['nota_correo_otro']}\n")
                    continue
                datos['correo'] = f"{usr_mail}{dom_mail}"
                break
        elif campo_elegido == "TODO":
            datos = capturar_datos_completos(idioma)

def cargar_matriz():
    try:
        df = pd.read_csv(CSV_PATH)
        df = df.fillna("[Sin Nombre]")
        if len(df) < 16:
            diferencia = 16 - len(df)
            cols = df.columns
            vacias = pd.DataFrame([[f"[Personaje {i+len(df)+1}]" for _ in cols] for i in range(diferencia)], columns=cols)
            df = pd.concat([df, vacias], ignore_index=True)
        return df.iloc[0:16].copy()
    except Exception as e:
        print(f"Error crítico al leer la matriz {CSV_PATH}: {e}")
        sys.exit(1)

def mostrar_menu_16_opciones(df_matriz, col_serie, txt, nombre_call):
    print(f"{txt['pregunta_personaje'].format(nombre=nombre_call)}\n")
    for i in range(16):
        row = df_matriz.iloc[i]
        nombre_personaje = str(row[col_serie]).strip()
        if not nombre_personaje or nombre_personaje == "[Sin Nombre]":
            nombre_personaje = f"Personaje Opción {i+1}"
        print(f"  {i+1:2d}. {nombre_personaje}")
        
    print("\n  Opciones adicionales de navegación:")
    print(f"  17. [ {txt['cambiar_serie']} ]")
    print(f"  18. {txt['btn_reiniciar_prueba']}")
    print(f"  19. {txt['btn_reiniciar_todo_datos']}")
    
    while True:
        eleccion = input("\nIngresa el número de tu opción / Enter option number (1-19): ").strip()
        if eleccion.isdigit():
            num = int(eleccion)
            if 1 <= num <= 16:
                return ("PERSONAJE", num - 1)
            elif num == 17:
                return ("CAMBIAR", None)
            elif num == 18:
                return ("INICIO_PRUEBA", None)
            elif num == 19:
                return ("REINICIAR_TODO", None)
        print(f"[!] {txt['err_campo_vacio']} (Elige un número del 1 al 19)")

def respuesta_ia_pregunta_adicional(tipo_pregunta, nombre_funcion, codigo_funcion, nombre_call, genero_actual, resp_idioma, mbti_val, area_ti, resp_usadas):
    if resp_idioma == "ESP":
        tratamiento = "estimado postulante" if genero_actual == "M" else ("estimada postulante" if genero_actual == "F" else "estimade postulante")
    else:
        tratamiento = "dear candidate"

    if OPENAI_AVAILABLE and OPENAI_API_KEY:
        try:
            client = OpenAI(api_key=OPENAI_API_KEY)
            prompt_usr = f"¿Para qué me sirve mi función cognitiva {nombre_funcion} ({codigo_funcion}) en mi trabajo como {mbti_val} en el área de {area_ti}?"
            sys_prompt = f"Eres Jung.IA, la musa de reclutamiento de Jung Tech Company. Explica brevemente (máximo 2 oraciones) y con tono inspirador la utilidad práctica de esta función."
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": sys_prompt},
                    {"role": "user", "content": prompt_usr}
                ],
                temperature=0.8,
                max_tokens=150
            )
            return completion.choices[0].message.content.strip()
        except Exception:
            pass

    lista_base = RESPUESTAS_UNICAS_ESP if resp_idioma == "ESP" else RESPUESTAS_UNICAS_ENG
    disponibles = [r for r in lista_base if r not in resp_usadas]
    if not disponibles:
        resp_usadas.clear()
        disponibles = list(lista_base)
        
    seleccionada = random.choice(disponibles)
    resp_usadas.append(seleccionada)
    return seleccionada.format(
        nombre=nombre_call, 
        tratamiento=tratamiento, 
        nombre_funcion=nombre_funcion,
        codigo_funcion=codigo_funcion,
        mbti=mbti_val, 
        area=area_ti
    )

def canal_interactivo_agente(nombre_call, genero_actual, resp_idioma, mbti_val, char_nombre, area_ti, razon_ti, arq_val, arq_desc, datos_usr):
    if resp_idioma == "ESP":
        tratamiento = "estimado postulante" if genero_actual == "M" else ("estimada postulante" if genero_actual == "F" else "estimade postulante")
        articulo = "bienvenido" if genero_actual == "M" else ("bienvenida" if genero_actual == "F" else "bienvenide")
    else:
        tratamiento = "dear candidate"
        articulo = "welcome"

    print(f"\nJung.IA: ¡Hola {nombre_call}! Como {tratamiento}, es un honor conversar contigo. Sé {articulo} a este espacio de diálogo.")
    print(f"Jung.IA: He registrado tus resultados: Perfil {mbti_val} ({char_nombre}), Arquetipo '{arq_val}' y recomendación para '{area_ti}'.")
    print("Jung.IA: Puedes hacerme cualquier pregunta sobre tus resultados, puesto o datos registrados.")

    resp_usadas_ia = []
    while True:
        opinion = input(f"\n{nombre_call}: ").strip()
        if not opinion:
            continue
            
        if opinion.lower() in ['exit', 'salir', 'quit', 'no', 'nada']:
            break
            
        op_low = opinion.lower()
        if any(w in op_low for w in ['dato', 'correo', 'email', 'telefono', 'teléfono', 'contacto', 'excel', 'verificar']):
            if resp_idioma == "ESP":
                print(f"\nJung.IA: Verificado, {nombre_call}. Correo registrado: {datos_usr['correo']} | Teléfono: {datos_usr['telefono']}.")
            else:
                print(f"\nJung.IA: Verified, {nombre_call}. Email: {datos_usr['correo']} | Phone: {datos_usr['telefono']}.")
        else:
            respuesta_ia = respuesta_ia_pregunta_adicional(
                "GENERAL", "General", "Jung", nombre_call, genero_actual, resp_idioma, mbti_val, area_ti, resp_usadas_ia
            )
            print(f"\nJung.IA: {respuesta_ia}")
            
        msg_menu = "¿Qué deseas hacer a continuación?" if resp_idioma == "ESP" else "What would you like to do next?"
        opts_cierre = [
            ("💬 Hacer otra pregunta a Jung.IA", "CONTINUAR"),
            ("↺ Volver al Inicio de la Prueba (Seleccionar otra serie)", "REINICIAR_TEST"),
            ("🏁 Finalizar proceso y salir", "SALIR")
        ] if resp_idioma == "ESP" else [
            ("💬 Ask another question to Jung.IA", "CONTINUAR"),
            ("↺ Return to Start of Test (Select another series)", "REINICIAR_TEST"),
            ("🏁 Finish process and exit", "SALIR")
        ]
        
        accion_cierre = inquirer.prompt([inquirer.List('act', message=msg_menu, choices=opts_cierre)])['act']
        if accion_cierre == "REINICIAR_TEST":
            return "REINICIAR_TEST"
        elif accion_cierre == "SALIR":
            despedida = f"\nJung.IA: Entendido, {nombre_call}. ¡Mucho éxito en tu proceso de selección!" if resp_idioma == "ESP" else f"\nJung.IA: Understood, {nombre_call}. Best of luck with your recruitment process!"
            print(despedida)
            return "SALIR"

def ejecutar_agente():
    df_matriz = cargar_matriz()
    while True:
        limpiar_pantalla()
        mostrar_cabecera()
        resp_idioma = inquirer.prompt([inquirer.List('idioma', message="Selecciona tu idioma / Select Language:", choices=[('Español', 'ESP'), ('English', 'ENG')])])['idioma']
        txt = TEXTOS[resp_idioma]
        
        limpiar_pantalla()
        mostrar_cabecera(idioma=resp_idioma)
        print(txt["bienvenida"])
        input(txt["press_enter"])
        
        limpiar_pantalla()
        mostrar_cabecera(idioma=resp_idioma)
        datos_usr = capturar_datos_completos(resp_idioma)
        datos_usr = verificar_y_editar_datos(datos_usr, resp_idioma)
        
        nombre_call = datos_usr['preferido']
        genero_actual = "N"
        
        limpiar_pantalla()
        mostrar_cabecera(nombre_usuario=nombre_call, idioma=resp_idioma)
        print(txt["intro_filtro_series"])
        for prod in PRODUCCIONES_LISTA:
            print(f"  {prod}")
        print()
        
        resp_filtro = inquirer.prompt([inquirer.List('filtro', message=txt["filtro_series"].format(nombre=nombre_call), choices=[(txt["opt_si"], "SI"), (txt["opt_no"], "NO")])])['filtro']
        
        if resp_filtro == "NO":
            limpiar_pantalla()
            mostrar_cabecera(nombre_usuario=nombre_call, idioma=resp_idioma)
            print(txt["no_series"].format(nombre=nombre_call))
            print("-" * 60)
            
            resp_mail_inmediato = inquirer.prompt([inquirer.List('envio_now', message=txt["pregunta_correo_inmediato"].format(nombre=nombre_call), choices=[(txt["opt_auth_mail_si"], "SI"), (txt["opt_auth_mail_no"], "NO")])])['envio_now']
            
            limpiar_pantalla()
            mostrar_cabecera(nombre_usuario=nombre_call, idioma=resp_idioma)
            if resp_mail_inmediato == "SI":
                print(txt["correo_confirmacion_enviado"].format(nombre=nombre_call))
            else:
                print(txt["consentimiento_no"].format(nombre=nombre_call))
                
            print("-" * 60)
            print(f"{txt['gracias'].format(nombre=nombre_call)}")
            input(txt["press_enter_inicio"])
            continue
            
        flujo_activo = True
        reiniciar_todo_el_sistema = False

        while flujo_activo:
            limpiar_pantalla()
            mostrar_cabecera(nombre_usuario=nombre_call, idioma=resp_idioma, genero=genero_actual)
            print(txt["select_una_produccion"].format(nombre=nombre_call))
            
            opciones_series_menu = list(SERIES_MAP.keys()) + [(txt["btn_reiniciar_todo_datos"], "REINICIAR_TODO")]
            serie_elegida = inquirer.prompt([inquirer.List('serie', message="Serie/Movie:", choices=opciones_series_menu)])['serie']
            
            if serie_elegida == "REINICIAR_TODO":
                reiniciar_todo_el_sistema = True
                break
                
            col_serie = SERIES_MAP[serie_elegida]
            
            while True:
                limpiar_pantalla()
                mostrar_cabecera(serie=serie_elegida, nombre_usuario=nombre_call, idioma=resp_idioma, genero=genero_actual)
                
                accion, idx_p = mostrar_menu_16_opciones(df_matriz, col_serie, txt, nombre_call)
                if accion == "REINICIAR_TODO":
                    reiniciar_todo_el_sistema = True
                    flujo_activo = False
                    break
                elif accion == "INICIO_PRUEBA" or accion == "CAMBIAR":
                    break
                    
                fila_datos = df_matriz.iloc[idx_p]
                char_nombre = str(fila_datos[col_serie]).strip()
                
                conf_char = inquirer.prompt([inquirer.List('conf', message=txt["confirmar_personaje"].format(nombre=nombre_call, personaje=char_nombre), choices=[(txt["opt_si"], "SI"), (txt["opt_no"], "NO")])])['conf']
                if conf_char == "NO":
                    continue
                    
                limpiar_pantalla()
                mostrar_cabecera(serie=serie_elegida, nombre_usuario=nombre_call, idioma=resp_idioma, genero=genero_actual)
                
                mbti_val = fila_datos['MBTI_ESP' if resp_idioma == "ESP" else 'MBTI_ENG']
                desc_val = fila_datos['MBTI_DESC_ESP' if resp_idioma == "ESP" else 'MBTI_DESC_ENG']
                
                print(txt["sospecha_texto"].format(nombre=nombre_call, mbti=mbti_val, desc=desc_val))
                print()
                
                conf_mbti = inquirer.prompt([inquirer.List('rep', message=txt["pregunta_mbti_confirmar"], choices=[(txt["opt_si"], "SI"), (txt["opt_no"], "NO")])])['rep']
                if conf_mbti == "NO":
                    continue
                    
                limpiar_pantalla()
                mostrar_cabecera(serie=serie_elegida, nombre_usuario=nombre_call, idioma=resp_idioma, genero=genero_actual)
                
                f_dom = fila_datos['Funcion_Dominante_ESP' if resp_idioma == "ESP" else 'Funcion_Dominante_ENG']
                f_dom_d = fila_datos['Funcion_Dominante_DESC_ESP' if resp_idioma == "ESP" else 'Funcion_Dominante_DESC_ENG']
                print(txt["diagnostico_base"].format(nombre=nombre_call, personaje=char_nombre, mbti_desc=desc_val, fun_dom=f_dom, fun_dom_desc=f_dom_d))
                
                area_ti = fila_datos['Area_TI_Recomendada']
                
                # Función Auxiliar
                f_aux = fila_datos['Funcion_Auxiliar_ESP' if resp_idioma == "ESP" else 'Funcion_Auxiliar_ENG']
                f_aux_d = fila_datos['Funcion_Auxiliar_DESC_ESP' if resp_idioma == "ESP" else 'Funcion_Auxiliar_DESC_ENG']
                while True:
                    opts_aux = [
                        (f"Quiero saber más sobre mi Función Auxiliar ({f_aux})", "SABER_EXCEL"),
                        (f"¿Para qué me sirve la Función Auxiliar en mi trabajo?", "UTILIDAD_IA"),
                        ("Pasar a la siguiente función", "PASAR")
                    ] if resp_idioma == "ESP" else [
                        (f"I want to learn more about my Auxiliary Function ({f_aux})", "SABER_EXCEL"),
                        (f"How does the Auxiliary Function help me at work?", "UTILIDAD_IA"),
                        ("Skip to next function", "PASAR")
                    ]
                    elec_aux = inquirer.prompt([inquirer.List('aux', message=f"\n¿Qué deseas explorar sobre tu Función Auxiliar ({f_aux})?:", choices=opts_aux)])['aux']
                    if elec_aux == "SABER_EXCEL":
                        print(f"\nJung.IA: Tu función auxiliar es {f_aux}. Apoya y equilibra a la función dominante. Tienes la habilidad de {f_aux_d}.")
                    elif elec_aux == "UTILIDAD_IA":
                        resp_ia = respuesta_ia_pregunta_adicional("AUXILIAR", f_aux, "Auxiliar", nombre_call, genero_actual, resp_idioma, mbti_val, area_ti, [])
                        print(f"\nJung.IA: {resp_ia}")
                    elif elec_aux == "PASAR":
                        break
                        
                # Función Terciaria
                f_ter = fila_datos['Funcion_Terciaria_ESP' if resp_idioma == "ESP" else 'Funcion_Terciaria_ENG']
                f_ter_d = fila_datos['Funcion_Terciaria_DESC_ESP' if resp_idioma == "ESP" else 'Funcion_Terciaria_DESC_ENG']
                while True:
                    opts_ter = [
                        (f"Quiero saber más sobre mi Función Terciaria ({f_ter})", "SABER_EXCEL"),
                        (f"¿Para qué me sirve la Función Terciaria en proyectos?", "UTILIDAD_IA"),
                        ("Pasar a la siguiente función", "PASAR")
                    ] if resp_idioma == "ESP" else [
                        (f"I want to learn more about my Tertiary Function ({f_ter})", "SABER_EXCEL"),
                        (f"How does the Tertiary Function serve me in projects?", "UTILIDAD_IA"),
                        ("Skip to next function", "PASAR")
                    ]
                    elec_ter = inquirer.prompt([inquirer.List('ter', message=f"\n¿Qué deseas explorar sobre tu Función Terciaria ({f_ter})?:", choices=opts_ter)])['ter']
                    if elec_ter == "SABER_EXCEL":
                        print(f"\nJung.IA: Tu función terciaria es {f_ter}, lo cual significa que con el tiempo has aprendido a {f_ter_d}.")
                    elif elec_ter == "UTILIDAD_IA":
                        resp_ia = respuesta_ia_pregunta_adicional("TERCIARIA", f_ter, "Terciaria", nombre_call, genero_actual, resp_idioma, mbti_val, area_ti, [])
                        print(f"\nJung.IA: {resp_ia}")
                    elif elec_ter == "PASAR":
                        break
                        
                # Función Inferior
                f_inf = fila_datos['Funcion_inferior_ESP' if resp_idioma == "ESP" else 'Funcion_inferior_ENG']
                f_inf_d = fila_datos['Funcion_inferior_DESC_ESP' if resp_idioma == "ESP" else 'Funcion_inferior_DESC_ENG']
                while True:
                    opts_inf = [
                        (f"Quiero saber más sobre mi Función Inferior ({f_inf})", "SABER_EXCEL"),
                        (f"¿Cómo puedo mejorar mi Función Inferior y áreas de oportunidad?", "UTILIDAD_IA"),
                        ("Pasar a la siguiente sección", "PASAR")
                    ] if resp_idioma == "ESP" else [
                        (f"I want to learn more about my Inferior Function ({f_inf})", "SABER_EXCEL"),
                        (f"How can I improve my Inferior Function and growth areas?", "UTILIDAD_IA"),
                        ("Skip to next section", "PASAR")
                    ]
                    elec_inf = inquirer.prompt([inquirer.List('inf', message=f"\n¿Qué deseas explorar sobre tu Función Inferior ({f_inf})?:", choices=opts_inf)])['inf']
                    if elec_inf == "SABER_EXCEL":
                        print(f"\nJung.IA: Tu función inferior es {f_inf}, dándote la oportunidad de {f_inf_d}.")
                    elif elec_inf == "UTILIDAD_IA":
                        resp_ia = respuesta_ia_pregunta_adicional("INFERIOR", f_inf, "Inferior", nombre_call, genero_actual, resp_idioma, mbti_val, area_ti, [])
                        print(f"\nJung.IA: {resp_ia}")
                    elif elec_inf == "PASAR":
                        break
                        
                # Patrón Loop
                val_loop = fila_datos['Loops-ESP' if resp_idioma == "ESP" else 'Loops-ENG']
                val_loop_d = fila_datos['Loops_DESC_ESP' if resp_idioma == "ESP" else 'Loops_DESC_ENG']
                while True:
                    opts_loop = [
                        (f"Quiero saber más sobre mi patrón de Loop ({val_loop})", "SABER_EXCEL"),
                        (f"¿Cómo puedo salir de mi patrón de Loop cuando estoy bajo estrés?", "UTILIDAD_IA"),
                        ("Finalizar diagnóstico cognitivo", "PASAR")
                    ] if resp_idioma == "ESP" else [
                        (f"I want to learn more about my Loop pattern ({val_loop})", "SABER_EXCEL"),
                        (f"How can I break my Loop pattern when under stress?", "UTILIDAD_IA"),
                        ("Finish cognitive diagnostic", "PASAR")
                    ]
                    elec_loop = inquirer.prompt([inquirer.List('loop', message=f"\n¿Qué deseas explorar sobre tu Patrón de Loop ({val_loop})?:", choices=opts_loop)])['loop']
                    if elec_loop == "SABER_EXCEL":
                        print(f"\nJung.IA: Tu patrón de loop es {val_loop}, lo que significa que {val_loop_d}.")
                    elif elec_loop == "UTILIDAD_IA":
                        resp_ia = respuesta_ia_pregunta_adicional("LOOP", val_loop, "Loop", nombre_call, genero_actual, resp_idioma, mbti_val, area_ti, [])
                        print(f"\nJung.IA: {resp_ia}")
                    elif elec_loop == "PASAR":
                        break
                        
                input(txt["press_enter_arquetipos"])
                
                limpiar_pantalla()
                gen_opts = [("Femenino", "F"), ("Masculino", "M"), ("Neutro", "N")] if resp_idioma == "ESP" else [("Female", "F"), ("Male", "M")]
                genero_actual = inquirer.prompt([inquirer.List('g', message=txt["pregunta_genero"].format(nombre=nombre_call), choices=gen_opts)])['g']
                
                limpiar_pantalla()
                mostrar_cabecera(serie=serie_elegida, nombre_usuario=nombre_call, idioma=resp_idioma, genero=genero_actual)
                
                col_arq = f"Arquetipos_{genero_actual}_{resp_idioma}"
                arq_val = fila_datos[col_arq] if col_arq in fila_datos else fila_datos.get('Arquetipos_F_ESP', '[Arquetipo]')
                arq_desc = fila_datos.get('arquetipos_DESC_ESP', '')
                
                print("\n" + txt["arquetipo_intro"].format(nombre=nombre_call, personaje=char_nombre, mbti=mbti_val))
                if resp_idioma == "ESP":
                    art = "un" if genero_actual == "M" else ("una" if genero_actual == "F" else "une")
                    print(f"Tu arquetipo profesional es {arq_val}.\nEres {art} {arq_desc}.")
                else:
                    print(f"Your workplace archetype is {arq_val}.\nYou are {arq_desc}.")
                print("\n" + txt["arquetipo_cierre"])
                
                input(txt["press_enter_area"])
                
                limpiar_pantalla()
                mostrar_cabecera(serie=serie_elegida, nombre_usuario=nombre_call, idioma=resp_idioma, genero=genero_actual)
                
                razon_ti = fila_datos['razon_Area_ESP' if resp_idioma == "ESP" else 'razon_Area_ENG']
                print(txt["area_ideal"].format(nombre=nombre_call, area=area_ti, razon=razon_ti))
                print("-" * 60)
                
                fb_opts = [(txt["opt_si"], "SI"), (txt["btn_reiniciar_test_personaje"], "REINICIAR_TEST"), (txt["btn_reiniciar_todo_datos"], "REINICIAR_TODO")]
                resp_fb = inquirer.prompt([inquirer.List('fb', message=txt["gusto_resultado"].format(nombre=nombre_call), choices=fb_opts)])['fb']
                
                if resp_fb == "REINICIAR_TODO":
                    reiniciar_todo_el_sistema = True
                    flujo_activo = False
                    break
                elif resp_fb == "REINICIAR_TEST":
                    break
                    
                datos_usr = verificar_y_editar_datos(datos_usr, resp_idioma, genero=genero_actual)
                nombre_call = datos_usr['preferido']
                
                limpiar_pantalla()
                mostrar_cabecera(serie=serie_elegida, nombre_usuario=nombre_call, idioma=resp_idioma, genero=genero_actual)
                
                tratamiento = "Estimado" if genero_actual == "M" else ("Estimada" if genero_actual == "F" else "Estimade")
                if resp_idioma == "ENG":
                    tratamiento = "Dear"
                    
                print(txt["prompt_final"].format(tratamiento=tratamiento, nombre=nombre_call))
                print("-" * 60)
                
                fechas_tentativas = generar_fechas_tentativas(resp_idioma)
                resumen_correo = f"Candidato: {datos_usr['nombres']} {datos_usr['apellidos']}\nPersonaje: {char_nombre}\nMBTI: {mbti_val}\nÁrea: {area_ti}"
                
                enviar_correo_real(datos_usr['correo'], nombre_call, resumen_correo, fechas_tentativas, resp_idioma)
                
                print(txt["correo_enviado"].format(correo=datos_usr['correo'], nombre=nombre_call))
                print(txt["fechas_enviadas"])
                for f in fechas_tentativas:
                    print(f"  • {f}")
                    
                print("\n" + ("=" * 60))
                print(txt["canal_conversacion_titulo"])
                print("=" * 60)
                print(txt["canal_conversacion_sub"])
                
                resultado_agente = canal_interactivo_agente(
                    nombre_call, genero_actual, resp_idioma, mbti_val, char_nombre, area_ti, razon_ti, arq_val, arq_desc, datos_usr
                )
                
                if resultado_agente == "REINICIAR_TEST":
                    break
                else:
                    flujo_activo = False
                    break
                    
            if reiniciar_todo_el_sistema:
                break

if __name__ == "__main__":
    try:
        ejecutar_agente()
    except KeyboardInterrupt:
        print("\n\nProceso interrumpido. ¡Gracias por interactuar con Jung Tech Company!")
        sys.exit(0)