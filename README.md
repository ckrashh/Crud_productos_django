# Crud_productos_django

## 📝 Descripción  
Este proyecto es una aplicación web sencilla de gestión de productos desarrollada con Django, creada como parte de la evaluación del Módulo 7 del bootcamp de Python de Talento Digital.

Permite realizar operaciones básicas de **CRUD** (Crear, Leer, Actualizar, Eliminar) sobre un catálogo de productos.

---

## 🎯 Objetivos del proyecto  
- Implementar un modelo de datos para productos.  
- Crear vistas para listar, crear, actualizar y eliminar productos.  
- Utilizar formularios de Django para la gestión de datos.  
- Renderizar plantillas HTML para la interacción del usuario.  
- Mostrar buenas prácticas básicas de Django: estructura de proyecto, rutas (URLs), modelos, vistas, formularios, templates.

---

## 🧩 Funcionalidades  
- Listar todos los productos registrados.  
- Ver detalles de un producto específico.  
- Crear un nuevo producto.  
- Editar un producto existente.  
- Eliminar un producto.  
- Validaciones básicas en formularios (por ejemplo, campos obligatorios).  
- Integración simple con base de datos SQLite (por defecto) o la que el usuario elija.

---

## 🚀 Tecnologías utilizadas  
- Python  
- Django  
- HTML / CSS (plantillas básicas)  
- PostgresSQL  
- Git & GitHub (control de versiones)  

---

## 🛠️ Instalación y puesta en marcha  

> Asegúrate de tener instalado Python 3.x y pip en tu máquina.

1. Clona este repositorio:  
   ```bash
   git clone https://github.com/ckrashh/Crud_productos_django.git
   cd Crud_productos_django
Crea (opcional) y activa un entorno virtual:

bash
Copiar código
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
Instala las dependencias de Django:

bash
Copiar código
pip install django
Aplica migraciones para configurar la base de datos:

bash
Copiar código
python manage.py migrate
(Opcional) Carga datos de ejemplo o crea productos manualmente desde el panel de administración o la interfaz.

bash
Copiar código
python manage.py createsuperuser
Inicia el servidor de desarrollo:

bash
Copiar código
python manage.py runserver
Abre en tu navegador la dirección:

cpp
Copiar código
http://127.0.0.1:8000/
📂 Estructura del proyecto
csharp
Copiar código
Crud_productos_django/
├── productos/            ← aplicación Django para el módulo de productos  
│   ├── migrations/       ← migraciones de la BD  
│   ├── templates/        ← plantillas HTML  
│   ├── static/           ← archivos estáticos (CSS, imágenes)  
│   ├── models.py         ← definición del modelo Product  
│   ├── views.py          ← vistas para CRUD  
│   ├── forms.py          ← formularios para producto  
│   ├── urls.py           ← rutas específicas de la app  
│   └── …  
├── db.sqlite3            ← base de datos por defecto  
├── manage.py             ← herramienta de gestión de Django  
├── requirements.txt      ← (opcional) lista de dependencias  
└── README.md             ← este archivo  
📌 Uso básico
Accede a la lista de productos.

Haz clic en “Crear nuevo” para añadir un producto.

Selecciona un producto para ver sus detalles.

Desde la vista de detalle puedes elegir “Editar” o “Eliminar”.

Para edición, el formulario mostrará los campos actuales y luego podrás modificarlos.

Tras eliminación, serás redireccionado a la lista principal.

✅ Buenas prácticas incluidas
Separación de la lógica en vistas, modelos y plantillas.

Utilización de rutas bien definidas para cada operación (listar, crear, editar, eliminar).

Validación de formularios Django.

Uso de entorno virtual para aislar dependencias.

Migraciones automatizadas para la BD.

🧪 Pruebas
Este proyecto está pensado como una prueba de evaluación — no incluye un suite de tests automatizados, pero se recomienda para producción:

Añadir pruebas unitarias para modelos, vistas y formularios.

Usar herramientas como pytest-django para ampliar cobertura.

Aplicar configuración de pruebas en settings.py.

🧭 Mejora futura (roadmap)
Autenticación de usuarios (logueo/registro) y permisos: solo usuarios autenticados pueden crear/editar.

Búsqueda y filtrado de productos.

Paginación en la lista de productos.

Añadir archivos estáticos (imágenes de productos) y subir desde el formulario.

Cambio de base de datos a PostgreSQL para producción.

Deployment a un servidor (Heroku, AWS, etc.).

📄 Licencia
Este proyecto está licenciado bajo MIT License (o especificar la que uses). Puedes usarlo como base para tus propios proyectos.

🙋 Contacto
Para dudas o colaboración puedes contactar con el autor:

GitHub: @ckrashh

¡Gracias por revisar el proyecto!


