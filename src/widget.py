from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_number: Union[str]) -> str:
    """Функция маскировки карт или счетов"""
    if len(user_number.split()[-1]) == 20:
        new_number = get_mask_account(user_number)
        return f"{user_number[:-20]} {new_number}"
    elif len(user_number.split()[-1]) == 16:
        new_number = get_mask_card_number(user_number.split()[-1])
        return f"{user_number[:-16]} {new_number}"
