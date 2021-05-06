import pygame
import math

# colors
pygame.init()
pygame.font.init()
WHITE = (255, 255, 255)

changable_color_1 = (255, 255, 255)
changable_color_2 = (255, 255, 255)

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

angle = math.pi/4
gravity = 0.01

origin = (width // 2, height / 2)

line_length = 200

angle_velocity = 0
angle_acceleration = 0


font = pygame.font.SysFont("font.ttf", 32)


clock = pygame.time.Clock()
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == pygame.K_j:
                angle_velocity -= 0.1
                changable_color_1 = (255, 0, 0)

            if event.key == pygame.K_k:
                angle_velocity += 0.1
                changable_color_1 = (0, 255, 0)
            if event.key == pygame.K_l:
                line_length += 10
                changable_color_2 = (0, 255, 0)
            if event.key == pygame.K_h:
                line_length -= 10
                changable_color_2 = (255, 0, 0)

    force = gravity * math.sin(angle)
    angle_acceleration = (-force)
    angle_velocity += angle_acceleration
    angle += angle_velocity

    rectangle = pygame.Rect(line_length * math.sin(angle) +
                            origin[0], line_length * math.cos(angle) + origin[1], 32, 32)
    line = (rectangle.x + 16, rectangle.y + 16)

    screen.fill((0, 0, 0))

    txt_angle_acceleration = font.render(
        "acceleration = " + str(round(angle_acceleration, 4)), True, WHITE)

    txt_angle_velocity = font.render(
        "velocity = " + str(round(angle_velocity, 4)), True, changable_color_1)

    txt_line_length = font.render(
        "line length = " + str(line_length), True, changable_color_2)

    txt_info = font.render(
        "press k to increase velocity and j to decrease", True, WHITE)

    txt_info_2 = font.render(
        "press l to increase line length and h to decrease", True, WHITE)

    screen.blit(txt_angle_velocity, (0, 0))
    screen.blit(txt_angle_acceleration, (0, 25))
    screen.blit(txt_line_length, (0, 50))
    screen.blit(txt_info, (0, height - 70))
    screen.blit(txt_info_2, (0, height - 35))

    pygame.draw.line(screen, WHITE, origin, line)
    pygame.draw.ellipse(screen, WHITE, rectangle)

    pygame.display.update()
