from math import ceil

import numpy as np

mu = 398600.0  # km^3/s^2


def TBP(x: np.ndarray, t: float) -> np.ndarray:
    pos: np.ndarray = x[:3]
    vel: np.ndarray = x[3:]
    r = np.linalg.norm(pos)
    acc = -mu * pos / (r ** 3)
    dx = np.concatenate((vel, acc))
    return dx


def euler(x: np.ndarray, t0: float, t1: float) -> np.ndarray:
    hmax = 0.1
    steps = ceil((t1 - t0) / hmax)
    h = (t1 - t0) / steps
    t = t0

    x = x.copy()
    for _ in range(steps):
        x += h * TBP(x, t)
        t += h

    return x


def main():

    # Set initial conditions
    ecc = 0.5

    x0 = np.zeros(6)
    x0[0] += 6678.0  # 300 km altitude
    x0[4] += np.sqrt(mu / 6678.0 * (1 + ecc))

    # integrate for half the orbital period
    a = 6678.0 / (1 - ecc)
    xf = euler(x0, 0.0, np.pi * np.sqrt(a**3 / mu))

    print(f"Initial conditions:\n{x0}\n")
    print(f"Final conditions:\n{xf}\n")


if __name__ == "__main__":
    main()
