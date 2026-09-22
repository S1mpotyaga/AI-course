from generator import TestGenerator
from check_utils import check, close, expect_value_error


def test_range_mean():
    generator = TestGenerator()
    for values in generator.cases():
        prefixes = generator.prefixes(values)
        left, right = generator.interval(len(values))
        close(range_mean(prefixes, left, right), generator.mean(values[left - 1:right]))
    prefixes = build_prefixes([1, 2, 3, 4])
    expect_value_error(range_mean, prefixes, 0, 2)


check("range_mean", test_range_mean)