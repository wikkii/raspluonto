import mysql.connector
from mysql.connector import errorcode
from flask import Flask, render_template, jsonify, json, request

app = Flask(__name__)


#home page
@app.route("/")
def main():
	return render_template('index.html')

#get request to this url returns cound of sensor detections fro mthe database from the last 5 minutes(300 seconds)
@app.route('/data')
def getData():

	#connection to database
	try:
	        cnx = mysql.connector.connect(user='nuotiovahti', password='passwd', host='127.0.0.1', database='nuotiovahti')
	except mysql.connector.Error as err:
	        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
	                print("Something is wrong with your user name or password")
	        elif err.errno == errorcode.ER_BAD_DB_ERROR:
	                print("Database does not exist")
	        else:
	                print(err)


	cursor = cnx.cursor()


	#get data from the database, feches detection count from both tables over the last 5 minutes
	cursor.execute("select (select count(f.detection_time) from Flame as f where detection_time >now()- INTERVAL 300 SECOND) as flame, (select count(p.detection_time) from Pir as p where detection_time >now()- INTERVAL 300 SECOND) as pir;")

	#getting colum names from the resultset
	columns = cursor.column_names
	#getting the counts fro mthe resultset
	datarows = cursor.fetchall()
	#get the values from the rows
	datalist = datarows[0]
	#combine the colum names and values into a dict

	dicta = dict(zip(columns, datalist))

	rows = jsonify(dicta)

	#close cursor and cnx
	cursor.close()
	cnx.close()

	return rows


if __name__ == "__main__":
	app.run()

