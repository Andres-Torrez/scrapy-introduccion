# Escenario 2 – Scraping con API pública usando API Key

En este escenario se muestra cómo utilizar **Scrapy** para consumir una **API pública que requiere autenticación mediante una API Key**.

Este tipo de APIs es muy común en proyectos reales, ya que permite a las plataformas
controlar el uso, evitar abusos y medir consumo.

## 📌 ¿Qué se aprende en este escenario?

- Qué es una API Key y para qué se usa
- Cómo autenticar requests en una API
- Cómo consumir APIs oficiales con Scrapy
- Buenas prácticas de seguridad (no subir claves a GitHub)

## 🛠️ Requisitos

Antes de comenzar necesitas:

- Python 3 instalado
- Visual Studio Code
- Cuenta en The Movie Database (TMDB)
- Una API Key válida
  

## 🔑 Paso 1: Obtener una API Key

Para este ejemplo utilizamos la API de **The Movie Database (TMDB)**.

Pasos:
1. Crear una cuenta en https://www.themoviedb.org
2. Ir a Settings → API
3. Solicitar una API Key
4. Copiar la clave generada

⚠️ Importante:  
La API Key **no debe subirse a repositorios públicos**.

## 📁 Paso 1: Crear la carpeta del proyecto

Creamos una carpeta para este escenario y la abrimos en Visual Studio Code:

```bash
mkdir scrapy_api_key
cd scrapy_api_key
```


---

## 🧪 Paso 2: Crear y activar el entorno virtual

Creamos un entorno virtual para aislar las dependencias del proyecto.

```bash
python -m venv venv
```

### Activar el entorno virtual

Una vez creado el entorno virtual, es necesario activarlo para que las dependencias
se instalen y ejecuten únicamente dentro del proyecto.

#### En Windows
```bash
venv\Scripts\activate
```

#### En macOS o Linux
```bash
source venv/bin/activate
```


---

## 📦 Paso 3: Instalar Scrapy

Con el entorno virtual activo, instalamos Scrapy:

```bash
pip install scrapy
```


---

## 🏗️ Paso 4: Crear el proyecto Scrapy

Creamos la estructura base del proyecto usando Scrapy:

```bash
scrapy startproject peliculas_tmdb
cd peliculas_tmdb
```

---

## 🕷️ Paso 5: Crear el Spider

Creamos un spider que se conectará a la API de TMDB:

```bash
scrapy genspider top_2025 api.themoviedb.org
```


---

## 🧠 Paso 6: Código del Spider (API con Key)

En este paso definimos la lógica del spider.
Scrapy se conecta a la API oficial de TMDB utilizando una **API Key** y procesa la respuesta en formato JSON.

```python
import scrapy
import json

class Top2025Spider(scrapy.Spider):
    name = "top_2025"

    api_key = "TU_API_KEY_AQUI"

    def start_requests(self):
        url = (
            "https://api.themoviedb.org/3/discover/movie"
            f"?api_key={self.api_key}"
            "&primary_release_year=2025"
            "&sort_by=vote_average.desc"
            "&vote_count.gte=500"
        )
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)

        for peli in data["results"]:
            yield {
                "titulo": peli["title"],
                "fecha": peli["release_date"],
                "rating": peli["vote_average"],
                "votos": peli["vote_count"]
            }
```

⚠️ Recuerda reemplazar TU_API_KEY_AQUI por tu propia clave.

---

## ▶️ Paso 7: Ejecutar el Spider

Ejecutamos el spider desde la carpeta donde se encuentra el archivo `scrapy.cfg`:

```bash
scrapy crawl top_2025 -o top_peliculas_2025.json
```


---

## 📄 Resultado

Se genera el archivo `top_peliculas_2025.json` que contiene información como:
- Título de la película
- Fecha de estreno
- Rating promedio
- Cantidad de votos


## ✅ Conclusión

Este escenario demuestra cómo Scrapy puede utilizarse para consumir **APIs oficiales con autenticación**.
Este enfoque es más estable, rápido y profesional que el scraping de HTML, y es ampliamente usado en proyectos reales.


