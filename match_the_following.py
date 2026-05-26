import pygame
pygame.init()

WIDTH = 500
HEIGHT = 500
font = pygame.font.SysFont("arial", 30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill("white")

cctext = font.render("Candy Crush", True, "light blue")
cctextrect = pygame.Rect(280, 300, 180, 50)

sstext = font.render("Subway Surfers", True, "light blue")
sstextrect = pygame.Rect(280, 75, 180, 50)

trtext = font.render("Temple Rush", True, "light blue")
trtextrect = pygame.Rect(280, 190, 180, 50)

ltext = font.render("Ludo", True, "light blue")
ltextrect = pygame.Rect(280, 400, 180, 50)

score = 0
score1 = font.render("Score: " + str (score), True, "black")

#pygame.draw.rect(screen, "Blue", cctextrect, 1)

screen.blit(cctext, cctextrect)
screen.blit(sstext, sstextrect)
screen.blit(trtext, trtextrect)
screen.blit(ltext, ltextrect)

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

matches = [(ccrec, cctextrect), (lrec, ltextrect), (ssrec, sstextrect), (trrec, trtextrect)]
start_pos = None
end_pos = None
start_rect = None
end_rect = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = pygame.mouse.get_pos()
            clicked_on_valid_area = False
            for imagerect, textrect in matches:
                if imagerect.collidepoint(start_pos):
                    clicked_on_valid_area = True
                    start_rect = imagerect
                    break
            if clicked_on_valid_area == True:
                pygame.draw.circle(screen, "yellow", start_pos, 10, 10)
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = pygame.mouse.get_pos()
            released_on_valid_area = False
            for imagerect, textrect in matches:
                if textrect.collidepoint(end_pos):
                    released_on_valid_area = True
                    end_rect = textrect
                    break
            if clicked_on_valid_area == True and released_on_valid_area == True:
                pygame.draw.circle(screen, "yellow", end_pos, 10, 10)
            if clicked_on_valid_area == True and released_on_valid_area == True:
                correct = False
                for imagerect, textrect in matches:
                    if imagerect == start_rect and textrect == end_rect:
                        correct = True
                        pygame.draw.line(screen, "green", start_pos, end_pos, 10)
                        score += 1
                if correct == False:
                    pygame.draw.line(screen, "red", start_pos, end_pos, 10)
    screen.blit(score1, (10, 10))
    pygame.display.update()