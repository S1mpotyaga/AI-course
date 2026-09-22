from generator import TestGenerator
from check_utils import check, close, expect_value_error


def test_integer_skewness():
    generator = TestGenerator()
    for values in generator.cases(50):
        shifted = [10**12 + value for value in values]
        prefixes = build_prefixes(shifted)
        left, right = generator.interval(len(values))
        expected = generator.skewness(values[left - 1:right])
        actual = range_skewness_integer(prefixes, left, right)
        if expected is None:
            assert actual is None
        else:
            close(actual, expected, tolerance=1e-7)
    prefixes = build_prefixes([10**12] * 3)
    assert range_skewness_integer(prefixes, 1, 3) is None
    expect_value_error(range_skewness_integer, prefixes, 0, 2)


check("range_skewness_integer", test_integer_skewness)
