class Player(GameObject):
    def __init__(self):
        super().__init__(WIDTH//2, HEIGHT-80)
        self._size = 50
        self._speed = 5
        self._lives = 3
        self.bullets_fired = 0
        self.hits = 0
        self.lives_lost = 0

    def get_lives(self):
        return self._lives

    def reduce_life(self):
        self._lives -= 1
        self.lives_lost += 1

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self._x > 0:
            self._x -= self._speed
        if keys[pygame.K_RIGHT] and self._x < WIDTH - self._size:
            self._x += self._speed

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self._x, self._y, self._size, self._size))

    def get_rect(self):
        return (self._x, self._y, self._size, self._size)
