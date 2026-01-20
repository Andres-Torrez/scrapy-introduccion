# Escenario 3 – Scraping de HTML sin API pública

En este escenario se muestra cómo utilizar **Scrapy** para extraer información
directamente del **HTML de una página web**, cuando **no existe una API pública** disponible.

Este es el enfoque clásico del web scraping y sigue siendo muy utilizado en la práctica.

---

## 📌 ¿Qué se aprende en este escenario?

- Qué hacer cuando una página no ofrece una API
- Cómo extraer datos directamente del HTML
- Uso de selectores CSS
- Limitaciones del scraping tradicional

---

## 🛠️ Requisitos

Antes de comenzar necesitas:

- Python 3 instalado
- Visual Studio Code
- Conexión a internet

---

## 📁 Paso 1: Crear la carpeta del proyecto

Creamos una carpeta para este escenario y la abrimos en Visual Studio Code:

```bash
mkdir scrapy_html
cd scrapy_html
```

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
scrapy startproject productos_html
cd productos_html
```



---

## 🕷️ Paso 5: Crear el Spider

Creamos un spider que extraerá información directamente desde el HTML del sitio web,
ya que no existe una API pública disponible.

```bash
scrapy genspider productos books.toscrape.com
```


## 🧠 Paso 6: Código del Spider (scraping HTML)

En este paso definimos la lógica del spider.
Scrapy descarga el HTML de la página y extrae los datos usando selectores CSS.

```python
import scrapy

class ProductosSpider(scrapy.Spider):
    name = "productos"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        for producto in response.css("article.product_pod"):
            yield {
                "titulo": producto.css("h3 a::attr(title)").get(),
                "precio": producto.css("p.price_color::text").get()
            }

```
En este código:

- Se accede al HTML de la página
- Se seleccionan los elementos con CSS
- Se extraen los datos visibles al usuario

---

## ▶️ Paso 7: Ejecutar el Spider

Ejecutamos el spider desde la carpeta donde se encuentra el archivo `scrapy.cfg`:

```bash
scrapy crawl productos -o productos.json

```


---

## 📄 Resultado

Se genera un archivo productos.json que contiene:
- Nombre del producto
- Precio
Los datos se obtienen directamente desde el HTML de la página web.

## ⚠️ Consideraciones importantes

- Este método es más frágil que usar APIs
- Cambios en el diseño de la página pueden romper el scraper
- Siempre se deben revisar los términos de uso del sitio web

## ✅ Conclusión

Este escenario demuestra cómo Scrapy puede utilizarse cuando **no existe una API pública**.
El scraping de HTML sigue siendo una técnica útil, aunque más frágil, y debe usarse de forma
responsable y ética.

