import telebot, os, time, sqlite3

SQL = sqlite3.connect("DataBase.db")
SQL.cursor().execute('''CREATE TABLE IF NOT EXISTS USERS (
	"TELEGRAM_ID" INT,
	"CASH" INT
	)''')
SQL.commit()