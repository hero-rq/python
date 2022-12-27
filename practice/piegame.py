import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

player_image = pygame.image.load("player.png")
monster_image = pygame.image.load("monster.png")

player_pos = [100, 100]

monster_pos = [500, 100]

player_speed = 5

monster_speed = 2

bullet_speed = 10

running = True
shooting = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shooting = True
                
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed
        
    if shooting:
        bullet_pos = [player_pos[0] + player_image.get_width() / 2, player_pos[1]]
        while bullet_pos[0] < screen.get_width():
            bullet_pos[0] += bullet_speed
            if (bullet_pos[0] > monster_pos[0] and
                bullet_pos[0] < monster_pos[0] + monster_image.get_width() and
                bullet_pos[1] > monster_pos[1] and
                bullet_pos[1] < monster_pos[1] + monster_image.get_height()):
                running = False
                break
                
    monster_pos[0] -= monster_speed
    if monster_pos[0] < 0:
        monster_pos[0] = screen.get_width()
        
    screen.fill((0, 0, 0))
    
    screen.blit(player_image, player_pos)
    
    screen.blit(monster_image, monster_pos)
    
    if shooting:
        pygame.draw.circle(screen, (255, 255, 255), bullet_pos, 5)
