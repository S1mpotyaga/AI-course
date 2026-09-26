expected = [0, 0.7071067811865475, -0.7071067811865475]
answers = globals().get("skewness_answers")
if answers is None:
    raise AssertionError("Сначала заполните skewness_answers в предыдущей ячейке")
if len(answers) != len(expected):
    raise AssertionError(f"Нужно ввести {len(expected)} ответа")

print("Ручная проверка коэффициента асимметрии")
for answer, expected_value in zip(answers, expected):
    if answer is None:
        raise AssertionError("Замените все None в skewness_answers числовыми ответами")
    assert abs(float(answer) - expected_value) <= 1e-9, (
        f"Неверно: ожидалось {expected_value}, получено {answer}"
    )
print(f"OK: проверено ответов: {len(expected)}")
