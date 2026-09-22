from generator import TestGenerator
from check_utils import check


SAMPLE_VALUES = [1, 2, 3, 5, 8]
SAMPLE_QUERIES = [[1, 5], [1, 3], [4, 5], [2, 2]]


def test_solver():
    generator = TestGenerator()
    MAXN = int(3e3) + 1
    MAXQ = int(3e3) + 1
    for _ in range(30):
        values = [generator.random.randint(1, MAXN) for _ in range(generator.random.randint(1, MAXN))]
        queries = [generator.interval(len(values)) for _ in range(MAXQ)]
        actual_lines = solve_text(len(values), values, len(queries), queries).splitlines()
        expected_lines = []
        for left, right in queries:
            expected = generator.skewness(values[left - 1:right])
            expected_lines.append("UNDEFINED" if expected is None else f"{expected:.9f}")
        assert len(actual_lines) == len(expected_lines)
        for actual, expected in zip(actual_lines, expected_lines):
            if expected == "UNDEFINED":
                assert actual == "UNDEFINED"
            else:
                assert actual != "UNDEFINED"
                assert abs(float(actual) - float(expected)) <= 1e-6

    expected = "0.621634858\n0.000000000\n0.000000000\nUNDEFINED"
    assert solve_text(5, SAMPLE_VALUES, 4, SAMPLE_QUERIES) == expected


check("solve_text", test_solver)
