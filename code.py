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

# Gravity sensor configuration
i2c = busio.I2C(scl = board.GP27, sda=board.GP26)  # uses board.SCL and board.SDA
bmi = BMI160.BMI160(i2c)
bmi.gyro_range = BMI160.GYRO_RANGE_500

# Create a group for the face and its features
face_group_1 = displayio.Group()
face1 = Face.Face(screen_width=display.width, screen_height=display.height)
face1.drawFace(face_group_1)

face_group_2 = displayio.Group()
face2 = Face.Face2(screen_width=display.width, screen_height=display.height)
face2.drawFace(face_group_2)

while True:
    display.show(face_group_1)
    time.sleep(5)
    display.show(face_group_2)
    time.sleep(5)

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
