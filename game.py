import pygame

pygame.init()
win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Игра")

walkRight = [pygame.image.load('img/right_1.png'),
             pygame.image.load('img/right_2.png'),
             pygame.image.load('img/right_3.png'),
             pygame.image.load('img/right_4.png'),
             pygame.image.load('img/right_5.png'),
             pygame.image.load('img/right_6.png')]

walkLeft = [pygame.image.load('img/left_1.png'),
            pygame.image.load('img/left_2.png'),
            pygame.image.load('img/left_3.png'),
            pygame.image.load('img/left_4.png'),
            pygame.image.load('img/left_5.png'),
            pygame.image.load('img/left_6.png')]

bg = pygame.image.load('img/bg.jpg')
playerStand = pygame.image.load('img/idle.png')

clock = pygame.time.Clock()

x = 50
y = 420
width = 60
height = 71
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0

def drawWindows():
    global animCount
    win.blit(bg, (0,0))

    if animCount >= 29:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount +=1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount +=1
    else:
        win.blit(playerStand, (x, y))


    pygame.display.update()

run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x-=speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - 15:
        x+=speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if isJump:
        if jumpCount >= - 10:
            if jumpCount < 0:
                y += (jumpCount ** 2)/2
            else:
                y -= (jumpCount ** 2)/2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10       

    elif keys[pygame.K_SPACE]:
        isJump = True
    drawWindows()

pygame.quit()
