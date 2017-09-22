# parallax_pir_reva.py - write to screen when movement detected
# (c) BotBook.com - Karvinen, Karvinen, Valtokari
# 22.9.2017 modified by Vesa Valli

import time
import botbook_gpio as gpio

learningPeriod = 30

def main():
	pirPin = 7	
	gpio.mode(pirPin,"in")
	#Learning period
	print ("learning... " + str(learningPeriod) + " seconds")
	time.sleep(learningPeriod) # <1>
	while (True):	
		movement = gpio.read(pirPin) # <2>	
		if(movement == gpio.HIGH):
			print ("Movement detected " + time.ctime())
		else:
			print ("No movement detected " + time.ctime())
		time.sleep(0.3)	


if __name__ == "__main__":
	main()
