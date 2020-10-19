import pytest


@pytest.mark.data_structure
def test_positive1(dictionary):
    device = {
        "brand": "apple",
        "hd": 255,
        "year": 2020
    }
    assert (device["hd"]) == 255


@pytest.mark.data_structure
def test_positive2(dictionary):
    device = {
        "brand": "apple",
        "hd": 255,
        "year": 2020
    }
    device["hd"] = 512
    assert (device["hd"]) == 512


@pytest.mark.data_structure
def test_positive3(dictionary):
    device = {
        "brand": "apple",
        "hd": 255,
        "year": 2020
    }
    assert (len(device)) == 3


@pytest.mark.data_structure
def test_positive4(dictionary):
    device = {
        "brand": "apple",
        "hd": 255,
        "year": 2020
    }
    del device["hd"]
    assert device == {"brand": "apple",
                      "year": 2020}


def find_year_difference(a, b):
    return a - b


device1 = {
    "brand": "apple",
    "hd": 256,
    "year": 2020
}

device2 = {
    "brand": "apple",
    "hd": 255,
    "year": 1993
}


@pytest.mark.data_structure
@pytest.mark.parametrize("d1, d2, expected_result", [(device1["year"], device2["year"], 27)])
def test_positive_6(d1, d2, expected_result):
    assert find_year_difference(d1, d2) == expected_result
