# Importando biblioteca pygame
import pygame

# Iniciando biblioteca pygame
pygame.init()

# Criando janela
window = pygame.display.set_mode([1280,720])
title = pygame.display.set_caption("Futrbal Pong")

win = pygame.image.load("assets/win.png")

score1 = 0
score1_img = pygame.image.load("assets/score/0.png")
score2 = 0
score2_img = pygame.image.load("assets/score/0.png")

# Carrgando imagem para as variaveeis
field = pygame.image.load("assets/field.png") #campo

bar = pygame.image.load("assets/bar.png") #campo
player1 = pygame.image.load("assets/player1.png") #Jogador1
player1_y = 310
player1_moveup = False
player1_movedown = False

player2 = pygame.image.load("assets/player2.png") #Jogador2
player2_y = 310

ball = pygame.image.load("assets/ball.png") #bola
ball_x = 617
ball_y = 337
ball_dir = -3
ball_dir_y = 1
def move_player():
    global player1_y

    if player1_moveup:
        player1_y -= 5
    else:
        player1_y += 0

    if player1_movedown:
        player1_y += 5
    else:
        player1_y += 0

    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 575:
        player1_y = 575

def move_player2():
    global player2_y
    player2_y = ball_y

def move_ball():
    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y
    global score1
    global score2
    global score1_img
    global score2_img

    ball_x += ball_dir
    ball_y += ball_dir_y

    if ball_x < 120:
        if player1_y < (ball_y + 23):
            if (player1_y + 146) > ball_y:
                ball_dir *= -1

    if ball_x > 1100:
        if player2_y < (ball_y + 23):
            if (player2_y + 146) > ball_y:
                ball_dir *= -1

    if ball_y > 685:
        ball_dir_y *= -1
    elif ball_y <= 0:
        ball_dir_y *= -1

    if ball_x < -50:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        score2 += 1
        score2_img = pygame.image.load("assets/score/" + str(score2) + ".png")

    elif ball_x > 1320:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        score1 += 1
        score1_img = pygame.image.load("assets/score/" + str(score1) + ".png")
def draw():
    if score1 or score2 < 9:
        window.blit(field,(0,0))
        window.blit(player1,(50,player1_y))
        window.blit(player2,(1150,player2_y))
        window.blit(ball,(ball_x,ball_y))
        window.blit(score1_img,(500,50))
        window.blit(score2_img,(710,50))

        move_ball()
        move_player()
        move_player2()
    else:
        window.blit(field, (0, 0))
        window.blit(win,(300,330))

# Criando loop
loop = True
while loop:

    for events in pygame.event.get(): # pega os eventos que estiver acontecendo
        if events.type == pygame.QUIT: # se tipo de envento for fechar
            loop = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                player1_moveup = True
            if events.key == pygame.K_s:
                player1_movedown = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player1_moveup = False
            if events.key == pygame.K_s:
                player1_movedown = False

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RETURN and (score1 or score2 > 8 ):
                score1_img = pygame.image.load("assets/score/0.png")
                score2_img = pygame.image.load("assets/score/0.png")
                score1 = 0
                score2 = 0

    draw()
    pygame.display.update() # dentro desse loop quero que o display fique aberto(atualizando)


