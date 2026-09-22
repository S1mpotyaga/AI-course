from generator import TestGenerator
from check_utils import check


def test_prefixes():
    generator = TestGenerator()
    for values in generator.cases():
        expected = tuple([int(value) for value in prefix] for prefix in generator.prefixes(values))
        assert build_prefixes(values) == expected
    assert build_prefixes([]) == ([0], [0], [0])


check("build_prefixes", test_prefixes)
