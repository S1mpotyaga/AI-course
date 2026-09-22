from generator import TestGenerator
from check_utils import check, close, expect_value_error


def test_raw_moment():
    generator = TestGenerator()
    for values in generator.cases():
        order = generator.moment_order()
        close(raw_moment(values, order), generator.raw_moment(values, order))
    expect_value_error(raw_moment, [], 2)


check("raw_moment", test_raw_moment)