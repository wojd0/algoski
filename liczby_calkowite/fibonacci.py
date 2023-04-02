import sys

def fib_iter(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

def fib_reku(n):
    if n <= 1:
        return n
    return fib_reku(n - 1) + fib_reku(n - 2)

print(fib_iter(20577)) # 20577 - maks dla pythona bez zmiany konfiguracji w os
print(fib_reku(200)) # a tu sie sra :<