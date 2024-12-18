import utils
import boards
import pygame
import math
import random
import pygame.mixer

# Bubble size: 44 x 44
# Odd rows: max 12 bubbles, first bubble center 22px width 22px height
# Even rows: max 11 bubbles, first bubble center 44px width 60px height
# Rows start with 1

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((528, 740))
pygame.display.set_caption('Bubble Buster')

bubble_center = [268, 650]
next_bubble_center = [90, 705]
bubble_radius = 20
bubbles_list = []
rect_list = []
velocity = [0, 0]
speed = 1.5
counting_shooting = 0
counting_rect = 0

rect_color = (25, 51, 0)
background_color = (229, 255, 204)
text_color = (51, 102, 0)
win_text_color = (0, 204, 0)
win_bubbles_color = (0, 153, 0)
lost_text_color = (204, 0, 0)
lost_bubbles_color = (153, 0, 0)
button_color = (200, 200, 200)
button_text_color = (0, 0, 0)
main_menu_button = pygame.Rect(428, 690, 80, 30)

running = True
destination = None
bubble_pos = bubble_center[:]
bubble_center_copy = bubble_center

winning_sound = pygame.mixer.Sound('sounds/winning.wav')
losing_sound = pygame.mixer.Sound('sounds/losing.wav')
shooting_sound = pygame.mixer.Sound('sounds/shooting.mp3')


def draw_bubbles_on_board(screen, color):
    """Draws bubbles on the game board.

    Keyword arguments:
        screen (pygame.Surface): The surface to draw the bubbles on.
        color (tuple): The color of the bubbles to be drawn.
    """
    pygame.draw.circle(screen, color, [50, 150], 20)
    pygame.draw.circle(screen, color, [140, 90], 20)
    pygame.draw.circle(screen, color, [300, 100], 20)
    pygame.draw.circle(screen, color, [420, 80], 20)
    pygame.draw.circle(screen, color, [220, 150], 20)
    pygame.draw.circle(screen, color, [450, 170], 20)
    pygame.draw.circle(screen, color, [480, 300], 20)
    pygame.draw.circle(screen, color, [450, 430], 20)
    pygame.draw.circle(screen, color, [300, 500], 20)
    pygame.draw.circle(screen, color, [140, 510], 20)
    pygame.draw.circle(screen, color, [50, 450], 20)
    pygame.draw.circle(screen, color, [80, 300], 20)
    pygame.draw.circle(screen, color, [264, 600], 20)
    pygame.draw.circle(screen, color, [420, 620], 20)
    pygame.draw.circle(screen, color, [65, 640], 20)


def show_menu(screen):
    """Displays the main menu of the game.

    Keyword arguments:
        screen (pygame.Surface): The surface to draw the menu on.

    Returns:
        str: The selected difficulty level ('easy', 'medium', or 'hard').
    """
    font_title = pygame.font.Font(None, 55)
    font_menu = pygame.font.Font(None, 60)
    welcome_text = font_title.render("Welcome to Bubble Buster", True, text_color)
    start_text = font_menu.render("Choose your level", True, text_color)
    easy_text = font_menu.render("Easy", True, text_color)
    medium_text = font_menu.render("Medium", True, text_color)
    hard_text = font_menu.render("Hard", True, text_color)

    easy_button = pygame.Rect(182, 280, 164, 40)
    medium_button = pygame.Rect(182, 330, 164, 40)
    hard_button = pygame.Rect(182, 380, 164, 40)

    welcome_rect = welcome_text.get_rect(center=(264, 30))
    start_rect = start_text.get_rect(center=(264, 230))
    easy_rect = easy_text.get_rect(center=(264, 300))
    medium_rect = medium_text.get_rect(center=(264, 350))
    hard_rect = hard_text.get_rect(center=(264, 400))

    while True:
        screen.fill(background_color)

        draw_bubbles_on_board(screen, text_color)

        screen.blit(welcome_text, welcome_rect)
        screen.blit(start_text, start_rect)
        pygame.draw.rect(screen, button_color, easy_button)
        pygame.draw.rect(screen, button_color, medium_button)
        pygame.draw.rect(screen, button_color, hard_button)
        screen.blit(easy_text, easy_rect)
        screen.blit(medium_text, medium_rect)
        screen.blit(hard_text, hard_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    return "easy"
                elif medium_button.collidepoint(event.pos):
                    return "medium"
                elif hard_button.collidepoint(event.pos):
                    return "hard"


menu_selection = show_menu(screen)
if menu_selection == "easy":
    boards.draw_board_easy(bubbles_list)
elif menu_selection == "medium":
    boards.draw_board_medium(bubbles_list)
elif menu_selection == "hard":
    boards.draw_board_hard(bubbles_list)

random_color = random.choice(list(utils.verify_colors_still_available(bubbles_list)))
bubble_color = random_color[0]
shadow_color = random_color[1]

next_random_color = random.choice(list(utils.verify_colors_still_available(bubbles_list)))
next_bubble_color = next_random_color[0]
next_shadow_color = next_random_color[1]


def reset_game():
    """Resets the game state to its initial configuration.

    This function clears the bubbles and rectangles lists, resets the velocity,
    shooting and rectangle counters, and reinitialized the bubble positions and colors.
    It also displays the main menu for the user to select the difficulty level and
    redraws the game board accordingly.
    """
    global bubbles_list, rect_list, velocity, counting_shooting, counting_rect, destination, bubble_center, bubble_pos, random_color, bubble_color, shadow_color, next_random_color, next_bubble_color, next_shadow_color

    bubbles_list = []
    rect_list = []
    velocity = [0, 0]
    counting_shooting = 0
    counting_rect = 0
    destination = None
    bubble_center = bubble_center_copy
    bubble_pos = bubble_center[:]
    utils.ceiling = 22
    utils.score = 0

    menu_selection = show_menu(screen)
    if menu_selection == "easy":
        boards.draw_board_easy(bubbles_list)
    elif menu_selection == "medium":
        boards.draw_board_medium(bubbles_list)
    elif menu_selection == "hard":
        boards.draw_board_hard(bubbles_list)

    random_color = random.choice(list(utils.verify_colors_still_available(bubbles_list)))
    bubble_color = random_color[0]
    shadow_color = random_color[1]

    next_random_color = random.choice(list(utils.verify_colors_still_available(bubbles_list)))
    next_bubble_color = next_random_color[0]
    next_shadow_color = next_random_color[1]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not destination:
            if main_menu_button.collidepoint(event.pos):
                reset_game()
                continue
            if event.pos[1] < 600:
                counting_shooting += 1
                destination = event.pos
                shooting_sound.play()
                dx, dy = destination[0] - bubble_center[0], destination[1] - bubble_center[1]
                distance = math.hypot(dx, dy)
                if distance > 0:
                    velocity = [dx / distance, dy / distance]

    screen.fill(background_color)

    if destination:
        bubble_pos[0] += velocity[0] * speed
        bubble_pos[1] += velocity[1] * speed
        bubble_center = [int(bubble_pos[0]), int(bubble_pos[1])]

        velocity = utils.verify_wall_collision(bubble_center, velocity, bubble_radius, 528)

        bubble_collision = utils.verify_bubble_collision(bubble_center, bubble_radius, bubbles_list, bubble_color,
                                                         shadow_color)
        ceiling_collision = utils.verify_ceiling_collision(bubble_center, bubbles_list, bubble_color, shadow_color)

        if utils.verify_game_over_win(bubbles_list):
            winning_sound.play()
            draw_bubbles_on_board(screen, win_bubbles_color)
            font = pygame.font.Font(None, 74)
            final_text = font.render("Game Over", True, win_text_color)
            winning_text = font.render("You did it!", True, win_text_color)
            score_text = font.render("Score: " + str(utils.score), True, win_text_color)
            screen.blit(final_text, (130, 250))
            screen.blit(winning_text, (150, 300))
            screen.blit(score_text, (150, 350))
            pygame.display.flip()
            pygame.time.wait(3000)
            reset_game()
            continue

        if bubble_collision or ceiling_collision:
            bubble_color = next_random_color[0]
            shadow_color = next_random_color[1]
            next_random_color = random.choice(list(utils.verify_colors_still_available(bubbles_list)))
            next_bubble_color = next_random_color[0]
            next_shadow_color = next_random_color[1]
            destination = None
            bubble_center = bubble_center_copy
            bubble_pos = bubble_center[:]
            velocity = [0, 0]

            if counting_shooting == 5:
                counting_rect += 1
                rect_list.append((0, 0, 528, 38 * counting_rect))
                utils.space_reduction(bubbles_list)
                counting_shooting = 0

    if counting_shooting == 4:
        warning_text = font.render("Be careful!", True, button_color)
        screen.blit(warning_text, (210, 580))

    if utils.verify_game_over_lost(bubbles_list):
        losing_sound.play()
        draw_bubbles_on_board(screen, lost_bubbles_color)
        font = pygame.font.Font(None, 74)
        final_text = font.render("Game Over", True, lost_text_color)
        winning_text = font.render("You lost :(", True, lost_text_color)
        try_again_text = font.render("Try again!", True, lost_text_color)
        score_text = font.render("Score: " + str(utils.score), True, lost_text_color)
        screen.blit(final_text, (130, 250))
        screen.blit(winning_text, (150, 300))
        screen.blit(try_again_text, (150, 350))
        screen.blit(score_text, (150, 400))
        pygame.display.flip()
        pygame.time.wait(3000)
        reset_game()
        continue

    pygame.draw.rect(screen, rect_color, (28, 612, 472, 2))
    pygame.draw.rect(screen, rect_color, (0, 672, 528, 70))
    utils.draw_bubble(screen, bubble_center, bubble_radius, bubble_color, shadow_color)
    utils.draw_bubble(screen, next_bubble_center, bubble_radius, next_bubble_color, next_shadow_color)

    utils.draw_from_map(screen, bubbles_list)
    utils.draw_rectangular(screen, rect_color, rect_list)

    pygame.draw.rect(screen, button_color, main_menu_button)
    font = pygame.font.Font(None, 30)
    button_text = font.render("Menu", True, button_text_color)
    screen.blit(button_text, (main_menu_button.x + 10, main_menu_button.y + 5))
    next_text = font.render("Next:", True, button_color)
    screen.blit(next_text, (next_bubble_center[0] - 75, next_bubble_center[1] - 10))
    score_text = font.render("Score: " + str(utils.score), True, button_color)
    screen.blit(score_text, (210, 697.5))

    pygame.display.flip()

utils.stop_program()
