import math
import random

def _assert(condition, message):
    if not condition:
        raise AssertionError(message)

def _close(a, b, eps=1e-7):
    return math.isclose(a, b, rel_tol=eps, abs_tol=eps)

def _mean_ref(a):
    return sum(a) / len(a)

def _var_ref(a):
    m = _mean_ref(a)
    return sum((x - m) ** 2 for x in a) / len(a)

def _skew_ref(a):
    m = _mean_ref(a)
    v = _var_ref(a)
    if abs(v) <= 1e-15:
        return None
    mu3 = sum((x - m) ** 3 for x in a) / len(a)
    return mu3 / (v ** 1.5)
