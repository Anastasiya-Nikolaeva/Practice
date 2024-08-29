from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(
    dictionaries: list[dict], dict_no_state_data: list[dict], dict_one_state_data: list[dict]
) -> None:
    assert filter_by_state(dictionaries) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(dict_no_state_data) == "В списке нет необходимых элементов"
    assert filter_by_state(dict_one_state_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}
    ]


def test_sort_by_date(
    dictionaries: list[dict], dict_no_state_data: list[dict], dict_one_state_data: list[dict]
) -> None:
    assert sort_by_date(dictionaries) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_by_date(dict_no_state_data) == [
        {"id": 41428829, "state": "", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": ""},
        {"id": 615064591, "state": "CANCELED", "date": ""},
    ]
    assert sort_by_date([{}]) == "В списке нет элементов"
    assert sort_by_date(dict_one_state_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": ""},
    ]