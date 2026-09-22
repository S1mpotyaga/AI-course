from generator import TestGenerator
from check_utils import check, expect_value_error


def test_range_sum():
    generator = TestGenerator()
    for values in generator.cases():
        prefixes = generator.prefixes(values)
        left, right = generator.interval(len(values))
        assert range_sum(prefixes[0], left, right) == sum(values[left - 1:right])
    prefix = build_prefixes([1, 2, 3, 4])[0]
    expect_value_error(range_sum, prefix, 0, 2)
    expect_value_error(range_sum, prefix, 3, 2)


check("range_sum", test_range_sum)