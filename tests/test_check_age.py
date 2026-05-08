import pytest
from check_age import check_age


@pytest.mark.parametrize("age, expected", [
    (17, 'Доступ запрещён'),
    (18, 'Доступ разрешён'),
    (25, 'Доступ разрешён'),
    (-1, 'Доступ запрещён'),
    (0, 'Доступ запрещён'),
])
def test_check_age(age, expected):
    assert check_age(age) == expected
