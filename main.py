# ----------------------
# COMMIT 1 — IMPORTS + BASIC SETUP
# ----------------------

import pygame
import random
import sys
import os
import csv
import time
from abc import ABC, abstractmethod

pygame.init()

WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter - Persistent Dataset CSV")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# create data folder
os.makedirs("data", exist_ok=True)
csv_path = os.path.join("data", "game_dataset.csv")
# ----------------------
# COMMIT 2 — ABSTRACT BASE CLASS
# ----------------------

class GameObject(ABC):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    def get_position(self):
        return self._x, self._y
# ----------------------
# COMMIT 3 — PLAYER, ENEMY, BULLET CLASSES
# ----------------------

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
# ----------------------
# COMMIT 4 — COLLISION, GAME VARIABLES, CSV START INDEX
# ----------------------

def check_collision(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    return x1 < x2+w2 and x1+w1 > x2 and y1 < y2+h2 and y1+h1 > y2


player = Player()
enemies = []
bullets = []
score = 0
game_over = False
start_time = time.time()

# Enemy tracking variables
enemies_spawned = 0
enemies_destroyed = 0
enemies_reached_bottom = 0

# Gameplay histories for CSV dataset
score_history = []
player_lives_history = []
bullets_fired_history = []
hits_history = []
enemies_spawned_history = []
enemies_destroyed_history = []
enemies_reached_bottom_history = []


def spawn_enemy():
    global enemies_spawned
    enemies.append(Enemy())
    enemies_spawned += 1


# determine CSV starting index
if os.path.exists(csv_path):
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        time_start = sum(1 for row in reader)
else:
    time_start = 0
