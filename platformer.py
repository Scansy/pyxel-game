import pyxel # type: ignore

APP_WIDTH = 160
APP_HEIGHT = 100

CENTER_X = APP_WIDTH / 2
CENTER_Y = APP_HEIGHT / 2

PLAYER_RADIUS = 7
PLAYER_COLOR = 3
PLAYER_X_SPEED = 3


class App():
    def __init__(self):
        pyxel.init(APP_WIDTH, APP_HEIGHT)
        self.player = Player(CENTER_X, CENTER_Y)
        pyxel.run(self.update, self.draw)

    def draw(self):
        self.player.draw()
    
    def update(self):
        self.player.update()

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.direction = 0
    
    def draw(self):
        pyxel.cls(1)
        pyxel.circ(self.x, self.y, PLAYER_RADIUS, PLAYER_COLOR)

    def update(self):
        # when directions are pressed
        if pyxel.btn(pyxel.KEY_D):
            self.dx = PLAYER_X_SPEED
        if pyxel.btn(pyxel.KEY_A) and self.x:
            self.dx = -PLAYER_X_SPEED
        
        # adds to current x 
        self.x += self.dx

        # reset velocity
        self.dx = 0

App()