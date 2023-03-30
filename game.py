import pygame

pygame.init()

# Set up the window
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Escapist")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up fonts
font_title = pygame.font.Font("GhoulFriAOE.ttf", 60)
font_options = pygame.font.Font("GhoulFriAOE.ttf", 30)
font_credits = pygame.font.Font("GhoulFriAOE.ttf", 30)
font_start = pygame.font.Font("GhoulFriAOE.ttf", 45)
font_quit = pygame.font.Font("GhoulFriAOE.ttf", 35)

# Set up texts
text_title = font_title.render("Escapist", True, WHITE)
text_options = font_options.render("Options", True, WHITE)
text_credits = font_credits.render("Credits", True, WHITE)
text_start = font_start.render("New Game", True, WHITE)
text_quit = font_quit.render("Quit", True, WHITE)
text_credit_info = font_credits.render("This game was made by Atilla Colak", True, WHITE)

# Set up buttons
button_start = pygame.Rect(screen_width//2 - 100, 350, 100, 50)
button_options = pygame.Rect(screen_width//2 - 100, 500, 100, 50)
button_credits = pygame.Rect(screen_width//2 - 100, 550, 100, 50)
button_quit = pygame.Rect(screen_width//2 - 100, 650, 100, 50)

# Set up game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if buttons are clicked
            if button_options.collidepoint(event.pos):
                print("Options clicked")
            elif button_credits.collidepoint(event.pos):
                print("Credits clicked")
            elif button_start.collidepoint(event.pos):
                print("Game started")
            elif button_quit.collidepoint(event.pos):
                running = False


    # Draw everything
    screen.fill(BLACK)
    screen.blit(text_title, (screen_width//2 - text_title.get_width()//2, 100))
    pygame.draw.rect(screen, BLACK, button_start)
    pygame.draw.rect(screen, BLACK, button_options)
    pygame.draw.rect(screen, BLACK, button_credits)
    pygame.draw.rect(screen, BLACK, button_quit)
    screen.blit(text_options, (screen_width//2 - text_options.get_width()//2, 500))
    screen.blit(text_credits, (screen_width//2 - text_credits.get_width()//2, 550))
    screen.blit(text_start, (screen_width//2 - text_start.get_width()//2, 350))
    screen.blit(text_quit, (screen_width//2 - text_quit.get_width()//2, 650))
    screen.blit(text_credit_info, (10, screen_height - text_credit_info.get_height() - 10))

    pygame.display.flip()

# Quit pygame
pygame.quit()
