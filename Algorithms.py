import json
import ctypes
import sys

from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

class DataMeta(type):
    """Мета класс для реализации паттерна одиночка"""

    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Data(metaclass=DataMeta):
    """Класс данных пользователя"""

    def __init__(self):
        """Загрузка данных пользователя в словарь data"""

        self.fernet = Fernet("ENmNo9Dvb-PONIezmlh8YCOsVU-dx52reTbGTCsLMzQ=")

        try:
            with open("settings.json", "rb") as read_file:
                self.data = self.fernet.decrypt(read_file.read())
                self.data = json.loads(self.data)
        except FileNotFoundError:
            ctypes.windll.user32.MessageBoxW(0, u"Не найден файл данных пользователя", u"Ошибка файла данных", 0)
            sys.exit()
        except InvalidToken:
            ctypes.windll.user32.MessageBoxW(0, u"Файл данных поврежден", u"Ошибка файла данных", 0)
            sys.exit()

    def save(self):
        """Сохранение данных пользователя"""

        encrypted = self.fernet.encrypt(json.dumps(self.data).encode("utf-8"))
        with open("settings.json", "wb") as write_file:
            write_file.write(encrypted)