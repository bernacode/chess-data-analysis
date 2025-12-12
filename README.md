# Análisis de partidas de Lichess (Proyecto de Data Science)

**Descripción concisa**

Proyecto de ciencia de datos desarrollado en Jupyter Notebook para analizar un dataset de partidas de Lichess. El objetivo es mostrar habilidades prácticas en limpieza y análisis de datos, visualización, extracción de características y exploración de ideas relacionadas con rendimiento y estilos de juego. Este repositorio sirve como proyecto de portafolio y práctica en técnicas de Data Science.

**Badges sugeridas**

- Estado: ![Status](https://img.shields.io/badge/status-prototype-yellow)
- Python: ![Python](https://img.shields.io/badge/python-3.11-blue)
- Notebook: ![Jupyter](https://img.shields.io/badge/notebook-Jupyter-orange)

Puedes copiar estos badges y adaptarlos (por ejemplo, reemplazar el badge de CI por GitHub Actions cuando añadas un workflow).

**Lenguajes y herramientas**

- **Lenguajes:** Python, Jupyter Notebook
- **Formato principal del proyecto:** Notebook interactivo ([lichess_games.ipynb](lichess_games.ipynb))

**Librerías principales (usadas / recomendadas)**

- `pandas` — manipulación y preparación de datos
- `numpy` — operaciones numéricas
- `matplotlib` / `seaborn` — visualización básica y estadísticas exploratorias
- `plotly` / `plotly.express` — visualizaciones interactivas (opcional)
- `scikit-learn` — extracción de características, modelado y validación (opcional)
- `scipy` — utilidades estadísticas (según necesidad)
- `python-chess` — análisis y manipulación de movimientos/posiciones (opcional)
- `tqdm` — barras de progreso para procesamiento de datos grandes

**Datos**

El dataset principal se encuentra en: [data/games.csv](data/games.csv)

Resumen de contenido y uso:
- Fuente: exportación de Lichess (CSV) u otros dumps públicos.
- Columnas típicas: identificadores de partida, jugadores, fecha, resultado, movimiento en formato PGN, duración, rating, apertura, variantes, etc.

**Estructura del repositorio**

- `lichess_games.ipynb` — Notebook principal con análisis, limpieza, EDA y visualizaciones.
- `data/games.csv` — Dataset de partidas

**Cómo ejecutar (Quick Start)**

1. Clona el repositorio.
2. Crea un entorno virtual e instala dependencias:

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

3. Abre el notebook con Jupyter:

```
jupyter lab
```

4. Ejecuta las celdas del notebook en orden; modifica rutas si tu `data/games.csv` está en otra ubicación.

**Contribuciones y contacto**

Si deseas comentar o mejorar el análisis, abre un Issue o un Pull Request. Para consultas directas, añade tu información de contacto aquí.

---

_Este repositorio es un proyecto personal para demostrar habilidades de Data Science y practicar técnicas de análisis aplicadas a datos de partidas de ajedrez._