from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_exceptions(dict_transactions: list[dict]) -> Any:
    result = filter_by_currency(dict_transactions, "EUR")
    assert list(result) == []
    result = filter_by_currency([], "EUR")
    assert result == "Список пустой!"


@pytest.mark.parametrize(
    "index, expected", [(0, "Перевод организации"), (1, "Перевод со счета на счет"), (2, "Перевод с карты на карту")]
)
def test_transaction_descriptions(index: int, expected: str) -> Any:
    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
    ]
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions[index] == expected


def test_card_number_generator() -> Any:
    generator = card_number_generator(start=0, stop=5)
    expected_numbers = [
        "0000 0000 0000 0000",
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
    ]

    for expected in expected_numbers:
        assert next(generator) == expected

    generator = card_number_generator(start=1234567800000000, stop=3)
    expected_numbers = ["1234 5678 0000 0000", "1234 5678 0000 0001", "1234 5678 0000 0002"]

    for expected in expected_numbers:
        assert next(generator) == expected
