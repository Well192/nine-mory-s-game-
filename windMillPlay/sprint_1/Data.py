import numpy as np

class Position:
    def __init__(self, x, y):
        self.empty=True
        self.x = int(x)
        self.y = int(y)

    def in_the_radio(self,x ,y):
        if np.sqrt((x-self.x)**2+(y-self.y)**2) < 4.83:
            return True
        return False

position_list=list()
position_list.append(Position(30, 20))
position_list.append(Position(190, 20))
position_list.append(Position(350, 20))
position_list.append(Position(350, 145))
position_list.append(Position(350, 265))
position_list.append(Position(190, 265))
position_list.append(Position(30, 265))
position_list.append(Position(30, 140))
position_list.append(Position(60, 50))
position_list.append(Position(315, 50))
position_list.append(Position(315, 145))
position_list.append(Position(315, 235))
position_list.append(Position(190, 235))
position_list.append(Position(60, 235))
position_list.append(Position(60, 145))
position_list.append(Position(100, 80))
position_list.append(Position(190, 80))
position_list.append(Position(275, 80))
position_list.append(Position(275, 145))
position_list.append(Position(275, 200))
position_list.append(Position(190, 200))
position_list.append(Position(100, 200))
position_list.append(Position(100, 145))

