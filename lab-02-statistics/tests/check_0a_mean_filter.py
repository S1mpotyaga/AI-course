from pathlib import Path
exec((Path("./tests")/"_helpers.py").read_text(encoding="utf-8"), globals())

cases = [
    ([], 10, []),
    ([1], 0, [1]),
    ([1, 2, 3], 1, [1, 2, 3]),
    ([1, 2, 3], 0, [2]),
    ([10, 11, 12, 13, 50], 10, [10, 11, 12, 13]),
    ([-10, 0, 10], 5, [0]),
]

for values, d, expected in cases:
    original = values[:]
    got = filter_by_mean_distance(values, d)
    _assert(got == expected, f"{values}, distance={d}: ожидалось {expected}, получено {got}")
    _assert(values == original, "Исходный список менять нельзя.")

print("OK: задача 0A")
