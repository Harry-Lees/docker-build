import time
from collections.abc import Generator


def fib() -> Generator[int, None, None]:
    """simple fibonacci function"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    f = fib()

    while True:
        n = next(f)
        print(n)
        time.sleep(1)
