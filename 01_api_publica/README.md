🧑‍💻 Paso 0 – Abrir Visual Studio Code

Abre Visual Studio Code

Haz clic en File → Open Folder

Selecciona la carpeta llamada:

01_api_publica


Abre la terminal integrada:

Ctrl + ñ

o View → Terminal

📌 Todos los comandos siguientes se escriben en la terminal.

🧪 Paso 1 – Crear entorno virtual

Escribe el siguiente comando y presiona Enter:

python -m venv venv


📌 Qué hace esto
Crea una carpeta llamada venv donde se instalarán las dependencias del proyecto.

⚠️ Aquí NO pasa nada más, el comando termina y vuelve a la línea normal.
Eso es correcto.

▶️ Paso 2 – Activar el entorno virtual
En Windows (PowerShell o CMD):
venv\Scripts\activate


Cuando esté activado verás algo así en la terminal:

(venv)


📌 Si NO ves (venv) no continúes.

📦 Paso 3 – Instalar Scrapy

Con el entorno virtual activado, ejecuta:

pip install scrapy


Espera a que termine la instalación.

🏗️ Paso 4 – Crear el proyecto Scrapy

Ejecuta:

scrapy startproject peliculas_publicas


Ahora entra a la carpeta del proyecto:

cd peliculas_publicas


📌 MUY IMPORTANTE
Debes estar en esta carpeta para que Scrapy funcione.

Si escribes:

ls


Debes ver un archivo llamado:

scrapy.cfg

🕷️ Paso 5 – Crear el Spider

Ejecuta el comando:

scrapy genspider peliculas_api ghibliapi.vercel.app


Esto crea el archivo:

peliculas_publicas/spiders/peliculas_api.py

✍️ Paso 6 – Escribir el código del Spider

Abre el archivo:

peliculas_publicas/spiders/peliculas_api.py


Borra todo el contenido

Copia y pega este código:

import scrapy
import json

class PeliculasApiSpider(scrapy.Spider):
    name = "peliculas_api"
    start_urls = ["https://ghibliapi.vercel.app/films"]

    def parse(self, response):
        data = json.loads(response.text)

        for peli in data:
            yield {
                "titulo": peli["title"],
                "director": peli["director"],
                "anio": peli["release_date"],
                "rating": peli["rt_score"]
            }


Guarda el archivo (Ctrl + S)

📌 Aquí Scrapy recibe JSON, no HTML.

▶️ Paso 7 – Ejecutar el Spider

Asegúrate de estar en la carpeta:

peliculas_publicas
