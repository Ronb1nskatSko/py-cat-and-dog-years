
from app.main import get_human_age


def test_zero_years() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_age_below_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_age_at_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_age_at_second_threshold_minus_one() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_age_at_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_different_thresholds() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_cat_age_first_extra_year() -> None:
    assert get_human_age(28, 29) == [3, 3]


def test_cat_age_before_extra_year() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_large_age() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_cat_age_independently() -> None:
    assert get_human_age(32, 0) == [4, 0]


def test_dog_age_independently() -> None:
    assert get_human_age(0, 34) == [0, 4]


def test_different_cat_and_dog_ages() -> None:
    assert get_human_age(24, 29) == [2, 3]
