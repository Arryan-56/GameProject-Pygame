# ----------------------
# BULLET CLASS
# ----------------------
class Bullet(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._width = 5
        self._height = 15
        self._speed = 7

    def move(self):
        self._y -= self._speed

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self._x, self._y, self._width, self._height))

    def off_screen(self):
        return self._y < -10

    def get_rect(self):
        return (self._x, self._y, self._width, self._height)
