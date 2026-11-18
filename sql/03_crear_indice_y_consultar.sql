-- Crear el índice B-Tree (método predeterminado de PostgreSQL).
CREATE INDEX idx_productos_nombre
ON productos USING btree (nombre);

ANALYZE productos;

-- Repetir la consulta y comparar el plan.
EXPLAIN (ANALYZE, BUFFERS)
SELECT *
FROM productos
WHERE nombre = 'Producto 500000';

-- Consultar tamaños de tabla e índice.
SELECT
    pg_size_pretty(pg_relation_size('productos')) AS tamano_tabla,
    pg_size_pretty(pg_relation_size('idx_productos_nombre')) AS tamano_indice;
