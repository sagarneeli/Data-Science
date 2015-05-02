import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_started.db')

cities = (('Las Vegas', 'NV'),('Atlanta', 'GA'))

weather = (('Las Vegas', 2013, 'July', 'December', 70),('Atlanta', 2013, 'July', 'January', 67), ("New York City", 2013, "July", "January", 55))

with con:
	cur = con.cursor()
	cur.execute('SELECT SQLITE_VERSION()')
	# You're fetching the data from the cursor object. Because you're only fetching one record, you'll use the `fetchone()` method. If fetching more than one record, use the `fetchall()` method.
	data = cur.fetchone()
	# Finally, print the result.
	print "SQLite version: %s" % data
	
	cur.execute("DROP TABLE IF EXISTS cities")
	cur.execute("DROP TABLE IF EXISTS weather")
	cur.execute("CREATE TABLE cities (name text, state text)")
	cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)")
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
	cur.execute("SELECT warm_month, AVG(average_high) FROM weather GROUP BY warm_month HAVING AVG(average_high) > 65")
	
	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	#df = pd.DataFrame(rows)
	df = pd.DataFrame(rows, columns = cols)
	
	for row in rows:
		print row
	