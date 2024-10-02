import json
import unittest
from typing import Any, Dict, List
from unittest.mock import mock_open, patch

from src.utils import load_transactions


class TestLoadTransactions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
    @patch("os.path.isfile", return_value=True)
    def test_load_transactions_valid_json(self, mock_isfile: Any, mock_file: Any) -> None:
        result: List[Dict[str, Any]] = load_transactions("dummy_path.json")
        expected: List[Dict[str, Any]] = [{"amount": 100, "currency": "USD"}]
        self.assertEqual(result, expected)

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    @patch("os.path.isfile", return_value=True)
    def test_load_transactions_empty_json(self, mock_isfile: Any, mock_file: Any) -> None:
        result: List[Dict[str, Any]] = load_transactions("dummy_path.json")
        expected: List[Dict[str, Any]] = []
        self.assertEqual(result, expected)

    @patch("builtins.open", new_callable=mock_open, read_data='{"not": "a list"}')
    @patch("os.path.isfile", return_value=True)
    def test_load_transactions_invalid_json(self, mock_isfile: Any, mock_file: Any) -> None:
        result: List[Dict[str, Any]] = load_transactions("dummy_path.json")
        expected: List[Dict[str, Any]] = []
        self.assertEqual(result, expected)

    @patch("os.path.isfile", return_value=False)
    def test_load_transactions_file_not_found(self, mock_isfile: Any) -> None:
        result: List[Dict[str, Any]] = load_transactions("dummy_path.json")
        expected: List[Dict[str, Any]] = []
        self.assertEqual(result, expected)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.isfile", return_value=True)
    def test_load_transactions_file_io_error(self, mock_isfile: Any, mock_file: Any) -> None:
        mock_file.side_effect = IOError("Ошибка ввода-вывода")
        result: List[Dict[str, Any]] = load_transactions("dummy_path.json")
        expected: List[Dict[str, Any]] = []
        self.assertEqual(result, expected)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.isfile", return_value=True)
    def test_load_transactions_json_decode_error(self, mock_isfile: Any, mock_file: Any) -> None:
        mock_file.side_effect = json.JSONDecodeError("Ошибка декодирования JSON", "", 0)
        result: List[Dict[str, Any]] = load_transactions("dummy_path.json")
        expected: List[Dict[str, Any]] = []
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
