import unittest
from unittest.mock import patch, MagicMock
from src.main import main  # ����������� ������� main �� ������ ��������� ������

class TestBankTransactions(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'EXECUTED', '��', '�� �����������', '��', '����'])
    @patch('src.dataframe.read_data_csv', return_value=[])  # �������� ������� ������ CSV
    @patch('src.dataframe.read_data_excel', return_value=[])  # �������� ������� ������ Excel
    @patch('src.utils.get_operations_info', return_value=[
        {
            "date": "2023-10-01",
            "description": "�������� ����������",
            "operationAmount": {"amount": 1000, "currency": {"name": "RUB"}},
            "from": "���� 1",
            "to": "���� 2"
        }
    ])  # �������� ��������� �������� �� JSON
    @patch('src.generators.filter_by_currency', return_value=[])  # �������� ���������� �� ������
    @patch('src.processing.filter_by_state', return_value=[])  # �������� ���������� �� �������
    @patch('src.processing.sort_by_date', return_value=[])  # �������� ���������� �� ����
    @patch('src.searching.group_by_description', return_value=[])  # �������� ����������� �� ��������
    @patch('src.widget.mask_account_card', side_effect=lambda x: x)  # �������� ������������ �����
    def test_main_function(self, mock_mask_account_card, mock_group_by_description, mock_sort_by_date,
                           mock_filter_by_state, mock_filter_by_currency, mock_get_operations_info,
                           mock_read_data_excel, mock_read_data_csv):
        # ������ ������� print ��� �������� ��������� ���������
        with patch('builtins.print') as mock_print:
            main()  # ��������� �������� �������
            # ���������, ��� ��������� ��������� � ������ ������ ����������
            mock_print.assert_any_call("������������ �������� ������ ����������...")
            # ���������, ��� ��������� ���������� ��������
            mock_print.assert_any_call("����� ���������� �������� � �������: 1")
            # ���������, ��� ��������� ���������� � ����������
            mock_print.assert_any_call("\n1. 01.10.2023 �������� ����������\n���� 1 -> ���� 2\n"
                                        "�����: 1000 RUB")

    @patch('builtins.input', side_effect=['1', 'INVALID_STATE'])
    @patch('src.utils.get_operations_info', return_value=[])
    def test_invalid_state_input(self, mock_get_operations_info):
        # ������ ������� print ��� �������� ��������� ���������
        with patch('builtins.print') as mock_print:
            main()  # ��������� �������� �������
            # ���������, ��� ��������� ��������� �� ������ ��� ������������� �������
            mock_print.assert_any_call("������ �������� 'INVALID_STATE' ����������.")

    @patch('builtins.input', side_effect=['1', 'EXECUTED', '���'])
    @patch('src.utils.get_operations_info', return_value=[])
    def test_no_sorting(self, mock_get_operations_info):
        # ������ ������� print ��� �������� ��������� ���������
        with patch('builtins.print') as mock_print:
            main()  # ��������� �������� �������
            # ���������, ��� ��������� ��������� � ���, ��� �� ������� �� ����� ����������
            mock_print.assert_any_call("�� ������� �� ����� ����������, ���������� ��� ���� ������� ����������")

if __name__ == '__main__':
    unittest.main()
