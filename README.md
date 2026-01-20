# 🕷️ Scrapy – Práctica paso a paso

Vamos a ver **tres formas reales de obtener datos de la web con Scrapy**:

1. API pública sin API Key  
2. API pública con API Key  
3. Página web sin API (HTML)

Este repositorio contiene **la práctica completa**, paso a paso, desde abrir Visual Studio Code hasta obtener los datos.

---

## 🧠 Requisitos

- Python 3.8+
- Visual Studio Code
- Conocimientos básicos de Python

---

## 📚 Índice

1. Introducción a Scrapy  
2. Escenario 1 – API pública sin API Key  
3. Escenario 2 – API con API Key  
4. Escenario 3 – Web sin API (HTML)  
5. Conclusiones  

---

## 🟢 Escenario 1 – API pública SIN API KEY

### 🎯 Objetivo
Extraer películas desde una API abierta sin autenticación.

---

### 🧑‍💻 Paso 0 – Abrir Visual Studio Code

1. Abrir Visual Studio Code
2. Crear una carpeta llamada:

```bash
scrapy_api_publica

🧪 Paso 1 – Crear entorno virtual
python -m venv venv


Activar:

Windows

venv\Scripts\activate

📦 Paso 2 – Instalar Scrapy
pip install scrapy

🏗️ Paso 3 – Crear proyecto Scrapy
scrapy startproject peliculas_publicas
cd peliculas_publicas

🕷️ Paso 4 – Crear el Spider
scrapy genspider peliculas_api ghibliapi.vercel.app

✍️ Paso 5 – Código del Spider

Archivo:

peliculas_publicas/spiders/peliculas_api.py

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

▶️ Paso 6 – Ejecutar el Spider
scrapy crawl peliculas_api -o peliculas.json


🎉 Primer WOW


👉 Scroll ↓  
👉 Click **Commit changes**

---

# 🔥 ¿POR QUÉ AHORA SE VE “PRO” COMO LOS EJEMPLOS?

Porque usaste:

- `#` → títulos grandes  
- `##` → subtítulos  
- ```bash``` → bloques de comandos  
- ```python``` → bloques de código  
- Listas → índice automático  
- Emojis → visual y didáctico  

💡 GitHub **renderiza Markdown automáticamente**

---

# 🧩 PASO 4 — ¿Y LOS OTROS ESCENARIOS?

Exactamente igual 👇  
Solo sigues escribiendo **debajo**:

```md
## 🟡 Escenario 2 – API con API KEY

## 🔴 Escenario 3 – Web sin API (HTML)


Cada uno:

Objetivo

Pasos

Código

Ejecutar

Resultado

🎤 CÓMO EXPLICARLO EN CLASE (IMPORTANTE)

💬 Di algo así:

“La teoría la vemos rápido en diapositivas.
Toda la práctica está documentada paso a paso en GitHub para que la puedan repetir luego.”

Eso vende profesionalismo.
