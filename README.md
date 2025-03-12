
# Sistema de Gestión Escolar

Sistema básico de gestión escolar desarrollado con Django. Cumple con los requisitos mínimos de la consigna, enfocándose en el patrón MVT y la herencia de plantillas HTML.

## Características Principales

- **Modelos**:

  - `Alumno`: Representa estudiantes con datos básicos y materias inscritas.
  - `Materia`: Representa asignaturas con descripción y profesor asignado.
  - `Profesor`: Representa docentes con datos básicos.
- **Herencia de Plantillas**:Usa una plantilla base (`base.html`) para mantener consistencia visual entre las páginas.
- **Vistas Simples**:

  - **Inicio (`home`)**: Página principal del sistema.
  - **Detalles (`detalles`)**: Información adicional sobre el sistema.
- **Base de Datos**:
  SQLite como motor de base de datos. Los modelos están definidos pero no manipulados directamente.

## Estructura del Proyecto

```
src/
├── config/          # Configuración global del proyecto
│   ├── settings.py  # Configuración de Django
│   ├── urls.py      # Rutas del proyecto
│   └── wsgi.py      # Configuración WSGI
├── core/            # Aplicación principal
│   ├── models.py    # Definición de los modelos
│   ├── views.py     # Vistas del sistema
│   └── templates/   # Plantillas HTML
│       ├── base.html
│       ├── home.html
│       └── detalles.html
db.sqlite3           # Base de datos SQLite
manage.py            # Archivo principal para ejecutar comandos Django
```


## Tecnologías

- **Django**: Framework web utilizado.
- **SQLite**: Base de datos ligera.
- **HTML**: Plantillas para la interfaz.

## Propósito

Proyecto inicial para un sistema de gestión escolar, buenas prácticas de organización y estructura en Django.
