from gpiozero import Robot, InputDevice, OutputDevice
import RPi.GPIO as GPIO
import Adafruit_PCA9685
from time import sleep, time

robin = Robot (left = (18,23) , right= (14,15))

GPIO.setmode(GPIO.BCM)
robin.stop()

print("clean up")
GPIO.cleanup() # cleanup all GPIO