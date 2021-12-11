from rules import get_user
import keyboard
import sys


class voteCreator:
    def __init__(self, email):
        self.email = email
        self.user = get_user(self.email)

    def check_role(self):
        if self.user[5] == "вчитель" or self.user[5] == "директор" or self.user[5] == "куратор":
            print("Чудово, ви можете створити голосування")
            return True
        else:
            print("Вибачте, ви не можете створити голосування")
            return False
            sys.exit()

    def create_vote(self, vote_name, vote_body):
        if self.check_role:
            print("Натисніть на J, щоби доєднатися")
            while True:
                if keyboard.is_pressed("j"):
                    print("Натисніть на Y, якщо так, або N, якщо ні")
                    while True:
                        yes = 0
                        no = 0
                        if keyboard.is_pressed("y"):
                            yes += 1
                        elif keyboard.is_pressed("n"):
                            no += 1
                        if yes > no:
                            percent = (yes/(yes + no)) * 100
                            print(f'{percent}% обрали "Так"')
                            break
                        elif yes < no:
                            percent = (no/(yes + no)) * 100
                            print(f'{percent}% обрали "Ні"')
                            break
            else:
                print("Ви не доєдналися до голосування")


if __name__ == "__main__":
    email = input("Введіть свій емейл: ")
    teacher = voteCreator(email)
    role = teacher.check_role()
    if role:
        name = input("Введіть назву голосування: ")
        body = input("Введіть опис голосування: ")
        teacher.create_vote(name, body)