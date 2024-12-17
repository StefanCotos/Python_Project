import pygame
import sys
import math


ceiling = 22


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


def verify_bubble_collision(bubble_center, bubble_radius, bubbles_list, bubble_color, shadow_color):
    for bubble in bubbles_list:
        dx, dy = bubble_center[0] - bubble['center'][0], bubble_center[1] - bubble['center'][1]
        distance = math.hypot(dx, dy)
        if distance < bubble_radius + bubble['radius'] + 2:
            verify_best_position(bubble, bubble_center[0], bubble_center[1], bubbles_list, bubble_color, shadow_color)
            return True
    return False


def verify_best_position(bubble, x, y, bubbles_list, bubble_color, shadow_color):
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
    bubbles_list.append({
        'center': closest_position,
        'radius': 20,
        'color': bubble_color,
        'shadow_color': shadow_color,
        'neighbours': []
    })
    add_neighbours(bubbles_list)
    verify_group_bubbles(bubbles_list[-1], bubbles_list)
    return closest_position


def verify_ceiling_collision(bubble_center, bubbles_list, bubble_color, shadow_color):
    if bubble_center[1] - ceiling <= 0:
        verify_best_position_when_ceiling_collision(bubble_center, bubbles_list, bubble_color, shadow_color)
        return True
    return False


def verify_best_position_when_ceiling_collision(bubble_center, bubbles_list, bubble_color, shadow_color):
    best_positions = [(22, ceiling), (66, ceiling), (110, ceiling), (154, ceiling), (198, ceiling), (242, ceiling),
                      (286, ceiling), (330, ceiling), (374, ceiling), (418, ceiling), (462, ceiling), (506, ceiling)]
    closest_position = min(best_positions,
                           key=lambda pos: math.hypot(pos[0] - bubble_center[0], pos[1] - bubble_center[1]))
    bubbles_list.append({
        'center': closest_position,
        'radius': 20,
        'color': bubble_color,
        'shadow_color': shadow_color,
        'neighbours': []
    })
    add_neighbours(bubbles_list)
    verify_group_bubbles(bubbles_list[-1], bubbles_list)
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
                dx, dy = bubble['center'][0] - other_bubble['center'][0], bubble['center'][1] - other_bubble['center'][1]
                distance = math.hypot(dx, dy)
                if distance <= (bubble['radius'] + 2) * 2:
                    bubble['neighbours'].append(other_bubble)


def verify_group_bubbles(bubble, bubbles_list):
    visited = set()
    group = []

    def dfs(b):
        if id(b) in visited:
            return
        visited.add(id(b))
        if b['color'] == bubble['color']:
            group.append(b)
            for neighbor in b['neighbours']:
                dfs(neighbor)

    dfs(bubble)

    if len(group) > 2:
        for b in group:
            bubbles_list.remove(b)
        add_neighbours(bubbles_list)
        remove_floating_bubbles(bubbles_list)


def remove_floating_bubbles(bubbles_list):
    ceiling_bubbles = [bubble for bubble in bubbles_list if bubble['center'][1] == ceiling]
    visited = set()

    def dfs(bubble):
        if id(bubble) in visited:
            return
        visited.add(id(bubble))
        for neighbor in bubble['neighbours']:
            dfs(neighbor)

    for bubble in ceiling_bubbles:
        dfs(bubble)

    floating_bubbles = [bubble for bubble in bubbles_list if id(bubble) not in visited]
    for bubble in floating_bubbles:
        bubbles_list.remove(bubble)


def verify_colors_still_available(bubbles_list):
    colors = set()
    for bubble in bubbles_list:
        colors.add((bubble['color'], bubble['shadow_color']))
    return colors


def verify_game_over_win(bubbles_list):
    if len(bubbles_list) == 0:
        return True
    return False


def verify_game_over_lost(bubbles_list):
    for bubble in bubbles_list:
        if bubble['center'][1] > 595:
            return True
    return False


def space_reduction(bubbles_list):
    global ceiling
    for bubble in bubbles_list:
        bubble['center'] = (bubble['center'][0], bubble['center'][1] + 38)
    add_neighbours(bubbles_list)
    ceiling += 38


def draw_rectangular(screen, rect_color, rect_list):
    for rect in rect_list:
        pygame.draw.rect(screen, rect_color, rect)
