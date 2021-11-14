import sqlite3

conn = sqlite3.connect('users.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   email TEXT,
   password MESSAGE_TEXT );
""")


def get_data() :
    """
    функція, яка повертає дані з бази даних:
    """
    cur.execute("SELECT * FROM users;")
    all_results = cur.fetchall()
    data = all_results
    return data


if __name__ == "__main__":
    pass
