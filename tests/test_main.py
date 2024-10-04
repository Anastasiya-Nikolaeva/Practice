import unittest
from typing import Any, Dict, List
from unittest.mock import mock_open, patch

import pandas as pd

from src.main import (
    filter_transactions_by_currency,
    filter_transactions_by_description,
    filter_transactions_by_status,
    load_transactions_from_csv,
    load_transactions_from_json,
    load_transactions_from_xlsx,
    print_transactions,
    sort_transactions,
)


class TestTransactionFunctions(unittest.TestCase):

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='[{"date": "2023-01-01T12:00:00Z", ' '"state": "EXECUTED", "description": "Тестовая транзакция"}]',
    )
    def test_load_transactions_from_json(self, _mock_file: Any) -> None:
        result: List[Dict[str, Any]] = load_transactions_from_json("dummy_path.json")
        expected: List[Dict[str, Any]] = [
            {"date": "2023-01-01T12:00:00Z", "state": "EXECUTED", "description": "Тестовая транзакция"}
        ]
        self.assertEqual(result, expected)

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="date;state;description\n" "2023-01-01T12:00:00Z;EXECUTED;Тестовая транзакция",
    )
    def test_load_transactions_from_csv(self, _mock_file: Any) -> None:
        result: List[Dict[str, Any]] = load_transactions_from_csv("dummy_path.csv")
        expected: List[Dict[str, Any]] = [
            {"date": "2023-01-01T12:00:00Z", "state": "EXECUTED", "description": "Тестовая транзакция"}
        ]
        self.assertEqual(result, expected)

    @patch("pandas.read_excel")
    def test_load_transactions_from_xlsx(self, mock_read_excel: Any) -> None:
        mock_read_excel.return_value = pd.DataFrame(
            [{"date": "2023-01-01T12:00:00Z", "state": "EXECUTED", "description": "Тестовая транзакция"}]
        )
        result: List[Dict[str, Any]] = load_transactions_from_xlsx("dummy_path.xlsx")
        expected: List[Dict[str, Any]] = [
            {"date": "2023-01-01T12:00:00Z", "state": "EXECUTED", "description": "Тестовая транзакция"}
        ]
        self.assertEqual(result, expected)

    def test_filter_transactions_by_status(self) -> None:
        transactions: List[Dict[str, Any]] = [
            {"date": "2023-01-01T12:00:00Z", "state": "EXECUTED"},
            {"date": "2023-01-02T12:00:00Z", "state": "CANCELED"},
        ]
        result: List[Dict[str, Any]] = filter_transactions_by_status(transactions, "EXECUTED")
        expected: List[Dict[str, Any]] = [{"date": "2023-01-01T12:00:00Z", "state": "EXECUTED"}]
        self.assertEqual(result, expected)

    def test_sort_transactions(self) -> None:
        transactions: List[Dict[str, Any]] = [
            {"date": "2023-01-02T12:00:00Z"},
            {"date": "2023-01-01T12:00:00Z"},
        ]
        result: List[Dict[str, Any]] = sort_transactions(transactions, ascending=True)
        expected: List[Dict[str, Any]] = [
            {"date": "2023-01-01T12:00:00Z"},
            {"date": "2023-01-02T12:00:00Z"},
        ]
        self.assertEqual(result, expected)

    def test_filter_transactions_by_currency(self) -> None:
        transactions: List[Dict[str, Any]] = [
            {"currency_code": "USD"},
            {"currency_code": "EUR"},
        ]
        result: List[Dict[str, Any]] = filter_transactions_by_currency(transactions, "USD")
        expected: List[Dict[str, Any]] = [{"currency_code": "USD"}]
        self.assertEqual(result, expected)

    def test_filter_transactions_by_description(self) -> None:
        transactions: List[Dict[str, Any]] = [
            {"description": "Тестовая транзакция"},
            {"description": "Другая транзакция"},
        ]
        result: List[Dict[str, Any]] = filter_transactions_by_description(transactions, "тестовая")
        expected: List[Dict[str, Any]] = [{"description": "Тестовая транзакция"}]
        self.assertEqual(result, expected)


def test_print_transactions(capsys: Any) -> None:
    transactions: List[Dict[str, Any]] = [
        {
            "date": "2023-01-01T12:00:00Z",
            "description": "Тестовая транзакция",
            "from": "Alice",
            "to": "Bob",
            "operationAmount": {"currency": {"code": "USD"}, "amount": 100},
        },
        {
            "date": "2023-01-02T12:00:00Z",
            "description": "Другая транзакция",
            "from": "Charlie",
            "to": "David",
            "operationAmount": {"currency": {"code": "EUR"}, "amount": 200},
        },
    ]
    print_transactions(transactions)
    captured = capsys.readouterr()
    expected_output = (
        "Всего банковских операций в выборке: 2\n"
        "2023-01-01T12:00:00Z Тестовая транзакция\n"
        "Alice -> Bob\n"
        "Сумма: 100 USD\n\n"
        "2023-01-02T12:00:00Z Другая транзакция\n"
        "Charlie -> David\n"
        "Сумма: 200 EUR\n\n"
    )
    assert captured.out == expected_output


def test_print_transactions_empty(capsys: Any) -> None:
    transactions: List[Dict[str, Any]] = []
    print_transactions(transactions)
    captured = capsys.readouterr()
    expected_output = "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.\n"
    assert captured.out == expected_output


if __name__ == "__main__":
    unittest.main()
