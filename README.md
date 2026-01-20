# 🕷️ Scrapy – Web Scraping Scenarios

Este repositorio presenta **ejemplos prácticos y educativos de web scraping con Scrapy**,
organizados en **tres escenarios reales** que representan cómo funcionan las páginas web modernas.

El objetivo no es solo mostrar código, sino **entender cómo obtener datos correctamente**
según el tipo de fuente disponible: APIs o HTML.

---

## 📌 ¿Qué es Scrapy?

Scrapy es un **framework de Python** diseñado para extraer información de páginas web
de forma **automática, rápida y estructurada**.

Se utiliza para:
- Recolección de datos
- Análisis de información
- Investigación
- Proyectos académicos
- Preparación de datasets

---

## 🧠 Idea clave del repositorio

No todas las páginas web funcionan igual.

Antes de scrapear, es importante **entender de dónde vienen los datos**.
Este repositorio muestra las **tres situaciones más comunes** en el mundo real.

---

## 📂 Estructura del repositorio
```
scrapy-web-scenarios/
│
├── 01_api_publica/
│ └── README.md
│
├── 02_api_con_api_key/
│ └── README.md
│
├── 03_html_sin_api/
│ └── README.md
│
└── README.md
```


Cada carpeta representa un escenario distinto y contiene:
- Un proyecto Scrapy funcional
- Un README con explicación paso a paso
- Código reproducible

---

## 🟢 Escenario 1 – API pública sin autenticación

📁 **01_api_publica**

En este escenario se consumen datos desde una **API pública** que no requiere API key.

### Qué se aprende:
- Qué es una API pública
- Cómo Scrapy puede consumir APIs directamente
- Procesar respuestas en formato JSON
- Generar datasets sin scrapear HTML

👉 Es el escenario más simple y ideal para aprender.

---

## 🟡 Escenario 2 – API pública con API Key

📁 **02_api_con_api_key**

En este escenario se utiliza una **API oficial** que requiere autenticación mediante una **API Key**.

### Qué se aprende:
- Qué es una API Key y por qué se utiliza
- Cómo autenticar requests con Scrapy
- Buenas prácticas de seguridad
- Uso de APIs profesionales (ej. películas)

👉 Es el escenario más común en proyectos reales.

---

## 🔴 Escenario 3 – Scraping de HTML sin API pública

📁 **03_html_sin_api**

En este escenario no existe una API pública disponible.
Los datos se extraen directamente desde el **HTML de la página web**.

### Qué se aprende:
- Scraping tradicional con selectores CSS
- Limitaciones del scraping HTML
- Por qué este método es más frágil
- Cuándo es la única opción posible

👉 Es el escenario clásico del web scraping.

---

## ⚖️ Ética y legalidad

Todos los ejemplos de este repositorio:
- Utilizan APIs públicas o sitios de práctica
- No acceden a datos privados
- Tienen fines educativos

Siempre se deben respetar:
- Los términos de uso de los sitios
- Las políticas de datos
- Las buenas prácticas de scraping responsable

---

## 🎯 Objetivo final

El objetivo de este repositorio es **enseñar a elegir la estrategia correcta** de scraping,
no solo escribir código.

> “Scrapear bien no es usar una herramienta, es entender cómo funciona la web.”

---

## 🚀 Conclusión

Scrapy no es una herramienta limitada.
Es una herramienta **estratégica**, que se usa de distintas formas dependiendo de:
- Si los datos vienen de una API
- Si requieren autenticación
- Si solo están disponibles en el HTML
