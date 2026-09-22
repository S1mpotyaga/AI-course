from generator import TestGenerator
from check_utils import check, close, expect_value_error


def test_median():
    generator = TestGenerator()
    for values in generator.cases():
        original = values.copy()
        close(median_manual(values), generator.median(values))
        assert values == original
    expect_value_error(median_manual, [])


check("median_manual", test_median)
