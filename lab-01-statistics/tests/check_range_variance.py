from generator import TestGenerator
from check_utils import check, close, expect_value_error


def test_range_variance():
    generator = TestGenerator()
    for values in generator.cases():
        prefixes = generator.prefixes(values)
        left, right = generator.interval(len(values))
        close(range_variance(prefixes, left, right), generator.variance(values[left - 1:right]))
    prefixes = build_prefixes([1, 2, 3, 4])
    expect_value_error(range_variance, prefixes, 3, 2)


check("range_variance", test_range_variance)