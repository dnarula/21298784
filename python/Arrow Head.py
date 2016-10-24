import sys, pygame, time, random, pygame.mixer
from pygame.locals import *

pygame.init()


display_width = 800
display_height = 650

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Arrow Head')
clock = pygame.time.Clock()




backgImg = pygame.image.load('background.png')
def backg(x,y):
    gameDisplay.blit(backgImg,(x,y))
x = (0)
y = (0)

helperImg = pygame.image.load('helping.png')
def helper(abc,abd):
    gameDisplay.blit(helperImg,(abc,abd))
abc = (0)
abd = (0)

backsImg = pygame.image.load('background2.png')
def backs(c,d):
    gameDisplay.blit(backsImg,(c,d))
c = (0)
d = (0)

backdImg = pygame.image.load('background3.png')
def backd(i,j):
    gameDisplay.blit(backdImg,(i,j))
i = (0)
j = (0)

backerImg = pygame.image.load('back.png')
def backer(iiii,jjjj):
    gameDisplay.blit(backerImg,(iiii,jjjj))
iiii = (10)
jjjj = (10)

kidImg = pygame.image.load('kid.png')
def kid(k,l):
    gameDisplay.blit(kidImg,(k,l))
k = (330)
l = (219)

twentyfiveImg = pygame.image.load('answers/25.png')
def twentyfive(m,n):
    gameDisplay.blit(twentyfiveImg,(m,n))
m = (330)
n = (10)

sixteenImg = pygame.image.load('answers/16.png')
def sixteen(o,p):
    gameDisplay.blit(sixteenImg,(o,p))
o = (330)
p = (474)


eightImg = pygame.image.load('answers/8.png')
def eight(o,p):
    gameDisplay.blit(eightImg,(o,p))
o = (330)
p = (474)

sixImg = pygame.image.load('answers/6.png')
def six(o,p):
    gameDisplay.blit(sixImg,(o,p))
o = (330)
p = (474)


tenImg = pygame.image.load('answers/10.png')
def ten(q,r):
    gameDisplay.blit(tenImg,(q,r))
q = (10)
r = (242)

sevenImg = pygame.image.load('answers/7.png')
def seven(s,t):
    gameDisplay.blit(sevenImg,(s,t))
s = (650)
t = (242)

solveImg = pygame.image.load('answers/solve.png')
def solve(u,v):
    gameDisplay.blit(solveImg,(u,v))
u = (500)
v = (400)

q1Img = pygame.image.load('answers/q1.png')
def q1(aa,bb):
    gameDisplay.blit(q1Img,(aa,bb))
aa = (530)
bb = (500)

q2Img = pygame.image.load('answers/q2.png')
def q2(aa,bb):
    gameDisplay.blit(q2Img,(aa,bb))
aa = (530)
bb = (500)

winImg = pygame.image.load('answers/won.png')
def win(aaa,bbb):
    gameDisplay.blit(winImg,(aaa,bbb))
aaa = (227)
bbb = (279)

lostImg = pygame.image.load('answers/loss.png')
def lost(aaaa,bbbb):
    gameDisplay.blit(lostImg,(aaaa,bbbb))
aaaa = (227)
bbbb = (279)

q3Img = pygame.image.load('answers/q3.png')
def q3(aa,bb):
    gameDisplay.blit(q3Img,(aa,bb))
aa = (530)
bb = (500)

q4Img = pygame.image.load('answers/q4.png')
def q4(aa,bb):
    gameDisplay.blit(q4Img,(aa,bb))
aa = (530)
bb = (500)


button2Img = pygame.image.load('button2.png')
def button2(a,b):
    gameDisplay.blit(button2Img,(a,b))
a = (40)
b = (360)

button3Img = pygame.image.load('button3.png')
def button3(e,f):
    gameDisplay.blit(button3Img,(e,f))
e = (165)
f = (420)

button4Img = pygame.image.load('button4.png')
def button4(g,h):
    gameDisplay.blit(button4Img,(g,h))
g = (290)
h = (480)


corner4 = (330,10)
corner5 = (330,474)
corner6 = (10,242)
corner7 = (650,242)
corner8 = (10,10)


image_lengy = 140
image_heighty = 166


image_lengyy = 80
image_heightyy = 77





def game_play1():

    play = True

    while play:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner4[0]) and (mouse_xxxxx <= corner4[0]+image_lengy) and (mouse_yyyyy >= corner4[1]) and (mouse_yyyyy <= corner4[1]+image_heighty):
                        game_play2()
                        pygame.display.flip()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner5[0]) and (mouse_xxxxx <= corner5[0]+image_lengy) and (mouse_yyyyy >= corner5[1]) and (mouse_yyyyy <= corner5[1]+image_heighty):
                        game_loss()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner6[0]) and (mouse_xxxxx <= corner6[0]+image_lengy) and (mouse_yyyyy >= corner6[1]) and (mouse_yyyyy <= corner6[1]+image_heighty):
                        game_loss()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner7[0]) and (mouse_xxxxx <= corner7[0]+image_lengy) and (mouse_yyyyy >= corner7[1]) and (mouse_yyyyy <= corner7[1]+image_heighty):
                        game_loss()
                        pygame.display.flip()
        backs(c,d)
        kid(k,l)
        twentyfive(m,n)
        sixteen(o,p)
        ten(q,r)
        seven(s,t)
        solve(u,v)
        q1(aa,bb)
        pygame.display.update()
        clock.tick(15)

def game_play2():

    play2 = True

    while play2:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner4[0]) and (mouse_xxxxx <= corner4[0]+image_lengy) and (mouse_yyyyy >= corner4[1]) and (mouse_yyyyy <= corner4[1]+image_heighty):
                        game_loss()
                        pygame.display.flip()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner5[0]) and (mouse_xxxxx <= corner5[0]+image_lengy) and (mouse_yyyyy >= corner5[1]) and (mouse_yyyyy <= corner5[1]+image_heighty):
                        game_loss()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner6[0]) and (mouse_xxxxx <= corner6[0]+image_lengy) and (mouse_yyyyy >= corner6[1]) and (mouse_yyyyy <= corner6[1]+image_heighty):
                        game_play3()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner7[0]) and (mouse_xxxxx <= corner7[0]+image_lengy) and (mouse_yyyyy >= corner7[1]) and (mouse_yyyyy <= corner7[1]+image_heighty):
                        game_loss()
                        pygame.display.flip()
        backs(c,d)
        kid(k,l)
        twentyfive(o,p)
        sixteen(q,r)
        ten(m,n)
        seven(s,t)
        solve(u,v)
        q2(aa,bb)
        pygame.display.update()
        clock.tick(15)

def game_play3():

    play3 = True

    while play3:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner4[0]) and (mouse_xxxxx <= corner4[0]+image_lengy) and (mouse_yyyyy >= corner4[1]) and (mouse_yyyyy <= corner4[1]+image_heighty):
                        game_loss()
                        pygame.display.flip()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner5[0]) and (mouse_xxxxx <= corner5[0]+image_lengy) and (mouse_yyyyy >= corner5[1]) and (mouse_yyyyy <= corner5[1]+image_heighty):
                        game_loss()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner6[0]) and (mouse_xxxxx <= corner6[0]+image_lengy) and (mouse_yyyyy >= corner6[1]) and (mouse_yyyyy <= corner6[1]+image_heighty):
                        game_loss()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner7[0]) and (mouse_xxxxx <= corner7[0]+image_lengy) and (mouse_yyyyy >= corner7[1]) and (mouse_yyyyy <= corner7[1]+image_heighty):
                        game_play4()
                        pygame.display.flip()
        backs(c,d)
        kid(k,l)
        six(m,n)
        sixteen(o,p)
        seven(q,r)
        eight(s,t)
        solve(u,v)
        q3(aa,bb)
        pygame.display.update()
        clock.tick(15)

def game_play4():

    play4 = True

    while play4:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner4[0]) and (mouse_xxxxx <= corner4[0]+image_lengy) and (mouse_yyyyy >= corner4[1]) and (mouse_yyyyy <= corner4[1]+image_heighty):
                        game_loss()
                        pygame.display.flip()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner5[0]) and (mouse_xxxxx <= corner5[0]+image_lengy) and (mouse_yyyyy >= corner5[1]) and (mouse_yyyyy <= corner5[1]+image_heighty):
                        game_loss()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner6[0]) and (mouse_xxxxx <= corner6[0]+image_lengy) and (mouse_yyyyy >= corner6[1]) and (mouse_yyyyy <= corner6[1]+image_heighty):
                        game_won()
                if event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner7[0]) and (mouse_xxxxx <= corner7[0]+image_lengy) and (mouse_yyyyy >= corner7[1]) and (mouse_yyyyy <= corner7[1]+image_heighty):
                        game_loss()
                        pygame.display.flip()
        backs(c,d)
        kid(k,l)
        twentyfive(m,n)
        sixteen(o,p)
        ten(q,r)
        seven(s,t)
        solve(u,v)
        q4(aa,bb)
        pygame.display.update()
        clock.tick(15)

def game_instructions():

    instructions = True

    while instructions:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner8[0]) and (mouse_xxxxx <= corner8[0]+image_lengyy) and (mouse_yyyyy >= corner8[1]) and (mouse_yyyyy <= corner8[1]+image_heightyy):
                        game_start()
                        pygame.display.flip()
        backd(i,j)
        helper(abc,abd)
        backer(iiii,jjjj)
        pygame.display.update()
        clock.tick(15)

def game_loss():

    loss = True

    while loss:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner8[0]) and (mouse_xxxxx <= corner8[0]+image_lengyy) and (mouse_yyyyy >= corner8[1]) and (mouse_yyyyy <= corner8[1]+image_heightyy):
                        game_start()
                        pygame.display.flip()
        
        backd(i,j)
        backer(iiii,jjjj)
        lost(aaaa,bbbb)
        pygame.display.update()
        clock.tick(15)

def game_won():

    won = True

    while won:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_xxxxx, mouse_yyyyy = event.pos
                    if (mouse_xxxxx >= corner8[0]) and (mouse_xxxxx <= corner8[0]+image_lengyy) and (mouse_yyyyy >= corner8[1]) and (mouse_yyyyy <= corner8[1]+image_heightyy):
                        game_start()
                        pygame.display.flip()
        
        backd(i,j)
        backer(iiii,jjjj)
        win(aaa,bbb)
        pygame.display.update()
        clock.tick(15)
        
   




corner1 = (40,360)
corner2 = (165,420)
corner3 = (290,480)


image_length = 120
image_height = 120



def game_start():



    
    crashed = False

    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner1[0]) and (mouse_xxxxx <= corner1[0]+image_length) and (mouse_yyyyy >= corner1[1]) and (mouse_yyyyy <= corner1[1]+image_height):
                    random.randint(game_play1(),gameplay1000())
                    pygame.display.flip()
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner2[0]) and (mouse_xxxxx <= corner2[0]+image_length) and (mouse_yyyyy >= corner2[1]) and (mouse_yyyyy <= corner2[1]+image_height):
                    game_instructions()
                    pygame.display.flip()
            if event.type == MOUSEBUTTONDOWN:
                mouse_xxxxx, mouse_yyyyy = event.pos
                if (mouse_xxxxx >= corner3[0]) and (mouse_xxxxx <= corner3[0]+image_length) and (mouse_yyyyy >= corner3[1]) and (mouse_yyyyy <= corner3[1]+image_height):
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()

                
                    
              
                



        gameDisplay.fill(white)
        backg(x,y)
        button2(a,b)
        button3(e,f)
        button4(g,h)
        pygame.display.update()
        clock.tick(60)
game_start()
pygame.quit()
quit()
