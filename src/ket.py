import unittest
from unittest.mock import patch, MagicMock
from src.main import main  # Импортируем функцию main из вашего основного модуля

class TestBankTransactions(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'EXECUTED', 'да', 'по возрастанию', 'да', 'тест'])
    @patch('src.dataframe.read_data_csv', return_value=[])  # Имитация функции чтения CSV
    @patch('src.dataframe.read_data_excel', return_value=[])  # Имитация функции чтения Excel
    @patch('src.utils.get_operations_info', return_value=[
        {
            "date": "2023-10-01",
            "description": "Тестовая транзакция",
            "operationAmount": {"amount": 1000, "currency": {"name": "RUB"}},
            "from": "Счет 1",
            "to": "Счет 2"
        }
    ])  # Имитация получения операций из JSON
    @patch('src.generators.filter_by_currency', return_value=[])  # Имитация фильтрации по валюте
    @patch('src.processing.filter_by_state', return_value=[])  # Имитация фильтрации по статусу
    @patch('src.processing.sort_by_date', return_value=[])  # Имитация сортировки по дате
    @patch('src.searching.group_by_description', return_value=[])  # Имитация группировки по описанию
    @patch('src.widget.mask_account_card', side_effect=lambda x: x)  # Имитация маскирования счета
    def test_main_function(self, mock_mask_account_card, mock_group_by_description, mock_sort_by_date,
                           mock_filter_by_state, mock_filter_by_currency, mock_get_operations_info,
                           mock_read_data_excel, mock_read_data_csv):
        # Патчим функцию print для проверки выводимых сообщений
        with patch('builtins.print') as mock_print:
            main()  # Запускаем основную функцию
            # Проверяем, что выводится сообщение о начале печати транзакций
            mock_print.assert_any_call("Распечатываю итоговый список транзакций...")
            # Проверяем, что выводится количество операций
            mock_print.assert_any_call("Всего банковских операций в выборке: 1")
            # Проверяем, что выводится информация о транзакции
            mock_print.assert_any_call("\n1. 01.10.2023 Тестовая транзакция\nСчет 1 -> Счет 2\n"
                                        "Сумма: 1000 RUB")

    @patch('builtins.input', side_effect=['1', 'INVALID_STATE'])
    @patch('src.utils.get_operations_info', return_value=[])
    def test_invalid_state_input(self, mock_get_operations_info):
        # Патчим функцию print для проверки выводимых сообщений
        with patch('builtins.print') as mock_print:
            main()  # Запускаем основную функцию
            # Проверяем, что выводится сообщение об ошибке для недопустимого статуса
            mock_print.assert_any_call("Статус операции 'INVALID_STATE' недоступен.")

    @patch('builtins.input', side_effect=['1', 'EXECUTED', 'нет'])
    @patch('src.utils.get_operations_info', return_value=[])
    def test_no_sorting(self, mock_get_operations_info):
        # Патчим функцию print для проверки выводимых сообщений
        with patch('builtins.print') as mock_print:
            main()  # Запускаем основную функцию
            # Проверяем, что выводится сообщение о том, что не найдено ни одной транзакции
            mock_print.assert_any_call("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

if __name__ == '__main__':
    unittest.main()
