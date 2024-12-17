import pygame
import sys
import math


def stop_program():
    pygame.quit()
    sys.exit()


def draw_bubble(screen, center, radius, color, shadow_color):
    shadow_offset = 2
    pygame.draw.circle(screen, shadow_color, center, radius + shadow_offset)  # Umbra
    pygame.draw.circle(screen, color, center, radius)  # Bula


def draw_from_map(screen, bubbles_list):
    for bubble in bubbles_list:
        draw_bubble(screen, bubble['center'], bubble['radius'], bubble['color'], bubble['shadow_color'])


def verify_bubble_collision(bubble_center, bubble_radius, bubbles_list):
    for bubble in bubbles_list:
        dx, dy = bubble_center[0] - bubble['center'][0], bubble_center[1] - bubble['center'][1]
        distance = math.hypot(dx, dy)
        if distance < bubble_radius + bubble['radius'] + 2:
            collision_point = (
                (bubble_center[0] + bubble['center'][0]) / 2,
                (bubble_center[1] + bubble['center'][1]) / 2
            )
            print(collision_point)
            print(bubble['center'])
            return True
    return False


def check_wall_collision(bubble_center, velocity, radius, screen_width):
    if bubble_center[0] - radius <= 0 or bubble_center[0] + radius >= screen_width:
        velocity[0] = -velocity[0]
    return velocity


def check_ceiling_collision(bubble_center, radius):
    if bubble_center[1] - radius <= 0:
        return True
    return False
