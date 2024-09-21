import logging
from typing import Union

logger = logging.getLogger("MaskingLogger")
logger.setLevel(logging.DEBUG)


file_handler = logging.FileHandler("../logs/masking.log", mode="w")
file_handler.setLevel(logging.DEBUG)


file_formatter = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)


logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Возвращает замаскированный номер карты"""
    if card_number != "":
        new_number = card_number.replace(" ", "")
        if new_number.isdigit():
            if len(new_number) == 16:
                masked_number = f"{new_number[:4]} {new_number[4:6]}{"*" * 2} {"*" * 4} {new_number[12:]}"
                logger.info(f"Замаскированный номер карты: {masked_number}")
                return masked_number
            logger.warning("Номер карты неверный")
            return "Номер карты неверный"
        logger.warning("Необходимо ввести 16-значный номер цифрами")
        return "Необходимо ввести 16-значный номер цифрами"
    logger.warning("Вы ввели пустой запрос")
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
                logger.info(f"Замаскированный номер счёта: {mask_account_user}")
                return mask_account_user
            logger.warning("Номер счёта неверный")
            return "Номер счёта неверный"
        logger.warning("Необходимо ввести 20-значный номер цифрами")
        return "Необходимо ввести 20-значный номер цифрами"
    logger.warning("Вы ввели пустой запрос")
    return "Вы ввели пустой запрос"


# if __name__ == "__main__":
#     print(get_mask_card_number(""))
#     print(get_mask_account("1234567890100234567890"))
