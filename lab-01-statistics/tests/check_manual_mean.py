expected = [4, 2, 2]
answers = globals().get("mean_answers")
if answers is None:
    raise AssertionError("Сначала заполните mean_answers в предыдущей ячейке")
if len(answers) != len(expected):
    raise AssertionError(f"Нужно ввести {len(expected)} ответа")

print("Ручная проверка среднего")
for answer, expected_value in zip(answers, expected):
    if answer is None:
        raise AssertionError("Замените все None в mean_answers числовыми ответами")
    answer = float(answer)
    assert abs(answer - expected_value) <= 1e-9, (
        f"Неверно: ожидалось {expected_value}, получено {answer}"
    )
print(f"OK: проверено ответов: {len(expected)}")
