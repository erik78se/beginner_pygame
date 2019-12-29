import pygame

# Starta spelmotorn
pygame.init()

# Storlek på spelskärmen
SCREEN_WIDTH=800
SCREEN_HEIGHT=500

# Skapa ett fönster med storlek: SCREEN_WIDTH x SCREEN_HEIGHT
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Sätt en titel
pygame.display.set_caption("Hoppspel")

# Välj en "fördröjning" så vi kan få spelet att gå lagom fort
GAME_DELAY = 20

# Sätt storlekar på:
#   spelaren:      width, height
#   hastighet:     vel
#   startposition: pos_x,pos_y
width = 40                                             # bredden på vår spelare
height = 60                                            # Höjd på vår spelare
vel = 10                                               # Hastighet på rörelser (pixlar per steg)
pos_x = ( SCREEN_WIDTH - (width + vel)) * 0.5          # X-position på spelaren
pos_y = SCREEN_HEIGHT - ( height + vel )             # Y-position på spelaren

# Variabler vi kommer behöva för att kunnna hoppa.
isJump = False
jumpCount = 10

# Säg till att vi kan starta
run = True

while run:
    pygame.time.delay(GAME_DELAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Making sure the top left position of our character is greater than our vel so we never move off the screen.
    if keys[pygame.K_LEFT] and pos_x > vel:
        pos_x -= vel
    # Making sure the top right corner of our character is less than the screen width - its width
    if keys[pygame.K_RIGHT] and pos_x < SCREEN_WIDTH - vel - width:
        pos_x += vel

    # Om vi INTE håller hoppar just nu, så...
    # Då får man röra sig upp, ner eller hoppa.
    if not (isJump):
        if keys[pygame.K_UP] and pos_y > vel:  # Same principles apply for the y coordinate
            pos_y -= vel

        if keys[pygame.K_DOWN] and pos_y < SCREEN_HEIGHT - height - vel:
            pos_y += vel

        if keys[pygame.K_SPACE]:
            isJump = True

    else:  # Om vi kommer hit, så hoppar vi -> då händer detta...
        if jumpCount >= -10:
            pos_y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:  # This will execute if our jump is finished
            jumpCount = 10
            isJump = False
            # Resetting our Variables

    # Här ritar vi in bakgund och spelaren i fönstret.
    win.fill((0, 0, 0))  # Fyll med Röd:0,Grön:0,Blå:0
    pygame.draw.rect(win, (255, 0, 0), (pos_x, pos_y, width, height)) # Rita vår spelare på den position vi har.

    # Slutligen uppdaterar vi skärmen.
    pygame.display.update()

pygame.quit()