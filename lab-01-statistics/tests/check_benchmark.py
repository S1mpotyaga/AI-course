from generator import TestGenerator
from check_utils import check


def test_benchmark():
    generator = TestGenerator()
    for n, q in [(10, 5), (25, 10), (50, 20)]:
        result = benchmark(n=n, q=q)
        assert isinstance(result, tuple)
        assert len(result) == 2
        slow_time, fast_time = result
        assert slow_time >= 0
        assert fast_time >= 0

    values = generator.values(5, 5)
    assert len(values) == 5


check("benchmark", test_benchmark)