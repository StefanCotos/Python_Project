import utils

between_rows = 38
bubble_radius_with_shadow = 22
colors = [((0, 0, 255), (0, 0, 0)),  # Blue
          ((255, 255, 0), (205, 205, 32)),  # Yellow
          ((255, 0, 0), (150, 0, 0)),  # Red
          ((0, 255, 0), (0, 150, 0)),  # Green
          ((255, 0, 255), (102, 0, 102)),  # Purple
          ((160, 160, 160), (64, 64, 64))]  # Gray


def draw_bubbles_on_board(bubbles_list, row, start, length, color, shadow_color):
    if row % 2 != 0:
        start = start * 2 - 1
        length = start + (length * 2)
        if length > 25:
            print("Error: Maximum number of bubbles exceeded")
            utils.stop_program()
        height = 22 + (between_rows * (row - 1))
        for i in range(start, length, 2):
            bubbles_list.append(
                {'center': [bubble_radius_with_shadow * i, height], 'row': row, 'radius': 20, 'color': color,
                 'shadow_color': shadow_color, 'neighbours': []})
    else:
        start = start * 2
        length = start + (length * 2)
        if length > 24:
            print("Error: Maximum number of bubbles exceeded")
            utils.stop_program()
        height = 22 + (between_rows * (row - 1))
        for i in range(start, length, 2):
            bubbles_list.append(
                {'center': [bubble_radius_with_shadow * i, height], 'row': row, 'radius': 20, 'color': color,
                 'shadow_color': shadow_color, 'neighbours': []})


def draw_board1(bubbles_list):
    draw_bubbles_on_board(bubbles_list, 1, 1, 4, colors[3][0], colors[3][1])
    draw_bubbles_on_board(bubbles_list, 1, 5, 4, colors[5][0], colors[5][1])
    # draw_bubbles_on_board(bubbles_list, 1, 9, 4, colors[2][0], colors[2][1])
    #
    # draw_bubbles_on_board(bubbles_list, 2, 1, 3, colors[3][0], colors[3][1])
    # draw_bubbles_on_board(bubbles_list, 2, 4, 4, colors[5][0], colors[5][1])
    # draw_bubbles_on_board(bubbles_list, 2, 8, 4, colors[2][0], colors[2][1])
    #
    # draw_bubbles_on_board(bubbles_list, 3, 1, 3, colors[0][0], colors[0][1])
    # draw_bubbles_on_board(bubbles_list, 3, 5, 4, colors[0][0], colors[0][1])
    # draw_bubbles_on_board(bubbles_list, 3, 10 , 3, colors[0][0], colors[0][1])
    #
    # draw_bubbles_on_board(bubbles_list, 4, 1, 1, colors[3][0], colors[3][1])
    # draw_bubbles_on_board(bubbles_list, 4, 2, 1, colors[5][0], colors[5][1])
    # draw_bubbles_on_board(bubbles_list, 4, 3, 1, colors[2][0], colors[2][1])
    # draw_bubbles_on_board(bubbles_list, 4, 5, 1, colors[3][0], colors[3][1])
    # draw_bubbles_on_board(bubbles_list, 4, 6, 1, colors[5][0], colors[5][1])
    # draw_bubbles_on_board(bubbles_list, 4, 7, 1, colors[2][0], colors[2][1])
    # draw_bubbles_on_board(bubbles_list, 4, 9, 1, colors[3][0], colors[3][1])
    # draw_bubbles_on_board(bubbles_list, 4, 10, 1, colors[5][0], colors[5][1])
    # draw_bubbles_on_board(bubbles_list, 4, 11, 1, colors[2][0], colors[2][1])

    # draw_bubbles_on_board(bubbles_list, 5, 1, 4, colors[0][0], colors[0][1])
    # draw_bubbles_on_board(bubbles_list, 5, 6, 2, colors[0][0], colors[0][1])
    # draw_bubbles_on_board(bubbles_list, 5, 9, 4, colors[0][0], colors[0][1])

    utils.add_neighbours(bubbles_list)
