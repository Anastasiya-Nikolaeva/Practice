import csv
import os
from typing import Any

import pandas as pd


def read_financial_operations_csv(file_name: str) -> Any:
    """
    Читает финансовые операции из файла CSV и возвращает их в виде списка словарей.

    Параметры:
    file_name (str): Имя файла CSV, содержащего финансовые операции.

    Возвращает:
    list: Список словарей, где каждый словарь представляет собой строку из файла CSV.
    Если файл не найден или произошла ошибка при чтении, возвращает пустой список.
    """
    file_path = os.path.join("..", "data", file_name)
    transactions = []

    try:
        with open(file_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                transactions.append(row)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    return transactions


def read_financial_operations_excel(file_name: str) -> Any:
    """
    Читает финансовые операции из файла Excel и возвращает их в виде списка словарей.

    Параметры:
    file_name (str): Имя файла Excel, содержащего финансовые операции.

    Возвращает:
    list: Список словарей, где каждый словарь представляет собой строку из файла Excel.
    Если файл не найден или произошла ошибка при чтении, возвращает пустой список.
    """
    file_path = os.path.join("..", "data", file_name)
    transactions: Any = []

    if not os.path.exists(file_path):
        print(f"Файл не найден: {file_path}")
        return transactions

    try:
        # Чтение данных из файла Excel
        df = pd.read_excel(file_path)  # Чтение данных из Excel файла
        transactions = df.to_dict(orient="records")  # Преобразование DataFrame в список словарей
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    return transactions


# if __name__ == "__main__":
#     excel_file_name = 'transactions_excel.xlsx'
#     transactions = read_financial_operations_excel(excel_file_name)
#     print(transactions)


# if __name__ == "__main__":
#     csv_transactions = 'transactions.csv'
#     transactions = read_financial_operations_csv(csv_transactions)
#     print(transactions)
