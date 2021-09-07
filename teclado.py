## import curses and GPIO
import curses
import RPi.GPIO as GPIO

#set GPIO numbering mode and define output pins
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.halfdelay(3)
screen.keypad(True)

try:
        while True:

            char = screen.getch()
            print (char)
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                print ("up")
                GPIO.output(18,True)
                GPIO.output(23,False)
                GPIO.output(15,False)
                GPIO.output(14,True)
# we can replace curses.key with other any digits like this  ord('p'), ord('m') ..etc
            elif char == curses.KEY_DOWN:
                print ("down")
                GPIO.output(18,False)
                GPIO.output(15,True)
                GPIO.output(23,True)
                GPIO.output(14,False)
            elif char == curses.KEY_RIGHT:
                print ("right")
                GPIO.output(18,False)
                GPIO.output(23,True)
                GPIO.output(15,False)
                GPIO.output(14,True)
            elif char == curses.KEY_LEFT:
                print ("left")
                GPIO.output(18,True)
                GPIO.output(23,False)
                GPIO.output(15,True)
                GPIO.output(14,False)

            else:
                print ("stop")
                GPIO.output(18,False)
                GPIO.output(23,False)
                GPIO.output(15,False)
                GPIO.output(14,False)

finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()