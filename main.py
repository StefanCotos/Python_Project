import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Pygame Window')

# Define button properties
button_color = (0, 255, 0)
button_center = [200, 550]  # Center of the circle
button_radius = 20
button_text = ''
font = pygame.font.Font(None, 36)


def draw_button(screen, center, radius, color, text):
    pygame.draw.circle(screen, color, center, radius)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=center)
    screen.blit(text_surface, text_rect)


# Main loop
running = True
button_clicked = False
destination = None
speed = 0.2

button_pos = button_center[:]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if math.hypot(event.pos[0] - button_center[0], event.pos[1] - button_center[1]) <= button_radius:
                button_clicked = True
                print('Button clicked')
            else:
                destination = event.pos
                print(f'Mouse clicked at ({destination})')

    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 0))

    # Move button towards destination
    if destination:
        dx, dy = destination[0] - button_pos[0], destination[1] - button_pos[1]
        distance = math.hypot(dx, dy)
        if distance > speed:
            dx, dy = dx / distance * speed, dy / distance * speed
            button_pos[0] += dx
            button_pos[1] += dy
            button_center = [int(button_pos[0]), int(button_pos[1])]
        else:
            button_center = destination
            destination = None

    # Draw the button
    draw_button(screen, button_center, button_radius, button_color, button_text)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
