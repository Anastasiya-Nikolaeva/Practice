from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Возвращает замаскированный номер карты"""
    return f"{card_number[:4]} {card_number[4:6]}{"*" * 2} {"*" * 4} {card_number[12:]}"


def get_mask_account(mask_account: Union[str]) -> Union[str]:
    """Возвращает замаскированный номер счёта"""
    list_number_account_user = ["**"]
    list_number_account_user += mask_account[-4:]
    mask_account_user = "".join(list_number_account_user)
    return mask_account_user
