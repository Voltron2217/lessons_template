import pygame


i = 0
j = 0


class Lines:
    name = 'Lines'

    def __init__(self, screen: pygame.Surface):
        width, height = screen.get_size()
        self.start_point = (width // 2, height // 2)

    def draw(self, screen: pygame.Surface):
        global i, j
        width, height = screen.get_size()
        pygame.draw.line(screen, 'black', self.start_point, (width - i, height - j))
        if height >= j >= 0 and i == 0:
            j += 4
        elif j >= height and width >= i >= 0:
            i += 4
        elif (height >= j >= 0 or height + 4 >= j >= 0) and i >= width:
            j -= 4
        elif j <= height and (width >= i >= 0 or width + 4 >= i >= 0):
            i -= 4
