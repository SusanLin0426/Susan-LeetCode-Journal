from lc.medium.lc062_unique_paths import unique_paths

def test_examples():
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3

def test_edges():
    assert unique_paths(1, 1) == 1
    assert unique_paths(1, 5) == 1
    assert unique_paths(5, 1) == 1
    assert unique_paths(0, 4) == 0
    assert unique_paths(4, 0) == 0

def test_more():
    assert unique_paths(2, 2) == 2     # RD, DR
    assert unique_paths(3, 3) == 6
    assert unique_paths(7, 3) == 28
