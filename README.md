# Proyecto de Registro de Infracciones de Tránsito
Este proyecto permite el manejo de registros de personas, vehículos, oficiales de policía, y la gestión de infracciones de tránsito. A continuación, se describen los pasos para interactuar con la API.

1. Creación de Persona, Vehículo y Oficial
No se requiere autenticación para crear registros de persona, vehículo u oficial. Puedes hacerlo de dos maneras:

Interfaz de Administración de Django:

Accede a http://127.0.0.1:8000/admin/.
Inicia sesión con tu nombre de usuario y contraseña.
Desde aquí, podrás crear, modificar, o eliminar instancias de Persona, Vehículo, u Oficial.
Interfaz de Django Rest Framework:

Accede a http://localhost:8000/.
Usa la interfaz que proporciona Django Rest Framework para crear las instancias.

2. Crear una Infracción (Requiere Autenticación)
Para crear una infracción, debes autenticarte primero obteniendo un token de acceso. Aquí te explico cómo hacerlo utilizando Postman:

Obtener el Token de Acceso
Abre Postman y selecciona una petición de tipo POST.

En el endpoint, ingresa http://localhost:8000/api/token/.

En la pestaña Body, selecciona raw y elige JSON como el tipo de contenido.

Ingresa el siguiente JSON con el nombre de usuario y contraseña:

json
Copiar código
{
  "username": "esteban",
  "password": "esteban"
}
Haz clic en Send.

Recibirás una respuesta similar a esta:

json
Copiar código
{
    "refresh": "token_de_refresco",
    "access": "token_de_acceso"
}
Copia el valor de "access" (el token de acceso).

Crear una Infracción
En Postman, selecciona una nueva petición de tipo POST.

En el endpoint, ingresa http://localhost:8000/infracciones/cargar_infraccion/.

Ve a la pestaña Authorization, selecciona Bearer Token en Auth Type.

Pega el token de acceso en el campo Token.

Ve a la pestaña Body, selecciona raw y JSON, e ingresa el siguiente JSON:

json
Copiar código
{
  "placa_patente": "jpm30b",
  "timestamp": "2024-08-06T12:35:56Z",
  "comentarios": "Exceso de velocidad"
}
Haz clic en Send.

Si todo es correcto, la infracción se guardará en la base de datos y recibirás una respuesta con el código HTTP 201 (Created).

3. Generar Informe de Infracciones
Para obtener un informe de las infracciones asociadas a un correo electrónico específico:

Selecciona una petición de tipo GET en Postman.
En el endpoint, ingresa http://localhost:8000/infracciones/generar_informe/<correo-de-la-persona>/.
Haz clic en Send.
Recibirás un JSON con todas las infracciones registradas para ese correo electrónico.