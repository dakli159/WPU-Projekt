# Pygame und so
import pygame
import random
import time
pygame.init()

#Sprung
sprungvar = 0.0








# Farben
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
höhe = 800
breiteeee= 600

V = 3

screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Alpaka One")
pygame.draw.rect(screen, [255,255,255], [0, 0, 800, 530])    # gefüllt
pygame.draw.rect(screen, [127,255,0], [0, 530, 800, 20])    # gefüllt
pygame.draw.rect(screen, [139,69,19], [0, 550, 800, 50])    # gefüllt
pygame.draw.rect(screen, [255,255,255], [0, 0, 800, 530])    # gefüllt
pygame.draw.rect(screen, [139,69,19], [150, 390, 200, 40])    # gefüllt
pygame.draw.rect(screen, [139,69,19], [200, 600, 200, 40])# gefüllt
pygame.draw.rect(screen, (255,115,0), (580, 200, 40, 300))
pygame.display.flip()
#torso
x = 2.5
y = 480 #
h = 50
b = 25
#Beine links (Rechteck)
a = 2.5
B = 505 #
c = 12.5
d = 25
#Bein rechts (Rechteck)
k = 40
l = 505 #
m = 12.5
n = 25
# hals
p = 40
q = 450 #
r = 12.5
S = 30
#Kopf
z = 50
u = 456.5 #
w = 12.5
s = 12.5
# Schließt das Fenster
spielaktiv = False

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

springend = False

# Schleife Hauptprogramm
while not spielaktiv:
    clock.tick(100)
    if y > 480 and sprungvar < 0:
        sprungvar = 0
        springend = False
    elif sprungvar > -15 and springend:
            sprungvar = sprungvar - 0.5

    
    if y > 340 and y < 380 and x > 100 and x < 300 and sprungvar < 0:
        sprungvar = 0
        springend = False

    if x > 351 and x <375:
        sprungvar = -1
        if y > 480:
                sprungvar = 0
        springend = True

    if y <= 50:
        sprungvar = -1
        if y > 480:
                sprungvar = 0
        springend = True

    if y > 240 and y >440 and x > 380 and x < 420:
        sprungvar = 0
        springend = False

    if y > 190 and y < 230 and x > 420 and x < 620 and sprungvar < 0:
        sprungvar = 0
        springend = False

    if x > 620:
        sprungvar = -1
        if y > 480:
                sprungvar = 0
        springend = True

    if x < 100:
         sprungvar = -1
         if y > 480:
                sprungvar = 0
         springend = True


    if x>= 800:
        spielaktiv = True
        for i in range(10):

            print("##############################")
 
            for i in range(3):
                print("#                            #")
 
                print("#DU HAST DAS SPIEL GEWONNEN!!#")
 
      
                print("#                            #")
     
                print("##############################")

    if x >300 and x < 501 and y >= 480:
        spielaktiv = True
        for i in range(10):

            print("##############################")
 
            for i in range(3):
                print("#                            #")
 
                print("#DU HAST DAS SPIEL VERLOREN!!#")
 
      
                print("#                            #")
     
                print("##############################")

       



    

        
    y = y - sprungvar
    B = B - sprungvar
    l = l - sprungvar
    u = u - sprungvar
    q = q - sprungvar
    pygame.draw.rect(screen, [255,255,255], [0, 0, 800, 530])    # gefüllt
    pygame.draw.rect(screen, [127,255,0], [0, 530, 800, 20])    # gefüllt
    pygame.draw.rect(screen, [139,69,19], [0, 550, 800, 50])    # gefüllt
    pygame.draw.rect(screen, [255,255,255], [0, 0, 800, 530])    # gefüllt
    pygame.draw.rect(screen, [139,69,19], [150, 390, 200, 40])    # gefüllt
    pygame.draw.rect(screen, ROT, [x, y, 50, 25]) #umrandung
    pygame.draw.rect(screen, ROT, [x, y, 50, 25]) #umrandung
    pygame.draw.rect(screen, (255,115,0), (300, 530, 200, 30)) #lava
    pygame.draw.rect(screen, (153,153,153), (0,0,900,20))#obere wand

   
    pygame.draw.rect(screen, ROT, [a, B, c, d])

    pygame.draw.rect(screen, [139,69,19], [420, 240, 200, 40])#obere Plattform


    pygame.draw.rect(screen, ROT,[k, l, m, n])


    pygame.draw.rect(screen, ROT,[p, q, r, S])


    pygame.draw.rect(screen, ROT, [z, u, w,s])
    pygame.display.flip()

    
    
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = True
            print("Spieler hat Quit-Button angeklickt")
        else:
            
            #farbe alpaka
            ROT = (255,211,155)
            
            # torso
            pygame.draw.rect(screen, [255,255,255], [0, 0, 800, 530])    # Hintergrund
            pygame.draw.rect(screen, [127,255,0], [0, 530, 800, 20])    # Grünboden
            pygame.draw.rect(screen, [139,69,19], [0, 550, 800, 50])    # Braunboden
            pygame.draw.rect(screen, [255,255,255], [0, 0, 800, 530])    # Hintergrund
            pygame.draw.rect(screen, [139,69,19], [150, 390, 200, 40])    # Plattform
            pygame.draw.rect(screen, [139,69,19], [420, 240, 200, 40])#obere Plattform
            pygame.draw.rect(screen, ROT, [x, y, 50, 25]) #umrandung


            pygame.draw.rect(screen, ROT, [a, B, c, d])


            pygame.draw.rect(screen, ROT,[k, l, m, n])



            pygame.draw.rect(screen, ROT,[p, q, r, S])


            pygame.draw.rect(screen, ROT, [z, u, w,s])




            
            #pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                print("Spieler hat Taste gedrückt")
                if event.key == pygame.K_RIGHT:
                    print("Spieler hat Pfeiltaste rechts gedrückt")
                if event.key == pygame.K_LEFT:
                    print("Spieler hat Pfeiltaste links gedrückt")
                if event.key == pygame.K_UP:
                    print("Spieler hat Pfeiltaste hoch gedrückt")
                if event.key == pygame.K_DOWN:
                    print("Spieler hat Pfeiltaste runter gedrückt")
                elif event.key == pygame.K_SPACE:
                    print("Spieler hat Leertaste gedrückt")

                # WAS/ Tasten
                if  event.key == pygame.K_w:
                    sprungvar = 14
                    springend = True
                    pygame.draw.rect(screen, [255,255,255], [0, 0, 800, 530])    # gefüllt
                    pygame.draw.rect(screen, [127,255,0], [0, 530, 800, 20])    # gefüllt
                    pygame.draw.rect(screen, [139,69,19], [0, 550, 800, 50])    # gefüllt
                    pygame.draw.rect(screen, [255,255,255], [0, 0, 800, 530])    # gefüllt
                    pygame.draw.rect(screen, [139,69,19], [150, 390, 200, 40])    # gefüllt
                    pygame.display.flip()

            
            

                elif event.key == pygame.K_d:
                    x = x + 25
                    a = a + 25
                    k = k + 25
                    p = p + 25
                    z = z + 25
                    pygame.draw.rect(screen, [255,255,255], [0, 0, 800, 530])    # gefüllt
                    pygame.draw.rect(screen, [127,255,0], [0, 530, 800, 20])    # gefüllt
                    pygame.draw.rect(screen, [139,69,19], [0, 550, 800, 50])    # gefüllt
                    pygame.draw.rect(screen, [255,255,255], [0, 0, 800, 530])    # gefüllt
                    pygame.draw.rect(screen, [139,69,19], [150, 390, 200, 40])    # gefüllt
                    pygame.display.flip()

                elif event.key == pygame.K_a:      
                    x = x - 15
                    a = a - 15
                    k = k - 15
                    p = p - 15
                    z = z - 15
                    pygame.draw.rect(screen, [255,255,255], [0, 0, 800, 530])    # gefüllt
                    pygame.draw.rect(screen, [127,255,0], [0, 530, 800, 20])    # gefüllt
                    pygame.draw.rect(screen, [139,69,19], [0, 550, 800, 50])    # gefüllt
                    pygame.draw.rect(screen, [255,255,255], [0, 0, 800, 530])    # gefüllt
                    pygame.draw.rect(screen, [139,69,19], [150, 390, 200, 40])    # gefüllt
                    pygame.display.flip()

                

                    

                    print("Spieler hat Taste w gedrückt")
                elif event.key == pygame.K_a:
                    print("Spieler hat Taste a gedrückt")
                elif event.key == pygame.K_s:
                    print("Spieler hat Taste s gedrückt")
                elif event.key == pygame.K_d:
                    print("Spieler hat Taste d gedrückt")

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("Spieler hast Maus angeklickt")


pygame.display.flip()
pygame.quit()
