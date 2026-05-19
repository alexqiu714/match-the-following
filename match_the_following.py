import pygame
pygame.init()

WIDTH = 500
HEIGHT = 500
font = pygame.font.SysFont("arial", 30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill("white")

cctext = font.render("Candy Crush", True, "light blue")
cctextrect = pygame.Rect(280, 300, 180, 50)

#pygame.draw.rect(screen, "Blue", cctextrect, 1)

screen.blit(cctext, cctextrect)

cc = pygame.image.load("Lesson 5 - Match The Following/images/candycrush.jpg")
l = pygame.image.load("Lesson 5 - Match The Following/images/ludo.png")
ss = pygame.image.load("Lesson 5 - Match The Following/images/subwaysurfer.png")
tr = pygame.image.load("Lesson 5 - Match The Following/images/templerun.png")

ccrec = pygame.Rect(100, 50, 90, 90)
lrec = pygame.Rect(100, 160, 90, 90)
ssrec = pygame.Rect(100, 270, 90, 90)
trrec = pygame.Rect(100, 380, 90, 90)

screen.blit(cc, ccrec)
screen.blit(l, lrec)
screen.blit(ss, ssrec)
screen.blit(tr, trrec)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()