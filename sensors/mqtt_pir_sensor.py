# parallax_pir_reva.py - write to screen when movement detected
# (c) BotBook.com - Karvinen, Karvinen, Valtokari
# modified from original 15.11.2017

#-*- coding: utf-8 -*-

import time
import botbook_gpio as gpio
import paho.mqtt.client as mqtt


learningPeriod = 30

def main():

        broker_address="139.59.140.158" 
        client = mqtt.Client("P1") #create new instance
        client.connect(broker_address) #connect to broker

        pirPin = 7
        gpio.mode(pirPin,"in")
        #Learning period
	client.publish("nuotiovahti","learning... " + str(learningPeriod) + " seconds")
        
	time.sleep(learningPeriod) # <1>
        while (True):
                movement = gpio.read(pirPin) # <2>
                if(movement == gpio.HIGH):
                        client.publish("nuotiovahti","1")


                time.sleep(1)


if __name__ == "__main__":
	main()
