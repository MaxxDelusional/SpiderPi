import pygame

pygame.init()

clock = pygame.time.Clock()
run = True

while run:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            print "Key Down"
            if event.key == K_LEFT:
                print "You pressed Left"

    clock.tick(60)
