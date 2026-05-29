import sqlite3
from fastapi import FastAPI

app = FastAPI()

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

@app.get("/")
def home():
    return {"melding": "hei!"}

@app.post("/Post")
def Legge_til():
    c.execute("INSERT INTO Max1000_lager (vare, antall) VALUES (?, ?)",
    ("Kake", 1))
    conn.commit()

@app.delete("/Delete")
def Slett():
    c.execute("DELETE FROM Max1000_lager WHERE id = ?", (2,))
    conn.commit()

@app.get("/Get")
def hent_all():
    c.execute("SELECT * FROM Max1000_lager")
    res = c.fetchall()
    return res

@app.get("/Get_id")
def hent_id():
    c.execute("SELECT * FROM Max1000_lager WHERE id = ?", (4, ))
    res = c.fetchall()
    return res

@app.put("/Put")
def update():
    c.execute("UPDATE Max1000_lager SET antall = ? WHERE id = ?", (5, 4 ))
    conn.commit()

