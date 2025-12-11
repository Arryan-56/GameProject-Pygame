# ----------------------
# ENEMY CLASS
# ----------------------
class Enemy(GameObject):
    def __init__(self):
        x_pos = random.randint(0, WIDTH-40)
        super().__init__(x_pos, 0)
        self._size = 40
        self._speed = 3

    def move(self):
        self._y += self._speed

    def draw(self):
        pygame.draw.circle(screen, RED, (self._x+self._size//2, self._y+self._size//2), self._size//2)

    def off_screen(self):
        return self._y > HEIGHT

    def get_rect(self):
        return (self._x, self._y, self._size, self._size)
