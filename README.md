# 🍜 Niko-Niko

**Niko-Niko** es una aplicación web desarrollada con Django que ofrece una experiencia culinaria centrada en la cocina japonesa y asiática. El nombre "Niko-Niko" (にこにこ) significa "sonriente" en japonés, reflejando la alegría y calidez que se experimenta al cocinar y compartir comida.

## 📋 Descripción del Proyecto

Niko-Niko es una plataforma web que presenta recetas de cocina japonesa tradicional y moderna, diseñada para ser accesible tanto para principiantes como para cocineros experimentados. La aplicación incluye:

- **Recetas destacadas**: Desde clásicos como Ramen Tonkotsu hasta postres como el Brazo de Gitano de Matcha
- **Múltiples categorías**: Fideos, aperitivos, platos principales, sopas y postres
- **Valoraciones de usuarios**: Opiniones y calificaciones de la comunidad
- **Preguntas frecuentes (FAQs)**: Información útil sobre ingredientes, dificultad y tipos de recetas

## 🏗️ Estructura del Proyecto

El proyecto está organizado siguiendo la arquitectura estándar de Django:

```
Niko-Niko/
├── config/                 # Configuración principal del proyecto Django
│   ├── settings.py        # Configuración de la aplicación
│   ├── urls.py            # URLs principales
│   └── wsgi.py            # Configuración WSGI
├── niko_niko/             # Aplicación principal
│   ├── views.py           # Lógica de vistas y datos de recetas
│   ├── urls.py            # URLs de la aplicación
│   ├── models.py          # Modelos de datos (actualmente sin modelos DB)
│   ├── static/            # Archivos estáticos (CSS, imágenes)
│   └── templates/         # Plantillas HTML
├── templates/             # Plantillas base y componentes compartidos
├── static/                # Archivos estáticos globales
├── manage.py              # Script de gestión de Django
├── requirements.txt       # Dependencias del proyecto
└── db.sqlite3             # Base de datos SQLite
```

## 🔧 Tecnologías Utilizadas

- **Django 6.0.1**: Framework web de Python
- **SQLite**: Base de datos (incluida por defecto con Django)
- **HTML5/CSS3**: Frontend con diseño responsive
- **Python 3.x**: Lenguaje de programación backend

## 🚀 Instalación y Despliegue

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Entorno virtual (recomendado)

### Paso 1: Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/Niko-Niko.git
cd Niko-Niko
```

### Paso 2: Crear y Activar Entorno Virtual

**En Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**En Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**En Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Configurar la Base de Datos

```bash
python manage.py migrate
```

### Paso 5: (Opcional) Crear Superusuario

Para acceder al panel de administración de Django:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear un usuario administrador.

## ▶️ Cómo Arrancar el Proyecto

### Modo Desarrollo

1. Asegúrate de que el entorno virtual está activado
2. Ejecuta el servidor de desarrollo:

```bash
python manage.py runserver
```

3. Abre tu navegador y visita:
   - Aplicación principal: `http://127.0.0.1:8000/niko-niko/`
   - Página de inicio: `http://127.0.0.1:8000/niko-niko/home/`
   - Panel de administración: `http://127.0.0.1:8000/admin/`

### Detener el Servidor

Presiona `Ctrl + C` en la terminal donde se ejecuta el servidor.

## 📁 Rutas Disponibles

- `/niko-niko/` o `/niko-niko/home/` - Página principal con recetas destacadas
- `/niko-niko/recipe/` - Página de recetas
- `/niko-niko/about/` - Página "Acerca de"
- `/niko-niko/faqs/` - Preguntas frecuentes
- `/admin/` - Panel de administración de Django

## 🎨 Características Principales

### Página Principal (Home)

- **Hero section**: Bienvenida visual con imagen de fondo
- **Recetas destacadas**: Selección aleatoria de 3 recetas de la colección
- **Valoraciones**: 3 testimonios aleatorios de usuarios
- **FAQs**: 4 preguntas frecuentes seleccionadas aleatoriamente

### Datos de Ejemplo

El proyecto incluye datos de ejemplo hardcodeados en `views.py`:
- 6 recetas completas con imágenes, tiempos y porciones
- 10 valoraciones de usuarios con calificaciones de estrellas
- 7 preguntas frecuentes sobre la plataforma

## 🛠️ Desarrollo

### Agregar Nuevas Recetas

Actualmente, las recetas están definidas en `niko_niko/views.py` en la lista `RECIPES`. Para agregar una nueva receta:

1. Abre [niko_niko/views.py](niko_niko/views.py)
2. Añade un nuevo diccionario a la lista `RECIPES` con la estructura:

```python
{
    'id': 7,
    'title': 'Nombre de la Receta',
    'category': 'Categoría',
    'description': 'Descripción breve',
    'image': 'img/nombre-imagen.jpg',
    'time': 'Tiempo de preparación',
    'servings': 'Número de raciones'
}
```

### Modificar Estilos

Los estilos CSS están organizados en:
- `static/css/` - Estilos globales (header, footer, colores, etc.)
- `niko_niko/static/css/` - Estilos específicos de la aplicación

## 📝 Notas Importantes

- El proyecto está configurado con `DEBUG = True`, lo cual es solo para desarrollo
- La `SECRET_KEY` está expuesta en el código, debe cambiarse en producción
- Los datos son estáticos (no se guardan en base de datos), ideales para prototipo/demo
- Las imágenes de las recetas deben estar en `niko_niko/static/img/`

## 🔒 Seguridad para Producción

Antes de desplegar en producción:

1. Cambia `DEBUG = False` en `config/settings.py`
2. Genera una nueva `SECRET_KEY` segura
3. Configura `ALLOWED_HOSTS` con tu dominio
4. Usa una base de datos más robusta (PostgreSQL, MySQL)
5. Configura archivos estáticos con `collectstatic`
6. Implementa HTTPS
7. Considera usar variables de entorno para configuración sensible

## 🤝 Contribuciones

Este proyecto es un prototipo educativo. Si deseas contribuir:

1. Haz un fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Añade nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👨‍💻 Autor

Desarrollado como proyecto de aprendizaje de Django.

---

**¡Disfruta cocinando con Niko-Niko! 🍱**
