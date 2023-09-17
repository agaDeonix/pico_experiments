import math
import displayio
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.rect import Rect


# Define colors
FACE_COLOR = 0xFFD700
BLACK_COLOR = 0x000000
WHITE_COLOR = 0xFFFFFF
GREY_COLOR = 0x333333
LIGHT_GREY_COLOR = 0x555555
LIGHT_PINK_COLOR = 0xFFB6C1
MOUTH_COLOR = 0x000000

PIXEL_SIZE = 8
SCREEN_WIDTH = 240
SCREEN_HEIGHT = 240

class Face:

    def drawEye(self, 
                center_x: int,
                center_y: int,
                face_group: Group):
        face_group.append(Rect(center_x - int(PIXEL_SIZE * 2.5), center_y - int(PIXEL_SIZE * 1.5), PIXEL_SIZE * 5, PIXEL_SIZE * 3, fill=BLACK_COLOR))
        face_group.append(Rect(center_x - int(PIXEL_SIZE * 1.5), center_y - int(PIXEL_SIZE * 2.5), PIXEL_SIZE * 3, PIXEL_SIZE * 5, fill=BLACK_COLOR))

        face_group.append(Rect(center_x - int(PIXEL_SIZE * 1.5), center_y - int(PIXEL_SIZE * 1.5), PIXEL_SIZE * 3, PIXEL_SIZE * 3, fill=GREY_COLOR))
        face_group.append(Rect(center_x - int(PIXEL_SIZE * 0.5), center_y - int(PIXEL_SIZE * 1.5), PIXEL_SIZE * 2, PIXEL_SIZE * 2, fill=BLACK_COLOR))
        face_group.append(Rect(center_x - int(PIXEL_SIZE * 0.5), center_y - int(PIXEL_SIZE * 0.5), PIXEL_SIZE * 1, PIXEL_SIZE * 1, fill=LIGHT_GREY_COLOR))
        face_group.append(Rect(center_x + int(PIXEL_SIZE * 0.5), center_y - int(PIXEL_SIZE * 1.5), PIXEL_SIZE * 1, PIXEL_SIZE * 1, fill=WHITE_COLOR))


    def drawCheek(self, 
            x: int,
            y: int,
            face_group: Group):
        face_group.append(Rect(x, y, PIXEL_SIZE * 4, PIXEL_SIZE * 2, fill=LIGHT_PINK_COLOR))

    

    def drawMouth(self, 
                  center_x: int,
                  center_y: int,
                  face_group: Group):
        face_group.append(Rect(center_x - int(PIXEL_SIZE * 1.5), center_y, PIXEL_SIZE * 3, PIXEL_SIZE * 1, fill=BLACK_COLOR))
        face_group.append(Rect(center_x - int(PIXEL_SIZE * 2.5), center_y - int(PIXEL_SIZE * 2), PIXEL_SIZE * 1, PIXEL_SIZE * 2, fill=BLACK_COLOR))
        face_group.append(Rect(center_x + int(PIXEL_SIZE * 1.5), center_y - int(PIXEL_SIZE * 2), PIXEL_SIZE * 1, PIXEL_SIZE * 2, fill=BLACK_COLOR))

    def drawFace(self, face_group: Group):
        # Draw the head (main circle)
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2
        head_radius = center_x
        head = Circle(center_x, center_y, head_radius, fill=FACE_COLOR)
        face_group.append(head)

        # Draw the eyes as pixel blocks
        eye_offset_x = PIXEL_SIZE * 8
        eye_offset_y = -PIXEL_SIZE * 1
        self.drawEye(center_x - eye_offset_x, center_y - eye_offset_y, face_group)
        self.drawEye(center_x + eye_offset_x, center_y - eye_offset_y, face_group)

        self.drawCheek(center_x - eye_offset_x - int(PIXEL_SIZE * 2.5), center_y - eye_offset_y + int(PIXEL_SIZE * 2.5), face_group)
        self.drawCheek(center_x + eye_offset_x - int(PIXEL_SIZE * 1.5), center_y - eye_offset_y + int(PIXEL_SIZE * 2.5), face_group)

        mouth_offset_y = PIXEL_SIZE * 3
        self.drawMouth(center_x, center_y - eye_offset_y + mouth_offset_y, face_group)
