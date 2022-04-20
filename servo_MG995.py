import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT) #pin 11 (BCM GPIO17) on the Raspberry Pi

pwm=GPIO.PWM(11, 50) #pin 11 (BCM GPIO17) on the Raspberry Pi and send a 50MHz PWM signal
pwm.start(0) //Start the signal at 0

pwm.ChangeDutyCycle(5) #left -90 deg position
sleep(1)
pwm.ChangeDutyCycle(7.5) #neutral position
sleep(1)
pwm.ChangeDutyCycle(10) #right +90 deg position
sleep(1)

pwm.stop()
GPIO.cleanup()
