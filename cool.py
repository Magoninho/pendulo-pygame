import pygame

largura = 800
altura = 600

screen = pygame.display.set_mode((largura, altura))

x = 400
y = 300

velocidade_x = 10
velocidade_y = 10

clock = pygame.time.Clock()
while True:

    clock.tick(60)  # isso aqui serve só pra limitar o jogo com 60 fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    x += velocidade_x
    y += velocidade_y

    if x > largura - 50:
        velocidade_x *= - 1
    if x < 0:
        velocidade_x *= - 1

    if y > altura - 50:
        velocidade_y *= -1
    if y < 0:
        velocidade_y *= -1
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), (x, y, 50, 50))

    pygame.display.update()
