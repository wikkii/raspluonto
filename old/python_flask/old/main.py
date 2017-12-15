from dbconnect import connection
from flask import Flask, render_template

@app.route('/index/')
def display_data():

	try:
		c, conn = connection()
		
		query = "SELECT * from sensors"
		c.execute(query)
		
		data = c.fetchall()
		
		conn.connection()
		
		#return data
		
		return render_template("index.php", data=data)
		
	except Exception as e:
		return (str(e))