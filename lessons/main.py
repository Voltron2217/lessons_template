import pygame


SIZE = (640, 480)
# SIZE = (320, 240)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE, pygame.SCALED, vsync=True)
    font = pygame.font.SysFont('Arial', 18, bold=False)
    pygame.display.set_caption('Pygame - Lesson')
    screen.fill('black')

    clock = pygame.time.Clock()
    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # TODO: Write your code here ...
        draw(screen)

        draw_fps_counter(screen, font, clock)
        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60

    pygame.quit()


def draw_fps_counter(screen, font, clock):
    fps = str(round(clock.get_fps(), 1))
    fps_t = font.render(fps, 1, pygame.Color('RED'), 'black')
    screen.blit(fps_t, (0, 0))


def draw(screen: pygame.Surface):
    screen.fill('black')
    width, height = screen.get_size()

    pygame.draw.rect(
        screen,
        'white',
        (100, 100, width - 200, height - 200),
    )

    mid_x, mid_y = width // 2, height // 2
    pygame.draw.line(screen, 'red', (100, mid_y), (width - 101, mid_y))

    screen.set_at((mid_x, mid_y - 50), 'black')
