# Proyecto de Gestión de Tareas

Sistema web de gestión de tareas desarrollado con **Django**, que permite registrar, consultar, editar, cambiar el estado y eliminar tareas.

## 1. Descripción del proyecto

Este proyecto consiste en una aplicación web que facilita la organización y administración de actividades mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar).

Cada tarea contiene un título, una descripción, una fecha de creación y un estado que permite identificar si está pendiente o completada.

## 2. Funcionalidades principales

- **Crear tareas:** registrar nuevas tareas con título y descripción.
- **Consultar tareas:** visualizar las tareas registradas.
- **Editar tareas:** modificar el título y la descripción de una tarea.
- **Cambiar estado:** marcar una tarea como completada o pendiente.
- **Eliminar tareas:** eliminar tareas que ya no sean necesarias.

## 3. Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje de programación |
| Django | Framework de desarrollo web |
| SQLite | Base de datos |
| HTML | Estructura de las páginas |
| Bootstrap 5 | Diseño y estilos de la interfaz |
| Git y GitHub | Control de versiones y trabajo colaborativo |

## 4. Requisitos previos

Para ejecutar el proyecto se necesita:

- Python instalado.
- Git instalado.
- Visual Studio Code u otro editor de código.
- Un navegador web.

## 5. Instalación y configuración

### 5.1. Clonar el repositorio

Abrir una terminal y ejecutar:

```bash
git clone https://github.com/ALLIOS-TK/proyecto-gestion-tareas.git
```

Ingresar a la carpeta del proyecto:

```bash
cd proyecto-gestion-tareas
```

### 5.2. Crear el entorno virtual

En Windows, utilizando PowerShell:

```powershell
python -m venv .venv
```

### 5.3. Activar el entorno virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la ejecución del script, se puede configurar la política para el usuario actual mediante:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### 5.4. Instalar Django

Con el entorno virtual activado, ejecutar:

```powershell
python -m pip install -r requirements.txt
```

### 5.5. Preparar la base de datos

Ejecutar las migraciones para crear las tablas necesarias:

```powershell
python manage.py migrate
```

## 6. Ejecutar el proyecto

Iniciar el servidor de desarrollo:

```powershell
python manage.py runserver
```

Abrir el siguiente enlace en el navegador:

http://127.0.0.1:8000/

Para detener el servidor, utilizar `CTRL + C` en la terminal.

## 7. Ejecutar las pruebas automatizadas

El proyecto incluye pruebas para comprobar las operaciones principales de gestión de tareas.

Ejecutar:

```powershell
python manage.py test
```

Las pruebas verifican:

- Consulta de tareas.
- Registro de tareas.
- Edición de tareas.
- Cambio de estado.
- Eliminación de tareas.

## 8. Estructura del proyecto

```text
proyecto-gestion-tareas/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── gestion_tareas/
│   ├── migrations/
│   ├── templates/
│   │   └── gestion_tareas/
│   │       ├── base.html
│   │       ├── listar.html
│   │       ├── registrar.html
│   │       └── editar.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── .gitignore
├── db.sqlite3
├── manage.py
└── README.md
```

### Descripción de los archivos principales

- `models.py`: define el modelo de datos de las tareas.
- `views.py`: contiene la lógica de las funcionalidades.
- `forms.py`: define el formulario para registrar y editar tareas.
- `urls.py`: establece las rutas de la aplicación.
- `tests.py`: contiene las pruebas automatizadas.
- `templates/`: almacena las páginas HTML.
- `base.html`: contiene la estructura común y la integración de Bootstrap.
- `settings.py`: contiene la configuración general del proyecto.
- `manage.py`: permite ejecutar comandos administrativos de Django.

## 9. Base de datos

El proyecto utiliza SQLite como sistema de gestión de base de datos. Django crea y administra las tablas mediante el sistema de migraciones.

## 10. Interfaz de usuario

La interfaz utiliza Bootstrap 5 para proporcionar un diseño organizado, adaptable a diferentes tamaños de pantalla y con componentes visuales reutilizables.

## 11. Autores

Proyecto académico desarrollado en equipo como actividad de investigación y aplicación práctica del framework Django.