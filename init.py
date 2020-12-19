import sqlite3

conn = sqlite3.connect("environment_readings.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS sensor_readings (id INTEGER PRIMARY KEY AUTOINCREMENT, ctemp TEXT, ftemp TEXT, pressure TEXT, humidity TEXT, created_date TEXT)")

conn.close()

