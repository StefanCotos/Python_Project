import utils
import boards
import pygame
import math
import random

# Bubble size: 44 x 44
# Odd rows: max 12 bubbles, first bubble center 22px width 22px height
# Even rows: max 11 bubbles, first bubble center 44px width 60px height
# Rows start with 1

pygame.init()

screen = pygame.display.set_mode((528, 700))
pygame.display.set_caption('Pygame Window')

bubble_center = [268, 650]
bubble_radius = 20
bubbles_list = []
velocity = [0, 0]
speed = 0.75

running = True
destination = None
bubble_pos = bubble_center[:]
bubble_center_copy = bubble_center

boards.draw_board1(bubbles_list)

# print(bubbles_list[51]['neighbours'][2]['center'])

random_color = random.choice(list(utils.verify_colors_still_available(bubbles_list)))
bubble_color = random_color[0]
shadow_color = random_color[1]

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

        velocity = utils.verify_wall_collision(bubble_center, velocity, bubble_radius, 528)

        bubble_collision = utils.verify_bubble_collision(bubble_center, bubble_radius, bubbles_list, bubble_color, shadow_color)
        ceiling_collision = utils.verify_ceiling_collision(bubble_center, bubble_radius, bubbles_list, bubble_color, shadow_color)

        if utils.verify_game_over(bubbles_list):
            font = pygame.font.Font(None, 74)
            final_text = font.render("Game Over", True, (0, 204, 0))
            winning_text = font.render("You did it!", True, (0, 204, 0))
            screen.blit(final_text, (130, 250))
            screen.blit(winning_text, (150, 300))
            pygame.display.flip()
            pygame.time.wait(4000)
            break

        if bubble_collision or ceiling_collision:
            random_color = random.choice(list(utils.verify_colors_still_available(bubbles_list)))
            bubble_color = random_color[0]
            shadow_color = random_color[1]
            destination = None
            bubble_center = bubble_center_copy
            bubble_pos = bubble_center[:]
            velocity = [0, 0]

    utils.draw_bubble(screen, bubble_center, bubble_radius, bubble_color, shadow_color)
    pygame.draw.rect(screen, (25, 51, 0), (0, 672, 528, 30))

    utils.draw_from_map(screen, bubbles_list)

    pygame.display.flip()

utils.stop_program()
