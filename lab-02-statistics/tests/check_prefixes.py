from pathlib import Path
exec((Path("./tests")/"_helpers.py").read_text(encoding="utf-8"), globals())

cases = [
    ([], ([0],[0],[0])),
    ([2], ([0,2],[0,4],[0,8])),
    ([1,2,3], ([0,1,3,6],[0,1,5,14],[0,1,9,36])),
    ([-2,3], ([0,-2,1],[0,4,13],[0,-8,19])),
]
for a, exp in cases:
    original = a[:]
    got = build_prefixes(a)
    _assert(isinstance(got,(tuple,list)) and len(got)==3, "Нужно вернуть три массива.")
    _assert(tuple(got)==exp, f"Неверный ответ для {a}: {got}")
    _assert(a==original, "Исходный массив менять нельзя.")
print("OK: префиксы")
