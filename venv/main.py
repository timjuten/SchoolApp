from data import user_info #імпортуємо дані з словника у файлі data

class Users: #створюємо клас Юзер, в якому буде метод перевірки користувача
    def __init__(self, email, password): #метод ініт спрацювовує під час ініціалізації об'єкта у класі
        self.email = email #локальний параметр з емейлом
        self.password = password #локальний параметр з паролем

    def check_user(self): #метод перевірки користувача
        if self.email == user_info["email"] and self.password == user_info["password"]:
            print(f"Вітаю, ви є {user_info['user_role']}")
        else:
            print("Я не знаю хто ви")

user = Users("timurjuten@gmail.com", "2345") #створюємо об'єкт у класі юзер
user.check_user() #визиваємо метод перевірки користувача





