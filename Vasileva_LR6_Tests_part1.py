import pytest
from Vasileva_LR6_Methods_part1 import *


@pytest.mark.parametrize("stroka, expected", [("", False), ("-8", False), ("a", False), ("a4", False), ("5.6", False),
                                              ("-0", False), ("4a", False), ("1", True)])
def test_input_integer(stroka, expected):
    assert is_digit_not_negative(stroka) == expected

@pytest.mark.parametrize("q, p, expected", [(8, 3, 2), (9, 2, 1)])
def test_mod_q_p (q, p, expected):
    assert mod_Q_on_P(q, p) == expected


@pytest.mark.parametrize("q, p, expected", [(9, 2, 4), (10, 3, 3)])
def test_div_q_p (q, p, expected):
    assert div_Q_on_P(q, p) == expected










#
#
#
#
# import pytest
# from Vasileva_LR6_Methods_part1 import *
#
#
# @pytest.mark.parametrize("stroka, expected", [("", False), ("-8", False), ("a", False), ("a4", False), ("5.6", False),
#                                               ("-0", False), ("4a", False)])
# def test_input_integer(stroka, expected):
#     assert is_digit_not_negative(stroka) == expected
#
# @pytest.mark.parametrize("q, p, expected", [(8, 3, 2), (9, 2, 1)])
# def test_mod_q_p (q, p, expected):
#     assert mod_Q_on_P(q, p) == expected
#
#
# @pytest.mark.parametrize("q, p, expected", [(9, 2, 4), (10, 3, 3)])
# def test_div_q_p (q, p, expected):
#     assert div_Q_on_P(q, p) == expected

