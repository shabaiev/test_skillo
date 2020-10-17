import pytest


@pytest.mark.data_structure
def test_positive_1():
    set1 = {"canon", "fujifilm", "sony"}
    set1.add("nikon")
    assert set1 == {"canon", "fujifilm", "sony", "nikon"}


@pytest.mark.data_structure
def test_positive_2():
    set1 = {"canon", "fujifilm", "sony"}
    set1.update(["nikon", "pentax", "leica"])
    assert set1 == {"canon", "fujifilm", "sony", "nikon", "pentax", "leica"}


@pytest.mark.data_structure
def test_positive_3():
    set1 = {"canon", "fujifilm", "sony", "leica"}
    set1.remove("leica")
    assert set1 == {"canon", "fujifilm", "sony"}


@pytest.mark.data_structure
def test_positive_4():
    set1 = {"canon", "fujifilm", "sony", "leica", "nikon", "olympus"}
    assert (len(set1)) == 6


@pytest.mark.data_structure
def test_positive_5():
    set1 = {"canon", "fujifilm", "sony", "leica", "nikon", "olympus"}
    set1.clear()
    assert set1 == set()


def combine_set(a, b):
    return a.union(b)


@pytest.mark.data_structure
@pytest.mark.parametrize("set1, set2, result",
                         [({"Aaron", "Jack", "Bob"}, {989, 211, 352}, {352, 'Jack', 'Bob', 'Aaron', 211, 989})])
def test_positive_6(set1, set2, result):
    assert combine_set(set1, set2) == result

