import math

class GeometryHelper:

    @staticmethod
    def get_new_goal_pos(x: float,
                         y: float,
                         goal_x: float,
                         goal_y: float,
                         radius: float):

        angle = GeometryHelper.angle_between_2_lines(
            x, y, x + 10.0, y, x, y, goal_x, goal_y
        )
        
        length = GeometryHelper.length(x, y, goal_x, goal_y)

        if length <= radius:
            return (goal_x, goal_y)
        else:
            return (
                x + radius * math.cos(angle),
                y - radius * math.sin(angle)
            )

    @staticmethod
    def angle_between_2_lines(x1: float, y1: float, x2: float, y2: float,
                              x3: float, y3: float, x4: float, y4: float) -> float:
        angle1 = math.atan2(y1 - y2, x1 - x2)
        angle2 = math.atan2(y3 - y4, x3 - x4)
        return angle1 - angle2

    @staticmethod
    def length(x1: float, y1: float, x2: float, y2: float) -> float:
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)