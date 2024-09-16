import unittest
from typing import Any, Dict
from unittest.mock import Mock, patch

import requests

from src.external_api import convert_transaction_to_rub


class TestCurrencyConverter(unittest.TestCase):

    @patch("src.external_api.requests.get")
    def test_convert_transaction_to_rub_success(self, mock_get: Mock) -> None:
        # Настройка мока для успешного ответа
        mock_response = Mock()
        mock_response.json.return_value = {"result": 100.0}
        mock_get.return_value = mock_response

        transaction: Dict[str, Any] = {"amount": 100, "currency": "USD"}
        result: float = convert_transaction_to_rub(transaction)

        self.assertEqual(result, 100.0)
        mock_get.assert_called_once()

    @patch("src.external_api.requests.get")
    def test_convert_transaction_to_rub_invalid_currency(self, mock_get: Mock) -> None:
        transaction: Dict[str, Any] = {"amount": 100, "currency": "GBP"}

        with self.assertRaises(ValueError) as context:
            convert_transaction_to_rub(transaction)

        self.assertEqual(str(context.exception), "Currency not supported for conversion.")

    @patch("src.external_api.requests.get")
    def test_convert_transaction_to_rub_api_error(self, mock_get: Mock) -> None:
        # Настройка мока для имитации ошибки API
        mock_get.side_effect = requests.exceptions.RequestException("API error")

        transaction: Dict[str, Any] = {"amount": 100, "currency": "USD"}

        with self.assertRaises(requests.exceptions.RequestException) as context:
            convert_transaction_to_rub(transaction)

        self.assertEqual(str(context.exception), "API error")


if __name__ == "__main__":
    unittest.main()
