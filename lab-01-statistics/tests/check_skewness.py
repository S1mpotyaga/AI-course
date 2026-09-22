from generator import TestGenerator
from check_utils import check, close, expect_value_error


def test_skewness():
    generator = TestGenerator()
    for values in generator.cases():
        expected = generator.skewness(values)
        actual = skewness_manual(values)
        if expected is None:
            assert actual is None
        else:
            close(actual, expected)
    expect_value_error(skewness_manual, [])


check("skewness_manual", test_skewness)
