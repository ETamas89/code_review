def fibonacci(n):
    number_fibo = (n+1) * [None]

    def recursive_fibonacci(x):
        if number_fibo[x] is None:
            number_fibo[x] = x if x <= 1 else recursive_fibonacci(x-1) + recursive_fibonacci(x-2)
        return number_fibo[x]

    return recursive_fibonacci(n)

for i in range(100):
    print(i, fibonacci(i))