import pygame
import random
import math
import sys

# ============================================================
#  FUJA DO RENAICON - o jogo mais tosco do mundo
#  Controles: WASD ou SETAS para mover
#  Objetivo: fugir do monstro Renaicon (o dinossauro raivoso)
#  Detalhe: quanto mais perto ele chega, mais você caga de medo
#  Aperte ESPAÇO pra começar / reiniciar
# ============================================================

LARGURA, ALTURA = 900, 600
TELA = None
RELOGIO = None

FONTE = None
FONTE_GRANDE = None
FONTE_PEQUENA = None

# ---------------------- CORES ----------------------
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (60, 160, 60)
VERDE_ESCURO = (30, 100, 30)
VERMELHO = (200, 30, 30)
AZUL = (60, 100, 220)
AMARELO = (230, 210, 40)
MARROM = (110, 70, 30)
MARROM_CLARO = (150, 100, 50)
ROSA = (230, 150, 170)
CINZA = (100, 100, 100)
FUNDO = (140, 210, 140)

# Falas curtas usadas pela IA independente dos parceiros e pelos eventos das fases.
# Cada linha e uma possibilidade diferente para o banheiro ficar menos silencioso.
FALAS_BANHEIRO = """Espiga: corre que eu vi uma sombra
Leoncio: eu nao vi nada e ja estou preocupado
Renaicon: seu cheiro chegou antes de voce
Espiga: o mapa esta de cabeca para baixo
Leoncio: talvez o banheiro seja assim mesmo
Renaicon: eu sou o fiscal da descarga
Espiga: achei uma moeda no chao
Leoncio: nao toque nessa moeda
Renaicon: moeda aceita no meu reino
Espiga: meu bumbum esta nervoso
Leoncio: o meu ja nasceu nervoso
Renaicon: nervosismo combina com perseguição
Espiga: alguem trouxe uma cueca reserva
Leoncio: trouxe duas e perdi as duas
Renaicon: eu encontrei uma no caminho
Espiga: nao pergunta de onde veio
Leoncio: definitivamente nao pergunta
Renaicon: pergunta sim, eu gosto de conversar
Espiga: o chao esta escorregadio
Leoncio: nao e agua
Renaicon: nao e meu problema
Espiga: eu vou pela esquerda
Leoncio: eu vou pela direita
Renaicon: eu vou pelo meio
Espiga: isso nao parece justo
Leoncio: nada aqui parece justo
Renaicon: justo seria voces pararem
Espiga: achei uma placa escrito cuidado
Leoncio: todas as placas dizem cuidado
Renaicon: e ninguem le nenhuma
Espiga: essa estrategia esta funcionando
Leoncio: ate agora
Renaicon: agora acabou
Espiga: alguem desligou o ventilador
Leoncio: fui eu, estava fazendo barulho
Renaicon: era o meu nariz
Espiga: que nariz barulhento
Leoncio: que monstro educado
Renaicon: obrigado pelo elogio estranho
Espiga: o item parece importante
Leoncio: ele tem uma letra desenhada
Renaicon: provavelmente significa perigo
Espiga: ou papel
Leoncio: neste lugar e a mesma coisa
Renaicon: papel e poder
Espiga: meu tenis esta fazendo barulho
Leoncio: esse e o menor dos problemas
Renaicon: eu ouvi o tenis
Espiga: nao conte para ele
Leoncio: ele ja contou para o monstro
Renaicon: eu tenho ouvidos enormes
Espiga: a arvore esta me encarando
Leoncio: e uma arvore
Renaicon: eu tambem encaro arvores
Espiga: isso nao ajuda
Leoncio: nada ajuda quando ele encara
Renaicon: eu treino no espelho
Espiga: meu plano e improvisar
Leoncio: seu plano sempre e improvisar
Renaicon: meu plano e seguir o plano
Espiga: qual plano
Leoncio: ele nao contou para a gente
Renaicon: segredo de monstro
Espiga: cuidado com a poça
Leoncio: qual poça
Renaicon: a que esta atras de voce
Espiga: por que voce avisou
Leoncio: ele gosta de brincar
Renaicon: e voces gostam de correr
Espiga: eu corro por necessidade
Leoncio: eu corro por vergonha
Renaicon: eu corro por hobby
Espiga: esse banheiro tem eco
Leoncio: eco eco eco
Renaicon: eco com dentes
Espiga: pare de repetir
Leoncio: repetir e minha especialidade
Renaicon: a minha tambem
Espiga: isso vai dar problema
Leoncio: ja deu problema
Renaicon: problema com cauda
Espiga: vi um papel voando
Leoncio: era uma gaivota de banheiro
Renaicon: era meu recibo
Espiga: desculpa, fiscal
Leoncio: nao pede desculpa para o dinossauro
Renaicon: pode pedir, eu gosto
Espiga: eu encontrei o caminho certo
Leoncio: como sabe
Renaicon: os tres caminhos tem meu nome
Espiga: isso e assustador
Leoncio: e um pouco narcisista
Renaicon: e eficiente
Espiga: meu cafe acabou
Leoncio: agora estamos realmente perdidos
Renaicon: eu tenho cafe de monstro
Espiga: nao quero saber o ingrediente
Leoncio: nem quero ver a xicara
Renaicon: voces sao exigentes
Espiga: o sol esta descendo
Leoncio: o monstro esta subindo
Renaicon: eu estou andando reto
Espiga: ninguem perguntou
Leoncio: mas todo mundo ouviu
Renaicon: minha voz e grande
Espiga: achei um banco
Leoncio: sentar seria uma pessima ideia
Renaicon: eu posso sentar em voces
Espiga: banco cancelado
Leoncio: fuga mantida
Renaicon: concordamos finalmente
Espiga: minha cara de bunda esta sorrindo
Leoncio: impossivel notar
Renaicon: eu notei
Espiga: o vento mudou
Leoncio: o cheiro tambem
Renaicon: vento e meu aliado
Espiga: vamos mudar de direcao
Leoncio: finalmente uma boa ideia
Renaicon: ideia rejeitada
Espiga: nao custa tentar
Leoncio: custa pernas
Renaicon: e custa tempo
Espiga: esse jogo tem regras
Leoncio: nenhuma regra foi explicada
Renaicon: regra um: nao seja pego
Espiga: regra dois
Leoncio: nao pergunte
Renaicon: regra tres: corra
Espiga: estamos obedecendo
Leoncio: por acidente
Renaicon: acidente aceito
Espiga: o placar esta subindo
Leoncio: a dignidade esta descendo
Renaicon: equilibrio perfeito
Espiga: mais um segundo
Leoncio: mais uma vergonha
Renaicon: mais uma passada
Espiga: quase consegui
Leoncio: quase e uma palavra perigosa
Renaicon: quase significa perto
Espiga: ele esta perto demais
Leoncio: concordo sem discutir
Renaicon: eu ouvi isso
Espiga: era para ouvir mesmo
Leoncio: coragem inesperada
Renaicon: coragem anotada
Espiga: agora corre
Leoncio: agora corre muito
Renaicon: agora eu corro tambem
Espiga: papel para ca
Leoncio: chinelo para la
Renaicon: monstro para frente
Espiga: isso e caos
Leoncio: caos organizado
Renaicon: organizado por mim
Espiga: o item sumiu
Leoncio: alguem pegou
Renaicon: fui eu
Espiga: devolve
Leoncio: ele nao vai devolver
Renaicon: posso devolver perseguindo
Espiga: isso nao conta
Leoncio: conta para ele
Renaicon: conta muito
Espiga: um dia vou abrir meu proprio banheiro
Leoncio: coloque uma placa grande
Renaicon: eu serei o segurança
Espiga: pessima ideia
Leoncio: ideia memoravel
Renaicon: negocio fechado
Espiga: o boss esta chegando
Leoncio: qual boss
Renaicon: o que fala repetido
Espiga: achei que era voce
Leoncio: temos dois problemas
Renaicon: temos uma final
Espiga: prepara o coco tatico
Leoncio: prepara a fuga tatica
Renaicon: preparem a derrota
Espiga: ga ga ga
Leoncio: nao comece a imitar
Renaicon: agora fiquei confuso
Espiga: confusao ajuda
Leoncio: as vezes atrapalha
Renaicon: nesta fase faz os dois
Espiga: ataque quando ele travar
Leoncio: F para jogar
Renaicon: eu odeio a tecla F
Espiga: por que
Leoncio: pergunta errada
Renaicon: porque faz sentido demais
Espiga: acertou o boss
Leoncio: mais um coco
Renaicon: isso e humilhante
Espiga: humilhante e perder para fezes
Leoncio: tecnicamente e estrategia
Renaicon: tecnicamente e nojento
Espiga: esta funcionando
Leoncio: nao comemora ainda
Renaicon: eu ainda tenho vida
Espiga: agora nao tem
Leoncio: ele caiu
Renaicon: eu cai com estilo
Espiga: vitoria do banheiro
Leoncio: vitoria do bumbum
Renaicon: revanche no proximo update""".splitlines()


# ---------------------- JOGADOR ----------------------
class Jogador:
    def __init__(self):
        self.x = LARGURA // 2
        self.y = ALTURA // 2
        self.raio = 22
        self.vel = 5
        self.medo = 0  # de 0 a 100, quanto mais perto o monstro, mais medo

    def mover(self, teclas):
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.x -= self.vel
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.x += self.vel
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            self.y -= self.vel
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            self.y += self.vel

        self.x = max(self.raio, min(LARGURA - self.raio, self.x))
        self.y = max(self.raio, min(ALTURA - self.raio, self.y))

    def desenhar(self, tela, tempo):
        # corpo (um boneco tosco: cabeça + tronco tremendo de medo)
        tremedeira = math.sin(tempo * 0.03 * (1 + self.medo / 20)) * (self.medo / 15)

        cx = int(self.x + tremedeira)
        cy = int(self.y)

        # corpo
        pygame.draw.circle(tela, AZUL, (cx, cy), self.raio)
        # cara (fica mais desesperada com o medo)
        olho_offset = 6
        pygame.draw.circle(tela, BRANCO, (cx - olho_offset, cy - 5), 5)
        pygame.draw.circle(tela, BRANCO, (cx + olho_offset, cy - 5), 5)
        pygame.draw.circle(tela, PRETO, (cx - olho_offset, cy - 5), 2)
        pygame.draw.circle(tela, PRETO, (cx + olho_offset, cy - 5), 2)

        # boca: quanto mais medo, mais boca de "aaaaaa"
        if self.medo > 40:
            pygame.draw.circle(tela, PRETO, (cx, cy + 8), 6)
        else:
            pygame.draw.arc(tela, PRETO, (cx - 8, cy, 16, 10), math.pi, 2 * math.pi, 2)

        # gotinhas de suor quando medo alto
        if self.medo > 30:
            pygame.draw.circle(tela, (150, 200, 255), (cx + self.raio, cy - 15), 4)


# ---------------------- MONSTRO RENAICON ----------------------
class Renaicon:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.vel = 2.2

    def mover(self, alvo_x, alvo_y):
        dx = alvo_x - self.x
        dy = alvo_y - self.y
        dist = math.hypot(dx, dy)
        if dist != 0:
            self.x += (dx / dist) * self.vel
            self.y += (dy / dist) * self.vel

    def distancia_ate(self, x, y):
        return math.hypot(self.x - x, self.y - y)

    def desenhar(self, tela, tempo):
        cx, cy = int(self.x), int(self.y)
        balanco = math.sin(tempo * 0.01) * 5

        # rabo
        pygame.draw.polygon(tela, VERDE_ESCURO, [
            (cx - 40, cy + 10 + balanco),
            (cx - 70, cy - 5 + balanco),
            (cx - 40, cy - 10 + balanco),
        ])

        # corpo (dinossauro tosco)
        pygame.draw.ellipse(tela, VERDE, (cx - 35, cy - 20, 75, 55))

        # espinhos nas costas
        for i in range(4):
            px = cx - 20 + i * 15
            pygame.draw.polygon(tela, VERDE_ESCURO, [
                (px, cy - 20),
                (px + 6, cy - 35),
                (px + 12, cy - 20),
            ])

        # pernas
        perna_anim = abs(math.sin(tempo * 0.02)) * 10
        pygame.draw.rect(tela, VERDE_ESCURO, (cx - 20, cy + 25, 12, 15 + perna_anim))
        pygame.draw.rect(tela, VERDE_ESCURO, (cx + 5, cy + 25, 12, 15 + (10 - perna_anim)))

        # cabeça de dinossauro com o rosto comprido da imagem enviada pelo usuario.
        # A arte e desenhada em pygame para o jogo continuar autocontido.
        pygame.draw.circle(tela, VERDE, (cx + 40, cy - 5), 27)
        pygame.draw.ellipse(tela, (246, 232, 181), (cx + 26, cy - 33, 48, 58))
        pygame.draw.polygon(tela, (246, 232, 181), [
            (cx + 30, cy - 10),
            (cx + 5, cy + 3),
            (cx + 26, cy + 16),
        ])
        # cabelo amarelo torto, igual ao retrato de referencia.
        pygame.draw.polygon(tela, (245, 191, 18), [
            (cx + 12, cy - 31),
            (cx + 28, cy - 45),
            (cx + 62, cy - 39),
            (cx + 73, cy - 20),
            (cx + 48, cy - 24),
            (cx + 28, cy - 16),
        ])
        pygame.draw.line(tela, (40, 35, 20), (cx + 26, cy - 21), (cx + 39, cy - 23), 2)
        pygame.draw.line(tela, (40, 35, 20), (cx + 39, cy - 1), (cx + 49, cy - 4), 2)
        pygame.draw.arc(tela, (40, 35, 20), (cx + 31, cy + 5, 28, 15), 0, math.pi, 2)
        pygame.draw.circle(tela, (20, 20, 20), (cx + 29, cy - 8), 3)
        # boca cheia de dentes tosca
        pygame.draw.polygon(tela, VERMELHO, [
            (cx + 20, cy + 5), (cx + 60, cy + 10), (cx + 55, cy + 20), (cx + 25, cy + 15)
        ])
        for i in range(4):
            dx = cx + 25 + i * 8
            pygame.draw.polygon(tela, BRANCO, [(dx, cy + 8), (dx + 4, cy + 14), (dx + 8, cy + 8)])

        # olho raivoso
        pygame.draw.circle(tela, BRANCO, (cx + 48, cy - 12), 7)
        pygame.draw.circle(tela, VERMELHO, (cx + 50, cy - 12), 3)


# ---------------------- PARCEIROS "CARA DE BUNDA" ----------------------
class Parceiro:
    def __init__(self, nome, cor, atraso, personalidade):
        self.nome = nome
        self.cor = cor
        self.personalidade = personalidade
        self.x = random.randint(100, LARGURA - 100)
        self.y = random.randint(100, ALTURA - 100)
        self.velocidade = 2.0 if nome == "Espiga" else 1.6
        self.timer = random.randint(20, 80)
        self.mensagem = ""
        self.mensagem_timer = 0

    def atualizar(self, jogador, renaicon, itens, textos):
        self.timer -= 1
        self.mensagem_timer -= 1
        if self.timer <= 0:
            self.timer = random.randint(35, 100)
            self.personalidade = random.choice(("ajuda", "atrapalha", "foge"))
            self.mensagem = random.choice(FALAS_BANHEIRO)
            if self.personalidade == "ajuda":
                self.mensagem = f"{self.nome}: ajuda tatica!"
            elif self.personalidade == "atrapalha":
                self.mensagem = f"{self.nome}: foi sem querer!"
            elif self.personalidade == "foge":
                self.mensagem = f"{self.nome}: cada um por si!"
            self.mensagem_timer = 100

        alvo_x, alvo_y = jogador.x, jogador.y
        if self.personalidade == "foge":
            alvo_x = LARGURA - jogador.x
            alvo_y = ALTURA - jogador.y
        elif self.personalidade == "atrapalha":
            alvo_x, alvo_y = renaicon.x, renaicon.y
        else:
            if itens:
                alvo_x, alvo_y = itens[0].x, itens[0].y

        dx, dy = alvo_x - self.x, alvo_y - self.y
        distancia = math.hypot(dx, dy)
        if distancia > 2:
            self.x += dx / distancia * self.velocidade
            self.y += dy / distancia * self.velocidade
        self.x = max(25, min(LARGURA - 25, self.x))
        self.y = max(70, min(ALTURA - 45, self.y))

        if self.personalidade == "ajuda" and distancia < 60 and jogador.medo > 0:
            jogador.medo = max(0, jogador.medo - 0.08)
        if self.personalidade == "atrapalha" and distancia < 42:
            jogador.medo = min(100, jogador.medo + 0.1)

    def posicao_atual(self):
        return self.x, self.y

    def desenhar(self, tela):
        x, y = self.posicao_atual()
        x, y = int(x), int(y)

        raio = 20
        # "cara de bunda": dois círculos de bochecha + risquinho no meio = bunda
        pygame.draw.circle(tela, self.cor, (x, y), raio)
        pygame.draw.line(tela, (0, 0, 0), (x, y - raio + 4), (x, y + raio - 4), 3)  # rachinha central
        pygame.draw.circle(tela, (0, 0, 0), (x - 8, y - 3), 3)  # "olho" esquerdo (cravinho kk)
        pygame.draw.circle(tela, (0, 0, 0), (x + 8, y - 3), 3)  # "olho" direito

        # nome em cima
        texto = FONTE_PEQUENA.render(self.nome, True, PRETO)
        tela.blit(texto, (x - texto.get_width() // 2, y - raio - 22))
        if self.mensagem_timer > 0:
            balao = FONTE_PEQUENA.render(self.mensagem, True, PRETO)
            tela.blit(balao, (x - balao.get_width() // 2, y + raio + 5))


class AGagueira:
    def __init__(self):
        self.x = LARGURA - 120
        self.y = ALTURA // 2
        self.vida = 12
        self.vida_maxima = 12
        self.velocidade = 1.8
        self.travada = False
        self.timer_fala = 0
        self.invulneravel = False

    def atualizar(self, jogador):
        self.timer_fala -= 1
        if self.timer_fala <= 0:
            self.timer_fala = random.randint(45, 120)
            self.travada = random.choice((True, False, False))
            self.invulneravel = not self.travada

        if not self.travada:
            dx, dy = jogador.x - self.x, jogador.y - self.y
            distancia = math.hypot(dx, dy)
            if distancia > 2:
                self.x += dx / distancia * self.velocidade
                self.y += dy / distancia * self.velocidade
        self.x = max(50, min(LARGURA - 50, self.x))
        self.y = max(90, min(ALTURA - 60, self.y))

    def distancia_ate(self, x, y):
        return math.hypot(self.x - x, self.y - y)

    def levar_coco(self):
        if self.travada and self.vida > 0:
            self.vida -= 1
            self.travada = False
            self.invulneravel = True
            self.timer_fala = 35
            return True
        return False

    def desenhar(self, tela, tempo):
        cx, cy = int(self.x), int(self.y)
        pygame.draw.ellipse(tela, (65, 35, 70), (cx - 58, cy - 34, 116, 72))
        pygame.draw.polygon(tela, (45, 25, 50), [(cx - 55, cy), (cx - 100, cy - 20), (cx - 75, cy + 22)])
        pygame.draw.circle(tela, (246, 232, 181), (cx + 35, cy - 8), 38)
        pygame.draw.polygon(tela, (246, 232, 181), [(cx + 20, cy - 8), (cx - 28, cy + 8), (cx + 18, cy + 22)])
        pygame.draw.polygon(tela, (245, 191, 18), [(cx + 3, cy - 38), (cx + 25, cy - 62), (cx + 65, cy - 48), (cx + 78, cy - 27), (cx + 35, cy - 33)])
        pygame.draw.circle(tela, PRETO, (cx + 24, cy - 15), 4)
        pygame.draw.line(tela, PRETO, (cx + 24, cy + 10), (cx + 52, cy + 7), 3)
        pygame.draw.circle(tela, VERMELHO, (cx + 55, cy - 20), 7)
        pygame.draw.circle(tela, BRANCO, (cx + 55, cy - 20), 3)
        pygame.draw.circle(tela, VERMELHO, (cx + 2, cy + 38), 10)
        pygame.draw.circle(tela, VERMELHO, (cx + 30, cy + 38), 10)
        frase = "GA-GA-GA..." if self.travada else "EU VOU TE PEGAR!"
        texto = FONTE.render(frase, True, VERMELHO if self.travada else BRANCO)
        tela.blit(texto, texto.get_rect(center=(cx, cy - 78)))


class CocoVoador:
    def __init__(self, x, y, alvo_x, alvo_y):
        self.x = x
        self.y = y
        dx, dy = alvo_x - x, alvo_y - y
        distancia = max(1, math.hypot(dx, dy))
        self.vx = dx / distancia * 8
        self.vy = dy / distancia * 8
        self.vida = 100

    def atualizar(self):
        self.x += self.vx
        self.y += self.vy
        self.vida -= 1
        return self.vida > 0 and -30 < self.x < LARGURA + 30 and -30 < self.y < ALTURA + 30

    def desenhar(self, tela):
        pygame.draw.circle(tela, MARROM, (int(self.x), int(self.y)), 10)
        pygame.draw.circle(tela, MARROM_CLARO, (int(self.x - 3), int(self.y - 3)), 3)


def desenhar_fase(tela, fase, boss=None):
    nomes = {
        1: "FASE 1 - CORRE DO DINOSSAURO",
        2: "FASE 2 - O BANHEIRO FICOU PIOR",
        3: "FASE 3 - A GAGUEIRA FINAL",
    }
    texto = FONTE.render(nomes[fase], True, VERMELHO if fase == 3 else PRETO)
    tela.blit(texto, texto.get_rect(center=(LARGURA // 2, 32)))
    if boss is not None:
        pygame.draw.rect(tela, PRETO, (LARGURA // 2 - 130, 52, 260, 15), 2)
        pygame.draw.rect(tela, VERMELHO, (LARGURA // 2 - 128, 54, int(256 * boss.vida / boss.vida_maxima), 11))
        texto_boss = FONTE_PEQUENA.render("vida da Gagueira", True, PRETO)
        tela.blit(texto_boss, (LARGURA // 2 - 60, 70))


def objetivo_da_fase(fase):
    objetivos = {
        1: "Fuja por 15 segundos e nao vire almoco.",
        2: "Fuja por mais 15 segundos e pegue itens.",
        3: "Aperte F quando A Gagueira travar na fala.",
    }
    return objetivos.get(fase, "Objetivo desconhecido, igual o mapa.")


def cor_da_fase(fase):
    cores = {
        1: VERDE_ESCURO,
        2: (90, 55, 25),
        3: VERMELHO,
    }
    return cores.get(fase, PRETO)


def dica_do_parceiro(parceiro):
    if parceiro.personalidade == "ajuda":
        return "esta tentando ajudar"
    if parceiro.personalidade == "atrapalha":
        return "esta atrapalhando"
    return "esta fugindo sozinho"


# ---------------------- SISTEMA DE COCÔ ----------------------
class Coco:
    def __init__(self, x, y):
        self.x = x + random.randint(-8, 8)
        self.y = y + random.randint(-8, 8)
        self.vida = 255  # some com o tempo

    def atualizar(self):
        self.vida -= 0.4
        return self.vida > 0

    def desenhar(self, tela):
        alpha = max(0, min(255, int(self.vida)))
        cor = MARROM
        superficie = pygame.Surface((26, 22), pygame.SRCALPHA)
        pygame.draw.circle(superficie, (*cor, alpha), (13, 16), 9)
        pygame.draw.circle(superficie, (*cor, alpha), (7, 8), 6)
        pygame.draw.circle(superficie, (*cor, alpha), (18, 8), 5)
        pygame.draw.circle(superficie, (*MARROM_CLARO, alpha), (13, 4), 4)
        tela.blit(superficie, (self.x - 13, self.y - 16))


# ---------------------- EFEITOS EXTRAS ----------------------
class Particula:
    def __init__(self, x, y, cor, vx, vy, vida=0.6, tamanho=4):
        self.x = float(x)
        self.y = float(y)
        self.cor = cor
        self.vx = vx
        self.vy = vy
        self.vida = vida
        self.vida_maxima = vida
        self.tamanho = tamanho

    def atualizar(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vy += 100 * dt
        self.vida -= dt
        return self.vida > 0

    def desenhar(self, tela):
        tamanho = max(1, int(self.tamanho * self.vida / self.vida_maxima))
        pygame.draw.circle(tela, self.cor, (int(self.x), int(self.y)), tamanho)


class TextoFlutuante:
    def __init__(self, frase, x, y, cor=PRETO):
        self.frase = frase
        self.x = x
        self.y = y
        self.cor = cor
        self.vida = 2.0

    def atualizar(self, dt):
        self.y -= 25 * dt
        self.vida -= dt
        return self.vida > 0

    def desenhar(self, tela):
        imagem = FONTE_PEQUENA.render(self.frase, True, self.cor)
        tela.blit(imagem, imagem.get_rect(center=(int(self.x), int(self.y))))


class ItemBanheiro:
    TIPOS = ("papel", "chinelo", "cafe", "spray", "desodorante")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tipo = random.choice(self.TIPOS)
        self.tempo = random.random() * 5
        self.coletado = False

    def atualizar(self, dt):
        self.tempo += dt
        return not self.coletado

    def retangulo(self):
        return pygame.Rect(int(self.x - 15), int(self.y - 15), 30, 30)

    def usar(self, jogador):
        self.coletado = True
        if self.tipo == "papel":
            jogador.medo = max(0, jogador.medo - 25)
            return "PAPEL: AGORA DA PRA RESPIRAR"
        if self.tipo == "chinelo":
            jogador.vel = min(10, jogador.vel + 2)
            return "CHINELO DE MAE: VELOCIDADE ABSURDA"
        if self.tipo == "cafe":
            jogador.vel = min(9, jogador.vel + 1)
            return "CAFE REQUENTADO: CORRE E TREME"
        if self.tipo == "spray":
            jogador.medo = max(0, jogador.medo - 10)
            return "SPRAY: NINGUEM SABE O QUE TEM NELE"
        jogador.vel = min(9, jogador.vel + 1)
        return "DESODORANTE VENCIDO: CHEIRO DE DERROTA"

    def desenhar(self, tela):
        y = int(self.y + math.sin(self.tempo * 4) * 4)
        cores = {
            "papel": (245, 245, 230),
            "chinelo": (230, 75, 95),
            "cafe": (105, 55, 25),
            "spray": (150, 210, 170),
            "desodorante": (100, 180, 240),
        }
        pygame.draw.circle(tela, cores[self.tipo], (int(self.x), y), 14)
        pygame.draw.circle(tela, PRETO, (int(self.x), y), 14, 2)
        abreviacao = {"papel": "P", "chinelo": "C", "cafe": "CA", "spray": "S", "desodorante": "D"}
        imagem = FONTE_PEQUENA.render(abreviacao[self.tipo], True, PRETO)
        tela.blit(imagem, imagem.get_rect(center=(int(self.x), y)))


class BolotaDeCoco:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = random.randint(45, 95)
        self.vida = 3
        self.tamanho = random.randint(5, 10)

    def atualizar(self, dt):
        self.y += self.velocidade * dt
        self.velocidade += 100 * dt
        self.vida -= dt
        return self.vida > 0 and self.y < ALTURA + 30

    def desenhar(self, tela):
        pygame.draw.circle(tela, MARROM, (int(self.x), int(self.y)), self.tamanho)
        pygame.draw.circle(tela, MARROM_CLARO, (int(self.x - 3), int(self.y - 3)), max(2, self.tamanho // 3))


class NuvemDePum:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vida = 1.6
        self.tamanho = random.randint(12, 22)

    def atualizar(self, dt):
        self.x -= 18 * dt
        self.y -= 8 * dt
        self.vida -= dt
        return self.vida > 0

    def desenhar(self, tela):
        superficie = pygame.Surface((110, 75), pygame.SRCALPHA)
        alpha = int(max(0, min(160, self.vida * 100)))
        cor = (125, 175, 80, alpha)
        pygame.draw.circle(superficie, cor, (28, 40), self.tamanho)
        pygame.draw.circle(superficie, cor, (54, 28), self.tamanho + 4)
        pygame.draw.circle(superficie, cor, (82, 42), self.tamanho - 2)
        tela.blit(superficie, (int(self.x - 55), int(self.y - 38)))


def criar_particulas(particulas, x, y, cor, quantidade=8):
    for _ in range(quantidade):
        particulas.append(Particula(x, y, cor, random.uniform(-100, 100), random.uniform(-130, 20)))


def frase_de_medidor(medo):
    if medo < 15:
        return "tranquilo demais"
    if medo < 35:
        return "um ventinho suspeito"
    if medo < 60:
        return "o bumbum esta nervoso"
    if medo < 80:
        return "alerta de cueca"
    return "SITUACAO DE CALAMIDADE"


def desenhar_arvore_torta(tela, x, y, escala=1):
    pygame.draw.rect(tela, (106, 76, 43), (x, y, int(18 * escala), int(75 * escala)))
    cor = (74, 139, 74)
    pygame.draw.circle(tela, cor, (x + int(8 * escala), y - int(10 * escala)), int(35 * escala))
    pygame.draw.circle(tela, cor, (x - int(18 * escala), y + int(8 * escala)), int(25 * escala))
    pygame.draw.circle(tela, cor, (x + int(35 * escala), y + int(9 * escala)), int(27 * escala))


def desenhar_banheiro_publico(tela, tempo):
    desenhar_arvore_torta(tela, 55, 380, 0.9)
    desenhar_arvore_torta(tela, 790, 365, 0.7)
    pygame.draw.rect(tela, (180, 180, 170), (330, 360, 170, 110))
    pygame.draw.polygon(tela, (130, 45, 55), [(315, 365), (415, 300), (515, 365)])
    pygame.draw.rect(tela, (230, 220, 180), (390, 405, 42, 65))
    pygame.draw.circle(tela, PRETO, (423, 438), 4)
    texto = FONTE_PEQUENA.render("BANHEIRO", True, PRETO)
    tela.blit(texto, (365, 375))
    for x in range(0, LARGURA, 80):
        altura = 3 + int(abs(math.sin(tempo * 0.02 + x)) * 4)
        pygame.draw.line(tela, (125, 175, 125), (x, ALTURA - 29), (x + 15, ALTURA - 29 - altura), 2)


# ---------------------- FUNÇÕES DE TEXTO ----------------------
def desenhar_texto_centralizado(texto, fonte, cor, y):
    render = fonte.render(texto, True, cor)
    TELA.blit(render, (LARGURA // 2 - render.get_width() // 2, y))


def ponto_aleatorio_longe_do(x, y, distancia_minima=170):
    """Escolhe um ponto para itens sem nascer em cima do monstro."""
    for _ in range(30):
        ponto = (
            random.randint(40, LARGURA - 40),
            random.randint(100, ALTURA - 70),
        )
        if math.hypot(ponto[0] - x, ponto[1] - y) >= distancia_minima:
            return ponto
    return (LARGURA - 80, ALTURA // 2)


# ---------------------- LOOP PRINCIPAL ----------------------
def main():
    global TELA, RELOGIO, FONTE, FONTE_GRANDE, FONTE_PEQUENA
    pygame.init()
    TELA = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Fuja do Renaicon!!!")
    RELOGIO = pygame.time.Clock()
    FONTE = pygame.font.SysFont("comicsansms", 28)
    FONTE_GRANDE = pygame.font.SysFont("comicsansms", 60)
    FONTE_PEQUENA = pygame.font.SysFont("comicsansms", 20)

    jogador = Jogador()
    renaicon = Renaicon()
    espiga = Parceiro("Espiga", AMARELO, atraso=15, personalidade="ajuda")
    leoncio = Parceiro("Leoncio", (200, 150, 40), atraso=35, personalidade="atrapalha")
    gagueira = None

    cocos = []
    bolotas = []
    nuvens = []
    particulas = []
    textos = []
    itens = []
    cocos_voadores = []
    tempo = 0
    cooldown_coco = 0
    cooldown_evento = 4.0
    pontuacao = 0
    fase = 1
    cooldown_ataque = 0
    estado = "MENU"  # MENU, JOGANDO, GAMEOVER, VITORIA

    while True:
        RELOGIO.tick(60)
        tempo += 1

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    if estado in ("MENU", "GAMEOVER"):
                        # reinicia tudo
                        jogador = Jogador()
                        renaicon = Renaicon()
                        espiga = Parceiro("Espiga", AMARELO, atraso=15, personalidade="ajuda")
                        leoncio = Parceiro("Leoncio", (200, 150, 40), atraso=35, personalidade="atrapalha")
                        gagueira = None
                        cocos = []
                        bolotas = []
                        nuvens = []
                        particulas = []
                        textos = []
                        itens = []
                        cocos_voadores = []
                        tempo = 0
                        pontuacao = 0
                        fase = 1
                        cooldown_ataque = 0
                        cooldown_evento = 4.0
                        estado = "JOGANDO"
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if evento.key == pygame.K_f and estado == "JOGANDO" and fase == 3 and gagueira is not None and cooldown_ataque <= 0:
                    cocos_voadores.append(CocoVoador(jogador.x, jogador.y, gagueira.x, gagueira.y))
                    cooldown_ataque = 25
                    textos.append(TextoFlutuante("COCO TATICO!", jogador.x, jogador.y - 35, MARROM))

        TELA.fill(FUNDO)

        if estado == "MENU":
            desenhar_texto_centralizado("FUJA DO RENAICON!!!", FONTE_GRANDE, VERMELHO, 130)
            desenhar_texto_centralizado("um jogo extremamente tosco", FONTE, PRETO, 210)
            desenhar_texto_centralizado("Use WASD ou SETAS pra fugir do dinossauro raivoso", FONTE_PEQUENA, PRETO, 270)
            desenhar_texto_centralizado("Cuidado: quanto mais perto, mais vc caga de medo", FONTE_PEQUENA, PRETO, 300)
            desenhar_texto_centralizado("Seus parceiros Espiga e Leoncio (cara de bunda) vão te seguir", FONTE_PEQUENA, PRETO, 330)
            desenhar_texto_centralizado("Aperte ESPAÇO pra começar", FONTE, VERDE_ESCURO, 400)

            # mostra os bichos parados no menu de decoração
            renaicon.x, renaicon.y = LARGURA - 150, ALTURA - 100
            renaicon.desenhar(TELA, tempo)

        elif estado == "JOGANDO":
            teclas = pygame.key.get_pressed()
            jogador.mover(teclas)
            if fase < 3:
                renaicon.mover(jogador.x, jogador.y)
            else:
                gagueira.atualizar(jogador)

            espiga.atualizar(jogador, renaicon, itens, textos)
            leoncio.atualizar(jogador, renaicon, itens, textos)

            dist = renaicon.distancia_ate(jogador.x, jogador.y) if fase < 3 else gagueira.distancia_ate(jogador.x, jogador.y)

            # calcula o "medo" do jogador (0 = longe e tranquilo, 100 = quase morrendo)
            dist_max = 500
            medo = max(0, min(100, (dist_max - dist) / dist_max * 100))
            jogador.medo = medo

            # quanto mais medo, mais rápido caga (cooldown menor)
            cooldown_coco -= 1
            if cooldown_coco <= 0 and medo > 15:
                cocos.append(Coco(jogador.x, jogador.y + jogador.raio))
                bolotas.append(BolotaDeCoco(jogador.x, jogador.y + jogador.raio))
                nuvens.append(NuvemDePum(jogador.x, jogador.y + jogador.raio))
                criar_particulas(particulas, jogador.x, jogador.y + jogador.raio, MARROM, 3)
                # de 40 frames (pouco medo) até 3 frames (medo máximo)
                cooldown_coco = max(3, int(40 - medo * 0.37))

            # atualiza cocôs
            cocos = [c for c in cocos if c.atualizar()]
            bolotas = [bolota for bolota in bolotas if bolota.atualizar(1 / 60)]
            nuvens = [nuvem for nuvem in nuvens if nuvem.atualizar(1 / 60)]
            particulas = [particula for particula in particulas if particula.atualizar(1 / 60)]
            textos = [flutuante for flutuante in textos if flutuante.atualizar(1 / 60)]

            cooldown_evento -= 1 / 60
            if cooldown_evento <= 0:
                x_item, y_item = ponto_aleatorio_longe_do(renaicon.x, renaicon.y)
                itens.append(ItemBanheiro(x_item, y_item))
                textos.append(TextoFlutuante("ITEM DUVIDOSO APARECEU", x_item, y_item - 30, VERDE_ESCURO))
                cooldown_evento = random.uniform(4, 8)

            for item in itens:
                item.atualizar(1 / 60)
                if item.retangulo().collidepoint(jogador.x, jogador.y) and not item.coletado:
                    textos.append(TextoFlutuante(item.usar(jogador), jogador.x, jogador.y - 30, VERDE_ESCURO))
                    criar_particulas(particulas, jogador.x, jogador.y, AMARELO, 12)
            itens = [item for item in itens if not item.coletado]

            # a velocidade do renaicon aumenta MUITO devagar com o tempo (fica mais difícil)
            renaicon.vel = 2.2 + tempo / 4000

            pontuacao += 1
            cooldown_ataque = max(0, cooldown_ataque - 1)

            if fase == 1 and pontuacao >= 900:
                fase = 2
                renaicon.x, renaicon.y = 70, ALTURA - 100
                textos.append(TextoFlutuante("FASE 2: O BANHEIRO PIOROU", LARGURA // 2, 130, VERMELHO))
            elif fase == 2 and pontuacao >= 1800:
                fase = 3
                gagueira = AGagueira()
                textos.append(TextoFlutuante("A GAGUEIRA DESCEU DO VASO", LARGURA // 2, 130, VERMELHO))

            cocos_voadores = [coco for coco in cocos_voadores if coco.atualizar()]
            if fase == 3:
                for coco in cocos_voadores[:]:
                    if gagueira.distancia_ate(coco.x, coco.y) < 45:
                        cocos_voadores.remove(coco)
                        if gagueira.levar_coco():
                            textos.append(TextoFlutuante("ACERTOU A GAGUEIRA!", gagueira.x, gagueira.y - 55, AMARELO))
                            criar_particulas(particulas, gagueira.x, gagueira.y, AMARELO, 15)
                if gagueira.vida <= 0:
                    estado = "VITORIA"

            if pontuacao % 300 == 0:
                textos.append(TextoFlutuante("VOCE SOBREVIVEU MAIS UM POUCO, MILAGRE", jogador.x, jogador.y - 40))

            # colisão = game over
            if fase < 3 and dist < jogador.raio + 25:
                estado = "GAMEOVER"

            # desenha tudo (cocôs atrás de tudo)
            for c in cocos:
                c.desenhar(TELA)
            for bolota in bolotas:
                bolota.desenhar(TELA)
            for nuvem in nuvens:
                nuvem.desenhar(TELA)
            for item in itens:
                item.desenhar(TELA)
            for particula in particulas:
                particula.desenhar(TELA)
            for flutuante in textos:
                flutuante.desenhar(TELA)
            for coco_voador in cocos_voadores:
                coco_voador.desenhar(TELA)

            espiga.desenhar(TELA)
            leoncio.desenhar(TELA)
            jogador.desenhar(TELA, tempo)
            if fase < 3:
                renaicon.desenhar(TELA, tempo)
            else:
                gagueira.desenhar(TELA, tempo)
            desenhar_fase(TELA, fase, gagueira if fase == 3 else None)

            # HUD
            texto_pontos = FONTE.render(f"Sobrevivendo há: {pontuacao // 60}s", True, PRETO)
            TELA.blit(texto_pontos, (10, 10))

            # barra de medo/cocô
            pygame.draw.rect(TELA, PRETO, (10, 50, 204, 24), 2)
            pygame.draw.rect(TELA, MARROM, (12, 52, int(2 * medo), 20))
            texto_medo = FONTE_PEQUENA.render("Nível de cocô", True, PRETO)
            TELA.blit(texto_medo, (12, 78))
            texto_estado = FONTE_PEQUENA.render(frase_de_medidor(medo), True, MARROM)
            TELA.blit(texto_estado, (12, 98))

            if medo > 70:
                aviso = FONTE.render("ELE ESTA CHEGANDO, CORRE!!!", True, VERMELHO)
                TELA.blit(aviso, (LARGURA // 2 - aviso.get_width() // 2, 10))

        elif estado == "GAMEOVER":
            for c in cocos:
                c.desenhar(TELA)
            for bolota in bolotas:
                bolota.desenhar(TELA)
            for nuvem in nuvens:
                nuvem.desenhar(TELA)
            espiga.desenhar(TELA)
            leoncio.desenhar(TELA)
            jogador.desenhar(TELA, tempo)
            if fase < 3:
                renaicon.desenhar(TELA, tempo)
            elif gagueira is not None:
                gagueira.desenhar(TELA, tempo)

            overlay = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 160))
            TELA.blit(overlay, (0, 0))

            desenhar_texto_centralizado("O RENAICON TE PEGOU!!!", FONTE_GRANDE, VERMELHO, 180)
            desenhar_texto_centralizado(f"Você sobreviveu {pontuacao // 60} segundos cagado de medo", FONTE, BRANCO, 260)
            desenhar_texto_centralizado("Espiga e Leoncio fugiram e te abandonaram, kkkk", FONTE_PEQUENA, BRANCO, 310)
            desenhar_texto_centralizado("Aperte ESPAÇO pra tentar de novo", FONTE, AMARELO, 380)

        elif estado == "VITORIA":
            desenhar_banheiro_publico(TELA, tempo)
            espiga.desenhar(TELA)
            leoncio.desenhar(TELA)
            jogador.desenhar(TELA, tempo)
            desenhar_texto_centralizado("A GAGUEIRA FOI DERROTADA!", FONTE_GRANDE, AMARELO, 170)
            desenhar_texto_centralizado("Voce venceu jogando coco tatico na hora certa.", FONTE, BRANCO, 260)
            desenhar_texto_centralizado("Espiga ajudou. Leoncio atrapalhou. Equilibrio.", FONTE_PEQUENA, BRANCO, 310)
            desenhar_texto_centralizado("Aperte ESPAÇO para jogar de novo", FONTE, AMARELO, 390)

        pygame.display.flip()

if __name__ == "__main__":
    main()