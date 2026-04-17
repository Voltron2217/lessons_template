import pygame
import random


class Stars:
    name = 'Stars'

    def __init__(self, count):
        self.count = count

    def draw(self, screen: pygame.Surface):
        if self.count <= 0:
            return

        width, height = screen.get_size()
        rand_x = random.randint(0, width - 1)
        rand_y = random.randint(0, height - 1)
        screen.set_at((rand_x, rand_y), 'white')
        self.count -= 1
