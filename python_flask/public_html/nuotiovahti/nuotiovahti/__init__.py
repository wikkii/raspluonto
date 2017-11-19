import mysql.connector
from mysql.connector import errorcode
from flask import Flask, render_template, jsonify, json, request
app = Flask(__name__)


#home page url
@app.route("/")
def main():
        return render_template('index.html')

#sensor data url, default nethod is GET
@app.route('/data')
def getData():
        #initialize cnx to stop error
        cnx=0 
        #connecting to database
        try:
                cnx = mysql.connector.connect(user='nuotiovahti', password='pass', host='127.0.0.1, database='nuotiovahti'
        except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                        print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                        print("Database does not exist")
                else:
                        print(err)

        cursor = cnx.cursor()
        #getting sensor data from the database, gets the last 300 seconds of data
        cursor.execute("select (select count(f.detection_time) from Flame as f where detection_time >now()- INTERVAL 300 SECOND) as flame, (select count(p.detection_time) from Pir as p where detection_time >now()- INTERVAL 300 SECOND) as pir;")
        #turning data into json and saving it into datarows
        datarows = jsonify(cursor.fetchall())
        #close cursor and database connection
        cursor.close()
        cnx.close()
        #return json data 
        return datarows


if __name__ == "__main__":
    app.run()

