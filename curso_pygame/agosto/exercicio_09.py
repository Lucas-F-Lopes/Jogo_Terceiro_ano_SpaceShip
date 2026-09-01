import pygame

pygame.init()

tela = pygame.display.set_mode((800, 450))

relogio = pygame.time.Clock()
FPS = 60

velocidade = 250

jogador = pygame.Rect(100, 180, 45, 45)
obstaculo = pygame.Rect(420, 130, 100, 170)

area_tela = tela.get_rect()

obstaculo_visivel = True

rodando = True

while rodando:

    dt = relogio.tick(FPS) / 1000

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_d]:
        jogador.x += velocidade * dt

    if teclas[pygame.K_a]:
        jogador.x -= velocidade * dt

    if teclas[pygame.K_w]:
        jogador.y -= velocidade * dt

    if teclas[pygame.K_s]:
        jogador.y += velocidade * dt

    # Impede o jogador de sair da tela
    jogador.clamp_ip(area_tela)

    # Verifica se o jogador encostou no obstáculo
    if jogador.colliderect(obstaculo):
        obstaculo_visivel = False

    # Desenha a tela
    tela.fill((30, 30, 30))

    # Desenha o jogador
    pygame.draw.rect(tela, (70, 150, 255), jogador)

    # Desenha o obstáculo somente se ele estiver visível
    if obstaculo_visivel:
        pygame.draw.rect(tela, (110, 110, 125), obstaculo)

    pygame.display.flip()

pygame.quit()