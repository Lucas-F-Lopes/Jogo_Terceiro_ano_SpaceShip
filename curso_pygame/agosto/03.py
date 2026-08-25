import pygame

pygame.init()

tela = pygame.display.set_mode((700, 400))

cor_fundo = (25, 25, 35)
BRANCO = (255, 255, 255)

rodando = True
mostrar_circulo = False

while rodando:

    tela.fill(cor_fundo)

    for evento in pygame.event.get():
        print(evento)

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_ESCAPE:
                rodando = False

            if evento.key == pygame.K_a:
                mostrar_circulo = True

    if mostrar_circulo:

        # Círculo do meio
        pygame.draw.circle(tela, BRANCO, (350, 200), 20)

        # Círculo em cima
        pygame.draw.circle(tela, BRANCO, (350, 80), 20)

        # Círculo na lateral
        pygame.draw.circle(tela, BRANCO, (550, 200), 20)

    pygame.display.flip()

pygame.quit()