from adafruit_display_shapes.rect import Rect
import displayio
import lib.face.colors as colors

class Mouth:
    def __init__(self,
                 pixel_size: int,
                 center_x: int,
                 center_y: int,):
        self.pixel_size=pixel_size
        self.center_x=center_x
        self.center_y=center_y

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y, self.pixel_size * 3, self.pixel_size * 1, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 1, self.pixel_size * 2, fill=colors.BLACK))
        face.append(Rect(self.center_x + int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 1, self.pixel_size * 2, fill=colors.BLACK))

class MouthDot(Mouth):

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 0.5), self.center_y - int(self.pixel_size * 1), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))

class MouthTongue(Mouth):

    def draw(self,
             face: Group):
        super().draw(face)
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y + int(self.pixel_size * 1), self.pixel_size * 3, self.pixel_size * 2, fill=colors.RED))

class MouthCat(Mouth):

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 3.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 1, self.pixel_size * 2, fill=colors.BLACK))
        face.append(Rect(self.center_x + int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 1, self.pixel_size * 2, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 0.5), self.center_y - int(self.pixel_size * 1), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y, self.pixel_size * 2, self.pixel_size * 1, fill=colors.BLACK))
        face.append(Rect(self.center_x + int(self.pixel_size * 0.5), self.center_y, self.pixel_size * 2, self.pixel_size * 1, fill=colors.BLACK))

class MouthKiss(Mouth):

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x + int(self.pixel_size * 0.5), self.center_y - int(self.pixel_size * 3), self.pixel_size * 1, self.pixel_size * 2, fill=colors.BLACK))
        face.append(Rect(self.center_x + int(self.pixel_size * 0.5), self.center_y - int(self.pixel_size * 0), self.pixel_size * 1, self.pixel_size * 2, fill=colors.BLACK))

        face.append(Rect(self.center_x - int(self.pixel_size * 0.5), self.center_y - int(self.pixel_size * 1), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))

        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 4), self.pixel_size * 2, self.pixel_size * 1, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y + int(self.pixel_size * 2), self.pixel_size * 2, self.pixel_size * 1, fill=colors.BLACK))

class MouthVampire(Mouth):

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 3, self.pixel_size * 1, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 1, self.pixel_size * 2, fill=colors.BLACK))
        face.append(Rect(self.center_x + int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 1, self.pixel_size * 2, fill=colors.BLACK))

class MouthSad(Mouth):

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 3, self.pixel_size * 1, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 1), self.pixel_size * 1, self.pixel_size * 2, fill=colors.BLACK))
        face.append(Rect(self.center_x + int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 1), self.pixel_size * 1, self.pixel_size * 2, fill=colors.BLACK))

class MouthAngry(Mouth):

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 1), self.pixel_size * 3, self.pixel_size * 1, fill=colors.BLACK))

class MouthOpen(Mouth):

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 3), self.pixel_size * 3, self.pixel_size * 1, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 5, self.pixel_size * 3, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 1), self.pixel_size * 3, self.pixel_size * 1, fill=colors.RED))

class MouthBigOpen(Mouth):

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 3, self.pixel_size * 1, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 1), self.pixel_size * 5, self.pixel_size * 4, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y + int(self.pixel_size * 1), self.pixel_size * 3, self.pixel_size * 1, fill=colors.RED))

class MouthLaugh(Mouth):

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y + int(self.pixel_size * 1), self.pixel_size * 3, self.pixel_size * 1, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 5, self.pixel_size * 3, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 0), self.pixel_size * 3, self.pixel_size * 1, fill=colors.RED))

class MouthBigLaugh(Mouth):

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y + int(self.pixel_size * 2), self.pixel_size * 3, self.pixel_size * 1, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 5, self.pixel_size * 4, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y + int(self.pixel_size * 1), self.pixel_size * 3, self.pixel_size * 1, fill=colors.RED))

class MouthLine(Mouth):

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 0), self.pixel_size * 5, self.pixel_size * 1, fill=colors.BLACK))

class MouthBigLine(Mouth):

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 3.5), self.center_y + int(self.pixel_size * 1), self.pixel_size * 7, self.pixel_size * 1, fill=colors.BLACK))

class MouthCatLaugh(Mouth):

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y + int(self.pixel_size * 2), self.pixel_size * 3, self.pixel_size * 1, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 1), self.pixel_size * 5, self.pixel_size * 3, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 1.5), self.center_y + int(self.pixel_size * 1), self.pixel_size * 3, self.pixel_size * 1, fill=colors.RED))
        face.append(Rect(self.center_x - int(self.pixel_size * 3.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))
        face.append(Rect(self.center_x + int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))
        face.append(Rect(self.center_x - int(self.pixel_size * 0.5), self.center_y - int(self.pixel_size * 2), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))

class MouthGrin(Mouth):

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 2.5), self.center_y - int(self.pixel_size * 0), self.pixel_size * 4, self.pixel_size * 1, fill=colors.BLACK))
        face.append(Rect(self.center_x + int(self.pixel_size * 1.5), self.center_y - int(self.pixel_size * 1), self.pixel_size * 1, self.pixel_size * 1, fill=colors.BLACK))

class Mouth2DotV(Mouth):

    def draw(self,
             face: Group):
        face.append(Rect(self.center_x - int(self.pixel_size * 0.5), self.center_y - int(self.pixel_size * 1), self.pixel_size * 1, self.pixel_size * 2, fill=colors.BLACK))