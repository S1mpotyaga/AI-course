from pathlib import Path
exec((Path("./tests")/"_helpers.py").read_text(encoding="utf-8"), globals())

def ref(values):
    if not values:
        return "UNDEFINED"
    m = sum(values) / len(values)
    mu3 = sum((x-m)**3 for x in values) / len(values)
    if abs(mu3) < 1e-12:
        return "SYMMETRIC"
    return "RIGHT" if mu3 > 0 else "LEFT"

cases = [
    [],
    [1],
    [1,2,3],
    [1,1,1,10],
    [-10,1,1,1],
    [2,2,2,2],
    [-3,-1,0,1,3],
]

for values in cases:
    expected = ref(values)
    got = skewness_direction(values)
    _assert(got == expected, f"{values}: ожидалось {expected}, получено {got}")

print("OK: задача 0C")
