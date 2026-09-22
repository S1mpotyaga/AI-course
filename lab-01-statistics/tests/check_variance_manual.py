from generator import TestGenerator
from check_utils import check, close, expect_value_error


def test_variance_manual():
    generator = TestGenerator()
    for values in generator.cases():
        close(variance_manual(values), generator.variance(values))
    expect_value_error(variance_manual, [])


check("variance_manual", test_variance_manual)
