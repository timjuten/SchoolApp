from news import get_news
import sqlite3
from school_project.User.data import get_user


conn = sqlite3.connect('../Database/main.db')

cur = conn.cursor()


news = get_news()


def create_news(args: list): # функція, яка створює новину
    try:
        cur.execute(f"""INSERT INTO news VALUES (?, ?, ?, ?, ?, ?, ?)""", args)
        conn.commit()
        print(f'Успішно додано новину {args[4]}')
    except TypeError:
        print("error")


if __name__ == "__main__":
    id = input("Введіть id новини: ")
    c_date = input("Введіть дату створення новини: ")
    p_date = input("Введіть дату публікації новини: ")
    author = input("Введіть ваш емейл: ")
    author = get_user(author)[0]
    title = input("Введіть заголовок новини: ")
    URL = input("Введіть URL картинки: ")
    body = input("Введіть текст новини: ")
    news_details = (id, c_date, p_date, author, title, URL, body)
    create_news(news_details)


