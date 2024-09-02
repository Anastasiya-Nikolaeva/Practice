from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Возвращает замаскированный номер карты"""
    if card_number != "":
        new_number = card_number.replace(" ", "")
        if new_number.isdigit():
            if len(new_number) == 16:
                return f"{new_number[:4]} {new_number[4:6]}{"*" * 2} {"*" * 4} {new_number[12:]}"
            return "Номер карты неверный"
        return "Необходимо ввести 16-значный номер цифрами"
    return "Вы ввели пустой запрос"


def get_mask_account(mask_account: Union[str]) -> Union[str]:
    """Возвращает замаскированный номер счёта"""
    list_number_account_user = ["**"]
    if mask_account != "":
        new_number_account = mask_account.replace(" ", "")
        if new_number_account.isdigit():
            if len(new_number_account) == 20:
                list_number_account_user += new_number_account[-4:]
                mask_account_user = "".join(list_number_account_user)
                return mask_account_user
            return "Номер счёта неверный"
        return "Необходимо ввести 20-значный номер цифрами"
    return "Вы ввели пустой запрос"
