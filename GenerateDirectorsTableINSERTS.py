with open('/home/ingrid/Downloads/insertresults.sql', 'w') as f2:
	with open('/home/ingrid/Downloads/results.json', 'r') as f:
	    results = json.load(f)
	INSERT_QUERY = "INSERT INTO director (dcode, bplace, bcountry, bpoint) VALUES (%s, %s, %s, ST_GeomFromText('POINT(%s %s)'))\n"
	for director, location, gps in results:
		if gps:
		    f2.write(INSERT_QUERY % ("'" + director.replace("'", "''") + "'", "'" + location.replace("'", "''") + "'", 'NULL', gps[1], gps[0]))
		else:
		    f2.write("INSERT INTO director (dcode, bplace, bcountry, bpoint) VALUES (%s, %s, NULL, NULL)\n" % ("'" + director.replace("'", "''") + "'", "'" + location.replace("'", "''") + "'"))
