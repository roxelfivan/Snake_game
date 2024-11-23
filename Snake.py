import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors as a dictionary
colors = {
    'white': (255, 255, 255),
    'yellow': (255, 255, 102),
    'black': (0, 0, 0),
    'red': (213, 50, 80),
    'green': (0, 255, 0),
    'blue': (50, 153, 213)
}

# Define the dimensions of the display window
dis_width = 800
dis_height = 600

# Create the Pygame window with specified dimensions
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Qwen')

# Set up a clock to control the frame rate
clock = pygame.time.Clock()

# Define the size of each block in the snake and the speed of the snake
snake_block = 10
snake_speed = 15

# Define fonts for displaying text on the screen
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list, color):
    for x in snake_list:
        pygame.draw.rect(dis, color, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def random_color():
    return tuple(random.randint(0, 255) for _ in range(3))

def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the snake's head
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Initial changes in position for the snake
    x1_change = 0       
    y1_change = 0

    # List to keep track of the segments of the snake
    snake_List = []
    Length_of_snake = 1

    # Initialize a random color for the snake
    snake_color = random_color()

    # Generate random positions for the food within the display window
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # Initialize lives to 3
    lives = 3

    while not game_over:

        while game_close == True:
            dis.fill(colors['blue'])
            message("You Lost! Press Q-Quit or C-Play Again", colors['red'])
            
            # Display current number of lives at the top-right corner of the window
            value = score_font.render("Lives: " + str(lives), True, colors['white'])
            dis.blit(value, [dis_width - 130, 10])
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check for boundary collisions (game over conditions)
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
            lives -= 1  # Decrease the number of lives
            if lives == 0:  # If no more lives, end the game
                game_over = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change
        
        dis.fill(colors['blue'])
        pygame.draw.rect(dis, colors['green'], [foodx, foody, snake_block, snake_block])

        # Add the new head to the snake list
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Remove segments that are no longer part of the snake
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check for self-collision (game over condition)
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
                lives -= 1  # Decrease the number of lives
                if lives == 0:  # If no more lives, end the game
                    game_over = True

        our_snake(snake_block, snake_List, snake_color)
        
        # Display current number of lives at the top-right corner of the window
        value = score_font.render("Lives: " + str(lives), True, colors['white'])
        dis.blit(value, [dis_width - 130, 10])

        pygame.display.update()

        # Check if the snake has eaten the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            snake_color = random_color()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game loop
gameLoop()