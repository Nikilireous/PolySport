import sqlite3

db = sqlite3.connect(
				"hackathon.db", detect_types=sqlite3.PARSE_DECLTYPES
			)
def create_db():
	with open("./hackathon.sql") as f:
		db.executescript(f.read())
		print("Database created")

def insert_data():
	