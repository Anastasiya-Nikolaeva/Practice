import json
import logging
import os
from typing import Any, Dict, List

logger = logging.getLogger("TransactionLogger")
logger.setLevel(logging.DEBUG)


file_handler = logging.FileHandler("../logs/transactions.log", mode="w")
file_handler.setLevel(logging.DEBUG)


file_formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)


logger.addHandler(file_handler)


def load_transactions(file_path: str = "../data/operations.json") -> List[Dict[str, Any]]:
    """
    Загружает финансовые транзакции из указанного JSON-файла.

    :param file_path: Путь к JSON-файлу (по умолчанию "data/operations.json").
    :return: Список словарей с данными о транзакциях или пустой список.
    """
    if not os.path.isfile(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                logger.info(f"Успешно загружено {len(data)} транзакций из файла: {file_path}")
                return data
            else:
                logger.warning("Данные не являются списком.")
                return []
    except json.JSONDecodeError as e:
        logger.error("Ошибка декодирования JSON: %s", e)
        return []
    except IOError as e:
        logger.error("Ошибка ввода-вывода: %s", e)
        return []


# if __name__ == '__main__':
#     # Вызываем функцию и выводим результат
#     transactions = load_transactions()
#     print("Загруженные транзакции:", transactions)
