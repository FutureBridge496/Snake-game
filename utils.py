SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SQUARE_LENGTH = 30
FPS = 60

rows = int(SCREEN_HEIGHT / SQUARE_LENGTH) # 20
cols = int(SCREEN_WIDTH / SQUARE_LENGTH) # 20

def get_x(col):
    return col * SQUARE_LENGTH

def get_y(row):
    return row * SQUARE_LENGTH