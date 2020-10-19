import pytest


@pytest.mark.data_structure
def test_positive_1(list1):
    list1.append("honda")
    list1.append("toyota")
    list1.append("mazda")
    assert list1[1] == "toyota"


@pytest.mark.data_structure
def test_positive_2():
    colors = ["orange", "black", "green", "blue", "red"]
    assert len(colors) == 5


@pytest.mark.data_structure
def test_positive_3():
    colors = ["orange", "black", "green", "blue", "red"]
    assert (colors[-1]) == "red"


@pytest.mark.data_structure
def test_positive_4():
    colors = ["orange", "black", "green", "blue", "red"]
    assert colors[-3:] == ["green", "blue", "red"]


@pytest.mark.data_structure
def test_positive_5():
    colors = ["orange", "black", "green", "blue", "red"]
    assert colors.pop() == "red"


def join_list(a, b):
    return a + b


@pytest.mark.data_structure
@pytest.mark.parametrize("list1, list2, expected_result", [(["CA", "IL", "NY", "MN"], [76.3, 5, None, 2],
                                                            ['CA', 'IL', 'NY', 'MN', 76.3, 5, None, 2])])
def test_positive_6(list1, list2, expected_result):
    assert join_list(list1, list2) == expected_result
