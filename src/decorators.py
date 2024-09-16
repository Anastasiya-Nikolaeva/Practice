import functools
import logging
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    # Настройка логирования
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Создаем обработчик для вывода в файл, если filename задан
    if filename:
        file_handler = logging.FileHandler(filename, encoding="utf-8")  # Указываем кодировку UTF-8
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Optional[Any]:
            logging.info(f"Начало выполнения функции '{func.__name__}' с аргументами: {args}, {kwargs}")
            try:
                result = func(*args, **kwargs)
                logging.info(f"Функция '{func.__name__}' завершена успешно. Результат: {result}")
                return result
            except Exception as e:
                logging.error(
                    f"Ошибка в функции '{func.__name__}': {type(e).__name__} - {e}. Аргументы: {args}, {kwargs}"
                )
                return None  # Возвращаем None или любое другое значение по умолчанию

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y
