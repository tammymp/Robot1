from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time

i2c = busio.I2C(SCL, SDA)

#crea la clase y define el ancho y alto de la pantalla
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

#limpia la pantalla
display.fill(0)
display.show()

#poner aqui el las caracteristicas del texto
image = Image.new ('1', (128,64))

draw = ImageDraw.Draw (image)

font = ImageFont.load_default()

#escribe 2 lineas de texto
draw.text((50,16),    "Hola", font=font, fill=255)
draw.text((50,26), "Mundo", font=font, fill=255)

#muestra texto
display.image(image)
display.show()
time.sleep(10)
display.fill()
display.show()

