import sqlite3


conn = sqlite3.connect('../Database/main.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE news(
   newsid INT PRIMARY KEY,
   creationDate TEXT,
   publicDate TEXT,
   author INT,
   FOREIGN KEY(author) REFERENCES users(userid),
   title TEXT,
   image_URL TEXT,
   body TEXT
    );
""")
conn.commit()
