def fibonacci(n):
    phi = (1 + (5 ** 0.5)) / 2
    psi = (1 - (5 ** 0.5)) / 2
    return int((phi**n - psi**n) / (5 ** 0.5))


n = 108

print(f"A {n}. Fibonacci-szám: {fibonacci(n)}")