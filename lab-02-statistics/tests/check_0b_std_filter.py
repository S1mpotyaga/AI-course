from pathlib import Path
exec((Path("./tests")/"_helpers.py").read_text(encoding="utf-8"), globals())

def ref(values, k):
    if not values:
        return []
    m = sum(values) / len(values)
    v = sum((x-m)**2 for x in values) / len(values)
    s = math.sqrt(v)
    return [x for x in values if abs(x-m) <= k*s + 1e-12]

cases = [
    ([], 1),
    ([5,5,5], 1),
    ([1,2,3], 1),
    ([10,10,11,9,30], 1),
    ([0,0,0,100], 2),
]

for values, k in cases:
    original = values[:]
    expected = ref(values, k)
    got = filter_by_std(values, k)
    _assert(got == expected, f"{values}, k={k}: ожидалось {expected}, получено {got}")
    _assert(values == original, "Исходный список менять нельзя.")

print("OK: задача 0B")
