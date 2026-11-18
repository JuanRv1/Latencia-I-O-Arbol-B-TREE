# Análisis de latencia de lectura I/O con índices B-Tree

Proyecto académico en **Python + PostgreSQL** para estudiar la latencia de lectura I/O en una base de datos indexada con B-Tree y relacionar los resultados con el modelo matemático trabajado en clase.

## Objetivos
- Evaluar la integral definida del modelo matemático en el intervalo `[1, 4]`.
- Comparar el resultado exacto con aproximaciones numéricas.
- Mostrar la función integranda y el área de integración.
- Analizar resultados de consultas PostgreSQL con y sin índice B-Tree.
- Documentar la comparación entre el modelo y la prueba experimental.

## Estructura

```text
proyecto_latencia_btree/
├── README.md
├── requirements.txt
├── .env.example
├── src/
│   ├── calculos.py
│   ├── graficas.py
│   └── medir_postgres.py
├── sql/
│   ├── 01_crear_tabla.sql
│   ├── 02_consulta_sin_indice.sql
│   └── 03_crear_indice_y_consultar.sql
├── docs/
│   └── metodologia.md
└── resultados/
    └── .gitkeep
```

## Requisitos
- Python 3.10 o superior.
- PostgreSQL (opcional, para ejecutar la parte experimental).
- Paquetes Python indicados en `requirements.txt`.

## Instalación

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

En macOS/Linux:

```bash
source .venv/bin/activate
```

Luego:

```bash
pip install -r requirements.txt
```

## Ejecutar los cálculos

Desde la carpeta raíz:

```bash
python -m src.calculos
```

## Generar las gráficas

```bash
python -m src.graficas
```

Las imágenes se guardan en `resultados/`.

## Ejecutar las pruebas PostgreSQL

1. Crear una base de datos PostgreSQL.
2. Ejecutar los scripts SQL en el orden indicado en la carpeta `sql/`.
3. Copiar `.env.example` como `.env` y completar los datos de conexión.
4. Instalar las dependencias.
5. Ejecutar:

```bash
python -m src.medir_postgres
```

El programa intenta obtener el plan de ejecución mediante `EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)`. Los resultados dependen del equipo, la configuración de PostgreSQL, la caché y el tamaño de los datos.

## Modelo matemático utilizado

Se utiliza la primitiva proporcionada para el desarrollo de la integral:

\[
F(x)=-6\ln|x|-\frac{3}{x}+11\ln|x+1|-\frac{5}{x+1}
\]

Por tanto, la función integranda es:

\[
f(x)=-\frac{6}{x}+\frac{3}{x^2}+\frac{11}{x+1}+\frac{5}{(x+1)^2}
\]

En el intervalo `[1, 4]`:

\[
\int_1^4 f(x)\,dx
=11\ln(5)-23\ln(2)+\frac{15}{4}
\approx 5.5114
\]

**Importante:** este repositorio implementa la función integranda deducida de la primitiva anterior. No se debe confundir el resultado de la integral (área acumulada en el intervalo) con una coordenada del eje X. La interpretación de las unidades debe justificarse según las unidades asignadas al modelo en el trabajo.

## Resultados experimentales de referencia

En la simulación descrita para la exposición se reportaron estos valores:

| Prueba | Resultado reportado |
|---|---:|
| Tabla de productos | 1.000.000 registros |
| Tamaño aproximado de tabla | 57 MB |
| Tamaño aproximado del índice | 30 MB |
| Páginas/buffers en lectura secuencial | 7.345 |
| Tiempo de lectura secuencial | 86,496 ms |
| Páginas/buffers en consulta indexada | 4 |
| Tiempo de consulta indexada | 0,098 ms |

Son valores de referencia de la simulación original, **no resultados garantizados** al ejecutar el proyecto en otro computador. La medición local se debe registrar por separado.

## Limitaciones y rigor
- Los tiempos reales pueden variar por CPU, disco, memoria, caché, versión y configuración de PostgreSQL.
- Para comparar correctamente, se recomienda ejecutar varias veces y registrar las condiciones.
- El plan de ejecución permite observar el tipo de acceso y los buffers; no demuestra por sí solo que toda consulta real tendrá el mismo rendimiento.
- Los valores de derivada reportados en la exposición se documentan en `docs/metodologia.md`. La fórmula explícita de la función de latencia `C(x)` debe incorporarse cuando se tenga confirmada; no se inventa en este repositorio.

## Autoría
Completar con los nombres de los integrantes, asignatura, docente y fecha antes de publicar.
