from data import get_data  # імпортуємо дані з словника у файлі data
import base64
import getpass

class Users:
    """створюємо клас Юзер, в якому буде метод перевірки користувача"""
    
    def __init__(self, email: str = None, password: str = None) -> None:
        """
        метод ініт спрацювовує під час ініціалізації об'єкта у класі
        """
        self.email = email  # локальний параметр з емейлом
        self.password = password # локальний параметр з паролем
    
    def check_user(self):
        """
        метод перевірки користувача
        """
        user_info = get_data()
        for u in range(0, len(user_info)):
            if self.email == user_info[u][3] and self.password == user_info[u][4]:
                print(f"Вітаю, {user_info[u][1]}")
                break
            else:
                print("Я не знаю хто ви")
                break


if __name__ == "__main__":
    email = input("Введіть емейл: ")
    password = getpass.getpass('Введіть пароль: ')

    password = base64.b64encode(password.encode("utf-8"))
    user = Users(email, password)  # створюємо об'єкт у класі юзер
    user.check_user()  # визиваємо метод перевірки користувача