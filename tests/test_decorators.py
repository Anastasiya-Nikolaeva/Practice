import logging
import os
import tempfile
from typing import Generator

import pytest

from src.decorators import my_function


@pytest.fixture
def cleanup_log_file() -> Generator[str, None, None]:
    """Фикстура для очистки файла лога перед и после тестов."""
    # Создаем временный файл для логов
    log_file = tempfile.NamedTemporaryFile(delete=False, suffix=".log")
    log_file.close()  # Закрываем файл, чтобы другие процессы могли к нему получить доступ

    # Настраиваем логирование
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file.name, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    yield log_file.name  # Возвращаем имя файла для тестов

    # Удаляем обработчик и временный файл после тестов
    logger.removeHandler(file_handler)
    file_handler.close()
    os.remove(log_file.name)


def test_logging_success(cleanup_log_file: str) -> None:
    """Тест успешного выполнения функции."""
    my_function(1, 2)  # Успешный вызов

    # Проверяем, что файл лога создан
    assert os.path.exists(cleanup_log_file)

    # Проверяем содержимое файла лога
    with open(cleanup_log_file, "r", encoding="utf-8") as f:
        logs = f.read()
        assert "Начало выполнения функции 'my_function'" in logs
        assert "Функция 'my_function' завершена успешно. Результат: 3" in logs


def test_logging_error(cleanup_log_file: str) -> None:
    """Тест обработки ошибки в функции."""
    my_function(1, "a")  # Это вызовет ошибку

    # Проверяем, что файл лога создан
    assert os.path.exists(cleanup_log_file)

    # Проверяем содержимое файла лога
    with open(cleanup_log_file, "r", encoding="utf-8") as f:
        logs = f.read()
        assert "Начало выполнения функции 'my_function'" in logs
        assert "Ошибка в функции 'my_function': TypeError" in logs


def test_logging_to_file(cleanup_log_file: str) -> None:
    """Тест логирования в файл."""
    my_function(1, 2)  # Успешный вызов
    my_function(1, "a")  # Это вызовет ошибку

    # Проверяем, что файл лога создан
    assert os.path.exists(cleanup_log_file)

    # Проверяем содержимое файла лога
    with open(cleanup_log_file, "r", encoding="utf-8") as f:
        logs = f.read()
        assert "Начало выполнения функции 'my_function'" in logs
        assert "Функция 'my_function' завершена успешно. Результат: 3" in logs
        assert "Ошибка в функции 'my_function': TypeError" in logs
