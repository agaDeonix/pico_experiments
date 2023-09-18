import math
import displayio
import lib.face.colors as colors
import lib.face.eye as eye
import lib.face.eyebrow as eyebrow
import lib.face.cheek as cheek
import lib.face.mouth as mouth
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.rect import Rect

class Face:

    FACE_WIDTH = 28

    def __init__(self,
                 screen_width: int,
                 screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pixel_size = min(screen_width, screen_height) // self.FACE_WIDTH

        center_x = self.screen_width // 2
        center_y = self.screen_height // 2
        eye_offset_x = self.pixel_size * 8
        eye_offset_y = -self.pixel_size * 1

        self.left_eye = eye.Eye(self.pixel_size, center_x - eye_offset_x, center_y - eye_offset_y)
        self.right_eye = eye.Eye(self.pixel_size, center_x + eye_offset_x, center_y - eye_offset_y)

        self.left_eyebrow = eyebrow.EyebrowNone(self.pixel_size, center_x - eye_offset_x, center_y - eye_offset_y - int(self.pixel_size * 3.5), True)
        self.right_eyebrow = eyebrow.EyebrowNone(self.pixel_size, center_x + eye_offset_x, center_y - eye_offset_y - int(self.pixel_size * 3.5), False)

        self.left_cheek = cheek.Cheek(self.pixel_size, center_x - eye_offset_x, center_y - eye_offset_y + int(self.pixel_size * 2.5), True)
        self.right_cheek = cheek.Cheek(self.pixel_size, center_x + eye_offset_x, center_y - eye_offset_y + int(self.pixel_size * 2.5), False)
        self.mouth = mouth.Mouth(self.pixel_size, center_x, center_y + self.pixel_size * 3)

    def drawCheek(self, 
            x: int,
            y: int,
            face_group: Group):
        face_group.append(Rect(x, y, self.pixel_size * 4, self.pixel_size * 2, fill=colors.PEACH))

    def drawFace(self, 
                 face_group: Group):
        # Draw the head (main circle)
        center_x = self.screen_width // 2
        center_y = self.screen_height // 2
        head_radius = center_x
        head = Circle(center_x, center_y, head_radius, fill=colors.FACE)
        face_group.append(head)

        self.left_eye.draw(face_group)
        self.right_eye.draw(face_group)

        self.left_eyebrow.draw(face_group)
        self.right_eyebrow.draw(face_group)

        self.left_cheek.draw(face_group)
        self.right_cheek.draw(face_group)

        self.mouth.draw(face_group)


class Face2(Face):

    FACE_WIDTH = 28

    def __init__(self,
                 screen_width: int,
                 screen_height: int):
        Face.__init__(self, screen_width, screen_height)

        center_x = self.screen_width // 2
        center_y = self.screen_height // 2
        eye_offset_x = self.pixel_size * 8
        eye_offset_y = -self.pixel_size * 1

        self.left_eyebrow = eyebrow.Eyebrow(self.pixel_size, center_x - eye_offset_x, center_y - eye_offset_y - int(self.pixel_size * 3.5), True)
        self.right_eyebrow = eyebrow.Eyebrow(self.pixel_size, center_x + eye_offset_x, center_y - eye_offset_y - int(self.pixel_size * 3.5), False)
        self.mouth = mouth.MouthDot(self.pixel_size, center_x, center_y + self.pixel_size * 3)
