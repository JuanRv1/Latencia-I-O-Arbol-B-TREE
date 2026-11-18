"""Mide planes de ejecución PostgreSQL y guarda el resultado JSON."""

import json
import os
from pathlib import Path

from dotenv import load_dotenv
import psycopg
from psycopg.rows import dict_row


CONSULTA = """
SELECT *
FROM productos
WHERE nombre = %s;
"""


def main() -> None:
    load_dotenv()
    config = {
        "host": os.getenv("PGHOST", "localhost"),
        "port": os.getenv("PGPORT", "5432"),
        "dbname": os.getenv("PGDATABASE", "latencia_btree"),
        "user": os.getenv("PGUSER", "postgres"),
        "password": os.getenv("PGPASSWORD", ""),
    }

    with psycopg.connect(**config, row_factory=dict_row) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) " + CONSULTA,
                ("Producto 500000",),
            )
            plan = cur.fetchone()["QUERY PLAN"]

    salida = Path("resultados")
    salida.mkdir(exist_ok=True)
    archivo = salida / "plan_consulta.json"
    archivo.write_text(json.dumps(plan, indent=2), encoding="utf-8")
    print(f"Plan guardado en: {archivo}")
    print(json.dumps(plan, indent=2))


if __name__ == "__main__":
    main()
