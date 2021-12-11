from data import get_data, get_user  # імпортуємо дані з словника у файлі data
import base64
import getpass
import validators
import sys


class Users :
    """створюємо клас Юзер, в якому буде метод перевірки користувача"""

    def __init__(self, email: str = None, password: str = None) -> None :
        """
        метод ініт спрацювовує під час ініціалізації об'єкта у класі
        """
        self.email = email  # локальний параметр з емейлом
        self.password = password  # локальний параметр з паролем

    def check_user(self):
        """
        метод перевірки користувача
        """
        user_info = get_user(self.email)
        if user_info and self.password == user_info[4] :
            print(f"Вітаю, {user_info[1]}")
        elif user_info is None :
            pass
        else :
            print("Я не знаю хто ви")


if __name__ == "__main__" :
    email = input("Введіть емейл: ")
    email_check = validators.email(email)
    if email_check :
        pass
    else :
        print("Такого емейлу не може існувати")
        sys.exit()
    password = getpass.getpass('Введіть пароль: ')

    password = base64.b64encode(password.encode("utf-8"))
    user = Users(email, password)  # створюємо об'єкт у класі юзер
    user.check_user()  # визиваємо метод перевірки користувача
    #hello ther
