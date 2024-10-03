import unittest
from typing import Any
from unittest.mock import mock_open, patch

import pandas as pd

from src.operation_finances import read_financial_operations_csv, read_financial_operations_excel


class TestFinancialOperations(unittest.TestCase):
    # Тестируем функцию чтения CSV файлов
    @patch("builtins.open", new_callable=mock_open, read_data="col1,col2\nval1,val2\nval3,val4")
    def test_read_financial_operations_csv(self, _mock_file: Any) -> None:
        result = read_financial_operations_csv("test.csv")
        expected = [{"col1": "val1", "col2": "val2"}, {"col1": "val3", "col2": "val4"}]
        self.assertEqual(result, expected)

    # Тестируем функцию чтения Excel файлов
    @patch("os.path.exists", return_value=True)
    @patch("pandas.read_excel")
    def test_read_financial_operations_excel(self, mock_read_excel: Any, _mock_exists: Any) -> None:
        mock_read_excel.return_value = pd.DataFrame({"col1": ["val1", "val2"], "col2": ["val3", "val4"]})

        result = read_financial_operations_excel("test.xlsx")
        expected = [{"col1": "val1", "col2": "val3"}, {"col1": "val2", "col2": "val4"}]
        self.assertEqual(result, expected)

    # Тестируем поведение функции при отсутствии файла
    @patch("os.path.exists", return_value=False)
    def test_read_financial_operations_excel_file_not_found(self, _mock_exists: Any) -> None:
        result = read_financial_operations_excel("non_existent_file.xlsx")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
