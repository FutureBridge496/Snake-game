class Snake:
    def __init__(self):
        self.position = [0,0] # Row, Column

        # 1 -> DOWN
        # 2 -> UP
        # 3 -> RIGHT
        # 4 -> LEFT
        self.direction = 1
        self.body_length = 2