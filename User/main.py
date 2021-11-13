from data import get_data  # імпортуємо дані з словника у файлі data


class Users:
    """створюємо клас Юзер, в якому буде метод перевірки користувача"""
    
    def __init__(self, email: str = None, password: str = None) -> None:
        """
        метод ініт спрацювовує під час ініціалізації об'єкта у класі
        """
        self.email = email  # локальний параметр з емейлом
        self.password = password  # локальний параметр з паролем
    
    def check_user(self):
        """
        метод перевірки користувача
        """
        user_info = get_data()
        if self.email == user_info[0][3] and self.password == user_info[0][4]:
            print(f"Вітаю, ви є {user_info[0][5]}")
        else:
            print("Я не знаю хто ви")


if __name__ == "__main__":
    user = Users("timurjuten@gmail.com", "12345")  # створюємо об'єкт у класі юзер
    user.check_user()  # визиваємо метод перевірки користувача
