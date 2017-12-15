# ky_026_flame.py - report presence of IR light from flame to serial
# (c) BotBook.com - Karvinen, Karvinen, Valtokari
# modified 6 Oct 2017

#-*- coding: utf-8 -*-

import time
import botbook_gpio as gpio


def main():

	flamePin = 8
	gpio.mode(flamePin, "in")
	#small wait before starting
	print ("starting flame sensor...")
	time.sleep(0.5)
	
	while(True):
		flame = gpio.read(flamePin)
		if(flame == gpio.LOW):
			print ("Flame detected " + time.ctime())
		else:
			print ("NO flame detected " + time.ctime())
		time.sleep(1)

if __name__ == "__main__":
	main()
