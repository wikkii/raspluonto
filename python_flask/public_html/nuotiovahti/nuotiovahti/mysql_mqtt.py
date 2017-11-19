
import paho.mqtt.client as mqtt
import mysql.connector
from mysql.connector import errorcode

def addtobase(topic):
        #connecting to database
        try:
                cnx = mysql.connector.connect(option_files='connector.cnf')
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
        print(topic + "adding")
        #checking the topic and adding data to the correct table accordingly
        add_sensordata = ''
        if topic == "Pir":
                add_sensordata = ("INSERT INTO Pir(pir_id) VALUES(1)")
        elif topic == "Flame":
                add_sensordata = ("INSERT INTO Flame(flame_id) VALUES(1)")
        executing transactions and closing the connection
        cursor.execute(add_sensordata)
        cnx.commit()
        cursor.close()
        cnx.close()
#when paho mqtt connects to the broker it subscribes to the nuotiovahti topic.
def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("nuotiovahti/#")
#when client receives message from mqtt broker it will check the content and call the addto base function
def on_message(client, userdata, msg):
        #if msg.payload.decode() == "Hello world!":
        print("payload is " + msg.payload)
        #if message is one topic is pir and if message is 2 topic is flame
        if msg.payload == "1":
                addtobase("Pir")
        elif msg.payload == "2":
                addtobase("Flame")
        else:
                print("error")
        #client.disconnect()

#connection to mqtt broker
client = mqtt.Client()
client.connect("127.0.0.1",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
