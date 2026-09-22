from generator import TestGenerator
from check_utils import check, close, expect_value_error


def test_range_skewness():
    generator = TestGenerator()
    for values in generator.cases():
        prefixes = generator.prefixes(values)
        left, right = generator.interval(len(values))
        expected = generator.skewness(values[left - 1:right])
        actual = range_skewness(prefixes, left, right)
        if expected is None:
            assert actual is None
        else:
            close(actual, expected)
    prefixes = build_prefixes([1, 2, 4])
    assert range_skewness(prefixes, 1, 1) is None
    expect_value_error(range_skewness, prefixes, 0, 2)


check("range_skewness", test_range_skewness)
