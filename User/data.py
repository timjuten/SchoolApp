import sqlite3
import base64

conn = sqlite3.connect('../Database/main.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   email TEXT,
   password MESSAGE_TEXT );
""")


def get_data():
    """
    функція, яка повертає дані з бази даних:
    """
    cur.execute("SELECT * FROM users;")
    all_results = cur.fetchall()
    data = all_results
    return data


def get_user(email):
    cur.execute(f"""SELECT * FROM USERS WHERE email='{email}';""")
    user = cur.fetchone()
    if user is None:
        print("При пошуку юзера трапилася помилка")
        return None
    else:
        return user


if __name__ == "__main__":
    pass
