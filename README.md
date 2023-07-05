# Prueba técnica PymeDesk

## Documentación Backend
Este es el backend de la aplicación simplificada para la gestión de pedidos y clientes de un comercio. Proporciona una API REST desarrollada con Django y Django Rest Framework.

### Requerimientos:
- Django==4.2.2
- django-cors-headers==4.1.0
- django-debug-toolbar==4.1.0
- django-import-export==3.2.0
- djangorestframework==3.14.0
- djangorestframework-simplejwt==5.2.2
- drf-yasg==1.21.6
- python-dotenv==1.0.0

### Configuración:
1. Clona o descaga este repositorio
2. Opcionalmente, crea y activa un entorno virtual de Python para aislar las dependencias del proyecto.
3. Instala las dependencias utilizando el siguiente comando:
    ```
    pip install -r REQUIREMENTS.txt
    ```
4. Crea un archivo .env en la raíz del proyecto y configura las variables de entorno necesarias. Aquí tienes un ejemplo:
    ```
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    INTERNAL_IPS=localhost,127.0.0.1
    SECRET_KEY=tu_clave_secreta
    ```
6. Realiza las migraciones de la base de datos ejecutando el comando:
    ```
    python manage.py migrate
    ```
7. Crea un superusuario para acceder al panel de administración con el comando:
    ```
    python manage.py createsuperuser
    ```
8. (Opcional) Carga datos de prueba predefinidos con el comando:
    ```
    python manage.py loaddata datos_de_prueba.json
    ```
9. Inicia el servidor de desarrollo con el comando:
    ```
    python manage.py runserver
    ```

### Acceso a la documentación de la API:
Puedes acceder a la documentación de la API utilizando Swagger (YASG). Está disponible en las siguientes rutas:
- `/api/docs/`: Documentación interactiva de la API con Swagger UI.
- `/api/docs/.json/`: Documentación de la API en formato JSON.
- `/api/docs/.yaml/`: Documentación de la API en formato YAML.

### Acceso al panel de administrador:
El panel de administración de Django está disponible en la ruta `/admin/`. Puedes iniciar sesión utilizando las credenciales del superusuario que creaste anteriormente.

### Endpoints de la API
- `/pedidos/`:
    - `GET`: Obtiene la lista de todos los pedidos. Admite paginación y filtros.
    - `POST`: Crea un nuevo pedido.
- `/pedidos/{id}/`:
    - `GET`: Obtiene los detalles de un pedido específico.
    - `PUT`: Actualiza todos los campos de un pedido específico.
    - `PATCH`: Actualiza uno o varios campos de un pedido específico.
    - `DELETE`: Elimina un pedido específico.
- `/usuarios/actualizar/{id}/`:
    - `PUT`: Actualiza todos los campos de un usuario específico. Se espera proporcionar el ID del usuario en la URL y enviar los nuevos datos del usuario en el cuerpo de la solicitud.
    - `PATCH`: Actualiza uno o varios campos de un usuario específico. Se espera proporcionar el ID del usuario en la URL y enviar los campos que se desean actualizar en el cuerpo de la solicitud.
- `/usuarios/crear/`
    - `POST`: Crea un nuevo usuario. Se espera enviar los datos del usuario a crear en el cuerpo de la solicitud.
- `/usuarios/eliminar/{id}/`
    - `DELETE`: Elimina un usuario específico. Se espera proporcionar el ID del usuario en la URL.
- `/usuarios/listar/`
    - `GET`: Obtiene la lista de todos los usuarios. Esta solicitud puede admitir paginación y filtros si se desea.
- `/usuarios/listar/{id}/`
    - `GET`: Obtiene los detalles de un usuario específico. Se espera proporcionar el ID del usuario en la URL.
- `/resumen/`:
    - `GET`: Obtiene métricas de resumen del desempeño del comercio, como el número de pedidos, el número de clientes, los ingresos del último mes, la ciudad con más pedidos y el producto más vendido.

Ten en cuenta que los endpoints de `/pedidos/` y `/usuarios/` admiten paginación y filtros para realizar consultas más específicas.

## Documentación Frontend


**¡Gracias por revisar la documentación!** \