from generator import TestGenerator
from check_utils import check, close, expect_value_error


def test_mean():
    generator = TestGenerator()
    for values in generator.cases():
        original = values.copy()
        close(mean_manual(values), generator.mean(values))
        assert values == original
    expect_value_error(mean_manual, [])


check("mean_manual", test_mean)
