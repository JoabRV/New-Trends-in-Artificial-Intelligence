import pygame


pygame.init()


screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")


ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player1 = pygame.Rect(10, screen_height/2 - 50, 10, 100)
player2 = pygame.Rect(screen_width - 20, screen_height/2 - 50, 10, 100)


ball_speed_x = 7
ball_speed_y = 7
player_speed = 0


bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)


def draw_objects():
    pygame.draw.rect(screen, light_grey, player1)
    pygame.draw.rect(screen, light_grey, player2)
    pygame.draw.ellipse(screen, light_grey, ball)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = -7
            elif event.key == pygame.K_DOWN:
                player_speed = 7
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_speed = 0


    player1.y += player_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height


    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1


    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1


    screen.fill(bg_color)
    draw_objects()


    pygame.display.update()