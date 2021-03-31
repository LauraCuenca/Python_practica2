categorias= """
tecnologías ptive
Software artístico
Comunicaciones

    BBS
    Chat
        ICQ
        Internet Relay Chat
        Charla Unix 
    Conferencias
    Correo electrónico
        Directorio
        Clientes de correo electrónico (MUA)
        Filtros
        Agentes de transporte de correo
        Servidores de listas de correo
        Oficina de correos
            IMAP
            POP3 
    FIDO
    Fax
    Compartición de archivos
        Gnutella 
    Radioaficionado
    Teléfono de Internet
    Telefonía
    Noticias de Usenet 

Base de datos

    Motores / servidores de bases de datos
    Frente termina 

Entorno de escritorio

    Administradores de archivos
    GNUstep
    Gnomo
    Entorno de escritorio K (KDE)
    Protectores de pantalla
    Administradores de ventanas
        Caja negra
        Fluxbox
        XFCE 

Documentación

    Esfinge 

Educación

    Instrucción asistida por computadora (CAI)
    Pruebas 

Juegos / Entretenimiento

    Arcada
    Juegos de mesa
    Juegos de disparos en primera persona
    Galletas de la fortuna
    Mazmorras multiusuario (MUD)
    Rompecabezas
    Estrategia en tiempo real
    Juego de rol
    Juegos de desplazamiento lateral / arcade
    Simulación
    Estrategia por turnos 

Automatización del hogar
Internet

    Protocolo de transferencia de archivos (FTP)
    Dedo
    Análisis de registros
    Servicio de nombres (DNS)
    Servidores proxy
    WAP
    WWW / HTTP
        Navegadores
        Contenido dinámico
            Herramientas / Bibliotecas CGI
            Sistema de gestión de contenidos
            Pizarrón de mensajes
            Noticias / Diario
            Contadores de páginas
            Wiki 
        Servidores HTTP
        Indexación / Búsqueda
        Sesión
        Manejo de sitio
            Verificación de enlaces 
        WSGI
            Solicitud
            Middleware
            Servidor 
    XMPP
    Z39.50 

Multimedia

    Gráficos
        modelado 3D
        Representación 3D
        Capturar
            Cámara digital
            Escáneres
            La captura de pantalla 
        Editores
            Basado en ráster
            Basado en vectores 
        Conversión de gráficos
        Presentación
        Espectadores 
    Sonido / Audio
        Análisis
        CD de audio
            Reproducción de CD
            Extracción de CD
            Escritura de CD 
        Captura / Grabación
        Conversión
        Editores
        MIDI
        Mezcladores
        Jugadores
            MP3 
        Síntesis de sonido
        Discurso 
    Video
        Capturar
        Conversión
        Monitor
        Editor no lineal 

Oficina / Negocio

    Financiero
        Contabilidad
        Inversión
        Punto de venta
        Hoja de cálculo 
    Groupware
    Noticias / Diario
    Suites de oficina
    Planificación 

Otro tema no incluido en la lista
Impresión
Religión
Científico / Ingeniería

    Inteligencia artificial
    Vida artificial
    Astronomía
    Ciencia atmosférica
    Bioinformática
    Química
    Automatización de diseño electrónico (EDA)
    SIG
    Interfaces hombre-máquina
    Hidrología
    Procesamiento de imágenes
    Reconocimiento de imagen
    Análisis de información
    Motor de interfaz / Traductor de protocolos
    Matemáticas
    Aplicaciones de ciencia médica.
    Física
    Visualización 

Seguridad

    Criptografía 

Sociología

    Genealogía
    Historia 

Desarrollo de software

    Ensambladores
    Seguimiento de errores
    Herramientas de construcción
    Generadores de código
    Compiladores
    Depuradores
    Desmontadores
    Documentación
    Sistemas embebidos
    Internacionalización
    Intérpretes
    Bibliotecas
        Marcos de aplicación
        Bibliotecas Java
        Clases PHP
        Módulos Perl
        Módulos Pike
        Módulos de Python
        Módulos Ruby
        Extensiones Tcl
        pygame 
    Localización
    Intermediación de objetos
        CORBA 
    Preprocesadores
    Seguro de calidad
    Pruebas
        Aceptación
        BDD
        Burlón
        Generación de tráfico
        Unidad 
    Interfaces de usuario
    Control de versiones
        Bazar
        CVS
        Git
        Mercurial
        RCS
        SCCS 
    Conjuntos de widgets 

Sistema

    Archivar
        Respaldo
        Compresión
        Reflejando
        embalaje 
    Punto de referencia
    Bota
        En eso 
    Agrupación
    Fuentes de consola
    Computación distribuída
    Emuladores
    Sistemas de archivos
    Hardware
        Controladores de hardware
        Mainframes
        Procesamiento múltiple simétrico
        Bus serie universal (USB) 
    Instalación / Configuración
    Inicio sesión
    Supervisión
    Redes
        Cortafuegos
        Supervisión
            Perro guardián de hardware 
        Sincronización de tiempo 
    Sistema operativo
    Núcleos del sistema operativo
        BSD
        GNU Hurd
        Linux 
    Energía (UPS)
    Herramientas de recuperación
    Conchas
    distribución de software
    Carcasas del sistema
    Administración de sistemas
        Autenticación / Directorio
            LDAP
            NIS 

Terminales

    De serie
    Telnet
    Emuladores de terminal / Terminales X 

Editores de texto

    Documentación
    Emacs
    Entornos de desarrollo integrados (IDE)
    Procesamiento de texto
    Procesadores de palabras 

Procesamiento de texto

    Filtros
    Fuentes
    General
    Indexación
    Lingüístico
    Margen
        HTML
        Látex
        Reducción
        SGML
        VRML
        XML
        reStructuredText 

Utilidades 
"""
#¿Conoces Pypi? Es un sitio con gran variedad de librerías que podés instalar libremente a
#través de la herramienta pip. Te permite buscar proyectos según el área de interés. Queremos
#procesar esta lista de categorías como un string para poder saber las subcategorías tiene cada
#una. Copia el contenido del archivo categorias como contenido de una variable string para
#poder obtener información de la cantidad de subcategorías y la lista que incluye cada
#categoría.
#Nota: no es necesario diferenciar las subcategorías que se encuentren anidadas.
#Ejemplo: De la categoría ‘Communications’ hay 23 subcategorías, y se debe contar con la lista
#que se encuentran dentro de la misma.
#‘Communications’:
#‘cant’: 23,
#‘nombres’:
#‘BBS’,
#‘Chat’,
#‘ICQ’,
#‘Internet Relay Chat’,
#……

def crear_diccionario():
     """ Funcion para crear el diccionario"""
     categorias= {}
     subcategoria= []
     for palabra in categorias:
         if palabra[0] != (' '):
            categorias[palabra]= subcategorias
         while palabra.startswith(' '):
             subcategoria.append(palabra)
     return categorias

categorias= categorias.split(" ") 
cat_completa= (crear_diccionario())   
