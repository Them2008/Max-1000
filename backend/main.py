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

print("Legger til vare")



















#def Slett():
#    c.execute("DELETE FROM Max1000_lager WHERE id = ?", (2,))
#    conn.commit()


#def hent_all():
#    c.execute("SELECT * FROM Max1000_lager")
#    res = c.fetchall()
#    return res


#def hent_id():
#    c.execute("SELECT * FROM Max1000_lager WHERE id = ?", (2, ))
#    res = c.fetchall()
#    return res


#def update():
#    c.execute("UPDATE Max1000_lager SET antall = ? WHERE id = ?", (5, 4 ))
#    conn.commit()



