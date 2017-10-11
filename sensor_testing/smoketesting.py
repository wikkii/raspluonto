#TARKISTA/KORJAA PINNIT ENNEN AJOA!
#http://www.knight-of-pi.org/digital-sensors-and-the-raspberry-pi-with-the-smoke-detector-mq-x-as-example/
#Vilkaise myös ylläolevasta linkistä ^

import time, sys
import RPi.GPIO as GPIO #Teron kirjastoa voi kokeilla, mutta siellä käytetään vissiin analogista singaalia.

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#If smoke is detected
def action(pin)
	print('Smoke detected!)
	return
	
GPIO.add_event_detect(7, GPIO.RISING)
GPIO.add_event_callbak(7, action)

try:
	while True:
		print('Sensor alive, but no smoke detected')
		time.sleep(0,5)
	except KeyboardInterrupt:
		GPIO.cleanup()
		sys.exit()
