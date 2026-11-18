"""Cálculos del modelo integral de latencia."""

import math

A = 1.0
B = 4.0


def integranda(x: float) -> float:
    """Derivada de la primitiva F(x) indicada en el README."""
    if x <= 0 or x == -1:
        raise ValueError("x está fuera del dominio de la función.")
    return -6 / x + 3 / (x ** 2) + 11 / (x + 1) + 5 / ((x + 1) ** 2)


def primitiva(x: float) -> float:
    if x <= 0 or x == -1:
        raise ValueError("x está fuera del dominio de la función.")
    return (
        -6 * math.log(abs(x))
        - 3 / x
        + 11 * math.log(abs(x + 1))
        - 5 / (x + 1)
    )


def integral_exacta(a: float = A, b: float = B) -> float:
    return primitiva(b) - primitiva(a)


def regla_simpson(a: float = A, b: float = B, n: int = 6) -> float:
    """Aproxima la integral con Simpson 1/3; n debe ser par."""
    if n <= 0 or n % 2:
        raise ValueError("El número de subintervalos debe ser positivo y par.")
    h = (b - a) / n
    total = integranda(a) + integranda(b)

    for i in range(1, n):
        x = a + i * h
        total += (4 if i % 2 else 2) * integranda(x)

    return total * h / 3


def suma_rectangulos(a: float = A, b: float = B, franjas: int = 1_000_000) -> float:
    """Suma de punto medio para aproximar el área."""
    if franjas <= 0:
        raise ValueError("El número de franjas debe ser positivo.")
    dx = (b - a) / franjas
    total = 0.0
    for i in range(franjas):
        x_medio = a + (i + 0.5) * dx
        total += integranda(x_medio) * dx
    return total


def main() -> None:
    exacta = integral_exacta()
    simpson = regla_simpson()
    rectangulos = suma_rectangulos()

    print("ANÁLISIS MATEMÁTICO DE LATENCIA I/O")
    print(f"Intervalo: [{A}, {B}]")
    print(f"Integral exacta:       {exacta:.8f}")
    print(f"Simpson (6 tramos):    {simpson:.8f}")
    print(f"Punto medio (1M):      {rectangulos:.8f}")
    print(f"Diferencia Simpson:    {abs(exacta - simpson):.8f}")
    print(f"Diferencia rectángulos:{abs(exacta - rectangulos):.8f}")


if __name__ == "__main__":
    main()
