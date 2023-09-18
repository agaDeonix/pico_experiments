from adafruit_display_shapes.rect import Rect
import displayio
import lib.face.colors as colors

class Cheek:
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
        if self.is_left:
            face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y, self.pixel_size * 4, self.pixel_size * 2, fill=colors.PEACH))
        else:
            face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y, self.pixel_size * 4, self.pixel_size * 2, fill=colors.PEACH))