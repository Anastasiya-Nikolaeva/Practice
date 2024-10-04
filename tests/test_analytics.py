import unittest
from typing import Dict, List

from src.analytics import count_operations_by_category, filter_transactions


class TestTransactionFunctions(unittest.TestCase):

    def setUp(self) -> None:
        # Подготовка тестовых данных
        self.transactions: List[Dict[str, str]] = [
            {"description": "Оплата за интернет"},
            {"description": "Перевод на карту"},
            {"description": "Оплата за мобильную связь"},
            {"description": "Покупка в магазине"},
            {"description": "Оплата за коммунальные услуги"},
        ]
        self.categories: List[str] = ["интернет", "мобильная связь", "магазин", "коммунальные услуги"]

    def test_filter_transactions(self) -> None:
        # Тестирование функции filter_transactions
        search_string: str = "оплата"
        expected_result: List[Dict[str, str]] = [
            {"description": "Оплата за интернет"},
            {"description": "Оплата за мобильную связь"},
            {"description": "Оплата за коммунальные услуги"},
        ]
        result: List[Dict[str, str]] = filter_transactions(self.transactions, search_string)
        self.assertEqual(result, expected_result)

        # Тестирование с пустой строкой
        search_string = ""
        expected_result = self.transactions  # Все транзакции должны быть возвращены
        result = filter_transactions(self.transactions, search_string)
        self.assertEqual(result, expected_result)

        # Тестирование с отсутствующим значением
        search_string = "неизвестно"
        expected_result = []  # Ничего не должно быть найдено
        result = filter_transactions(self.transactions, search_string)
        self.assertEqual(result, expected_result)

    def test_count_operations_by_category(self) -> None:
        # Тестирование функции count_operations_by_category
        expected_result: Dict[str, int] = {
            "интернет": 1,
            "магазин": 1,
            "коммунальные услуги": 1,
        }
        result: Dict[str, int] = count_operations_by_category(self.transactions, self.categories)
        self.assertEqual(result, expected_result)

        # Тестирование с пустым списком категорий
        expected_result = {}
        result = count_operations_by_category(self.transactions, [])
        self.assertEqual(result, expected_result)

        # Тестирование с отсутствующими категориями
        unknown_categories: List[str] = ["неизвестно"]
        expected_result = {}
        result = count_operations_by_category(self.transactions, unknown_categories)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
