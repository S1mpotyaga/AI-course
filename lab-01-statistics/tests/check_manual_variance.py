variance_expected = [2 / 3, 5, 8 / 3]
std_expected = [(2 / 3) ** 0.5, 5 ** 0.5, (8 / 3) ** 0.5]
variance_answers = globals().get("variance_answers")
std_answers = globals().get("std_answers")
for name, answers, expected in (
    ("variance_answers", variance_answers, variance_expected),
    ("std_answers", std_answers, std_expected),
):
    if answers is None:
        raise AssertionError(f"Сначала заполните {name} в предыдущей ячейке")
    if len(answers) != len(expected):
        raise AssertionError(f"В {name} нужно ввести {len(expected)} ответа")

print("Ручная проверка дисперсии")
for answer, expected in zip(variance_answers, variance_expected):
    if answer is None:
        raise AssertionError("Замените все None в variance_answers числовыми ответами")
    assert abs(float(answer) - expected) <= 1e-9, (
        f"Неверно: ожидалось {expected}, получено {answer}"
    )

print("Ручная проверка стандартного отклонения")
for answer, expected in zip(std_answers, std_expected):
    if answer is None:
        raise AssertionError("Замените все None в std_answers числовыми ответами")
    assert abs(float(answer) - expected) <= 1e-9, (
        f"Неверно: ожидалось {expected}, получено {answer}"
    )
print(f"OK: проверено ответов: {len(variance_expected) + len(std_expected)}")
