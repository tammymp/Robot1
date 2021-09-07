from gpiozero import Robot, InputDevice, OutputDevice
from time import sleep, time
#pantalla oled
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306



trig = OutputDevice (21)
echo = InputDevice (20)

i2c = busio.I2C(SCL, SDA)

#crea la clase y define el ancho y alto de la pantalla
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

#limpia la pantalla
display.fill(0)
display.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = display.width
height = display.height
image = Image.new("1", (width, height))

#poner aqui el las caracteristicas del texto
image = Image.new ('1', (128,64))

draw = ImageDraw.Draw (image)

font = font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
# ImageFont.load_default()



#motores robot
robin = Robot (left = (18,23) , right= (14,15))

duration = 30


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

    sleep (0.06)

    print ("Distancia:",round(distance,2),"cm")
    
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    
    #escribe 2 lineas de texto
    draw.text((5,12),"Distancia: ", font=font, fill=255)
    draw.text((5,35), str (round(distance,2)) + "cm", font=font, fill=255)
    
    #muestra texto
    display.image(image)
    display.show()
    sleep(0.01)
    

    