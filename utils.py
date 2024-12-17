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
            return True, verify_best_position(bubble, bubble_center[0], bubble_center[1], bubbles_list)
    return False, None


def verify_best_position(bubble, x, y, bubbles_list):
    best_positions = [(bubble['center'][0] - 44, bubble['center'][1]),
                      (bubble['center'][0] + 44, bubble['center'][1]),
                      (bubble['center'][0] - 22, bubble['center'][1] + 38),
                      (bubble['center'][0] + 22, bubble['center'][1] + 38),
                      (bubble['center'][0] - 22, bubble['center'][1] - 38),
                      (bubble['center'][0] + 22, bubble['center'][1] - 38)]
    closest_position = min(best_positions, key=lambda pos: math.hypot(pos[0] - x, pos[1] - y))
    for neighbor in bubble['neighbours']:
        if neighbor['center'] == closest_position:
            best_positions.remove(closest_position)
            closest_position = min(best_positions, key=lambda pos: math.hypot(pos[0] - x, pos[1] - y))
    add_neighbours(bubbles_list)
    return closest_position


def verify_ceiling_collision(bubble_center, bubble_radius, bubbles_list):
    if bubble_center[1] - bubble_radius <= 0:
        return True, verify_best_position_when_ceiling_collision(bubble_center, bubbles_list)
    return False, None


def verify_best_position_when_ceiling_collision(bubble_center, bubbles_list):
    best_positions = [(22, 22), (66, 22), (110, 22), (154, 22), (198, 22), (242, 22),
                      (286, 22), (330, 22), (374, 22), (418, 22), (462, 22), (506, 22)]
    closest_position = min(best_positions, key=lambda pos: math.hypot(pos[0] - bubble_center[0], pos[1] - bubble_center[1]))
    add_neighbours(bubbles_list)
    return closest_position


def verify_wall_collision(bubble_center, velocity, radius, screen_width):
    if bubble_center[0] - radius <= 0 or bubble_center[0] + radius >= screen_width:
        velocity[0] = -velocity[0]
    return velocity


def add_neighbours(bubbles_list):
    for bubble in bubbles_list:
        bubble['neighbours'] = []
        for other_bubble in bubbles_list:
            if bubble != other_bubble:
                dx, dy = bubble['center'][0] - other_bubble['center'][0], bubble['center'][1] - other_bubble['center'][
                    1]
                distance = math.hypot(dx, dy)
                if distance <= (bubble['radius'] + 2) * 2:
                    bubble['neighbours'].append(other_bubble)
