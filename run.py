import time

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fib()

while True:
    n = next(f)
    print(n)
    time.sleep(1)