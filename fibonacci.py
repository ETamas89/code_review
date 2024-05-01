def fibonacci(n):
    phi = (1 + (5 ** 0.5)) / 2
    return int((phi**n - (1 - phi)**n) / (5 ** 0.5))

n = 108

print(f"A {n}. Fibonacci-szám: {fibonacci(n)}")