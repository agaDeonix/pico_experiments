from adafruit_display_shapes.rect import Rect
import displayio
import lib.face.colors as colors

class Eyebrow:
    def __init__(self,
                 pixel_size: int,
                 center_x: int,
                 center_y: int,
                 is_left: bool):
        self.pixel_size=pixel_size
        self.center_x=center_x
        self.center_y=center_y
        self.is_left=is_left

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 3), self.pixel_size * 3, self.pixel_size * 1, fill=colors.BLACK))
        face.append(Rect(self.center_x + int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))

class EyebrowNone(Eyebrow):

    def draw(self,
             face: Group):
        pass

class EyebrowSad(Eyebrow):

    def draw(self,
             face: Group):
        if self.is_left:
            face.append(Rect(self.center_x - int(self.pixel_size * 1), self.center_y - int(self.pixel_size * 1), self.pixel_size * 2, self.pixel_size * 1, fill=colors.BLACK))
            face.append(Rect(self.center_x + int(self.pixel_size * 1), self.center_y - int(self.pixel_size * 2), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))
        else:
            face.append(Rect(self.center_x - int(self.pixel_size * 1), self.center_y - int(self.pixel_size * 1), self.pixel_size * 2, self.pixel_size * 1, fill=colors.BLACK))
            face.append(Rect(self.center_x - int(self.pixel_size * 2), self.center_y - int(self.pixel_size * 2), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))

class EyebrowShock(Eyebrow):

    def draw(self,
             face: Group):
        if self.is_left:
            face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 3), self.pixel_size * 3, self.pixel_size * 1, fill=colors.BLACK))
            face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))
        else:
            face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 3), self.pixel_size * 3, self.pixel_size * 1, fill=colors.BLACK))
            face.append(Rect(self.center_x + int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))

class EyebrowLong(Eyebrow):

    def draw(self,
             face: Group):
        if self.is_left:
            face.append(Rect(self.center_x + int(self.pixel_size * 0.5), self.center_y - int(self.pixel_size * 3), self.pixel_size * 2, self.pixel_size * 1, fill=colors.BLACK))
            face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 2, self.pixel_size * 1, fill=colors.BLACK))
        else:
            face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 3), self.pixel_size * 2, self.pixel_size * 1, fill=colors.BLACK))
            face.append(Rect(self.center_x - int(self.pixel_size * 0.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 2, self.pixel_size * 1, fill=colors.BLACK))

class EyebrowGrin(Eyebrow):

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 0), self.pixel_size * 5, self.pixel_size * 1, fill=colors.BLACK))

class EyebrowAngry(Eyebrow):

    def draw(self,
             face: Group):
        if self.is_left:
            face.append(Rect(self.center_x - int(self.pixel_size * 0.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))
            face.append(Rect(self.center_x + int(self.pixel_size * 0.5), self.center_y - int(self.pixel_size * 1), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))
            face.append(Rect(self.center_x + int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 0), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))
        else:
            face.append(Rect(self.center_x - int(self.pixel_size * 0.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))
            face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 1), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))
            face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 0), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))