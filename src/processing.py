from operator import itemgetter
from typing import Union, Any
from typing import Iterable

import pytest


def filter_by_state(dictionaries: Iterable[dict], state: Union[str] = "EXECUTED") -> Any:
    """Функция из списка словарей возвращает новый список словарей,
    у которых ключ state соответствует указанному значению"""
    new_list = []
    alternative_list = []

    for key in dictionaries:
        if key.get("state") == state:
            new_list.append(key)
        elif key.get("state") == "CANCELED":
            alternative_list.append(key)
    if len(new_list) == 0:
        return "В списке нет необходимых элементов"
    return new_list


def sort_by_date(dictionaries: Any, sort_revers: bool = True) -> Any:
    """Функция сортирующая список по определенному ключу"""
    if dictionaries != [{}]:
        return sorted(dictionaries, key=itemgetter("date"), reverse=sort_revers)
    return "В списке нет элементов"


with pytest.raises(KeyError):
    sort_by_date(KeyError)
