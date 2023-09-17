import time
import board
import busio
import displayio
# import neopixel
import math
import lib.geometry_helper as geometry_helper

import lib.gc9a01 as gc9a01
import lib.bmi160 as BMI160
import lib.face.Face as Face
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.rect import Rect

# # Configure the setup
# PIXEL_PIN = board.GP16  # pin that the NeoPixel is connected to
# ORDER = neopixel.RGB  # pixel color channel order
# COLOR = (200, 50, 50)  # color to blink
# CLEAR = (50, 200, 50)  # clear (or second color)
# DELAY = 0.5  # blink rate in seconds

# # Create the NeoPixel object
# pixel = neopixel.NeoPixel(PIXEL_PIN, 1, pixel_order=ORDER)

# # Loop forever and blink the color
# while True:
#     pixel[0] = COLOR
#     time.sleep(DELAY)
#     pixel[0] = CLEAR
#     time.sleep(DELAY)


#define TFT_RST 7  //ORANGE
#define TFT_DC  6  //GREEN
#define TFT_CS  5  //BLUE
#define TFT_SCK 2  //WHITE
#define TFT_MOSI 3 //YELLOW
#define TFT_BL 4   //PURPLE

#Display configuration
displayio.release_displays()

spi = busio.SPI(clock=board.GP2, MOSI=board.GP3)
while not spi.try_lock():
    pass

spi.configure(baudrate=24000000) # Configure SPI for 24MHz
spi.unlock()

cs = board.GP5
dc = board.GP6
reset = board.GP7

display_bus = displayio.FourWire(spi, command=dc, chip_select=cs, reset=reset)
display = gc9a01.GC9A01(display_bus, width=240, height=240)

BALL_COLOR = 0xFFFFFF
BACKGROUND_COLOR = 0xFF0000

# Initial position and size of the ball
x = 120
y = 120
radius = 20

center_x = display.width // 2 - radius
center_y = display.height // 2 - radius
screen_radius = center_x


# Create a ball (circle) at the initial position
ball = Circle(x, y, radius, fill=BALL_COLOR)

# Create a display group and add the ball
group = displayio.Group()

# # Outside the while loop
# bitmap = displayio.Bitmap(display.width, display.height, 2)
# palette = displayio.Palette(2)
# palette[0] = BACKGROUND_COLOR
# palette[1] = BALL_COLOR

# background = displayio.TileGrid(bitmap, pixel_shader=palette)
# group.append(background)


# group.append(ball)

# Gravity sensor configuration
# RED - 3.3v
# BLACK - GND
# YELLOW - SCL - GP27
# WHITE - SDA - GP26

i2c = busio.I2C(scl = board.GP27, sda=board.GP26)  # uses board.SCL and board.SDA
bmi = BMI160.BMI160(i2c)
bmi.gyro_range = BMI160.GYRO_RANGE_500
print("Gravity sensor configured!")



# Create a group for the face and its features
face_group = displayio.Group()

face = Face.Face()
face.drawFace(face_group)

# Display the face on the screen
display.show(face_group)

while True:
    pass

# while True:

#     gyrox, gyroy, gyroz = bmi.acceleration
#     speed_x = (int)(gyrox * 20)
#     speed_y = (int)(gyroy * 20)

#     # # Update the position
#     x += speed_x
#     y += speed_y 

#     x, y = geometry_helper.GeometryHelper.get_new_goal_pos(center_x, center_y, x, y, screen_radius)

#     # Update ball's position in the group
#     ball.x = int(x)
#     ball.y = int(y)

#     # Redraw ball at new position
#     # group.append(ball)
#     display.show(group)
#     time.sleep(0.01)
