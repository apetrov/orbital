
import pygame
import time
import math

state = dict(
    earth=[-1, 0],
    sun=[0, 0],
    mars=[-1.5, 0],
    earth_r = 20,
    mars_r=18,
    sun_r = 45,
)

def move(z):
    x, y = z
    r = (x**2 + y**2)**0.5
    phi = math.atan2(y, x)
    phi += 0.1 * r**(-1.5)

    return [
            r * math.cos(phi),
            r * math.sin(phi)
    ]

def project(coords):
    return [
        int(coords[0]*200 + 400),
        int(coords[1]*200 + 300)
    ]

def draw_cicle(screen):
    pygame.draw.circle(screen, (255, 255, 255), (400, 300), 50)


def draw_sun_and_planel(screen):
    pygame.draw.circle(screen, (255, 255, 0), project(state['sun']), state['sun_r']) # sun
    pygame.draw.circle(screen, (255, 0,0), project(state['mars']) , state['mars_r'])   # mars
    pygame.draw.circle(screen, (0, 0, 255), project(state['earth']) , state['earth_r'])   # earth
    ##########pygame.draw.rect(screen, (255, 255, 255), (400, 300, 100, 20))
    ##############pygame.draw.polygon(screen, (255, 255, 255), [(400, 300), (300, 300), (400, 200)])


def create_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    pygame.display.set_caption('Basic Pygame Window')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        #draw_cicle(screen)
        time.sleep(0.1)
        state['earth'] = move(state['earth'])
        state['mars'] = move(state['mars'])
        draw_sun_and_planel(screen)
        pygame.display.flip()

    pygame.quit()

def main():
    create_game()

if __name__ == '__main__':
    main()

def main():
    print('Hello, World!')

if __name__ == '__main__':
    main()
