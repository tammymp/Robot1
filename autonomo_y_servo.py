from __future__ import division
from gpiozero import Robot, InputDevice, OutputDevice
import Adafruit_PCA9685
from time import sleep, time

trig = OutputDevice (21)
echo = InputDevice (20)

robin = Robot (left = (18,23) , right= (14,15))

duration = 15

end_time = time () + duration
running = True

sleep (2)

def get_pulse_time ():
    pulse_start , pulse_end = 0 , 0

    trig.on()
    sleep(0.00001)
    trig.off()

    while echo.is_active == False:
        pulse_start = time ()

    while echo.is_active == True:
        pulse_end = time ()

    return pulse_end - pulse_start

def calculate_distance (duration):
    speed = 343
    distance = speed * duration / 2
    return distance

while running:
    duration = get_pulse_time ()
    distance = calculate_distance (duration)

    if distance <0.2:
        robin.left(0.5)
        sleep(0.5)

    else: robin.forward(0.5)

    if time () >=  end_time:
        running = False
        robin.stop()
        GPIO.cleanup() # cleanup all GPIO

    sleep (0.06)
    print (distance)

pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    # Move servo on channel O between extremes.
    pwm.set_pwm(0, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(0, 0, servo_mid)
    time.sleep(1)
    pwm.set_pwm(0, 0, servo_max)
    time.sleep(1)

servo.stop()