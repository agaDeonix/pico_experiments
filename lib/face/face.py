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

        self.center_x = self.screen_width // 2
        self.center_y = self.screen_height // 2
        self.eye_offset_x = self.pixel_size * 8
        self.eye_offset_y = -self.pixel_size * 1

        self.left_eye = eye.Eye(self.pixel_size, self.center_x - self.eye_offset_x, self.center_y - self.eye_offset_y)
        self.right_eye = eye.Eye(self.pixel_size, self.center_x + self.eye_offset_x, self.center_y - self.eye_offset_y)

        self.left_eyebrow = eyebrow.EyebrowNone(self.pixel_size, self.center_x - self.eye_offset_x, self.center_y - self.eye_offset_y - int(self.pixel_size * 3.5), True)
        self.right_eyebrow = eyebrow.EyebrowNone(self.pixel_size, self.center_x + self.eye_offset_x, self.center_y - self.eye_offset_y - int(self.pixel_size * 3.5), False)

        self.left_cheek = cheek.Cheek(self.pixel_size, self.center_x - self.eye_offset_x, self.center_y - self.eye_offset_y + int(self.pixel_size * 2.5), True)
        self.right_cheek = cheek.Cheek(self.pixel_size, self.center_x + self.eye_offset_x, self.center_y - self.eye_offset_y + int(self.pixel_size * 2.5), False)
        self.mouth = mouth.Mouth(self.pixel_size, self.center_x, self.center_y + self.pixel_size * 3)

    def drawFace(self, 
                 face_group: Group):
        # Draw the head (main circle)
        head_radius = self.center_x
        head = Circle(self.center_x, self.center_y, head_radius, fill=colors.FACE)
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

        self.left_eyebrow = eyebrow.Eyebrow(self.pixel_size, self.center_x - self.eye_offset_x, self.center_y - self.eye_offset_y - int(self.pixel_size * 3.5), True)
        self.right_eyebrow = eyebrow.Eyebrow(self.pixel_size, self.center_x + self.eye_offset_x, self.center_y - self.eye_offset_y - int(self.pixel_size * 3.5), False)
        self.mouth = mouth.MouthDot(self.pixel_size, self.center_x, self.center_y + self.pixel_size * 3)


class FaceSleep(Face):

    def __init__(self,
                 screen_width: int,
                 screen_height: int):
        Face.__init__(self, screen_width, screen_height)

        self.left_eye = eye.EyeClosed(self.pixel_size, self.center_x - self.eye_offset_x, self.center_y - self.eye_offset_y)
        self.right_eye = eye.EyeClosed(self.pixel_size, self.center_x + self.eye_offset_x, self.center_y - self.eye_offset_y)
        self.mouth = mouth.MouthDot(self.pixel_size, self.center_x, self.center_y + self.pixel_size * 3)

class FaceBlink(Face):

    def __init__(self,
                 screen_width: int,
                 screen_height: int):
        Face.__init__(self, screen_width, screen_height)

        self.left_eye = eye.EyeBlink(self.pixel_size, self.center_x - self.eye_offset_x, self.center_y - self.eye_offset_y)

class FaceBlinkTongue(Face):

    def __init__(self,
                 screen_width: int,
                 screen_height: int):
        Face.__init__(self, screen_width, screen_height)

        self.left_eye = eye.EyeBlink(self.pixel_size, self.center_x - self.eye_offset_x, self.center_y - self.eye_offset_y)
        self.mouth = mouth.MouthTongue(self.pixel_size, self.center_x, self.center_y + self.pixel_size * 3)

class FaceTongue(Face):

    def __init__(self,
                 screen_width: int,
                 screen_height: int):
        Face.__init__(self, screen_width, screen_height)

        self.mouth = mouth.MouthTongue(self.pixel_size, self.center_x, self.center_y + self.pixel_size * 3)


class FaceTest(Face):

    def __init__(self,
                 screen_width: int,
                 screen_height: int):
        Face.__init__(self, screen_width, screen_height)
        self.left_eye = eye.EyeHeart(self.pixel_size, self.center_x - self.eye_offset_x, self.center_y - self.eye_offset_y)
        self.right_eye = eye.EyeHeart(self.pixel_size, self.center_x + self.eye_offset_x, self.center_y - self.eye_offset_y)
        self.left_cheek = cheek.CheekNone(self.pixel_size, self.center_x - self.eye_offset_x, self.center_y - self.eye_offset_y + int(self.pixel_size * 2.5), True)
        self.right_cheek = cheek.CheekNone(self.pixel_size, self.center_x + self.eye_offset_x, self.center_y - self.eye_offset_y + int(self.pixel_size * 2.5), False)
        # self.left_eyebrow = eyebrow.Eyebrow(self.pixel_size, self.center_x - self.eye_offset_x, self.center_y - self.eye_offset_y - int(self.pixel_size * 3.5), True)
        # self.right_eyebrow = eyebrow.Eyebrow(self.pixel_size, self.center_x + self.eye_offset_x, self.center_y - self.eye_offset_y - int(self.pixel_size * 3.5), False)
        self.mouth = mouth.MouthCat(self.pixel_size, self.center_x, self.center_y + self.pixel_size * 3)
