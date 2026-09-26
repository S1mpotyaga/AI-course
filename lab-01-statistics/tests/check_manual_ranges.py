expected_sum = [10, 5, 4]
expected_mean = [2.5, 2.5, 4]
expected_variance = [1.25, 0.25, 0]
answers = globals().get("range_answers")
if answers is None:
    raise AssertionError("Сначала заполните range_answers в предыдущей ячейке")
if len(answers) != 9:
    raise AssertionError("В range_answers нужно ввести 9 чисел")

expected = expected_sum + expected_mean + expected_variance
for answer, expected_value in zip(answers, expected):
    if answer is None:
        raise AssertionError("Замените все None в range_answers числовыми ответами")
    assert abs(float(answer) - expected_value) <= 1e-9, (
        f"Неверно: ожидалось {expected_value}, получено {answer}"
    )
print("OK: проверено ответов: 9")
