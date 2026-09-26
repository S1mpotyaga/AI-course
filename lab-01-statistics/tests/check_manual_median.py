expected = [7, 5, 3]
answers = globals().get("median_answers")
if answers is None:
    raise AssertionError("Сначала заполните median_answers в предыдущей ячейке")
if len(answers) != len(expected):
    raise AssertionError(f"Нужно ввести {len(expected)} ответа")

print("Ручная проверка медианы")
for answer, expected_value in zip(answers, expected):
    if answer is None:
        raise AssertionError("Замените все None в median_answers числовыми ответами")
    answer = float(answer)
    assert abs(answer - expected_value) <= 1e-9, (
        f"Неверно: ожидалось {expected_value}, получено {answer}"
    )
print(f"OK: проверено ответов: {len(expected)}")
