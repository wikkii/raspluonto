# ky_026_flame.py - report presence of IR light from flame to serial
# (c) BotBook.com - Karvinen, Karvinen, Valtokari
# modified 15th of November 2017

#-*- coding: utf-8 -*-

import time
import botbook_gpio as gpio
import paho.mqtt.client as mqtt


def main():

        broker_address="139.59.140.158"
        client = mqtt.Client("P2")
        client.connect(broker_address)
        topic = "nuotiovahti/flame"
        flamePin = 8
        gpio.mode(flamePin, "in")


        while(True):
                flame = gpio.read(flamePin)

                if(flame == gpio.LOW):
                        client.publish(topic,"2")

                else:
                        client.publish(topic,"NO flame detected")

                time.sleep(2)

if __name__ == "__main__":
        main()
