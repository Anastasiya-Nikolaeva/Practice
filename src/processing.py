from typing import Union


def filter_by_state(dictionaries: Union[list], state: Union[str] = "EXECUTED") -> list:
    """Функция из списка словарей возвращает новый список словарей,
    у которых ключ state соответствует указанному значению"""
    new_list = []
    alternative_list = []

    for key in dictionaries:
        if key.get("state") == state:
            new_list.append(key)
        elif key.get("state") == "CANCELED":
            alternative_list.append(key)
    return new_list


def sort_by_date(dictionaries: Union[list]) -> list:
    """Функция сортирующая список по определенному ключу"""

    sorted_list = sorted(dictionaries, key=lambda dictionaries: dictionaries["date"], reverse=True)
    return sorted_list


if __name__ == "__main__":
    filtered = filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )

    for i in filtered:
        print(i)


if __name__ == "__main__":
    ordered = sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
    for i in ordered:
        print(i)
