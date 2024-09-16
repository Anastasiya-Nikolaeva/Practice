import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_currency}&amount={amount}"
API_KEY = os.getenv("API_KEY")


def convert_transaction_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует транзакцию в рубли.

    :param transaction: Словарь с данными о транзакции, должен содержать ключи 'amount' и 'currency'.
    :return: Сумма в рублях.
    :raises ValueError: Если валюта не поддерживается.
    """
    amount = transaction["amount"]
    currency = transaction["currency"]

    if currency == "RUB":
        return amount

    if currency not in ["USD", "EUR"]:
        raise ValueError("Currency not supported for conversion.")

    url = API_URL.format(to="RUB", from_currency=currency, amount=amount)
    headers = {"apikey": API_KEY}

    try:
        response = requests.get(url, headers=headers, timeout=20)  # Тайм-аут 20 секунд

        data = response.json()
        return float(data["result"])
    except Exception as e:
        print(f"Ошибка: {e}")
        raise


# if __name__ == "__main__":
#     transaction = {
#         'amount': 300,
#         'currency': 'RUB'
#     }
#
#     result = convert_transaction_to_rub(transaction)
#     print(f"Сумма в рублях: {result}")
