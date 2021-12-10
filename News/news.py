import sqlite3

conn = sqlite3.connect('../Database/main.db')

cur = conn.cursor()

news = ('0001', '2021-12-04', '2021-12-04', '0001', 'Bruh', 'bruh', 'bruh')


def get_news():
    """
    функція, яка повертає новини з бази даних:
    """
    cur.execute("SELECT * FROM news;")
    all_results = cur.fetchall()
    data = all_results
    return data


if __name__ == '__main__':
    pass
