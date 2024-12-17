import pygame
import sys
import math

pygame.init()

screen = pygame.display.set_mode((422, 600))
pygame.display.set_caption('Pygame Window')

bubble_color = (0, 255, 0)
bubble_center = [210, 550]
bubble_radius = 20
bubbles_list = []
velocity = [0, 0]
speed = 1


def draw_bubble(screen, center, radius, color, shadow_color):
    shadow_offset = 2
    pygame.draw.circle(screen, shadow_color, center, radius + shadow_offset)  # Umbra
    pygame.draw.circle(screen, color, center, radius)  # Bula


def draw_from_map(screen, bubbles_list):
    for bubble in bubbles_list:
        draw_bubble(screen, bubble['center'], bubble['radius'], bubble['color'], bubble['shadow_color'])


def draw_table(screen_width):
    bubble_diameter = 2 * bubble_radius
    hex_row_height = int(math.sqrt(3) / 2 * bubble_diameter)  # Distanta verticala intre randuri
    max_bubbles_per_row = screen_width // bubble_diameter

    # Generăm 10 rânduri pentru demonstrație
    for row in range(10):
        # Calculăm decalajul pentru rândurile impare
        x_offset = 0 if row % 2 == 0 else bubble_radius

        for col in range(max_bubbles_per_row):
            x = col * bubble_diameter + x_offset + bubble_radius
            y = row * hex_row_height + bubble_radius

            # Adaugăm fiecare bulă la lista de bule
            bubbles_list.append({
                'center': [x, y],
                'radius': bubble_radius,
                'color': (255, 0, 0),  # Poți schimba culoarea pentru diversitate
                'shadow_color': (150, 0, 0)
            })


# def make_bubbles():
#     bubbles_list.append({'center': [43, 22], 'radius': 20, 'color': (0, 0, 255), 'shadow_color': (0, 0, 0)})
#     bubbles_list.append({'center': [85, 22], 'radius': 20, 'color': (0, 0, 255), 'shadow_color': (0, 0, 0)})
#     bubbles_list.append({'center': [127, 22], 'radius': 20, 'color': (0, 0, 255), 'shadow_color': (0, 0, 0)})
#     bubbles_list.append({'center': [169, 22], 'radius': 20, 'color': (0, 0, 255), 'shadow_color': (0, 0, 0)})
#     bubbles_list.append({'center': [253, 22], 'radius': 20, 'color': (0, 0, 255), 'shadow_color': (0, 0, 0)})
#     bubbles_list.append({'center': [295, 22], 'radius': 20, 'color': (0, 0, 255), 'shadow_color': (0, 0, 0)})
#     bubbles_list.append({'center': [337, 22], 'radius': 20, 'color': (0, 0, 255), 'shadow_color': (0, 0, 0)})
#     bubbles_list.append({'center': [379, 22], 'radius': 20, 'color': (0, 0, 255), 'shadow_color': (0, 0, 0)})
#
#     bubbles_list.append({'center': [22, 60], 'radius': 20, 'color': (255, 255, 0), 'shadow_color': (205, 205, 32)})
#     bubbles_list.append({'center': [64, 60], 'radius': 20, 'color': (255, 255, 0), 'shadow_color': (205, 205, 32)})
#     bubbles_list.append({'center': [106, 60], 'radius': 20, 'color': (255, 255, 0), 'shadow_color': (205, 205, 32)})
#     bubbles_list.append({'center': [148, 60], 'radius': 20, 'color': (255, 255, 0), 'shadow_color': (205, 205, 32)})
#     bubbles_list.append({'center': [190, 60], 'radius': 20, 'color': (255, 255, 0), 'shadow_color': (205, 205, 32)})
#     bubbles_list.append({'center': [232, 60], 'radius': 20, 'color': (255, 255, 0), 'shadow_color': (205, 205, 32)})
#     bubbles_list.append({'center': [274, 60], 'radius': 20, 'color': (255, 255, 0), 'shadow_color': (205, 205, 32)})
#     bubbles_list.append({'center': [316, 60], 'radius': 20, 'color': (255, 255, 0), 'shadow_color': (205, 205, 32)})
#     bubbles_list.append({'center': [358, 60], 'radius': 20, 'color': (255, 255, 0), 'shadow_color': (205, 205, 32)})
#     bubbles_list.append({'center': [400, 60], 'radius': 20, 'color': (255, 255, 0), 'shadow_color': (205, 205, 32)})
#
#     bubbles_list.append({'center': [85, 97], 'radius': 20, 'color': (255, 0, 0), 'shadow_color': (150, 0, 0)})
#     bubbles_list.append({'center': [127, 97], 'radius': 20, 'color': (255, 0, 0), 'shadow_color': (150, 0, 0)})
#     bubbles_list.append({'center': [295, 97], 'radius': 20, 'color': (255, 0, 0), 'shadow_color': (150, 0, 0)})
#     bubbles_list.append({'center': [337, 97], 'radius': 20, 'color': (255, 0, 0), 'shadow_color': (150, 0, 0)})
#
#     bubbles_list.append({'center': [64, 134], 'radius': 20, 'color': (0, 255, 0), 'shadow_color': (0, 150, 0)})
#     bubbles_list.append({'center': [106, 134], 'radius': 20, 'color': (0, 255, 0), 'shadow_color': (0, 150, 0)})
#     bubbles_list.append({'center': [148, 134], 'radius': 20, 'color': (0, 255, 0), 'shadow_color': (0, 150, 0)})
#     bubbles_list.append({'center': [274, 134], 'radius': 20, 'color': (0, 255, 0), 'shadow_color': (0, 150, 0)})
#     bubbles_list.append({'center': [316, 134], 'radius': 20, 'color': (0, 255, 0), 'shadow_color': (0, 150, 0)})
#     bubbles_list.append({'center': [358, 134], 'radius': 20, 'color': (0, 255, 0), 'shadow_color': (0, 150, 0)})


def find_hexagonal_position(bubble_center, bubble_radius, bubbles_list):
    bubble_diameter = 2 * bubble_radius
    hex_row_height = int(math.sqrt(3) / 2 * bubble_diameter)

    # Setul de direcții hexagonale relative
    directions = [
        [bubble_diameter, 0],  # Dreapta
        [-bubble_diameter, 0],  # Stânga
        [bubble_radius, hex_row_height],  # Dreapta jos
        [-bubble_radius, hex_row_height],  # Stânga jos
        [bubble_radius, -hex_row_height],  # Dreapta sus
        [-bubble_radius, -hex_row_height],  # Stânga sus
    ]

    # Începem de la bula actuală
    queue = [bubble_center]
    visited = set()

    while queue:
        current_pos = queue.pop(0)
        visited.add(tuple(current_pos))

        for direction in directions:
            # Calculăm poziția potențială
            new_pos = [current_pos[0] + direction[0], current_pos[1] + direction[1]]

            # Verificăm dacă poziția este liberă
            if not any(
                    math.hypot(new_pos[0] - b['center'][0], new_pos[1] - b['center'][1]) < bubble_diameter
                    for b in bubbles_list
            ):
                return new_pos

            # Adăugăm poziția în coadă pentru explorare dacă nu a fost vizitată
            if tuple(new_pos) not in visited:
                queue.append(new_pos)

    # Dacă nu găsim (nu ar trebui să ajungem aici), returnăm centrul inițial ca fallback
    return bubble_center


def verify_bubble_collision(bubble_center, bubble_radius, bubbles_list):
    for bubble in bubbles_list:
        dx, dy = bubble_center[0] - bubble['center'][0], bubble_center[1] - bubble['center'][1]
        distance = math.hypot(dx, dy)
        if distance < bubble_radius + bubble['radius'] + 2:
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


running = True
destination = None
bubble_pos = bubble_center[:]
bubble_center_copy = bubble_center

draw_table(422)

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

        velocity = check_wall_collision(bubble_center, velocity, bubble_radius, 422)

        if verify_bubble_collision(bubble_center, bubble_radius, bubbles_list):
            # Găsim o poziție disponibilă în rețeaua hexagonală
            new_position = find_hexagonal_position(bubble_center, bubble_radius, bubbles_list)

            # Adăugăm bula la lista bulelor
            bubbles_list.append({
                'center': new_position,
                'radius': bubble_radius,
                'color': bubble_color,
                'shadow_color': (40, 175, 40)
            })

            # Resetăm bula activă
            bubble_center = bubble_center_copy
            bubble_pos = bubble_center[:]
            destination = None
            velocity = [0, 0]

    draw_bubble(screen, bubble_center, bubble_radius, bubble_color, (40, 175, 40))
    pygame.draw.rect(screen, (25, 51, 0), (0, 572, 422, 30))

    draw_from_map(screen, bubbles_list)

    pygame.display.flip()

pygame.quit()
sys.exit()
