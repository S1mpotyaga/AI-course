expected = [2 / 3, 5, 5]
answers = globals().get("variance_sums_answers")
if answers is None:
    raise AssertionError("Сначала заполните variance_sums_answers в предыдущей ячейке")
if len(answers) != len(expected):
    raise AssertionError(f"Нужно ввести {len(expected)} ответа")

print("Ручная проверка дисперсии через две суммы")
for answer, expected_value in zip(answers, expected):
    if answer is None:
        raise AssertionError("Замените все None в variance_sums_answers числовыми ответами")
    assert abs(float(answer) - expected_value) <= 1e-9, (
        f"Неверно: ожидалось {expected_value}, получено {answer}"
    )
print(f"OK: проверено ответов: {len(expected)}")
