from stud.main import division
import pytest


@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (20, 10, 2),
                                                   (30, -10, -3),
                                                   (5, 2.5, 2)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


@pytest.mark.parametrize('expected_exception, divider, divisional',
                         [(ZeroDivisionError, 0, 10),
                          (TypeError, '2', 20)])
def test_with_error(expected_exception, divider, divisional):
    with pytest.raises(ZeroDivisionError):
        division(divisional, divider)


