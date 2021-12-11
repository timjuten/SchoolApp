import sqlite3


conn = sqlite3.connect("../Database/main.db")
cur = conn.cursor()


def get_user(email):
    cur.execute(f"""SELECT * FROM USERS WHERE email='{email}';""")
    user = cur.fetchone()
    if user is None:
        print("При пошуку юзера трапилася помилка")
        return None
    else:
        return user
