import pygame
pygame.init()
tela = pygame.display.set_mode((700, 400))
cor_fundo = (25, 25, 35)
rodando = True
while rodando:
    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                rodando = False
            if evento.key == pygame.K_SPACE:
                cor_fundo = (60, 30, 90)
    tela.fill(cor_fundo)
    pygame.draw.rect(tela, (60, 180, 90), (0, 330, 800, 120))
    pygame.draw.circle(tela, (255, 230, 200), (400, 245), 28)
    pygame.draw.line(tela, (20, 20, 20), (375, 245), (390, 245), 4)
    pygame.draw.line(tela, (20, 20, 20), (410, 245), (425, 245), 4)
    pygame.display.flip()
pygame.quit()