import paho.mqtt.client as mqtt
import mysql.connector
from mysql.connector import errorcode

#cursor = cnx.cursor()

def addtobase(message):
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
        print(message + "adding")
        add_sensordata = ("INSERT INTO sensordata VALUES(%(data)s)")

        data_sensordata = {
                'data': message
        }

        cursor.execute(add_sensordata, data_sensordata)
        cnx.commit()
        cursor.close()
        cnx.close()

def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("nuotiovahti")
def on_message(client, userdata, msg):
        #if msg.payload.decode() == "Hello world!":
        addtobase(msg.payload)
        print(msg.payload + " hello")
        #client.disconnect()


client = mqtt.Client()
client.connect("127.0.0.1",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()



