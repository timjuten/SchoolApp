import sqlite3


conn = sqlite3.connect('../Database/main.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE news(
   newsid INT PRIMARY KEY,
   creationDate TEXT,
   publicDate TEXT,
   author INT,
   title TEXT,
   image_URL TEXT,
   body TEXT,
   FOREIGN KEY (author) REFERENCES users (userid)
);
""")
conn.commit()
