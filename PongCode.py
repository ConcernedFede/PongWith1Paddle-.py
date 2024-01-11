import pygame

pygame.init()
pygame.display.set_caption('Pong 2.0')
icono = pygame.image.load("Pong\icono.png")
pygame.display.set_icon(icono)

negro = (0, 0, 0,)
blanco = (255, 255, 255)
ventana = (900, 600)

boing = pygame.mixer.Sound("Pong\Rebote.mp3")
paleta = pygame.mixer.Sound("Pong\Paddle.mp3")
out = pygame.mixer.Sound(("Pong\Beep.mp3"))
wall = pygame.mixer.Sound(("Pong\Wall.mp3"))
#textos
puntos = 0
fuente = pygame.font.SysFont("Courier", 26) 

mventana = pygame.display.set_mode(ventana)
reloj = pygame.time.Clock()

limite = False
velI = 4
ball_x = ventana[0] / 2
ball_y = ventana[1] / 2
ballspeed_x = velI
ballspeed_y = velI

gameover = False

while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    print(ballspeed_x, ballspeed_y)
    ballspeed_x = round(ballspeed_x, 2)
    mventana.fill(negro)
    if ballspeed_x >= 24:
        limite = True
    
    reloj.tick(60)
    posY = pygame.mouse.get_pos()
    
	#Mov Pelota
    ball_x += ballspeed_x
    ball_y += ballspeed_y
    
	#Zona visual                               coorX, coorY, ancho, largo
    player = pygame.draw.rect(mventana, blanco, (800, posY[1], 15, 90))
    pared = pygame.draw.rect(mventana, blanco, (0, 0, 50, 600))
    ball = pygame.draw.circle(mventana, blanco, (ball_x, ball_y), 10)
    #contador puntos
    texto = fuente.render("Puntos:" + (str(puntos)), 0, (blanco))
    mventana.blit(texto, ((ventana[0] / 2) - 60, 20))

    pygame.display.flip()

    # Colisiones
    if limite is False and  ball.colliderect(pared):
        ballspeed_x *= -1.2
        puntos += 1
        wall.play()
        
        
    if(limite is True and ball.colliderect(pared)):
        ballspeed_x *= -1
        puntos += 1
        wall.play()
        
    if ball.colliderect(player):
        ballspeed_x *= -1
        paleta.play()

    if ball_y > 590 or ball_y < 10:
        ballspeed_y *= -1
        boing.play()


    if ball_x > ventana[0]:
        ball_x = ventana[0] / 2
        ball_y = ventana[1] / 2
        ballspeed_x = velI
        ballspeed_y = velI
        puntos = 0
        out.play()
        

    