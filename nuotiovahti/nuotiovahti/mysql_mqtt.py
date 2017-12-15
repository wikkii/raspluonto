import paho.mqtt.client as mqtt
import mysql.connector
from mysql.connector import errorcode

#inserts timestamps into the database when mqtt message is received from the broker
def addtobase(topic):
	#connecting to the database
        try:
                cnx = mysql.connector.connect(option_files='connector.cnf')
        except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                        print("Something is wrong with your user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                        print("Database does not exist")
                else:
                        print(err)

        cursor = cnx.cursor()
	#check the topic and form the sql statement accordingly.
	add_sensordata = ''
        if topic == "Pir":
		add_sensordata = ("INSERT INTO Pir(pir_id) VALUES(1)")
        elif topic == "Flame":
		add_sensordata = ("INSERT INTO Flame(flame_id) VALUES(1)")
	#execute and commit the data int othe database
        cursor.execute(add_sensordata)
        cnx.commit()
        cursor.close()
        cnx.close()

#paho-mqtt on connect function, for when the paho mqtt client connects succesfully to the broker
def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
	#subscribes to the broker topic nuotiovahti/# so it can receive both pir and flame sensor messages
        client.subscribe("nuotiovahti/#")

#paho-mqtt on message function that runs when the paho-mqtt client receives an mqtt message from the broker
def on_message(client, userdata, msg):
	#check the message and set the topic for which table to add the data and then calls the add to base function.
	# if message contains something else prints the message instead
	if msg.payload == "1":
        	addtobase("Pir")
	elif msg.payload == "2":
		addtobase("Flame")
#	else:
#		print(msg.payload)

#connecting to the mqtt broker
client = mqtt.Client()
client.connect("127.0.0.1",1883,60)
#calls the defined functions when event happens
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()



