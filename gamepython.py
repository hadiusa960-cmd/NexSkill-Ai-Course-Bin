
import pygame
import random
import sys

pygame.init()

# Window
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Car Racing")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GRAY = (70, 70, 70)
GREEN = (40, 160, 60)
RED = (220, 40, 40)
BLUE = (40, 100, 230)
YELLOW = (255, 210, 40)

font = pygame.font.SysFont("Arial", 28)
big_font = pygame.font.SysFont("Arial", 60, bold=True)

# Road
ROAD_LEFT = 200
ROAD_RIGHT = 600
ROAD_WIDTH = ROAD_RIGHT - ROAD_LEFT

# Player car
player_width = 50
player_height = 90

player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - 130

player_speed = 7

# Enemy cars
enemy_width = 50
enemy_height = 90

enemies = []

# Road lines
road_lines = []

for i in range(10):
    road_lines.append(i * 80)

# Game variables
score = 0
game_speed = 4
game_over = False


def reset_game():
    global player_x
    global score
    global game_speed
    global game_over

    player_x = WIDTH // 2 - player_width // 2

    score = 0
    game_speed = 6
    game_over = False

    enemies.clear()

    for i in range(10):
        road_lines[i] = i * 80


def create_enemy():
    x = random.randint(
        ROAD_LEFT + 20,
        ROAD_RIGHT - enemy_width - 20
    )

    y = random.randint(
        -500,
        -100
    )

    color = random.choice([
        RED,
        BLUE,
        YELLOW
    ])

    enemy = {
        "x": x,
        "y": y,
        "color": color
    }

    enemies.append(enemy)


def draw_car(x, y, color):
    # Main body
    pygame.draw.rect(
        screen,
        color,
        (x, y, player_width, player_height),
        border_radius=8
    )

    # Windows
    pygame.draw.rect(
        screen,
        (100, 180, 220),
        (x + 8, y + 12, 34, 25),
        border_radius=4
    )

    pygame.draw.rect(
        screen,
        (100, 180, 220),
        (x + 8, y + 50, 34, 20),
        border_radius=4
    )

    # Wheels
    pygame.draw.rect(
        screen,
        BLACK,
        (x - 5, y + 12, 8, 22)
    )

    pygame.draw.rect(
        screen,
        BLACK,
        (x + player_width - 3, y + 12, 8, 22)
    )

    pygame.draw.rect(
        screen,
        BLACK,
        (x - 5, y + 55, 8, 22)
    )

    pygame.draw.rect(
        screen,
        BLACK,
        (x + player_width - 3, y + 55, 8, 22)
    )


def draw_road():
    # Grass
    screen.fill(GREEN)

    # Road
    pygame.draw.rect(
        screen,
        GRAY,
        (
            ROAD_LEFT,
            0,
            ROAD_WIDTH,
            HEIGHT
        )
    )

    # Road borders
    pygame.draw.rect(
        screen,
        WHITE,
        (
            ROAD_LEFT,
            0,
            8,
            HEIGHT
        )
    )

    pygame.draw.rect(
        screen,
        WHITE,
        (
            ROAD_RIGHT - 8,
            0,
            8,
            HEIGHT
        )
    )

    # Moving center lines
    for i in range(len(road_lines)):

        y = road_lines[i]

        pygame.draw.rect(
            screen,
            WHITE,
            (
                WIDTH // 2 - 5,
                y,
                10,
                50
            )
        )


def update_road():

    for i in range(len(road_lines)):

        road_lines[i] += game_speed

        if road_lines[i] > HEIGHT:
            road_lines[i] = -80


def update_enemies():
    global score
    global game_speed

    for enemy in enemies[:]:

        enemy["y"] += game_speed

        if enemy["y"] > HEIGHT:

            enemies.remove(enemy)

            score += 1

            if score % 10 == 0:
                game_speed += 0.5

    # Create more cars
    if len(enemies) < 4:

        create_enemy()


def check_collision():
    player_rect = pygame.Rect(
        player_x,
        player_y,
        player_width,
        player_height
    )

    for enemy in enemies:

        enemy_rect = pygame.Rect(
            enemy["x"],
            enemy["y"],
            enemy_width,
            enemy_height
        )

        if player_rect.colliderect(enemy_rect):

            return True

    return False


def draw_hud():
    score_text = font.render(
        "Score: " + str(score),
        True,
        WHITE
    )

    screen.blit(
        score_text,
        (20, 20)
    )

    speed_text = font.render(
        "Speed: " + str(round(game_speed, 1)),
        True,
        WHITE
    )

    screen.blit(
        speed_text,
        (20, 55)
    )


def draw_game_over():

    overlay = pygame.Surface(
        (WIDTH, HEIGHT)
    )

    overlay.set_alpha(190)
    overlay.fill(BLACK)

    screen.blit(
        overlay,
        (0, 0)
    )

    title = big_font.render(
        "GAME OVER",
        True,
        RED
    )

    screen.blit(
        title,
        (
            WIDTH // 2 - title.get_width() // 2,
            220
        )
    )

    score_text = font.render(
        "Final Score: " + str(score),
        True,
        WHITE
    )

    screen.blit(
        score_text,
        (
            WIDTH // 2 -
            score_text.get_width() // 2,
            310
        )
    )

    restart_text = font.render(
        "Press ENTER to restart",
        True,
        WHITE
    )

    screen.blit(
        restart_text,
        (
            WIDTH // 2 -
            restart_text.get_width() // 2,
            360
        )
    )


# Start game
reset_game()

running = True

while running:

    clock.tick(60)

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_RETURN:

                if game_over:
                    reset_game()

    # Game update
    if not game_over:

        keys = pygame.key.get_pressed()

        # Move left
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:

            player_x -= player_speed

        # Move right
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:

            player_x += player_speed

        # Keep car on road
        if player_x < ROAD_LEFT + 10:

            player_x = ROAD_LEFT + 10

        if player_x > ROAD_RIGHT - player_width - 10:

            player_x = ROAD_RIGHT - player_width - 10

        update_road()

        update_enemies()

        if check_collision():

            game_over = True

    # Drawing
    draw_road()

    # Enemy cars
    for enemy in enemies:

        draw_car(
            enemy["x"],
            enemy["y"],
            enemy["color"]
        )

    # Player car
    draw_car(
        player_x,
        player_y,
        BLUE
    )

    draw_hud()

    if game_over:
        draw_game_over()

    pygame.display.flip()

pygame.quit()
sys.exit()