
# parallax_pir_reva.py - write to screen when movement detected
# (c) BotBook.com - Karvinen, Karvinen, Valtokari
# modified from original 27.9.2017

#-*- coding: utf-8 -*-

import time
import botbook_gpio as gpio
import paho.mqtt.client as mqtt


learningPeriod = 30

def main():

	broker_address="172.28.172.185" 
	client = mqtt.Client("P1") #create new instance
	client.connect(broker_address) #connect to broker

	pirPin = 7	
	gpio.mode(pirPin,"in")
	#Learning period
	print ("learning... " + str(learningPeriod) + " seconds")
	time.sleep(learningPeriod) # <1>
	while (True):	
		movement = gpio.read(pirPin) # <2>	
		if(movement == gpio.HIGH):
			client.publish("nuotiovahti","Movement detected" + time.ctime())
			print ("Movement detected " + time.ctime())
		else:
			client.publish("nuotiovahti","NO movement detected " + time.ctime())
			print ("No movement detected " + time.ctime())
		time.sleep(2)	


if __name__ == "__main__":
	main()
