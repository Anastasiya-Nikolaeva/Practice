import json
import os
from typing import Any, Dict, List


def load_transactions(file_path: str = "../data/operations.json") -> List[Dict[str, Any]]:
    """
    Загружает финансовые транзакции из указанного JSON-файла.

    :param file_path: Путь к JSON-файлу (по умолчанию "data/operations.json").
    :return: Список словарей с данными о транзакциях или пустой список.
    """
    # Проверяем, существует ли файл
    if not os.path.isfile(file_path):
        print(f"Файл не найден: {file_path}")
        return []

    try:
        # Открываем файл и загружаем данные
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            # Проверяем, является ли загруженные данные списком
            if isinstance(data, list):
                return data
            else:
                print("Данные не являются списком.")
                return []
    except json.JSONDecodeError as e:
        print("Ошибка декодирования JSON:", e)
        return []
    except IOError as e:
        print("Ошибка ввода-вывода:", e)
        return []

# if __name__ == '__main__':
#     # Вызываем функцию и выводим результат
#     transactions = load_transactions()
#     print("Загруженные транзакции:", transactions)
