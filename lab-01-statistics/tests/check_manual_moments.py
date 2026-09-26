raw_expected = [14 / 3, 8 / 3, 5]
central_expected = [2 / 3, 8 / 3, 1]
raw_answers = globals().get("raw_moment_answers")
central_answers = globals().get("central_moment_answers")
for name, answers, expected in (
    ("raw_moment_answers", raw_answers, raw_expected),
    ("central_moment_answers", central_answers, central_expected),
):
    if answers is None:
        raise AssertionError(f"Сначала заполните {name} в предыдущей ячейке")
    if len(answers) != len(expected):
        raise AssertionError(f"В {name} нужно ввести {len(expected)} ответа")

print("Ручная проверка начального момента порядка 2")
for answer, expected in zip(raw_answers, raw_expected):
    if answer is None:
        raise AssertionError("Замените все None в raw_moment_answers числовыми ответами")
    assert abs(float(answer) - expected) <= 1e-9, (
        f"Неверно: ожидалось {expected}, получено {answer}"
    )

print("Ручная проверка центрального момента порядка 2")
for answer, expected in zip(central_answers, central_expected):
    if answer is None:
        raise AssertionError("Замените все None в central_moment_answers числовыми ответами")
    assert abs(float(answer) - expected) <= 1e-9, (
        f"Неверно: ожидалось {expected}, получено {answer}"
    )
print(f"OK: проверено ответов: {len(raw_expected) + len(central_expected)}")
