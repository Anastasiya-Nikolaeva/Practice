from datetime import datetime
from typing import Any, Union

from src.masks import get_mask_card_number


def mask_account_card(user_number: Union[str]) -> str:
    """Функция маскировки карт или счетов"""
    if user_number != "":
        new_number = user_number.replace(" ", "")
        if new_number[-20:].isdigit():
            if new_number[-20:].isdigit() and len(new_number) == 24:
                mask_num = ["**"]
                mask_num += new_number[-4:]
                mask_account_user = "".join(mask_num)
                return new_number[:4] + " " + mask_account_user
            return "Неверный ввод данных"
        elif len(user_number.split()[-1]) == 16:
            new_number = get_mask_card_number(user_number.split()[-1])
            result = user_number[:-16] + new_number
            return result
        return "Неверный ввод данных"
    return "Вы ввели пустой запрос"


def get_date(user_date: Union[str]) -> Any:
    """Функция получения даты в определенном формате и возвращения в формате ДД.ММ.ГГГГ"""
    date_format = datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    return new_date
