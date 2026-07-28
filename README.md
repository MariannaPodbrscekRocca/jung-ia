# 🎪 JUNG.AI: THE CIRCUS OF PERSONALITIES 🎪

> **Link para testear la aplicación (evidencias del despliegue):** [https://jungai.streamlit.app/](https://jungai.streamlit.app/)

> **Sistema Inteligente de Reclutamiento y Diagnóstico Psicométrico según el modelo de Carl Jung**  
> *Diseñado por Marianna Podbrscek Rocca* 

---

<p align="center">
  <img src="https://media.giphy.com/media/HcFKOOXeJ95fFOkTbP/giphy.gif" width="100%" alt="Banner Animado Jung.AI">
</p>

---

## 🌟 Descripción General del Proyecto

**Jung.AI: The Circus of Personalities** es un sistema inteligente, interactivo y bilingüe de reclutamiento y diagnóstico psicométrico impulsado por inteligencia artificial 🤖✨. Ambientado bajo la mágica y vibrante atmósfera de un circo digital 🎪🔮, el sistema transforma el proceso clásico de contratación de la empresa ficticia **Jung Tech Company** en una experiencia totalmente inmersiva y fuera de este mundo. 

La pestaña del navegador cuenta con un **emoji personalizado de una carpa de circo (`🎪`)** que otorga identidad temática desde el primer instante. La aplicación guía a los postulantes a través de una entrevista de trabajo virtual donde seleccionan una producción audiovisual de culto, se identifican con personajes icónicos 🎭, y exploran paso a paso sus funciones cognitivas (dominante, auxiliar, terciaria, inferior), loops cognitivos y arquetipos digitales de Carl Jung. Todo esto culmina en un análisis de compatibilidad con áreas de tecnología y el agendamiento automatizado de una entrevista de Fase 2 con envío de reportes vía correo electrónico 📩✨.

---

## ✨ Características y Funciones Innovadoras Principales

* 🧠 **Diagnóstico Psicométrico Dinámico por IA:** Evaluación automatizada de la tipología de Carl Jung y arquetipos cruzados con la personalidad del candidato, combinando un archivo Excel estructural (`matriz_personalidades.csv`) con generación en tiempo real mediante OpenAI GPT-4o-mini.
* 🤖 **Funcionamiento Inteligente por Secciones y Caja de Texto IA:**
  * **Sección 1:** El agente de IA responde integrando la descripción estática obtenida del archivo `matriz_personalidades.csv` y la cruza dinámicamente con la esencia del personaje elegido.
  * **Secciones 2 y 3:** El sistema utiliza los datos de la matriz junto con el contexto del perfil del postulante para generar análisis profundos sobre luz y sombra profesional.
  * **Caja de Texto Interactiva Personalizada:** Cada sección cuenta con una caja de texto con opción de autocompletado inteligente mediante la tecla `TAB` (utilizando preguntas sugeridas contextuales por fase), permitiendo al usuario plantear cualquier duda libre al agente inteligente y recibir respuestas únicas adaptadas al instante.
* 🌐 **Soporte Bilingüe Nativo en Tiempo Real:** Selector de idioma interactivo en la barra lateral disponible en cualquier momento de la prueba para alternar de forma fluida entre **Español** e **Inglés**.
* 🎨 **Diseño Visual Dinámico y Hover Effects:** Botones estilizados con colores fucsias y dorados vibrantes inspirados en la estética de un circo digital. El botón de **"Siguiente Sección" (Next Section)** destaca de manera prominente, y cuenta con efectos visuales *hover* interactivos al pasar el cursor por encima para mejorar la experiencia de usuario.
* 🔄 **Navegabilidad Interactiva Inteligente y Botones de Retorno ("Oops"):** 
  * Sistema de validación de exploración mediante iconos de **Check Verde (`✅`)** en contraposición a los **Corazones Rotos (`💔`)**, indicando visualmente qué apartados obligatorios debe abrir el postulante para desbloquear el avance.
  * Incorporación de botones especiales de retroceso y corrección denominados **"Oops"** (identificados con emojis específicos como 😕 u 🎪) diseñados de forma intuitiva para que el usuario pueda regresar, cambiar de producción audiovisual, corregir sus datos de registro o resetear el test únicamente cuando sea estrictamente necesario.
* 📧 **Generación y Envío Automatizado de Reportes SMTP:** Sistema de agendamiento de fecha y hora tentativa para la Fase 2 con envío multilingüe de cartas de resultado y temario de entrevista.
* **Sistema de Anclaje DOM Dinámico:** Implementación de un mecanismo avanzado en HTML5/JavaScript que garantiza el retorno automático al tope de la página (`#top-circus-anchor`) en cada cambio de sección o navegación del usuario.

---

## 🏛️ Constitución de la Prueba e Interfaz Web

La interfaz web está construida bajo una arquitectura modular y reactiva en Streamlit. A continuación, se muestra cómo interactúan los elementos visuales y lógicos dentro de la plataforma:

<p align="center">
  <img src="https://raw.githubusercontent.com/MariannaPodbrscekRocca/jung-ia/main/Constitucion_web.png" width="90%" alt="Constitución Web">
</p>

1. **Encabezado Dinámico y Tarjetas de Identificación:** Muestran en tiempo real el nombre del postulante y el personaje de ficción seleccionado.
2. **Sistema de Pestañas y Secciones Obligatorias:** Para avanzar de sección, el postulante debe interactuar con las opciones de lectura y consulta de IA. Los botones muestran **`✅`** al ser explorados o **`💔`** si están pendientes.
3. **Caja de Preguntas Libres a la IA:** Espacio integrado con autocompletado por la tecla `TAB` para plantear inquietudes directamente al agente sabio y compasivo al estilo del Ánima/Ánimus.

---

## 🎥 Demostraciones de Flujo (Video Demos)

### 1. Pantalla de Bienvenida, Idioma y Colores Vibrantes
* **Descripción:** Se muestra la interfaz inicial bajo la carpa del circo digital con el banner de bienvenida de Jung.AI. Los botones cuentan con colores vibrantes y efectos de realce visual al pasar el cursor (*hover effects*). Se incluye también el selector de idioma para cambiar dinámicamente entre español e inglés.
* [🎬 Ver Demostración en Video: Botones y Colores Vibrantes](https://github.com/MariannaPodbrscekRocca/jung-ia/blob/main/Video_demos/botones_colores_vibrantes.mp4)
* [🎬 Ver Demostración en Video: Menú Español / English](https://github.com/MariannaPodbrscekRocca/jung-ia/blob/main/Video_demos/English_Spanish_Menu%20(1).mp4)

---

### 2. Registro de Datos del Candidato (`nombre_apellido_opcional_sexo.mp4` y `telefono_mail.mp4`)
* **Descripción Detallada:** 
  * En `nombre_apellido_opcional_sexo.mp4`, se explica cómo el sistema solicita el nombre y los apellidos obligatorios, un nombre preferido de uso opcional para que el sistema se dirija al postulante de forma personalizada, y la selección de género mediante un menú desplegable adaptado.
  * En `telefono_mail.mp4`, se detalla la validación estricta de credenciales: el usuario selecciona su prefijo telefónico internacional (ej. `+57`, `+1`, etc.) e ingresa su número depurando espacios en blanco de forma automática. Del mismo modo, en el apartado de correo electrónico, el usuario escribe su usuario antes del símbolo `@` y selecciona el dominio corporativo o de proveedor en un menú desplegable (`@gmail.com`, `@outlook.com`, etc.), asegurando un formato unificado y limpio.
* [🎬 Ver Demostración en Video: Nombres, Apellidos y Género](https://github.com/MariannaPodbrscekRocca/jung-ia/blob/main/Video_demos/nombre_apellido_opcional_sexo.mp4)
* [🎬 Ver Demostración en Video: Teléfono y Correo Electrónico](https://github.com/MariannaPodbrscekRocca/jung-ia/blob/main/Video_demos/telefono_mail.mp4)

---

### 3. Selección de Producción Audiovisual, Personaje y Botones de Retorno ("Oops")
* **Descripción:** Selección de series y películas (*Harry Potter*, *Breaking Bad*, etc.) con un banco dinámico de 16 arquetipos de personalidad. Se aprecian en acción los botones de retroceso o redirección "Oops" (como `Oops, ingresé mal mis datos, quiero regresar al menú anterior` o `Oops, no conozco ninguna de estas películas o series`), diseñados con emojis específicos para garantizar la máxima intuición en caso de que el usuario necesite corregir algo.
* [🎬 Ver Demostración en Video: Botones de Regreso y Oops](https://github.com/MariannaPodbrscekRocca/jung-ia/blob/main/Video_demos/botones_de_regreso.mp4)
* [🎬 Ver Demostración en Video: Oops al no identificarse](https://github.com/MariannaPodbrscekRocca/jung-ia/blob/main/Video_demos/oops_no_me_identifico.mp4)

---

### 4. Evaluación de Funciones Cognitivas, Loops, Arquetipos y Controles Interactivos
* **Descripción:** El núcleo de la prueba interactiva. Se detalla el uso de las opciones 1, 2 y 3. La *Opción 1* extrae y procesa información estática directamente del archivo matriz en Excel (`matriz_personalidades.csv`), mientras que las *Secciones 2 y 3* cruzan dicha matriz con los datos del perfil y respuestas anteriores del usuario para generar un análisis de IA un poco más libre pero estrictamente controlado. Asimismo, se evidencia la diferencia visual entre los checks verdes (`✅`) y los corazones rotos con titileo (`💔`) que exigen completar la exploración de botones antes de avanzar.
* [🎬 Ver Demostración en Video: Opciones 1, 2 y 3](https://github.com/MariannaPodbrscekRocca/jung-ia/blob/main/Video_demos/opciones_1_2_y_3.mp4)
* [🎬 Ver Demostración en Video: Detalle Opción 1 y Excel](https://github.com/MariannaPodbrscekRocca/jung-ia/blob/main/Video_demos/opcion_1.mp4)
* [🎬 Ver Demostración en Video: Checks Verdes vs Corazones Rotos](https://github.com/MariannaPodbrscekRocca/jung-ia/blob/main/Video_demos/check_vs_corazones.mp4)
* [🎬 Ver Demostración en Video: Soporte de Inglés en cualquier momento](https://github.com/MariannaPodbrscekRocca/jung-ia/blob/main/Video_demos/Ingles_en_cualquier_momento.mp4)

---

### 5. Resultado Final, Verificación de Datos y Envío Automatizado por Correo
* **Descripción:** Revelación del área tecnológica recomendada, verificación final de los datos del postulante, selección de horario para la entrevista de Fase 2, opción de resetear ante desacuerdo con el perfil mediante el botón Oops, y el proceso de envío SMTP del reporte multilingüe. Cuando el correo es enviado con éxito al buzón del candidato, se visualiza en la carpeta de recibidos del postulante un mensaje formal con la carpa del circo, el saludo personalizado según su género, el rol asignado (*Product Management*, etc.), el horario agendado y el compendio completo de todas las reflexiones e interacciones sostenidas con la IA durante la entrevista virtual.

* **Banner y Vistas de Éxito del Envío:**
<p align="center">
  <img src="https://raw.githubusercontent.com/MariannaPodbrscekRocca/jung-ia/main/banner.png" width="90%" alt="Banner Éxito Correo">
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/MariannaPodbrscekRocca/jung-ia/main/no_conforme_resultado.png" width="90%" alt="Resultado No Conforme">
</p>

* [🎬 Ver Demostración en Video: Explicación Final y Resultado](https://github.com/MariannaPodbrscekRocca/jung-ia/blob/main/Video_demos/explicacion_final.mp4)
* [🎬 Ver Demostración en Video: Envío Automatizado de Correo (SMTP)](https://github.com/MariannaPodbrscekRocca/jung-ia/blob/main/Video_demos/email.mp4)

---

## 🛠️ Explicación Técnica y Tecnologías Utilizadas

* **Python & Streamlit:** Base de la aplicación web reactiva y gestión robusta de estados de sesión (`st.session_state`).
* **OpenAI API (`gpt-4o-mini`):** Motor de inteligencia artificial encargado de generar respuestas reflexivas, equilibrando la luz y la sombra de los perfiles junguianos en un solo párrafo fluido y compasivo.
* **Pandas:** Procesamiento y lectura de la matriz psicométrica estructurada en `matriz_personalidades.csv`.
* **SMTP & EmailMime:** Automatización del backend para la distribución multilingüe de correos electrónicos con plantillas HTML personalizadas.
* **HTML5 / CSS3 / JavaScript:** Estilos personalizados oscuros con temática de circo digital, animaciones fluidas, efectos *hover* en botones y anclaje DOM dinámico.
