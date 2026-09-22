from generator import TestGenerator
from check_utils import check, close, expect_value_error


def test_central_moment():
    generator = TestGenerator()
    for values in generator.cases():
        order = generator.moment_order()
        close(central_moment(values, order), generator.central_moment(values, order))
    expect_value_error(central_moment, [], 2)


check("central_moment", test_central_moment)