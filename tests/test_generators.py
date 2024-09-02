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
    result = card_number_generator()
    # Проверяем, что результат является строкой
    assert isinstance(result, str), "Результат должен быть строкой"
    # Проверяем, что строка состоит из 4 групп по 4 цифры
    groups = result.split()
    assert len(groups) == 4, "Должно быть 4 группы"
    for group in groups:
        assert len(group) == 4, "Каждая группа должна содержать 4 цифры"
        assert group.isdigit(), "Группа должна содержать только цифры"
