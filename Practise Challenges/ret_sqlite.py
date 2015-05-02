import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_started.db')

with con:
	cur = con.cursor()
	cur.execute("SELECT * FROM CITIES")
	
	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	#df = pd.DataFrame(rows)
	df = pd.DataFrame(rows, columns = cols)
	
	for row in rows:
		print row