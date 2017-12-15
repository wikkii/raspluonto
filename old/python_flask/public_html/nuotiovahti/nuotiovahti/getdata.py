import paho.mqtt.client as mqtt
import mysql.connector
from flask import Flask, jsonify, json, request

app = Flask(__name__)
app.route("/")
with app.app_context():


	def fetchfrombase():
		try:
		        cnx = mysql.connector.connect(option_files='/home/mint/connectors.cnf')
		except mysql.connector.Error as err:
		        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		                print("Something is wrong with your user name or password")
		        elif err.errno == errorcode.ER_BAD_DB_ERROR:
		                print("Database does not exist")
		        else:
		                print(err)
		else:
		        print("connected to database")


		cursor = cnx.cursor()
		print("selecting")


		cursor.execute("select (select count(f.detection_time) from Flame as f where detection_time >now()- INTERVAL 300 SECOND) as flame, (select count(p.detection_time) from Pir as p where detection_time >now()- INTERVAL 300 SECOND) as pir;")
	
		datarows = jsonify(cursor.fetchall) 
	
		print (datarows)

		cnx.close()
	
	fetchfrombase()

if __name__ == "__name__":
    app.run()
