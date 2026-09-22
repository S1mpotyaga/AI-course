from generator import TestGenerator
from check_utils import check, close, expect_value_error


def test_variance_via_sums():
    generator = TestGenerator()
    for values in generator.cases():
        close(variance_via_sums(values), generator.variance(values))
    expect_value_error(variance_via_sums, [])


check("variance_via_sums", test_variance_via_sums)
