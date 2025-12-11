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
