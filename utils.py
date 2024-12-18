import pygame
import sys
import math


# The initial vertical position of the ceiling in the game
ceiling = 22
score = 0


def stop_program():
    """
    Stops the Pygame program and exits the system.
    """
    pygame.quit()
    sys.exit()


def draw_bubble(screen, center, radius, color, shadow_color):
    """Draws a bubble with a shadow on the given screen.

    Keyword arguments:
        screen (pygame.Surface): The surface to draw the bubble on.
        center (tuple): The (x, y) coordinates of the bubble's center.
        radius (int): The radius of the bubble.
        color (tuple): The color of the bubble in RGB format.
        shadow_color (tuple): The color of the bubble's shadow in RGB format.
    """
    shadow_offset = 2
    pygame.draw.circle(screen, shadow_color, center, radius + shadow_offset)  # Umbra
    pygame.draw.circle(screen, color, center, radius)  # Bula


def draw_from_map(screen, bubbles_list):
    """Draws all bubbles from the given list on the screen.

    Keyword arguments:
    screen (pygame.Surface): The surface to draw the bubbles on.
    bubbles_list (list): A list of dictionaries, each containing bubble properties such as center, radius, color, and shadow_color.
    """
    for bubble in bubbles_list:
        draw_bubble(screen, bubble['center'], bubble['radius'], bubble['color'], bubble['shadow_color'])


def verify_bubble_collision(bubble_center, bubble_radius, bubbles_list, bubble_color, shadow_color):
    """Verifies if a bubble collides with any other bubble in the list.

    Keyword arguments:
        bubble_center (tuple): The (x, y) coordinates of the bubble's center.
        bubble_radius (int): The radius of the bubble.
        bubbles_list (list): A list of dictionaries, each containing bubble properties.
        bubble_color (tuple): The color of the bubble in RGB format.
        shadow_color (tuple): The color of the bubble's shadow in RGB format.

    Returns:
        bool: True if a collision is detected, False otherwise.
    """
    for bubble in bubbles_list:
        dx, dy = bubble_center[0] - bubble['center'][0], bubble_center[1] - bubble['center'][1]
        distance = math.hypot(dx, dy)
        if distance < bubble_radius + bubble['radius'] + 2:
            verify_best_position(bubble, bubble_center[0], bubble_center[1], bubbles_list, bubble_color, shadow_color)
            return True
    return False


def verify_best_position(bubble, x, y, bubbles_list, bubble_color, shadow_color):
    """Determines the best position for a bubble to be placed after a collision.

    Keyword arguments:
        bubble (dict): The bubble that collided.
        x (int): The x-coordinate of the collision point.
        y (int): The y-coordinate of the collision point.
        bubbles_list (list): A list of dictionaries, each containing bubble properties.
        bubble_color (tuple): The color of the bubble in RGB format.
        shadow_color (tuple): The color of the bubble's shadow in RGB format.

    Returns:
        tuple: The (x, y) coordinates of the best position for the bubble.
    """
    best_positions = [(bubble['center'][0] - 44, bubble['center'][1]),
                      (bubble['center'][0] + 44, bubble['center'][1]),
                      (bubble['center'][0] - 22, bubble['center'][1] + 38),
                      (bubble['center'][0] + 22, bubble['center'][1] + 38),
                      (bubble['center'][0] - 22, bubble['center'][1] - 38),
                      (bubble['center'][0] + 22, bubble['center'][1] - 38)]

    if bubble['center'][1] == ceiling:
        best_positions.remove((bubble['center'][0] - 22, bubble['center'][1] - 38))
        best_positions.remove((bubble['center'][0] + 22, bubble['center'][1] - 38))
    elif bubble['center'][0] == 22:
        best_positions.remove((bubble['center'][0] - 22, bubble['center'][1] - 38))
        best_positions.remove((bubble['center'][0] - 44, bubble['center'][1]))
        best_positions.remove((bubble['center'][0] - 22, bubble['center'][1] + 38))
    elif bubble['center'][0] == 506:
        best_positions.remove((bubble['center'][0] + 22, bubble['center'][1] - 38))
        best_positions.remove((bubble['center'][0] + 44, bubble['center'][1]))
        best_positions.remove((bubble['center'][0] + 22, bubble['center'][1] + 38))

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
    """Verifies if a bubble collides with the ceiling.

    Keyword arguments:
        bubble_center (tuple): The (x, y) coordinates of the bubble's center.
        bubbles_list (list): A list of dictionaries, each containing bubble properties.
        bubble_color (tuple): The color of the bubble in RGB format.
        shadow_color (tuple): The color of the bubble's shadow in RGB format.

    Returns:
        bool: True if a collision with the ceiling is detected, False otherwise.
    """
    if bubble_center[1] - ceiling <= 0:
        verify_best_position_when_ceiling_collision(bubble_center, bubbles_list, bubble_color, shadow_color)
        return True
    return False


def verify_best_position_when_ceiling_collision(bubble_center, bubbles_list, bubble_color, shadow_color):
    """Determines the best position for a bubble to be placed when it collides with the ceiling.

    Keyword arguments:
        bubble_center (tuple): The (x, y) coordinates of the bubble's center.
        bubbles_list (list): A list of dictionaries, each containing bubble properties.
        bubble_color (tuple): The color of the bubble in RGB format.
        shadow_color (tuple): The color of the bubble's shadow in RGB format.

    Returns:
        tuple: The (x, y) coordinates of the best position for the bubble.
    """
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
    """Verifies if a bubble collides with the wall and updates its velocity accordingly.

    Keyword arguments:
        bubble_center (tuple): The (x, y) coordinates of the bubble's center.
        velocity (list): The velocity vector of the bubble.
        radius (int): The radius of the bubble.
        screen_width (int): The width of the screen.

    Returns:
        list: The updated velocity vector of the bubble.
    """
    if bubble_center[0] - radius <= 0 or bubble_center[0] + radius >= screen_width:
        velocity[0] = -velocity[0]
    return velocity


def add_neighbours(bubbles_list):
    """Updates the neighbours for each bubble in the list.

    Keyword arguments:
        bubbles_list (list): A list of dictionaries, each containing bubble properties.
    """
    for bubble in bubbles_list:
        bubble['neighbours'] = []
        for other_bubble in bubbles_list:
            if bubble != other_bubble:
                dx, dy = bubble['center'][0] - other_bubble['center'][0], bubble['center'][1] - other_bubble['center'][1]
                distance = math.hypot(dx, dy)
                if distance <= (bubble['radius'] + 2) * 2:
                    bubble['neighbours'].append(other_bubble)


def verify_group_bubbles(bubble, bubbles_list):
    """Verifies and groups bubbles of the same color that are connected.

    Keyword arguments:
        bubble (dict): The bubble to start the verification from.
        bubbles_list (list): A list of dictionaries, each containing bubble properties.
    """
    visited = set()
    group = []
    global score

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
        score += len(group) * 10
        print('Score:', score)
        for b in group:
            bubbles_list.remove(b)
        add_neighbours(bubbles_list)
        remove_floating_bubbles(bubbles_list)


def remove_floating_bubbles(bubbles_list):
    """Removes bubbles that are not connected to the ceiling.

    Keyword arguments:
        bubbles_list (list): A list of dictionaries, each containing bubble properties.
    """
    ceiling_bubbles = [bubble for bubble in bubbles_list if bubble['center'][1] == ceiling]
    visited = set()
    global score

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
        score += 10
        bubbles_list.remove(bubble)


def verify_colors_still_available(bubbles_list):
    """Verifies the colors still available in the bubbles list.

    Keyword arguments:
        bubbles_list (list): A list of dictionaries, each containing bubble properties.

    Returns:
        set: A set of tuples, each containing the color and shadow color of the bubbles.
    """
    colors = set()
    for bubble in bubbles_list:
        colors.add((bubble['color'], bubble['shadow_color']))
    return colors


def verify_game_over_win(bubbles_list):
    """Verifies if the game is won by checking if there are no bubbles left.

    Keyword arguments:
        bubbles_list (list): A list of dictionaries, each containing bubble properties.

    Returns:
        bool: True if there are no bubbles left, indicating a win, False otherwise.
    """
    if len(bubbles_list) == 0:
        return True
    return False


def verify_game_over_lost(bubbles_list):
    """Verifies if the game is lost by checking if any bubble has crossed a certain vertical threshold.

    Keyword arguments:
        bubbles_list (list): A list of dictionaries, each containing bubble properties.

    Returns:
        bool: True if any bubble has crossed the vertical threshold, indicating a loss, False otherwise.
    """
    for bubble in bubbles_list:
        if bubble['center'][1] > 595:
            return True
    return False


def space_reduction(bubbles_list):
    """Adjusts the position of all bubbles in the list to simulate a reduction in space.

    Keyword arguments:
        bubbles_list (list): A list of dictionaries, each containing bubble properties.
    """
    global ceiling
    for bubble in bubbles_list:
        bubble['center'] = (bubble['center'][0], bubble['center'][1] + 38)
    add_neighbours(bubbles_list)
    ceiling += 38


def draw_rectangular(screen, rect_color, rect_list):
    """Draws a list of rectangles on the given screen.

    Keyword arguments:
        screen (pygame.Surface): The surface to draw the rectangles on.
        rect_color (tuple): The color of the rectangles in RGB format.
        rect_list (list): A list of pygame.Rect objects representing the rectangles to be drawn.
    """
    for rect in rect_list:
        pygame.draw.rect(screen, rect_color, rect)
