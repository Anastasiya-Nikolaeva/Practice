import re
from collections import Counter
from typing import Any, Dict, List


def filter_transactions(transactions: List[Dict[str, Any]], search_string: str) -> Any:
    """
    Фильтрует список транзакций по строке поиска в описании.

    :param transactions: Список словарей с данными о транзакциях.
    :param search_string: Строка для поиска в описании транзакций.
    :return: Список словарей, в которых описание содержит строку поиска.
    """
    filtered_transactions = []
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)  # Регулярное выражение для поиска

    for transaction in transactions:
        if "description" in transaction and pattern.search(transaction["description"]):
            filtered_transactions.append(transaction)

    return filtered_transactions


def count_operations_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Any:
    """
    Подсчитывает количество операций в каждой категории.

    :param transactions: Список словарей с данными о транзакциях.
    :param categories: Список категорий для подсчета.
    :return: Словарь с категориями и количеством операций в каждой категории.
    """
    category_count: Counter = Counter()  # Инициализация Counter для подсчета категорий

    for transaction in transactions:
        description = transaction.get("description", "")
        for category in categories:
            if category in description:
                category_count[category] += 1  # Увеличиваем счетчик для соответствующей категории

    return dict(category_count)  # Преобразуем Counter обратно в обычный словарь


# if __name__ == "__main__":
#     # Пример тестовых данных
#     transactions = [
#         {'description': 'Перевод на счет 12345', 'amount': 100},
#         {'description': 'Оплата за услуги', 'amount': 200},
#         {'description': 'Перевод на счет 67890', 'amount': 150},
#         {'description': 'Покупка в магазине', 'amount': 50},
#         {'description': 'Оплата за интернет', 'amount': 75},
#     ]
#
#     categories = ['в магазине', 'за услуги', 'на счет', 'за интернет']
#

#     # Проверка функции filter_transactions
#     search_string = 'перевод'
#     filtered = filter_transactions(transactions, search_string)
#     print("Отфильтрованные транзакции:", filtered)
#

#     # Проверка функции count_operations_by_category
#     category_counts = count_operations_by_category(transactions, categories)
#     print("Количество операций по категориям:", category_counts)
