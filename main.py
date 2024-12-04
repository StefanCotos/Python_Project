import time

import pygame
import sys
import math

pygame.init()

screen = pygame.display.set_mode((420, 600))
pygame.display.set_caption('Pygame Window')

bubble_color = (0, 255, 0)
bubble_center = [200, 550]
bubble_radius = 20


def draw_bubble(screen, center, radius, color, shadow_color):
    shadow_offset = 2
    # Shadow
    pygame.draw.circle(screen, shadow_color, (center[0] + shadow_offset, center[1] + shadow_offset), radius)
    # Bubble
    pygame.draw.circle(screen, color, center, radius)


def draw_table(screen):
    draw_bubble(screen, [40, 20], 20, (0, 0, 255), (0, 0, 0))
    draw_bubble(screen, [82, 20], 20, (0, 0, 255), (0, 0, 0))
    draw_bubble(screen, [124, 20], 20, (0, 0, 255), (0, 0, 0))
    draw_bubble(screen, [166, 20], 20, (0, 0, 255), (0, 0, 0))
    draw_bubble(screen, [248, 20], 20, (0, 0, 255), (0, 0, 0))
    draw_bubble(screen, [290, 20], 20, (0, 0, 255), (0, 0, 0))
    draw_bubble(screen, [332, 20], 20, (0, 0, 255), (0, 0, 0))
    draw_bubble(screen, [374, 20], 20, (0, 0, 255), (0, 0, 0))

    draw_bubble(screen, [20, 56], 20, (255, 255, 0), (205, 205, 32))
    draw_bubble(screen, [62, 56], 20, (255, 255, 0), (205, 205, 32))
    draw_bubble(screen, [104, 56], 20, (255, 255, 0), (205, 205, 32))
    draw_bubble(screen, [146, 56], 20, (255, 255, 0), (205, 205, 32))
    draw_bubble(screen, [188, 56], 20, (255, 255, 0), (205, 205, 32))
    draw_bubble(screen, [230, 56], 20, (255, 255, 0), (205, 205, 32))
    draw_bubble(screen, [272, 56], 20, (255, 255, 0), (205, 205, 32))
    draw_bubble(screen, [314, 56], 20, (255, 255, 0), (205, 205, 32))
    draw_bubble(screen, [356, 56], 20, (255, 255, 0), (205, 205, 32))
    draw_bubble(screen, [398, 56], 20, (255, 255, 0), (205, 205, 32))

    draw_bubble(screen, [84, 91], 20, (255, 0, 0), (150, 0, 0))
    draw_bubble(screen, [126, 91], 20, (255, 0, 0), (150, 0, 0))
    draw_bubble(screen, [292, 91], 20, (255, 0, 0), (150, 0, 0))
    draw_bubble(screen, [334, 91], 20, (255, 0, 0), (150, 0, 0))

    draw_bubble(screen, [64, 126], 20, (0, 255, 0), (0, 150, 0))
    draw_bubble(screen, [106, 126], 20, (0, 255, 0), (0, 150, 0))
    draw_bubble(screen, [148, 126], 20, (0, 255, 0), (0, 150, 0))
    draw_bubble(screen, [274, 126], 20, (0, 255, 0), (0, 150, 0))
    draw_bubble(screen, [316, 126], 20, (0, 255, 0), (0, 150, 0))
    draw_bubble(screen, [358, 126], 20, (0, 255, 0), (0, 150, 0))


running = True
bubble_clicked = False
destination = None
speed = 0.2

bubble_pos = bubble_center[:]

rect_color = (25, 51, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            destination = event.pos
            # print(f'Mouse clicked at ({destination})')

    screen.fill((229, 255, 204))

    # Move bub towards destination
    if destination:
        dx, dy = destination[0] - bubble_pos[0], destination[1] - bubble_pos[1]
        distance = math.hypot(dx, dy)
        if distance > speed:
            dx, dy = dx / distance * speed, dy / distance * speed
            bubble_pos[0] += dx
            bubble_pos[1] += dy
            bubble_center = [int(bubble_pos[0]), int(bubble_pos[1])]
        else:
            bubble_center = destination
            time.sleep(0.5)
            bubble_center = [200, 550]
            bubble_pos = bubble_center[:]
            destination = None

    draw_bubble(screen, bubble_center, bubble_radius, bubble_color, (40, 175, 40))
    pygame.draw.rect(screen, rect_color, (0, 572, 420, 30))

    draw_table(screen)

    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
