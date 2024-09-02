import random
from typing import Union, Any


def filter_by_currency(transactions: list[dict], currency: str = "USD") -> Any:
    """Функция принимает на вход список словарей, и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    if len(transactions) > 0:
        filtered_transactions: Any = filter(
            lambda transactions_list: transactions_list.get("operationAmount").get("currency").get("code") ==
            currency, transactions)
        return filtered_transactions
    else:
        return "Список пустой!"


def transaction_descriptions(transactions: list[dict]) -> Any:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for description_operation in transactions:
        yield description_operation.get("description")
    try:
        for description_operation in transactions:
            description_operation.get("description")
            yield "Больше нет транзакций"
    except StopIteration:
        return "Нет транзакций"


def card_number_generator(start: Union[int] = 0, stop: Union[int] = 9) -> str:
    """Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    digits = [random.randint(start, stop) for _ in range(16)]
    grouped_string = " ".join("".join(map(str, digits[i: i + 4])) for i in range(0, 16, 4))
    return grouped_string


for _ in range(5):
    print(card_number_generator())
