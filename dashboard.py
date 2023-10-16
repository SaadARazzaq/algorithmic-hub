import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
royal_blue = (0, 0, 139)

# Fonts
font = pygame.font.Font(None, 36)

# List of AI algorithms
algorithms = [
    "A* Algorithm",
    "Best First Search",
    "Breadth First Search",
    "Depth First Search",
    "Uniform Cost Search",
    "Depth Limited Search",
    "Iterative Deepening Search",
    "Bidirectional BFS",
    "Dijkstra Algorithm"
]

selected_algorithm = None

# Dropdown menu variables
dropdown_rect = pygame.Rect(30, 30, 350, 35)  # parameters: x,y,width,height
dropdown_list_rects = []

for i in range(len(algorithms)):
    dropdown_list_rects.append(pygame.Rect(30, 66 + i * 50, 350, 50))

dropdown_open = False

# How to Play button
how_to_play_button_rect = pygame.Rect(420, 30, 350, 35)
how_to_play_button = "How to Play"
how_to_play_button_clicked = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if dropdown_rect.collidepoint(mouse_pos):
                dropdown_open = not dropdown_open
            elif dropdown_open:
                for i, rect in enumerate(dropdown_list_rects):
                    if rect.collidepoint(mouse_pos):
                        selected_algorithm = algorithms[i]
                        dropdown_open = False
            elif how_to_play_button_rect.collidepoint(mouse_pos):
                # Add your "How to Play" logic here
                how_to_play_button_clicked = True

    screen.fill(black)

    # Draw dropdown box
    pygame.draw.rect(screen, royal_blue, dropdown_rect)

    # Draw selected algorithm
    selected_text = font.render(selected_algorithm if selected_algorithm else "Select Algorithm", True, yellow)
    screen.blit(selected_text, (42, 35))

    # Draw dropdown list
    if dropdown_open:
        for i, rect in enumerate(dropdown_list_rects):
            pygame.draw.rect(screen, royal_blue, rect)
            algorithm_text = font.render(algorithms[i], True, yellow)
            screen.blit(algorithm_text, (rect.x + 12, rect.y + 10))

    # Draw "How to Play" button
    pygame.draw.rect(screen, royal_blue, how_to_play_button_rect)
    how_to_play_text = font.render(how_to_play_button, True, yellow)
    screen.blit(how_to_play_text, (430, 35))

    # Display instructions or "How to Play" content if the button is clicked
    if how_to_play_button_clicked:
        # Add your "How to Play" content rendering here
        pass

    pygame.display.flip()
