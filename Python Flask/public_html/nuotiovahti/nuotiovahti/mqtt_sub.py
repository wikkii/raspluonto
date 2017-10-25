import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("nuotiovahti")
def on_message(client, userdata, msg):
	#if msg.payload.decode() == "Hello world!":
	print(msg.payload + " hello")
	#client.disconnect()

client = mqtt.Client()
client.connect("127.0.0.1",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
