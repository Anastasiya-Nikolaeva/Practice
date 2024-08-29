import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "num, expected_result",
    [
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет73654108430135874305", "Счет **4305"),
        ("", "Вы ввели пустой запрос"),
        ("VisaGold5999414228426353", "Неверный ввод данных"),
        ("Visa Gold 59994214228426353", "Неверный ввод данных"),
        ("Счет736541084301358743056", "Неверный ввод данных"),
    ],
)
def test_mask_account_card(num: str, expected_result: str) -> None:
    assert mask_account_card(num) == expected_result


def test_get_data() -> None:
    assert get_date("2020-10-10T10:10:10.0") == "10.10.2020"
