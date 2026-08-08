# Taller de Big Data

Repositorio didáctico para enseñar un taller práctico de **Big Data** con Python y Apache Spark (PySpark).

El caso de estudio usa mensajes políticos (tweets) para recorrer el ciclo completo: exploración, comparación pandas vs Spark, ETL distribuido, formatos columnares, agregaciones y un mini data warehouse.

## Objetivos de aprendizaje

Al terminar el taller, las personas participantes podrán:

1. Explicar cuándo un problema requiere técnicas de Big Data.
2. Comparar procesamiento local (pandas) frente a distribuido (Spark).
3. Diseñar un pipeline ETL reproducible sobre datos semi-estructurados.
4. Elegir formatos de almacenamiento (CSV vs Parquet) con criterios de rendimiento.
5. Construir agregaciones analíticas y un dataset listo para consumo.

## Estructura del repositorio

```text
docs/                 Material teórico y agenda
modulos/              Ejercicios guiados (uno por bloque)
src/taller_bigdata/   Biblioteca compartida del taller
data/raw/             Datos de entrada (Tweets.csv)
data/generated/       Datos sintéticos generados en el taller
data/processed/       Salidas de pipelines
soluciones/           Soluciones de referencia (para instructores)
tests/                Pruebas automatizadas de la biblioteca
scripts/              Utilidades de setup y demo
```

## Requisitos

- Python 3.10+
- Java 11+ (necesario para Spark)
- ~4 GB de RAM recomendados

## Setup rápido

```bash
make install
make generate-sample   # genera un dataset sintético pequeño
make test              # valida que el entorno funciona
```

Activa el entorno virtual:

```bash
source .venv/bin/activate
```

## Agenda sugerida (~4 horas)

| Bloque | Módulo | Duración |
|--------|--------|----------|
| 0 | Conceptos de Big Data (`docs/conceptos`) | 30 min |
| 1 | Exploración del dataset | 30 min |
| 2 | Pandas vs Spark | 40 min |
| 3 | ETL distribuido | 45 min |
| 4 | Formatos columnares | 30 min |
| 5 | Agregaciones analíticas | 30 min |
| 6 | Proyecto final | 45 min |

Detalle en [`docs/agenda.md`](docs/agenda.md).

## Cómo trabajar los módulos

Cada carpeta en `modulos/` incluye:

- `README.md` — objetivos y teoría breve
- `ejercicio.py` — tareas a completar (`TODO`)
- comandos sugeridos en el README

Flujo recomendado:

```bash
# Ejemplo: módulo 1
python -m modulos.01_exploracion.ejercicio
```

O abre el archivo del módulo, completa los `TODO` y ejecuta con:

```bash
PYTHONPATH=src python modulos/01_exploracion/ejercicio.py
```

## Comandos útiles

```bash
make install           # crea .venv e instala dependencias
make test              # corre pytest
make generate-sample   # genera data/generated/eventos_sample.csv
make generate-large    # genera un dataset más grande para demos
make demo-etl          # ejecuta el pipeline ETL de demostración
make clean             # limpia artefactos locales
```

## Para instructores

Consulta [`docs/guia-instructor.md`](docs/guia-instructor.md) para ritmo, puntos de discusión y uso de `soluciones/`.

## Licencia de uso didáctico

Material pensado para formación. Adapta módulos y datasets según la audiencia.
