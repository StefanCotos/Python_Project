import utils

between_rows = 38
bubble_radius_with_shadow = 22
colors = [((0, 0, 255), (0, 0, 51)),  # Blue
          ((255, 255, 0), (205, 205, 32)),  # Yellow
          ((255, 0, 0), (150, 0, 0)),  # Red
          ((0, 255, 0), (0, 150, 0)),  # Green
          ((0, 255, 255), (0, 51, 102)),  # Light Blue
          ((160, 160, 160), (64, 64, 64)),  # Gray
          ((64, 64, 64), (0, 0, 0))]  # Dark Gray


def draw_bubbles_on_board(bubbles_list, row, start, length, color, shadow_color):
    """Draws bubbles on the board.

    Keyword arguments:
        bubbles_list (list): The list to append bubble dictionaries to.
        row (int): The row number to draw the bubbles on.
        start (int): The starting position for the bubbles.
        length (int): The number of bubbles to draw.
        color (tuple): The color of the bubbles.
        shadow_color (tuple): The shadow color of the bubbles.
    """
    if row % 2 != 0:
        start = start * 2 - 1
        length = start + (length * 2)
        if length > 25:
            print("Error: Maximum number of bubbles exceeded")
            utils.stop_program()
        height = utils.ceiling + (between_rows * (row - 1))
        for i in range(start, length, 2):
            bubbles_list.append(
                {'center': [bubble_radius_with_shadow * i, height],
                 'radius': 20,
                 'color': color,
                 'shadow_color': shadow_color,
                 'neighbours': []})
    else:
        start = start * 2
        length = start + (length * 2)
        if length > 24:
            print("Error: Maximum number of bubbles exceeded")
            utils.stop_program()
        height = utils.ceiling + (between_rows * (row - 1))
        for i in range(start, length, 2):
            bubbles_list.append(
                {'center': [bubble_radius_with_shadow * i, height],
                 'radius': 20,
                 'color': color,
                 'shadow_color': shadow_color,
                 'neighbours': []})


def draw_board_easy(bubbles_list):
    """Draws an easy level board configuration with bubbles.

    Keyword arguments:
        bubbles_list (list): The list to append bubble dictionaries to.
    """
    draw_bubbles_on_board(bubbles_list, 1, 2, 10, colors[3][0], colors[3][1])

    draw_bubbles_on_board(bubbles_list, 2, 1, 1, colors[3][0], colors[3][1])
    draw_bubbles_on_board(bubbles_list, 2, 3, 1, colors[3][0], colors[3][1])
    draw_bubbles_on_board(bubbles_list, 2, 4, 2, colors[1][0], colors[1][1])
    draw_bubbles_on_board(bubbles_list, 2, 6, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 2, 7, 2, colors[1][0], colors[1][1])
    draw_bubbles_on_board(bubbles_list, 2, 9, 1, colors[3][0], colors[3][1])
    draw_bubbles_on_board(bubbles_list, 2, 11, 1, colors[3][0], colors[3][1])

    draw_bubbles_on_board(bubbles_list, 3, 3, 3, colors[1][0], colors[1][1])
    draw_bubbles_on_board(bubbles_list, 3, 6, 2, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 3, 8, 3, colors[1][0], colors[1][1])

    draw_bubbles_on_board(bubbles_list, 4, 4, 2, colors[1][0], colors[1][1])
    draw_bubbles_on_board(bubbles_list, 4, 6, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 4, 7, 2, colors[1][0], colors[1][1])

    draw_bubbles_on_board(bubbles_list, 5, 2, 1, colors[3][0], colors[3][1])
    draw_bubbles_on_board(bubbles_list, 5, 5, 1, colors[3][0], colors[3][1])
    draw_bubbles_on_board(bubbles_list, 5, 6, 2, colors[1][0], colors[1][1])
    draw_bubbles_on_board(bubbles_list, 5, 8, 1, colors[3][0], colors[3][1])
    draw_bubbles_on_board(bubbles_list, 5, 11, 1, colors[3][0], colors[3][1])

    draw_bubbles_on_board(bubbles_list, 6, 2, 9, colors[3][0], colors[3][1])

    draw_bubbles_on_board(bubbles_list, 7, 1, 2, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 7, 4, 2, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 7, 7, 2, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 7, 10, 2, colors[0][0], colors[0][1])

    draw_bubbles_on_board(bubbles_list, 8, 2, 2, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 8, 5, 2, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 8, 8, 2, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 8, 11, 1, colors[5][0], colors[5][1])

    draw_bubbles_on_board(bubbles_list, 9, 1, 2, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 9, 4, 2, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 9, 7, 2, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 9, 10, 2, colors[0][0], colors[0][1])

    utils.add_neighbours(bubbles_list)


def draw_board_medium(bubbles_list):
    """Draws a medium level board configuration with bubbles.

    Keyword arguments:
    bubbles_list (list): The list to append bubble dictionaries to.
    """
    draw_bubbles_on_board(bubbles_list, 1, 1, 4, colors[3][0], colors[3][1])
    draw_bubbles_on_board(bubbles_list, 1, 5, 4, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 1, 9, 4, colors[2][0], colors[2][1])

    draw_bubbles_on_board(bubbles_list, 2, 1, 3, colors[3][0], colors[3][1])
    draw_bubbles_on_board(bubbles_list, 2, 4, 4, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 2, 8, 4, colors[2][0], colors[2][1])

    draw_bubbles_on_board(bubbles_list, 3, 1, 3, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 3, 5, 4, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 3, 10, 3, colors[0][0], colors[0][1])

    draw_bubbles_on_board(bubbles_list, 4, 1, 1, colors[3][0], colors[3][1])
    draw_bubbles_on_board(bubbles_list, 4, 2, 1, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 4, 3, 1, colors[2][0], colors[2][1])
    draw_bubbles_on_board(bubbles_list, 4, 5, 1, colors[3][0], colors[3][1])
    draw_bubbles_on_board(bubbles_list, 4, 6, 1, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 4, 7, 1, colors[2][0], colors[2][1])
    draw_bubbles_on_board(bubbles_list, 4, 9, 1, colors[3][0], colors[3][1])
    draw_bubbles_on_board(bubbles_list, 4, 10, 1, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 4, 11, 1, colors[2][0], colors[2][1])

    draw_bubbles_on_board(bubbles_list, 5, 1, 4, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 5, 6, 2, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 5, 9, 4, colors[0][0], colors[0][1])

    utils.add_neighbours(bubbles_list)


def draw_board_hard(bubbles_list):
    """Draws a hard level board configuration with bubbles.

    Keyword arguments:
    bubbles_list (list): The list to append bubble dictionaries to.
    """
    draw_bubbles_on_board(bubbles_list, 1, 1, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 1, 2, 3, colors[4][0], colors[4][1])
    draw_bubbles_on_board(bubbles_list, 1, 6, 2, colors[4][0], colors[4][1])
    draw_bubbles_on_board(bubbles_list, 1, 9, 3, colors[4][0], colors[4][1])
    draw_bubbles_on_board(bubbles_list, 1, 12, 1, colors[0][0], colors[0][1])

    draw_bubbles_on_board(bubbles_list, 2, 1, 2, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 2, 4, 2, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 2, 6, 1, colors[1][0], colors[1][1])
    draw_bubbles_on_board(bubbles_list, 2, 7, 2, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 2, 10, 2, colors[5][0], colors[5][1])

    draw_bubbles_on_board(bubbles_list, 3, 1, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 3, 2, 3, colors[4][0], colors[4][1])
    draw_bubbles_on_board(bubbles_list, 3, 6, 2, colors[4][0], colors[4][1])
    draw_bubbles_on_board(bubbles_list, 3, 9, 3, colors[4][0], colors[4][1])
    draw_bubbles_on_board(bubbles_list, 3, 12, 1, colors[0][0], colors[0][1])

    draw_bubbles_on_board(bubbles_list, 4, 1, 1, colors[6][0], colors[6][1])
    draw_bubbles_on_board(bubbles_list, 4, 2, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 4, 3, 1, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 4, 4, 1, colors[6][0], colors[6][1])
    draw_bubbles_on_board(bubbles_list, 4, 5, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 4, 6, 1, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 4, 7, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 4, 8, 1, colors[6][0], colors[6][1])
    draw_bubbles_on_board(bubbles_list, 4, 9, 1, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 4, 10, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 4, 11, 1, colors[6][0], colors[6][1])

    draw_bubbles_on_board(bubbles_list, 5, 1, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 5, 2, 1, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 5, 3, 1, colors[6][0], colors[6][1])
    draw_bubbles_on_board(bubbles_list, 5, 5, 1, colors[4][0], colors[4][1])
    draw_bubbles_on_board(bubbles_list, 5, 8, 1, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 5, 10, 1, colors[6][0], colors[6][1])
    draw_bubbles_on_board(bubbles_list, 5, 11, 1, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 5, 12, 1, colors[0][0], colors[0][1])

    draw_bubbles_on_board(bubbles_list, 6, 1, 1, colors[4][0], colors[4][1])
    draw_bubbles_on_board(bubbles_list, 6, 3, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 6, 5, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 6, 7, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 6, 9, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 6, 11, 1, colors[4][0], colors[4][1])

    draw_bubbles_on_board(bubbles_list, 7, 2, 1, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 7, 5, 1, colors[6][0], colors[6][1])
    draw_bubbles_on_board(bubbles_list, 7, 8, 1, colors[6][0], colors[6][1])
    draw_bubbles_on_board(bubbles_list, 7, 11, 1, colors[5][0], colors[5][1])

    draw_bubbles_on_board(bubbles_list, 8, 2, 1, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 8, 3, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 8, 4, 1, colors[4][0], colors[4][1])
    draw_bubbles_on_board(bubbles_list, 8, 8, 1, colors[4][0], colors[4][1])
    draw_bubbles_on_board(bubbles_list, 8, 9, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 8, 10, 1, colors[5][0], colors[5][1])

    draw_bubbles_on_board(bubbles_list, 9, 2, 1, colors[4][0], colors[4][1])
    draw_bubbles_on_board(bubbles_list, 9, 4, 1, colors[6][0], colors[6][1])
    draw_bubbles_on_board(bubbles_list, 9, 9, 1, colors[6][0], colors[6][1])
    draw_bubbles_on_board(bubbles_list, 9, 11, 1, colors[4][0], colors[4][1])

    draw_bubbles_on_board(bubbles_list, 10, 2, 1, colors[4][0], colors[4][1])
    draw_bubbles_on_board(bubbles_list, 10, 3, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 10, 9, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 10, 10, 1, colors[4][0], colors[4][1])

    draw_bubbles_on_board(bubbles_list, 11, 2, 1, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 11, 4, 1, colors[6][0], colors[6][1])
    draw_bubbles_on_board(bubbles_list, 11, 9, 1, colors[6][0], colors[6][1])
    draw_bubbles_on_board(bubbles_list, 11, 11, 1, colors[5][0], colors[5][1])

    draw_bubbles_on_board(bubbles_list, 12, 2, 1, colors[5][0], colors[5][1])
    draw_bubbles_on_board(bubbles_list, 12, 3, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 12, 9, 1, colors[0][0], colors[0][1])
    draw_bubbles_on_board(bubbles_list, 12, 10, 1, colors[5][0], colors[5][1])

    draw_bubbles_on_board(bubbles_list, 13, 3, 1, colors[1][0], colors[1][1])
    draw_bubbles_on_board(bubbles_list, 13, 10, 1, colors[1][0], colors[1][1])

    utils.add_neighbours(bubbles_list)
