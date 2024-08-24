from datetime import datetime
from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_number: Union[str]) -> str:
    """Функция маскировки карт или счетов"""
    if len(user_number.split()[-1]) == 20:
        new_number = get_mask_account(user_number)
        result = user_number[:-20] + new_number
    elif len(user_number.split()[-1]) == 16:
        new_number = get_mask_card_number(user_number.split()[-1])
        result = user_number[:-16] + new_number
    return result


def get_date(user_date: Union[str]) -> str:
    """Функция получения даты в определенном формате и возвращения в формате ДД.ММ.ГГГГ"""
    date_format = datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    return new_date