<div align="center">

# ♟️ Lichess Data Analysis

**Explorando estrategias y patrones en partidas de ajedrez con Data Science**

![Status](https://img.shields.io/badge/Status-En_Progreso-yellow?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

</div>

---

## 📖 Descripción del Proyecto

Este repositorio contiene un análisis exploratorio de datos (EDA) exhaustivo sobre un conjunto de partidas de la plataforma Lichess.

El objetivo principal es transformar datos crudos en **insights accionables**, respondiendo preguntas sobre cómo influyen las aperturas, el ELO y el control de tiempo en el resultado final. Este proyecto sirve como demostración de habilidades en el ciclo completo de Data Science: desde la limpieza de datos hasta la visualización narrativa.

### 🎯 Objetivos
- 🧹 **Limpieza de Datos:** Manejo de valores nulos y formatos de fecha.
- 📊 **Visualización:** Gráficos de distribución de ELO y victorias.
- 🧠 **Insights:** Correlación entre movimientos iniciales y tasa de victoria.

---

## 🛠️ Tecnologías y Herramientas

| Categoría | Librerías / Herramientas | Uso principal |
| :--- | :--- | :--- |
| **Core** | `Python 3.11` | Lenguaje base |
| **Datos** | `Pandas`, `NumPy` | Manipulación y álgebra lineal |
| **Vis** | `Matplotlib`, `Seaborn` | Visualización estática y estadística |
| **Entorno**| `Jupyter Notebook` | Desarrollo interactivo |
| **Control**| `Git` / `GitHub` | Control de versiones |

---

## 📂 Estructura del Repositorio

El proyecto sigue una estructura estandarizada (basada en *Cookiecutter Data Science*) para garantizar la reproducibilidad y el orden:

```text
├── data/
│   ├── games.csv           # Dataset original (Ignorado en git si es muy pesado)
│   └── processed/          # Datos limpios (opcional)
│
├── notebooks/
│   ├── lichess_games.ipynb # 📓 Notebook principal de análisis
│   └── drafts/             # Pruebas y borradores
│
├── src/                    # ⚙️ Código fuente y scripts auxiliares
│   ├── __init__.py
│   └── save_figure.py      # Script para exportar gráficos
│
├── figures/                # 📈 Gráficos generados por el código
│
├── reports/                # 📄 Reportes finales y conclusiones
│
└── requirements.txt        # Dependencias del proyecto
```

---

## 🚀 Cómo empezar

### 1. Clonar el repositorio:

```bash
    git clone [https://github.com/bernacode/chess-data-analysis.git](https://github.com/bernacode/chess-data-analysis.git)
```

### 2. install -r requirements.txt

```bash
    pip install -r requirements.txt
```

### 3. Explorar el analisis

Abre el archivo notebooks/02_analisis.ipynb en tu editor favorito (VS Code o Jupyter Lab).