DROP TABLE IF EXISTS productos;

CREATE TABLE productos (
    id BIGINT PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    categoria VARCHAR(80),
    precio NUMERIC(12, 2)
);

-- Genera un millón de registros de prueba.
INSERT INTO productos (id, nombre, categoria, precio)
SELECT
    n,
    'Producto ' || n,
    CASE WHEN n % 3 = 0 THEN 'Tecnologia'
         WHEN n % 3 = 1 THEN 'Hogar'
         ELSE 'Oficina' END,
    (10000 + (n % 500000))::NUMERIC / 100
FROM generate_series(1, 1000000) AS n;

ANALYZE productos;
