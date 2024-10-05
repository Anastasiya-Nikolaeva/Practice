import csv
import json
import os
from datetime import datetime
from typing import Any, Dict, List

import pandas as pd


def load_transactions_from_json(file_path: str) -> Any:
    """
        Загружает транзакции из JSON-файла.

        :param file_path: Путь к JSON-файлу.
        :return: Список транзакций, загруженных из файла.
        """
    print(f"Загрузка транзакций из JSON-файла: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_transactions_from_csv(file_path: str) -> Any:
    """
        Загружает транзакции из CSV-файла.

        :param file_path: Путь к CSV-файлу.
        :return: Список транзакций, загруженных из файла.
        """
    print(f"Загрузка транзакций из CSV-файла: {file_path}")
    transactions = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            transactions = list(reader)  # Преобразуем reader в список
    except Exception as e:
        print(f"Ошибка при загрузке CSV-файла: {e}")
    return transactions


def load_transactions_from_xlsx(file_path: str) -> Any:
    """
        Загружает транзакции из XLSX-файла.

        :param file_path: Путь к XLSX-файлу.
        :return: Список транзакций, загруженных из файла.
        """
    print(f"Загрузка транзакций из XLSX-файла: {file_path}")
    return pd.read_excel(file_path).to_dict(orient="records")


def filter_transactions_by_status(transactions: List[Dict[str, Any]], state: str) -> Any:
    """
        Фильтрует транзакции по заданному состоянию.

        :param transactions: Список транзакций для фильтрации.
        :param state: Состояние, по которому необходимо выполнить фильтрацию.
        :return: Список транзакций, соответствующих заданному состоянию.
        """
    print(f"Фильтрация транзакций по состоянию: {state}")
    return [
        transaction
        for transaction in transactions
        if isinstance(transaction.get("state"), str) and transaction["state"].lower() == state.lower()
    ]


def sort_transactions(transactions: List[Dict[str, Any]], ascending: bool) -> Any:
    """
        Сортирует транзакции по дате.

        :param transactions: Список транзакций для сортировки.
        :param ascending: Флаг, указывающий порядок сортировки (True - по возрастанию, False - по убыванию).
        :return: Отсортированный список транзакций.
        """
    print(f"Сортировка транзакций по дате в {'возрастающем' if ascending else 'убывающем'} порядке.")
    return sorted(
        transactions, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%SZ"), reverse=not ascending
    )


def filter_transactions_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Any:
    """
        Фильтрует транзакции по заданной валюте.

        :param transactions: Список транзакций для фильтрации.
        :param currency: Код валюты, по которому необходимо выполнить фильтрацию.
        :return: Список транзакций, соответствующих заданной валюте.
        """
    print(f"Фильтрация транзакций по валюте: {currency}")
    return [
        transaction for transaction in transactions if transaction.get("currency_code", "").upper() == currency.upper()
    ]


def filter_transactions_by_description(transactions: List[Dict[str, Any]], keyword: str) -> Any:
    """
        Фильтрует транзакции по ключевому слову в описании.

        :param transactions: Список транзакций для фильтрации.
        :param keyword: Ключевое слово для фильтрации по описанию.
        :return: Список транзакций, содержащих заданное ключевое слово в описании.
        """
    print(f"Фильтрация транзакций по ключевому слову: {keyword}")
    return [
        transaction for transaction in transactions if keyword.lower() in transaction.get("description", "").lower()
    ]


def print_transactions(transactions: List[Dict[str, Any]]) -> None:
    """
        Выводит список транзакций на экран.

        :param transactions: Список транзакций для вывода.
        """
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print(f"Всего банковских операций в выборке: {len(transactions)}")
    for transaction in transactions:
        print(
            f"{transaction.get('date', 'Дата не указана')} " f"{transaction.get('description', 'Описание не указано')}"
        )
        print(
            f"{transaction.get('from', 'Отправитель не указан')} -> "
            f"{transaction.get('to', 'Получатель не указан')}"
        )

        # Получаем код валюты
        if "operationAmount" in transaction:
            currency_code = transaction["operationAmount"].get("currency", {}).get("code", "N/A")
            amount = transaction["operationAmount"].get("amount", "N/A")
        else:
            currency_code = transaction.get("currency_code", "N/A")
            amount = transaction.get("amount", "N/A")

        print(f"Сумма: {amount} {currency_code}\n")


def main() -> None:
    """
        Основная функция программы, которая управляет взаимодействием с пользователем
        и выполняет загрузку, фильтрацию и вывод транзакций.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    if choice == "1":
        file_path = os.path.join("..", "data", "operations.json")
        transactions = load_transactions_from_json(file_path)
    elif choice == "2":
        file_path = os.path.join("..", "data", "transactions.csv")
        transactions = load_transactions_from_csv(file_path)
    elif choice == "3":
        file_path = os.path.join("..", "data", "transactions_excel.xlsx")
        transactions = load_transactions_from_xlsx(file_path)
    else:
        print("Неверный выбор. Пожалуйста, выберите пункт из меню.")
        return

    # Фильтрация по состоянию
    available_states = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        state = input(
            "Введите состояние, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтрации состояния: EXECUTED, CANCELED, PENDING\nПользователь: "
        )

        if state.upper() in available_states:
            filtered_transactions = filter_transactions_by_status(transactions, state)
            print(f'Найдено {len(filtered_transactions)} транзакций с состоянием "{state}".')
            break
        else:
            print(f'Состояние операции "{state}" недоступно.')

        # Уточнение выборки операций
    sort_choice = input("Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    while sort_choice not in ["да", "нет", ""]:
        sort_choice = (
            input("Пожалуйста, введите 'Да', 'Нет' или оставьте пустым для пропуска.\nПользователь: ").strip().lower()
        )

    if sort_choice == "да":
        order_choice = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        while order_choice not in ["по возрастанию", "по убыванию"]:
            order_choice = (
                input("Пожалуйста, введите 'По возрастанию' или 'По убыванию'.\nПользователь: ").strip().lower()
            )
        ascending = order_choice == "по возрастанию"
        filtered_transactions = sort_transactions(filtered_transactions, ascending)

    currency_choice = input("Выводить только транзакции в определенной валюте? Да/Нет\nПользователь: ").strip().lower()
    while currency_choice not in ["да", "нет", ""]:
        currency_choice = (
            input("Пожалуйста, введите 'Да', 'Нет' или оставьте пустым для пропуска.\nПользователь: ").strip().lower()
        )

    if currency_choice == "да":
        currency_code = input("Введите код валюты (например, RUB, USD):\nПользователь: ").strip().upper()
        filtered_transactions = filter_transactions_by_currency(filtered_transactions, currency_code)

    description_choice = (
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ")
        .strip()
        .lower()
    )
    while description_choice not in ["да", "нет", ""]:
        description_choice = (
            input("Пожалуйста, введите 'Да', 'Нет' или оставьте пустым для пропуска.\nПользователь: ").strip().lower()
        )

    if description_choice == "да":
        keyword = input(
            "Введите слово для фильтрации по описанию (или оставьте пустым, чтобы пропустить):\nПользователь: "
        )
        if keyword:  # Проверяем, введено ли слово
            filtered_transactions = filter_transactions_by_description(filtered_transactions, keyword)

    # Вывод итогового списка транзакций
    print("Распечатываю итоговый список транзакций...")
    print_transactions(filtered_transactions)


# if __name__ == "__main__":
#     main()
