import pytest


@pytest.mark.data_structure
def test_positive1():
    tuple1 = ("bmw", "mercedes", "lexus")
    assert tuple1[2] == "lexus"


@pytest.mark.data_structure
def test_positive2():
    tuple1 = ("bmw", "mercedes", "lexus", "ferrari", "subaru")
    assert tuple1[::-1] == ("subaru", "ferrari", "lexus", "mercedes", "bmw")


@pytest.mark.data_structure
def test_positive3():
    tuple1 = ("bmw", "mercedes", "lexus", "ferrari", "subaru")
    assert len(tuple1) == 5


@pytest.mark.data_structure
def test_positive4():
    tuple1 = ("bmw", "mercedes", "bmw", "lexus", "ferrari", "bmw", "subaru")
    count = tuple1.count("bmw")
    assert count == 3


def combine_tuples(a, b):
    return a + b


eastern_eur = ("Kyiv", "Minsk", "Warsaw")
western_eur = ("London", "Paris", "Berlin")


@pytest.mark.data_structure
@pytest.mark.parametrize("t1, t2, result", [(western_eur, eastern_eur, ("London", "Paris", "Berlin",
                                                                        "Kyiv", "Minsk", "Warsaw"))])
def test_positive_5(t1, t2, result):
    assert combine_tuples(t1, t2) == result



