from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("1452368954756248") == "1452 36** **** 6248"
    assert get_mask_card_number("1452 3689 5475 6248") == "1452 36** **** 6248"
    assert get_mask_card_number("слова не цифры") == "Необходимо ввести 16-значный номер цифрами"
    assert get_mask_card_number("") == "Вы ввели пустой запрос"
    assert get_mask_card_number("145236895475624877") == "Номер карты неверный"


def test_get_mask_account() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("слова не цифры") == "Необходимо ввести 20-значный номер цифрами"
    assert get_mask_account("") == "Вы ввели пустой запрос"
    assert get_mask_account("24589564785632547856125495") == "Номер счёта неверный"
    assert get_mask_account("73 654 108 4301 35 8743 0 5") == "**4305"