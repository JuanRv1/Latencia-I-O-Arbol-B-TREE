# Metodología y datos del caso

## 1. Problema

Se estudia cómo cambia el costo de lectura de información cuando una base de datos busca registros mediante lectura secuencial o mediante un índice B-Tree.

## 2. Parte matemática

La primitiva utilizada en el desarrollo es:

`F(x) = -6 ln|x| - 3/x + 11 ln|x+1| - 5/(x+1)`

Su derivada, que corresponde a la función integrada, es:

`f(x) = -6/x + 3/x² + 11/(x+1) + 5/(x+1)²`

La integral se evalúa desde `x=1` hasta `x=4`:

`F(4) - F(1) = 11 ln(5) - 23 ln(2) + 15/4 ≈ 5.5114`

El valor de la integral representa el área acumulada en el intervalo; no es una coordenada horizontal. La gráfica debe limitarse a `1 ≤ x ≤ 4`.

## 3. Resultados de derivada reportados en la exposición

| x | C'(x) reportada |
|---:|---:|
| 1 | -4.0000 |
| 2 | -0.8426 |
| 3 | -0.3993 |
| 4 | -0.2388 |

La interpretación reportada es que la derivada negativa representa una disminución de la latencia conforme aumenta la profundidad considerada por el modelo.

**Dato pendiente para reproducibilidad:** agregar aquí la expresión exacta de `C(x)` utilizada en la exposición. Los valores de la tabla se conservan como datos reportados y no se reconstruye una fórmula sin evidencia.

## 4. Prueba PostgreSQL

Los scripts crean un millón de productos y comparan una búsqueda antes y después de crear un índice B-Tree sobre `nombre`. Se utiliza `EXPLAIN (ANALYZE, BUFFERS)` para observar el plan, el tiempo y los buffers.

## 5. Valores de referencia de la exposición

- Sin índice: 7.345 buffers y 86,496 ms.
- Con índice: 4 buffers y 0,098 ms.
- Tabla: aproximadamente 57 MB.
- Índice: aproximadamente 30 MB.

Estos números pertenecen a la ejecución de referencia de la exposición. Las ejecuciones locales pueden producir valores distintos.

## 6. Interpretación

Un índice B-Tree puede reducir las páginas que PostgreSQL necesita examinar para localizar un registro. La diferencia observada debe analizarse teniendo en cuenta caché, hardware, configuración y selectividad de la consulta. No se debe afirmar que los tiempos serán idénticos en todos los equipos.
