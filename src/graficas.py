"""Genera la gráfica de la función integranda y el área entre x=1 y x=4."""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from src.calculos import integranda, A, B, integral_exacta


def main() -> None:
    x = np.linspace(A, B, 500)
    y = np.array([integranda(float(valor)) for valor in x])

    plt.figure(figsize=(9, 5))
    plt.plot(x, y, label="f(x)", linewidth=2)
    plt.fill_between(x, y, 0, alpha=0.25, label="Área entre x=1 y x=4")
    plt.axhline(0, linewidth=0.8)
    plt.xlim(A, B)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Integral definida en [1, 4] = {integral_exacta():.4f}")
    plt.grid(True, alpha=0.3)
    plt.legend()

    salida = Path("resultados")
    salida.mkdir(exist_ok=True)
    archivo = salida / "area_integral.png"
    plt.tight_layout()
    plt.savefig(archivo, dpi=160)
    print(f"Gráfica guardada en: {archivo}")


if __name__ == "__main__":
    main()
