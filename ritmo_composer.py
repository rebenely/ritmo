import pygame, sys, os
from pygame import gfxdraw
from entities.beat import Beat
from entities.song import Song
os.environ['SDL_VIDEO_CENTERED'] = '1'
SIZE = WIDTH, HEIGHT = 480, 640
pygame.mixer.pre_init(22050, -16, 2, 1024)
pygame.init()
pygame.mixer.quit()
pygame.mixer.init(22050, -16, 2, 1024)
screen = pygame.display.set_mode(SIZE)
effect_screen = pygame.surface.Surface(SIZE)
animation_timer = pygame.time.Clock()
beat_screen = pygame.surface.Surface(SIZE)  
score = 0
time = 0
# https://stackoverflow.com/questions/783897/truncating-floats-in-python #
def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])
    
def drawPolygon(x, y, color):
    pygame.gfxdraw.filled_polygon(a_screen, [(y, x - 39), (y - 19, x), (y, x - 19), (y + 19, x)], color)
    pygame.gfxdraw.aapolygon(a_screen, [(y, x - 40), (y - 20, x), (y, x - 20), (y + 20, x)], color)
    
def drawLeft(x, y, color, size, fill , a_screen):
    if(fill):
        pygame.gfxdraw.filled_polygon(a_screen, [(x - size, y), (x + size, y - size), (x, y), (x + size, y + size)], color)
    pygame.gfxdraw.aapolygon(a_screen,  [(x - size, y), (x + size, y - size), (x, y), (x + size, y + size)], color)
    if(fill):
        pygame.gfxdraw.filled_circle(a_screen, int(x + size/2), int(y), int(size/4), color)
    pygame.gfxdraw.aacircle(a_screen, int(x + size/2), int(y), int(size/4), color)
    if(fill):
        pygame.gfxdraw.filled_circle(a_screen, int(x + size), int(y), int(size/8), color)
    pygame.gfxdraw.aacircle(a_screen, int(x + size), int(y), int(size/8), color)
    
def drawRight(x, y, color, size, fill , a_screen):
    if(fill):
        pygame.gfxdraw.filled_polygon(a_screen, [(x + size, y), (x - size, y - size), (x, y), (x - size, y + size)], color)
    pygame.gfxdraw.aapolygon(a_screen,  [(x + size, y), (x - size, y - size), (x, y), (x - size, y + size)], color)
    if(fill):
        pygame.gfxdraw.filled_circle(a_screen, int(x - size/2), int(y), int(size/4), color)
    pygame.gfxdraw.aacircle(a_screen, int(x - size/2), int(y), int(size/4), color)
    if(fill):
        pygame.gfxdraw.filled_circle(a_screen,  int(x - size), int(y), int(size/8), color)
    pygame.gfxdraw.aacircle(a_screen, int(x - size), int(y), int(size/8), color)
    
def drawCircle(x, y, color, size, fill , a_screen):
    ## pygame.gfxdraw.filled_circle(a_screen, int(x - size/2), int(y - size/2), size, color)
    pygame.gfxdraw.aacircle(a_screen, int(x), int(y), size, color)
    if(fill):
        pygame.gfxdraw.filled_circle(a_screen, int(x), int(y), size, color)
    pygame.gfxdraw.arc(a_screen, int(x), int(y), size * 2, 180, 360, color)

def result_hit(hit_score):
    if(hit_score == 100):
        return 'COOL'
    elif(hit_score == 50):
        return 'GOOD'
    elif(hit_score == 25):
        return 'BAD'
    else:
        return 'MISS'
        
    
myfont = pygame.font.SysFont("ARBONNIE", 30)
getTicksLastFrame = 0
size_effect = 20
animator_l = 20
animator_r = 20
animator_c = 20
animator_result = 0

animate = False
started_c = False
started_r = False
started_l = False
y = 0
s = 0
x = 0
result = -1

#temp = Beat(-1, 20, 'assets/button-23.wav')
#temp1 = Beat(1, 25, 'assets/button-23.wav')
#temp2 = Beat(0, 30, 'assets/button-23.wav')

if(len(sys.argv) == 4):
    f = open("assets/" + sys.argv[1] + "/" +sys.argv[3] +".ritmo","w+")
    song = Song(sys.argv[1], int(sys.argv[2]), sys.argv[3])
    
else:
    print("Input must be:\npython ritmo.py title speed difficulty")
    pygame.quit()
    exit()
beat_list = song.get_beat_list()

# gawan ng sariling list ung mga nasa screen lang sa song class#

while True:
    time += 0.1
    if (animator_result > 20):
        animator_result = 0
        result = -1
    animation_timer.tick(60)
    screen.fill((0,0,0))
    effect_screen.fill((0,0,0))
    beat_screen.fill((0,0,0))
    
    #if len(beat_list) == 0:
    #    print('yehaw')

    t = pygame.time.get_ticks()
    # deltaTime in seconds.
    deltaTime = (t - getTicksLastFrame)
    getTicksLastFrame = t

    if(animator_c > 40):
        animator_c = 0
        started_c = False
    if(animator_l > 40):
        animator_l = 0
        started_l= False
    if(animator_r> 40):
        animator_r = 0
        started_r = False

    fill_l = False
    fill_r = False
    fill_c = False
    pressed = pygame.key.get_pressed()
    if(pressed[pygame.K_a]):
        fill_l = True
      
    if(pressed[pygame.K_d]):
        fill_r = True
        
    if(pressed[pygame.K_s]):
        fill_c = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            # have own check per button to enable multi press #
            if event.key == pygame.K_j :
                
                pressed_key = 2
                if(fill_c):
                    started_c = True
                    pressed_key = 0
                if(fill_l):
                    started_l = True
                    pressed_key = -1
                if(fill_r):
                    started_r = True
                    pressed_key = 1
                size_effect = 20
                hit_happened = False

                write_line = str(pressed_key) + ', ' + str(truncate(time/6 - 1/60, 3)) + ', CYCdh_ElecK03-Kick01.wav'
                print(write_line)   
                f.write("%s\n" % write_line)
            if event.key == pygame.K_k :
                
                pressed_key = 2
                if(fill_c):
                    started_c = True
                    pressed_key = 0
                if(fill_l):
                    started_l = True
                    pressed_key = -1
                if(fill_r):
                    started_r = True
                    pressed_key = 1
                size_effect = 20
                hit_happened = False

                write_line = str(pressed_key) + ', ' + str(truncate(time/6, 3)) + ', CYCdh_ElecK03-Clap01.wav'
                print(write_line)   
                f.write("%s\n" % write_line)
            if event.key == pygame.K_l :
                
                pressed_key = 2
                if(fill_c):
                    started_c = True
                    pressed_key = 0
                if(fill_l):
                    started_l = True
                    pressed_key = -1
                if(fill_r):
                    started_r = True
                    pressed_key = 1
                size_effect = 20
                hit_happened = False

                write_line = str(pressed_key) + ', ' + str(truncate(time/6 , 3)) + ', button-23.wav'
                print(write_line)   
                f.write("%s\n" % write_line)
    # beat screen #
    effect_screen.blit(beat_screen, (0, 0))   
    
    # effects #
    if(result != -1):
        pygame.gfxdraw.arc(effect_screen, int(WIDTH/2) - 50 - int(animator_result * 100) , int(HEIGHT/10 + 10), 20 + int(animator_result * 100), 90, 270, (0, 255, 0))  
        pygame.gfxdraw.arc(effect_screen, int(WIDTH/2) + 50 + int(animator_result * 100), int(HEIGHT/10 + 10  ), 20 + int(animator_result * 100), 270, 450, (0, 255, 0)) 
    
    if(started_c):
        animator_c += 4
        drawCircle(WIDTH/2, 6 * HEIGHT/7, (0,255,249), animator_c * 5, False, effect_screen)
        started_c = True
    if(started_l):
        animator_l += 4
        drawLeft(WIDTH/6, 6 * HEIGHT/7, (0,255,249), animator_l * 5, False, effect_screen)
        started_l = True
    if(started_r):
        animator_r += 4
        drawRight(5 * WIDTH/6, 6 * HEIGHT/7, (0,255,249), animator_r * 5, False, effect_screen)
        started_r = True
    
    drawCircle(WIDTH/2, HEIGHT/5 , (0,255,0), 10, False, effect_screen)
    drawLeft(2*WIDTH/6,  HEIGHT/5, (0,255,0), 20, False, effect_screen)
    drawRight(4*WIDTH/6,  HEIGHT/5, (0,255,0), 20, False, effect_screen)
    pygame.draw.aaline(effect_screen, (0, 255, 0), (2*WIDTH/6 + 10, HEIGHT/5), (WIDTH/6 + 20,6 * HEIGHT/7 )) 
    pygame.draw.aaline(effect_screen, (0, 255, 0), (WIDTH/2, HEIGHT/5), (WIDTH/2,6 * HEIGHT/7)) 
    pygame.draw.aaline(effect_screen, (0, 255, 0), (4*WIDTH/6 - 10, HEIGHT/5), (5 * WIDTH/6 - 20,6 * HEIGHT/7 )) 
        
     
    screen.blit(effect_screen, (0, 0))
    
    # score 
    score_surface = myfont.render(str(score), True, (0, 255, 255))
    
    if(result != -1):
        #print('update')
        result_surface = myfont.render(result_hit(result), True, (0, 255, 255))
        animate = True
        animator_result += 0.1
        pygame
        screen.blit(result_surface, (WIDTH/2 - result_surface.get_width()/2, HEIGHT/10))
    time_surface = myfont.render(str(truncate(time/6, 3)), True, (0, 255, 255))
    screen.blit(time_surface,(WIDTH/2 - time_surface.get_width()/2, HEIGHT/50))
    screen.blit(score_surface,(WIDTH/2 - score_surface.get_width()/2, HEIGHT/20))
    
    
    
    drawLeft(WIDTH/6, 6 * HEIGHT/7, (0,255,249), 40, fill_l, screen)
    drawCircle(WIDTH/2, 6 * HEIGHT/7, (0,255,249), 20, fill_c, screen)
    drawRight(5 * WIDTH/6, 6 * HEIGHT/7, (0,255,249), 40, fill_r, screen)
    
    
    pygame.display.update()
