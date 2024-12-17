import utils
import boards
import pygame
import math

# Bubble size: 44 x 44
# Odd rows: max 12 bubbles, start from 0px width, first bubble center 22px width 22px height
# Even rows: max 11 bubbles, start from 22px width, first bubble center 44px width
# Rows start with 1

pygame.init()

screen = pygame.display.set_mode((528, 700))
pygame.display.set_caption('Pygame Window')

bubble_color = (0, 255, 0)
bubble_center = [268, 650]
bubble_radius = 20
bubbles_list = []
velocity = [0, 0]
speed = 1

running = True
destination = None
bubble_pos = bubble_center[:]
bubble_center_copy = bubble_center

boards.draw_board1(bubbles_list)

# print(bubbles_list[51]['neighbours'][2]['center'])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            destination = event.pos
            dx, dy = destination[0] - bubble_center[0], destination[1] - bubble_center[1]
            distance = math.hypot(dx, dy)
            if distance > 0:
                velocity = [dx / distance, dy / distance]

    screen.fill((229, 255, 204))

    if destination:
        bubble_pos[0] += velocity[0] * speed
        bubble_pos[1] += velocity[1] * speed
        bubble_center = [int(bubble_pos[0]), int(bubble_pos[1])]

        velocity = utils.check_wall_collision(bubble_center, velocity, bubble_radius, 528)

        if utils.verify_bubble_collision(bubble_center, bubble_radius, bubbles_list) or utils.check_ceiling_collision(bubble_center, bubble_radius):
            destination = None
            bubbles_list.append({
                'center': [bubble_center[0] + 2, bubble_center[1] + 2],
                'radius': 20,
                'row': None,
                'color': bubble_color,
                'shadow_color': (40, 175, 40),
                'neighbours': []
            })
            bubble_center = bubble_center_copy
            bubble_pos = bubble_center[:]
            velocity = [0, 0]

    utils.draw_bubble(screen, bubble_center, bubble_radius, bubble_color, (40, 175, 40))
    pygame.draw.rect(screen, (25, 51, 0), (0, 672, 528, 30))

    utils.draw_from_map(screen, bubbles_list)

    pygame.display.flip()

utils.stop_program()
