# 💼 Ronald Santos | Portafolio Personal

Este repositorio contiene el código fuente de mi portafolio personal, desarrollado para presentar mi experiencia profesional, proyectos y tecnologías como Backend Developer.

El sitio fue desarrollado con Django, PostgreSQL, Bootstrap y CSS, permitiendo administrar los proyectos dinámicamente mediante Django Admin sin necesidad de modificar el código.


## 🚀 Demo

**Portafolio:** *()*


## ✨ Características

- Presentación profesional.
- Gestión dinámica de proyectos mediante Django Admin.
- Descarga del currículum en PDF.
- Sección de experiencia profesional.
- Tecnologías organizadas por categoría.
- Enlaces a GitHub y demostraciones en video.
- Diseño responsive.
- Base de datos PostgreSQL.


## ⚙️ Instalación

Clonar el repositorio

```bash
git clone https://github.com/Ronsan12/portafolio.git
```

Entrar al proyecto

```bash
cd portafolio
```

Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno virtual

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Crear el archivo `.env`

```env
SECRET_KEY=tu_secret_key
DEBUG=True

DB_NAME=portfolio_db
DB_USER=postgres
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=5432
```

Ejecutar migraciones

```bash
python manage.py migrate
```

Crear superusuario

```bash
python manage.py createsuperuser
```

Iniciar el servidor

```bash
python manage.py runserver
```


## 📂 Estructura del proyecto

```
portafolio/
│
├── core/
├── portfolio/
├── static/
├── media/
├── templates/
├── manage.py
├── requirements.txt
└── .env.example
```


## 📬 Contacto

📧 Email: **ronsan12@outlook.com**

💼 LinkedIn:
https://www.linkedin.com/in/ronsan12

🐙 GitHub:
https://github.com/Ronsan12



## 📄 Licencia

Este proyecto fue desarrollado como portafolio personal con fines académicos y profesionales.