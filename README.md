🎪 JUNG.IA: Sistema Inteligente de Reclutamiento y Diagnóstico Psicométrico 🧠✨
Desarrollado para Jung Tech Company en colaboración con el agente de inteligencia artificial Jung.IA. 🤖💼

Alumna: Marianna Podbrscek Rocca

📋 1. Descripción General y Propósito del Proyecto
Jung.IA es un software híbrido avanzado de reclutamiento y selección de personal diseñado específicamente para el área tecnológica. Su objetivo principal es automatizar la Etapa 1 del proceso de selección, evaluando a los candidatos a través de un test psicométrico riguroso fundamentado en la tipología de personalidades de Carl Gustav Jung y el marco tipológico MBTI, entrelazado dinámicamente con franquicias de cultura pop seleccionadas (Harry Potter, Arrested Development, South Park y Breaking Bad). El sistema cuenta con una arquitectura de más de 1000 líneas que unifica una consola interactiva robusta y una interfaz visual basada en la estética de un circo retro.

🌟 2. Resumen Completo de Características y Funciones Técnicas del Código (agente.py)
El script maestro concentra una lógica backend muy robusta y detallada, estructurada a través de las siguientes funciones y componentes clave:

🌍 Estructura Bilingüe Nativa (Español / Inglés):

Se migró la totalidad de los mensajes del sistema, prompts de entrada y etiquetas de navegación a un diccionario centralizado (TEXTOS).

Se corrigieron las inconsistencias de idioma en los mensajes de transición de consola (por ejemplo, Press Enter to continue..., Displaying illustrative images..., Data to verify:), asegurando que la experiencia en inglés sea 100% fluida de principio a fin, incluyendo una aclaración amigable sobre las siglas "IA" (Artificial Intelligence).

🎨 Integración del Mecanismo de Despliegue Visual:

Se incorporó la función auxiliar desplegar_imagen(), la cual interactúa directamente con el sistema operativo para abrir vistas previas de imágenes e ilustraciones (personajes y arquetipos) en el visor predeterminado o navegador web durante las fases de presentación y selección.

📊 Gestión de Personalidades y Matriz Junguiana:

Se aseguró la lectura estricta y limpia de las 16 filas correspondientes a los tipos de personalidad del MBTI dentro de matriz_personalidades.csv, evitando recortes por celdas vacías y mapeando de forma dinámica las 4 series del sistema sin mostrar números en pantalla para mantener una interfaz elegante.

👥 Reglas de Género, Arquetipos y Tratamiento Inclusivo:

Se programó la lógica de concordancia gramatical según el género seleccionado (Femenino, Masculino o Neutro), aplicando la exclusión del género neutro en el flujo en inglés para respetar la estructura formal del idioma.

Una vez que el candidato ingresa su nombre preferido de trato, la Musa Jung.IA lo utiliza de manera activa y personalizada en todas las pantallas y confirmaciones siguientes.

📞 Captura Avanzada y Validación de Datos de Contacto:

Nombres y Apellidos Múltiples: Permite ingresar uno o más nombres y apellidos, formateándolos automáticamente en mayúsculas iniciales (Title Case).

Selector de Prefijos Telefónicos (inquirer): Menú interactivo con el código de Estados Unidos (+1), República Dominicana dividida en sus 3 prefijos oficiales (+1-809, +1-829, +1-849) y los principales países de Latinoamérica. Incluye una nota aclaratoria sobre la cobertura actual de la convocatoria.

Dominio de Correo Inteligente (inquirer): El usuario escribe únicamente su nombre de usuario y selecciona su proveedor de una lista desplegable con los 10 dominios más comunes (@gmail.com, @hotmail.com, @outlook.com, @yahoo.com, etc.), o elige "Otro / Other" con un aviso de validación.

🔍 Sistema Modular de Confirmación y Submenú Granular de Edición:

Al capturar la información, el sistema pregunta: "¿Tus datos están correctos?". Si la respuesta es negativa, despliega un submenú para corregir selectivamente solo nombres, solo teléfono, solo correo o reiniciar todo desde cero.

🚪 Flujo Optimizado para Postulantes que NO han visto las Series:

Si el usuario responde que no ha visto ninguna de las 4 franquicias, se le explican los motivos amablemente, se le solicita su autorización explícita para ser contactado por correo o teléfono para entrevistas alternativas, y se simula el despacho de una confirmación oficial.

🔄 Mecanismos de Rescate, Canal Abierto y Botones de Retorno:

Se integró en todas las pantallas la opción permanente de retorno y reinicio para permitir cambiar de serie, reintentar el test o volver al inicio ante cualquier error.

Al finalizar, se abre un canal de conversación interactivo con la Musa Jung.IA y un módulo de simulación de envío de correos HTML corporativos con fechas tentativas de entrevista.

🏛️ 3. Arquitectura del Repositorio y Componentes
El proyecto está distribuido de manera modular para separar responsabilidades:

🐍 agente.py: El motor principal del sistema (núcleo lógico, procesamiento con Pandas, flujos de consola y bloques de interfaz web en Gradio).

🎨 styles.css: Hoja de estilos personalizada que otorga la identidad visual y el diseño estético de carpa digital / circo retro a la aplicación web.

📊 matriz_personalidades.csv: Base de datos estructurada con las 16 filas exactas del MBTI, arquetipos y recomendaciones de tecnología para los perfiles TI.

🌐 index.html: Archivo de vista previa visual complementario. (Nota: Se añadió con el propósito específico de permitir una revisión rápida y directa mediante la extensión Live Server de Visual Studio Code, facilitando la visualización del diseño gráfico de forma estática, dado que el script principal en Python supera las 1000 líneas de código y requiere un entorno local específico).

🚀 4. Instrucciones de Ejecución y Visualización
Para comprobar el correcto funcionamiento y la estética de Jung.IA, dispones de dos alternativas prácticas:

🌟 Opción A: Vista Previa Visual Rápida (Ideal para revisión gráfica inmediata con Live Server)
Como el archivo principal en Python (agente.py) contiene una estructura avanzada de más de 1000 líneas que combina consola y servidor web, puedes revisar la interfaz gráfica de forma inmediata sin necesidad de correr scripts masivos:

Abre la carpeta del proyecto en Visual Studio Code.

Asegúrate de tener instalada la extensión Live Server en tu editor.

Haz clic derecho sobre el archivo index.html y selecciona "Open with Live Server". Esto abrirá instantáneamente una pestaña en tu navegador web mostrando la estructura visual y los enlaces al diseño CSS del circo digital.
