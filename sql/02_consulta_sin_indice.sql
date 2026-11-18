-- Ejecutar antes de crear el índice sobre nombre.
EXPLAIN (ANALYZE, BUFFERS)
SELECT *
FROM productos
WHERE nombre = 'Producto 500000';
