import numpy as np

from check_utils import check


def test_sum_matrice():
    rng = np.random.default_rng(20260922)
    for _ in range(30):
        n = int(rng.integers(1, 20))
        m = int(rng.integers(1, 20))
        matrix = rng.integers(-30, 31, size=(n, m)).tolist()
        q = int(rng.integers(1, 50))
        queries = []
        expected = []
        array = np.asarray(matrix, dtype=np.int64)
        for _ in range(q):
            left_x = int(rng.integers(1, n + 1))
            right_x = int(rng.integers(left_x, n + 1))
            left_y = int(rng.integers(1, m + 1))
            right_y = int(rng.integers(left_y, m + 1))
            queries.append([left_x, left_y, right_x, right_y])
            expected.append(str(array[left_x - 1:right_x, left_y - 1:right_y].sum()))

        actual = sum_matrice(n, m, matrix, q, queries)
        assert actual.splitlines() == expected

    matrix = [[1, 2], [3, 4]]
    assert sum_matrice(2, 2, matrix, 1, [[1, 1, 2, 2]]) == "10"


check("sum_matrice", test_sum_matrice)