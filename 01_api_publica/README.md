
Eso es TODO.  
Ahora lo aplicamos a tu proyecto de Scrapy.

---

# 🟢 README EJEMPLO COMPLETO  
## (Escenario 1 – API pública sin API key)

📄 **Archivo:** `01_api_publica/README.md`

👉 **Copia TODO esto tal cual**:

---

# Escenario 1 – Scraping con API pública (sin API key)

En este escenario se muestra cómo usar **Scrapy** para consumir una **API pública**
que no requiere autenticación.  
Los datos se obtienen directamente en formato **JSON**, sin necesidad de scrapear HTML.

---

## 📌 ¿Qué se aprende en este escenario?

- Qué es una API pública
- Cómo Scrapy puede consumir APIs
- Cómo convertir respuestas JSON en datasets
- Diferencia entre API y scraping HTML

---

## 🛠️ Requisitos

Antes de comenzar necesitas:

- Python 3 instalado
- Visual Studio Code
- Conexión a internet

---

## 📁 Paso 1: Crear la carpeta del proyecto

Abrimos Visual Studio Code y creamos una carpeta para el proyecto:

```bash
mkdir scrapy_api_publica
cd scrapy_api_publica
```    

## 🧪 Paso 2: Crear y activar el entorno virtual

En este paso creamos un **entorno virtual** para aislar las dependencias del proyecto y evitar conflictos con otros proyectos de Python.

### Crear el entorno virtual

Ejecutamos el siguiente comando en la terminal:

```bash
python -m venv venv
```

## 📦 Paso 3: Instalar Scrapy

Con el entorno virtual activo, instalamos **Scrapy**, el framework que usaremos para realizar web scraping.

```bash
pip install scrapy
```

## 🏗️ Paso 4: Crear el proyecto Scrapy

Creamos la estructura del proyecto utilizando Scrapy, lo que genera automáticamente
la arquitectura básica necesaria para comenzar a trabajar.

```bash
scrapy startproject peliculas_publicas
cd peliculas_publicas
```

## 🕷️ Paso 5: Crear el Spider

Creamos un **spider**, que es el componente de Scrapy encargado de realizar las peticiones
y extraer los datos desde la fuente indicada, en este caso una **API pública**.

```bash
scrapy genspider peliculas_api ghibliapi.vercel.app
```

## 🧠 Paso 6: Código del Spider

En este paso definimos la lógica del spider.  
El spider se conecta directamente a la **API pública**, recibe la respuesta en formato **JSON**
y extrae los datos que nos interesan.

```python
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
                "año": peli["release_date"],
                "rating": peli["rt_score"]
            }

```

## ▶️ Paso 7: Ejecutar el Spider

Ejecutamos el spider desde la carpeta donde se encuentra el archivo `scrapy.cfg`.
Este comando inicia el proceso de scraping y guarda los datos obtenidos en un archivo JSON.

```bash
scrapy crawl peliculas_api -o peliculas.json
```

### ✅ Qué ocurre en este paso
- Scrapy ejecuta el spider definido
- Se realizan las peticiones a la API
- Los datos se guardan en un archivo estructurado
