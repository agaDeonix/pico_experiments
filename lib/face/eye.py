from adafruit_display_shapes.rect import Rect
import displayio
import lib.face.colors as colors

class Eye:
    def __init__(self,
                 pixel_size: int,
                 center_x: int,
                 center_y: int,):
        self.pixel_size=pixel_size
        self.center_x=center_x
        self.center_y=center_y

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 1.5), self.pixel_size * 5, self.pixel_size * 3, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 2.5), self.pixel_size * 3, self.pixel_size * 5, fill=colors.BLACK))

        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 1.5), self.pixel_size * 3, self.pixel_size * 3, fill=colors.GREY))
        face.append(Rect(self.center_x - int(self.pixel_size * 0.5), self.center_y - int(self.pixel_size * 1.5), self.pixel_size * 2, self.pixel_size * 2, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 0.5), self.center_y - int(self.pixel_size * 0.5), self.pixel_size * 1, self.pixel_size * 1, fill=colors.LIGHT_GREY))
        face.append(Rect(self.center_x + int(self.pixel_size * 0.5), self.center_y - int(self.pixel_size * 1.5), self.pixel_size * 1, self.pixel_size * 1, fill=colors.WHITE))

class EyeBlink(Eye):
    def __init__(self,
                 pixel_size: int,
                 center_x: int,
                 center_y: int,):
        self.pixel_size=pixel_size
        self.center_x=center_x
        self.center_y=center_y

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 1.5), self.pixel_size * 1, self.pixel_size * 3, fill=colors.BLACK))
        face.append(Rect(self.center_x + int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 1.5), self.pixel_size * 1, self.pixel_size * 3, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 2.5), self.pixel_size * 3, self.pixel_size * 1, fill=colors.BLACK))

class EyeClosed(Eye):
    def __init__(self,
                 pixel_size: int,
                 center_x: int,
                 center_y: int,):
        self.pixel_size=pixel_size
        self.center_x=center_x
        self.center_y=center_y

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 1.5), self.pixel_size * 1, self.pixel_size * 3, fill=colors.BLACK))
        face.append(Rect(self.center_x + int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 1.5), self.pixel_size * 1, self.pixel_size * 3, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y + int(self.pixel_size * 1.5), self.pixel_size * 3, self.pixel_size * 1, fill=colors.BLACK))