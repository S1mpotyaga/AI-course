from generator import TestGenerator
from check_utils import check, close, expect_value_error


def test_std_manual():
    generator = TestGenerator()
    for values in generator.cases():
        close(std_manual(values), generator.std(values))
    expect_value_error(std_manual, [])


check("std_manual", test_std_manual)
