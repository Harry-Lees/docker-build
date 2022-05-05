import run


def test_fibonacci():
    fn = run.fib()
    assert next(fn) == 0
    assert next(fn) == 1
    assert next(fn) == 1
    assert next(fn) == 2
