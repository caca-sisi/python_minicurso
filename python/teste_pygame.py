import pygame
pygame.init()
import musica as mus

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True



while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

    if keys[pygame.K_LEFT]: # We can check if a key is pressed like this
        x -= vel
        print("left")
    if keys[pygame.K_RIGHT]:
        x += vel
        print("right")
    if keys[pygame.K_UP]:
        y -= vel
        print("up")
    if keys[pygame.K_DOWN]:
        y += vel
        print("down")
    if x==100 and y==100:
        print("sing")
        mus.Do.toca(0.2)
        mus.Re.toca(0.2)
        mus.Mi.toca(0.2)
        sleep(0.1)
        mus.Fa.toca(0.5)
        mus.Fa.toca(0.2)
        mus.Fa.toca(0.2)

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))  #This takes: window/surface, color, rect
    pygame.draw.circle(win,(0,255,0),(100,100),20,2)
    pygame.display.update() # This updates the screen so we can see our rectangle

pygame.quit()
