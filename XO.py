import pygame
from time import sleep
pygame.init()
window=pygame.display.set_mode((600,600))
done=False
def draw_table():
    pygame.draw.line(window,(255,255,255),(120,240),(480,240),6)
    pygame.draw.circle(window,(255,255,255),(120,241),3)
    pygame.draw.circle(window,(255,255,255),(480,241),3)
    pygame.draw.line(window,(255,255,255),(120,360),(480,360),6)
    pygame.draw.circle(window,(255,255,255),(120,361),3)
    pygame.draw.circle(window,(255,255,255),(480,361),3)
    pygame.draw.line(window,(255,255,255),(240,120),(240,480),6)
    pygame.draw.circle(window,(255,255,255),(241,120),3)
    pygame.draw.circle(window,(255,255,255),(241,480),3)
    pygame.draw.line(window,(255,255,255),(360,120),(360,480),6)
    pygame.draw.circle(window,(255,255,255),(361,120),3)
    pygame.draw.circle(window,(255,255,255),(361,480),3)
def array_count(s):
    l=0
    for i in s:
        l+=1
    return l
def draw_O(placex,placey):
    pygame.draw.circle(window,(255,255,0),(placex,placey),55,6)
def draw_X(placex,placey):
    pygame.draw.line(window,(255,65,0),(placex-50,placey+50),(placex+50,placey-50),8)
    pygame.draw.line(window,(255,65,0),(placex+50,placey+50),(placex-50,placey-50),8)
def win_check_X():
    pl=True
    k=True
    if x_fills.count((180,180)) and x_fills.count((300,180)) and x_fills.count((420,180)):
        xpos=100
        pygame.draw.circle(window,(200,200,200),(100,181),3)
        while k:
            pygame.draw.line(window,(200,200,200),(xpos,180),(xpos+10,180),6)
            pygame.display.update()
            if xpos>=500:
                k=False
            xpos+=2
        pygame.draw.circle(window,(200,200,200),(510,181),3)
        pygame.display.update()
        return True
    elif x_fills.count((180,300)) and x_fills.count((300,300)) and x_fills.count((420,300)):
        xpos=100
        pygame.draw.circle(window,(200,200,200),(100,301),3)
        while k:
            pygame.draw.line(window,(200,200,200),(xpos,300),(xpos+10,300),6)
            pygame.display.update()
            if xpos>=500:
                k=False
            xpos+=2
        pygame.draw.circle(window,(200,200,200),(510,301),3)
        pygame.display.update()
        return True
    elif x_fills.count((180,420)) and x_fills.count((300,420)) and x_fills.count((420,420)):
        xpos=100
        pygame.draw.circle(window,(200,200,200),(100,421),3)
        while k:
            pygame.draw.line(window,(200,200,200),(xpos,420),(xpos+10,420),6)
            pygame.display.update()
            if xpos>=500:
                k=False
            xpos+=2
        pygame.draw.circle(window,(200,200,200),(510,421),3)
        pygame.display.update()
        return True
    elif x_fills.count((180,180)) and x_fills.count((180,300)) and x_fills.count((180,420)):
        ypos=100
        pygame.draw.circle(window,(200,200,200),(181,100),3)
        while k:
            pygame.draw.line(window,(200,200,200),(180,ypos),(180,ypos+10),6)
            pygame.display.update()
            if ypos>=500:
                k=False
            ypos+=2
        pygame.draw.circle(window,(200,200,200),(181,510),3)
        pygame.display.update()
        return True
    elif x_fills.count((300,180)) and x_fills.count((300,300)) and x_fills.count((300,420)):
        ypos=100
        pygame.draw.circle(window,(200,200,200),(301,100),3)
        while k:
            pygame.draw.line(window,(200,200,200),(300,ypos),(300,ypos+10),6)
            pygame.display.update()
            if ypos>=500:
                k=False
            ypos+=2
        pygame.draw.circle(window,(200,200,200),(301,510),3)
        pygame.display.update()
        return True
    elif x_fills.count((420,180)) and x_fills.count((420,300)) and x_fills.count((420,420)):
        ypos=100
        pygame.draw.circle(window,(200,200,200),(421,100),3)
        while k:
            pygame.draw.line(window,(200,200,200),(420,ypos),(420,ypos+10),6)
            pygame.display.update()
            if ypos>=500:
                k=False
            ypos+=2
        pygame.draw.circle(window,(200,200,200),(421,510),3)
        pygame.display.update()
        return True
    elif x_fills.count((180,180)) and x_fills.count((300,300)) and x_fills.count((420,420)):
        xpos=120
        ypos=120
        while k:
            pygame.draw.line(window,(200,200,200),(xpos,ypos),(xpos+5,ypos+5),10)
            pygame.display.update()
            if ypos>=500:
                k=False
            xpos+=2
            ypos+=2
        return True
    elif x_fills.count((420,180)) and x_fills.count((300,300)) and x_fills.count((180,420)):
        xpos=480
        ypos=120
        while k:
            pygame.draw.line(window,(200,200,200),(xpos,ypos),(xpos-5,ypos+5),10)
            pygame.display.update()
            if ypos>=500:
                k=False
            xpos-=2
            ypos+=2
        return True
    else:
        pl=True
    if pl:
        return False
    else:
        hm='lold'
def win_check_O():
    pl=False
    k=True
    if o_fills.count((180,180)) and o_fills.count((300,180)) and o_fills.count((420,180)):
        xpos=100
        pygame.draw.circle(window,(200,200,200),(100,181),3)
        while k:
            pygame.draw.line(window,(200,200,200),(xpos,180),(xpos+10,180),6)
            pygame.display.update()
            if xpos>=500:
                k=False
            xpos+=2
        pygame.draw.circle(window,(200,200,200),(510,181),3)
        pygame.display.update()
        return True
    elif o_fills.count((180,300)) and o_fills.count((300,300)) and o_fills.count((420,300)):
        xpos=100
        pygame.draw.circle(window,(200,200,200),(100,301),3)
        while k:
            pygame.draw.line(window,(200,200,200),(xpos,300),(xpos+10,300),6)
            pygame.display.update()
            if xpos>=500:
                k=False
            xpos+=2
        pygame.draw.circle(window,(200,200,200),(510,301),3)
        pygame.display.update()
        return True
    elif o_fills.count((180,420)) and o_fills.count((300,420)) and o_fills.count((420,420)):
        xpos=100
        pygame.draw.circle(window,(200,200,200),(100,421),3)
        while k:
            pygame.draw.line(window,(200,200,200),(xpos,420),(xpos+10,420),6)
            pygame.display.update()
            if xpos>=500:
                k=False
            xpos+=2
        pygame.draw.circle(window,(200,200,200),(510,421),3)
        pygame.display.update()
        return True
    elif o_fills.count((180,180)) and o_fills.count((180,300)) and o_fills.count((180,420)):
        ypos=100
        pygame.draw.circle(window,(200,200,200),(181,100),3)
        while k:
            pygame.draw.line(window,(200,200,200),(180,ypos),(180,ypos+10),6)
            pygame.display.update()
            if ypos>=500:
                k=False
            ypos+=2
        pygame.draw.circle(window,(200,200,200),(181,510),3)
        pygame.display.update()
        return True
    elif o_fills.count((300,180)) and o_fills.count((300,300)) and o_fills.count((300,420)):
        ypos=100
        pygame.draw.circle(window,(200,200,200),(301,100),3)
        while k:
            pygame.draw.line(window,(200,200,200),(300,ypos),(300,ypos+10),6)
            pygame.display.update()
            if ypos>=500:
                k=False
            ypos+=2
        pygame.draw.circle(window,(200,200,200),(301,510),3)
        pygame.display.update()
        return True
    elif o_fills.count((420,180)) and o_fills.count((420,300)) and o_fills.count((420,420)):
        ypos=100
        pygame.draw.circle(window,(200,200,200),(421,100),3)
        while k:
            pygame.draw.line(window,(200,200,200),(420,ypos),(420,ypos+10),6)
            pygame.display.update()
            if ypos>=500:
                k=False
            ypos+=2
        pygame.draw.circle(window,(200,200,200),(421,510),3)
        pygame.display.update()
        return True
    elif o_fills.count((180,180)) and o_fills.count((300,300)) and o_fills.count((420,420)):
        xpos=120
        ypos=120
        while k:
            pygame.draw.line(window,(200,200,200),(xpos,ypos),(xpos+5,ypos+5),10)
            pygame.display.update()
            if ypos>=500:
                k=False
            xpos+=2
            ypos+=2
        return True
    elif o_fills.count((420,180)) and o_fills.count((300,300)) and o_fills.count((180,420)):
        xpos=480
        ypos=120
        while k:
            pygame.draw.line(window,(200,200,200),(xpos,ypos),(xpos-5,ypos+5),10)
            pygame.display.update()
            if ypos>=500:
                k=False
            xpos-=2
            ypos+=2
        return True
    else:
        pl=True
    if pl:
        return False
    else:
        hm='lold'
pygame.font.init()
myfont=pygame.font.SysFont('Carier New',100)
myfont1=pygame.font.SysFont('Carier New',80)
myfont2=pygame.font.SysFont('Calibri',43,1)
myfont3=pygame.font.SysFont('Calibri',40,1)
played_again=False
while not done:
    text1=myfont.render('XO',0,(255,255,255))
    text2=myfont2.render('CLICK ANYWHERE TO START',0,(255,255,255))
    window.fill((0,0,0))
    started=False
    while (not started) and (not played_again):
        window.blit(text1,(260,200))
        window.blit(text2,(70,290))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.display.quit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                started=True
                hm='lold'
        pygame.display.update()
    window.fill((0,0,0))
    turn=0
    filled=[]
    o_fills=[]
    x_fills=[]
    game_in_progress=True
    draw_table()
    while game_in_progress:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                click_pos=pygame.mouse.get_pos()
                click_pos=list(click_pos)
                if 240<click_pos[0]<360 and 240<click_pos[1]<360 and filled.count((300,300))==0:
                    if turn==0:
                        draw_X(300,300)
                        turn=1
                        x_fills.append((300,300))
                    else:
                        draw_O(300,300)
                        turn=0
                        o_fills.append((300,300))
                    filled.append((300,300))
                    hm='lold'
                elif 240<click_pos[0]<360 and 120<click_pos[1]<240 and filled.count((300,180))==0:
                    if turn==0:
                        draw_X(300,180)
                        turn=1
                        x_fills.append((300,180))
                    else:
                        draw_O(300,180)
                        turn=0
                        o_fills.append((300,180))
                    filled.append((300,180))
                    hm='lold'
                elif 240<click_pos[0]<360 and 360<click_pos[1]<480 and filled.count((300,420))==0:
                    if turn==0:
                        draw_X(300,420)
                        turn=1
                        x_fills.append((300,420))
                    else:
                        draw_O(300,420)
                        turn=0
                        o_fills.append((300,420))
                    filled.append((300,420))
                    hm='lold'
                elif 120<click_pos[0]<240 and 120<click_pos[1]<240 and filled.count((180,180))==0:
                    if turn==0:
                        draw_X(180,180)
                        turn=1
                        x_fills.append((180,180))
                    else:
                        draw_O(180,180)
                        turn=0
                        o_fills.append((180,180))
                    filled.append((180,180))
                    hm='lold'
                elif 360<click_pos[0]<480 and 120<click_pos[1]<240 and filled.count((420,180))==0:
                    if turn==0:
                        draw_X(420,180)
                        turn=1
                        x_fills.append((420,180))
                    else:
                        draw_O(420,180)
                        turn=0
                        o_fills.append((420,180))
                    filled.append((420,180))
                    hm='lold'
                elif 120<click_pos[0]<240 and 240<click_pos[1]<360 and filled.count((180,300))==0:
                    if turn==0:
                        draw_X(180,300)
                        turn=1
                        x_fills.append((180,300))
                    else:
                        draw_O(180,300)
                        turn=0
                        o_fills.append((180,300))
                    filled.append((180,300))
                    hm='lold'
                elif 360<click_pos[0]<480 and 240<click_pos[1]<360 and filled.count((420,300))==0:
                    if turn==0:
                        draw_X(420,300)
                        turn=1
                        x_fills.append((420,300))
                    else:
                        draw_O(420,300)
                        turn=0
                        o_fills.append((420,300))
                    filled.append((420,300))
                    hm='lold'
                elif 120<click_pos[0]<240 and 360<click_pos[1]<480 and filled.count((180,420))==0:
                    if turn==0:
                        draw_X(180,420)
                        turn=1
                        x_fills.append((180,420))
                    else:
                        draw_O(180,420)
                        turn=0
                        o_fills.append((180,420))
                    filled.append((180,420))
                    hm='lold'
                elif 360<click_pos[0]<480 and 360<click_pos[1]<480 and filled.count((420,420))==0:
                    if turn==0:
                        draw_X(420,420)
                        turn=1
                        x_fills.append((420,420))
                    else:
                        draw_O(420,420)
                        turn=0
                        o_fills.append((420,420))
                    filled.append((420,420))
                    hm='lold'
        pygame.display.update()
        if win_check_X():
            sleep(1)
            window.fill((0,0,0))
            text3=myfont1.render('PLAYER 1 WON',0,(255,255,255))
            text4=myfont3.render('PRESS R TO PLAY AGAIN',0,(255,255,0))
            text5=myfont3.render('PRESS ESCAPE TO QUIT',0,(255,65,0))
            window.blit(text3,(100,200))
            window.blit(text4,(115,300))
            window.blit(text5,(125,350))
            pygame.display.update()
            hm='lold'
            no_input=True
            while no_input:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.display.quit()
                    elif event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_ESCAPE:
                            pygame.display.quit()
                            no_input=False
                        elif event.key==pygame.K_r:
                            played_again=True
                            no_input=False
                            game_in_progress=False
        elif win_check_O():
            sleep(1)
            window.fill((0,0,0))
            text3=myfont1.render('PLAYER 2 WON',0,(255,255,255))
            text4=myfont3.render('PRESS R TO PLAY AGAIN',0,(255,255,0))
            text5=myfont3.render('PRESS ESCAPE TO QUIT',0,(255,65,0))
            window.blit(text3,(100,200))
            window.blit(text4,(115,300))
            window.blit(text5,(125,350))
            pygame.display.update()
            hm='lold'
            no_input=True
            while no_input:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.display.quit()
                    elif event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_ESCAPE:
                            pygame.display.quit()
                            no_input=False
                        elif event.key==pygame.K_r:
                            played_again=True
                            no_input=False
                            game_in_progress=False
        elif array_count(filled)>=9:
            sleep(1)
            window.fill((0,0,0))
            text3=myfont1.render('TIE',0,(255,255,255))
            text4=myfont3.render('PRESS R TO PLAY AGAIN',0,(255,255,0))
            text5=myfont3.render('PRESS ESCAPE TO QUIT',0,(255,65,0))
            window.blit(text3,(260,200))
            window.blit(text4,(115,300))
            window.blit(text5,(125,350))
            pygame.display.update()
            hm='lold'
            no_input=True
            while no_input:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.display.quit()
                    elif event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_ESCAPE:
                            pygame.display.quit()
                            no_input=False
                        elif event.key==pygame.K_r:
                            played_again=True
                            no_input=False
                            game_in_progress=False
        pygame.display.update()
    window.fill((0,0,0))
        
