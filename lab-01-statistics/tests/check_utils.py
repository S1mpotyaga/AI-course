import math


def close(actual, expected, tolerance=1e-9):
    assert math.isclose(actual, expected, rel_tol=tolerance, abs_tol=tolerance), (
        f"Ожидалось {expected}, получено {actual}"
    )


def expect_value_error(function, *args):
    try:
        function(*args)
    except ValueError:
        return
    raise AssertionError(f"{function.__name__} должна поднять ValueError")


def check(name, test):
    test()
    print(f"OK: {name}")
