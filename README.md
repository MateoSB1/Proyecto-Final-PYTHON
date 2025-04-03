# **CG Peripherals - Proyecto Django**

![CG Peripherals Banner](https://i.postimg.cc/VYd3cq2L/assets-banner2-CG.jpg)

## **Descripción del Proyecto**

**CG Peripherals** es una aplicación web desarrollada con Django que permite gestionar productos y categorías relacionados con periféricos de gaming. La aplicación incluye funcionalidades como:

- **Gestión de Categorías**: Crear, editar, listar y eliminar categorías.
- **Gestión de Productos**: Crear, editar, listar, ver detalles y eliminar productos.
- **Autenticación de Usuarios**: Registro, inicio de sesión y cierre de sesión de usuarios.
- **Interfaz Responsiva**: Diseño limpio y moderno utilizando Bootstrap 5.
- **Imágenes Online**: Los productos pueden tener imágenes vinculadas desde URLs externas.

La aplicación está diseñada para ser escalable y modular, permitiendo futuras mejoras y la integración de nuevas funcionalidades.

## **Tecnologías Utilizadas**

- **Backend**: Django 5.1.6
- **Frontend**: HTML, CSS (Bootstrap 5), JavaScript
- **Base de Datos**: SQLite
- **Autenticación**: Sistema de autenticación integrado de Django
- **Despliegue**: Compatible con entornos de desarrollo y producción

## **Estructura del Proyecto**

El proyecto sigue una estructura modular organizada en aplicaciones Django:
```
Projects-Python/
├── src/
│   ├── config/ # Configuración global del proyecto Django
│   ├── core/ # Aplicación principal (autenticación, páginas generales)
│   └── producto/ # Aplicación para gestión de productos y categorías
├── manage.py # Script principal para ejecutar comandos Django
├── requirements.txt # Dependencias del proyecto
└── README.md # Documentación del proyecto (este archivo)
```

### Comandos Opcionales y de Ejecución:
- virtualenv venv
- venv\\\Scripts\\\activate
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

### Repositorio del Proyecto:
```bash
   https://github.com/MateoSB1/Proyecto-Final-PYTHON
```

---

_🧑‍💻 Autor Mateo Brancato – Est. Desarrollador Full Stack | **LinkedIn**: https://www.linkedin.com/in/mateobrancatosb1/ | **GitHub**: https://github.com/MateoSB1_
