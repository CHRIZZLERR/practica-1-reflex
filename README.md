# Práctica 1: Creación de tu Primera Página Web con Reflex

## Descripción del proyecto

Este proyecto corresponde a la **Práctica 1: Creación de tu Primera Página Web con Reflex**.

El objetivo principal fue desarrollar una aplicación web básica utilizando el framework **Reflex**, siguiendo como guía la documentación oficial del framework. La aplicación está basada en el ejemplo introductorio del contador interactivo, donde se trabajan conceptos fundamentales como `State`, `event handlers` y componentes visuales.

La página desarrollada incluye un título principal, un texto de bienvenida y botones interactivos que permiten modificar el estado de un contador. Además, se realizó una personalización visual con diseño oscuro, tarjeta central, bordes redondeados y botones con colores diferenciados.

## Objetivos cumplidos

Con este proyecto se trabajaron los siguientes objetivos:

- Familiarizarse con el uso de Reflex para el desarrollo web.
- Comprender la estructura básica de una aplicación web creada con Python.
- Utilizar la documentación oficial de Reflex como guía.
- Aplicar conceptos como `State`, `event handlers` y componentes visuales.
- Usar Git y GitHub para controlar versiones y publicar el proyecto.
- Documentar el proceso realizado durante el desarrollo de la práctica.

## Tecnologías utilizadas

Para el desarrollo del proyecto se utilizaron las siguientes herramientas:

- **Python:** lenguaje utilizado para construir la aplicación.
- **Reflex:** framework utilizado para crear la página web.
- **uv:** herramienta utilizada para administrar el entorno y las dependencias.
- **Git:** sistema de control de versiones utilizado para registrar los avances.
- **GitHub:** plataforma utilizada para publicar el repositorio.
- **Visual Studio Code:** editor utilizado para modificar el código fuente.

## Requisitos previos

Antes de ejecutar este proyecto en otra computadora, se debe tener instalado:

- Python
- Git
- uv

Para verificar si Git está instalado, se puede ejecutar:

```bash
git --version
```

Para verificar si `uv` está instalado, se puede ejecutar:

```bash
uv --version
```

## Instrucciones de instalación

Para instalar el proyecto en cualquier computadora, se deben seguir estos pasos:

### 1. Clonar el repositorio

Abrir una terminal y ejecutar el siguiente comando:

```bash
git clone https://github.com/CHRIZZLERR/practica-1-reflex.git
```

Este comando descargará el código fuente del proyecto desde GitHub.

### 2. Entrar a la carpeta del proyecto

Después de clonar el repositorio, se debe entrar a la carpeta del proyecto:

```bash
cd practica-1-reflex
```

### 3. Instalar o sincronizar las dependencias

El proyecto utiliza `uv` para administrar las dependencias. Para instalar todo lo necesario, se debe ejecutar:

```bash
uv sync
```

Este comando crea o actualiza el entorno del proyecto e instala las dependencias necesarias, incluyendo Reflex.

## Cómo ejecutar la aplicación paso a paso

### 1. Ejecutar la aplicación

Dentro de la carpeta del proyecto, ejecutar el siguiente comando:

```bash
uv run reflex run
```

Este comando inicia el servidor local de Reflex.

### 2. Abrir la página en el navegador

Cuando la aplicación esté corriendo, la terminal mostrará una dirección parecida a esta:

```text
http://localhost:3000
```

Se debe abrir esa dirección en el navegador.

Si Reflex utiliza otro puerto, por ejemplo:

```text
http://localhost:3001
```

se debe abrir la dirección que aparezca en la terminal.

## Funcionalidades de la aplicación

La aplicación permite:

- Visualizar un título principal.
- Leer un texto de bienvenida.
- Incrementar el valor del contador.
- Decrementar el valor del contador.
- Reiniciar el contador a cero.
- Ver el cambio del estado en pantalla al interactuar con los botones.
- Utilizar una interfaz personalizada con diseño oscuro.

## Relación con la documentación oficial de Reflex

La aplicación fue desarrollada siguiendo la documentación oficial de Reflex, especialmente el ejemplo del contador interactivo presentado en la introducción.

En ese ejemplo se explican tres partes principales de una aplicación en Reflex:

- **State:** almacena los datos que pueden cambiar dentro de la aplicación.
- **Event handlers:** son funciones que modifican el estado cuando ocurre una acción del usuario.
- **Components:** son los elementos visuales que forman la interfaz de la página.

En este proyecto se mantuvo esa estructura base y luego se personalizó la interfaz para cumplir con el criterio de creatividad y personalización.

## Estructura básica del proyecto

La estructura principal del proyecto es la siguiente:

```text
practica-1-reflex/
│
├── practica_1_reflex/
│   └── practica_1_reflex.py
│
├── assets/
├── rxconfig.py
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

## Archivo principal

El archivo principal del proyecto es:

```text
practica_1_reflex/practica_1_reflex.py
```

En este archivo se encuentra el código de la página, incluyendo el estado de la aplicación, los eventos del contador y los componentes visuales.

## Control de versiones

Durante el desarrollo del proyecto se realizaron commits en Git para registrar los avances importantes. Esto permitió mantener un historial organizado del proceso, desde la inicialización del proyecto hasta la personalización final de la página.

## Entregables del proyecto

Este proyecto incluye los entregables solicitados en la práctica:

- Código fuente publicado en GitHub.
- Repositorio público.
- Archivo `README.md` con descripción del proyecto, instrucciones de instalación y ejecución paso a paso.
- Documento PDF con la documentación del proceso realizado.

## Autor

Christopher Sánchez
