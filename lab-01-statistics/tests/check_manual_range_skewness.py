expected = [0, 0, 0]
answers = globals().get("range_skewness_answers")
if answers is None:
    raise AssertionError("Сначала заполните range_skewness_answers в предыдущей ячейке")
if len(answers) != len(expected):
    raise AssertionError(f"Нужно ввести {len(expected)} ответа")

print("Ручная проверка асимметрии на отрезках массива [1, 2, 3, 4]")
for answer, expected_value in zip(answers, expected):
    if answer is None:
        raise AssertionError("Замените все None в range_skewness_answers числовыми ответами")
    assert abs(float(answer) - expected_value) <= 1e-9, (
        f"Неверно: ожидалось {expected_value}, получено {answer}"
    )
print(f"OK: проверено ответов: {len(expected)}")
