import sqlite3

conn = sqlite3.connect("Max1000_lager.db")

c = conn.cursor()


c.execute("""
CREATE TABLE IF NOT EXISTS Max1000_lager(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vare TEXT NOT NULL,
    antall INTEGER
)
""")
conn.commit()

print("________________")

c.execute("INSERT INTO Max1000_lager (vare, antall) VALUES (?, ?)",
          ("Eple", 1))
conn.commit()


c.execute("DELETE FROM Max1000_lager WHERE id = ?", (2,))
conn.commit()


c.execute("SELECT * FROM Max1000_lager")
res = c.fetchall()
print(res) 


c.execute("UPDATE Max1000_lager SET antall = ? WHERE id = ?", (5, 4 ))
conn.commit()



