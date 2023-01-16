from SnakeBox import *
distance = 20

class SnakeBody:

    def __init__(self, boxes=3):
        self.self = []
        for i in range(boxes):
            self.self.append(SnakeBox())

        start_index = distance
        for box in self.self:
            print(box.pos())
            # cor = (start_index-distance)
            box.setx(start_index-distance)
            start_index -= distance
