import pygame
class Beat:
    """A beat in ritmo"""
    
    def __init__(self, direction, time, WIDTH, HEIGHT, sound):
        self.direction = direction
        if(self.direction == -1):
            self.x = 2*WIDTH/6
            self.target = (WIDTH/6, 6 * HEIGHT/7)
            
        elif (self.direction == 1):
            self.x = 4*WIDTH/6
            self.target = (5 * WIDTH/6, 6 * HEIGHT/7)
        else:
            self.x = WIDTH/2
            self.target = (WIDTH/2, 6 * HEIGHT/7)
        self.sound_effect = pygame.mixer.Sound('assets/' + sound)
        self.s = 10
        self.time = time
        Beat.speed = 30
        self.hit = False
        self.y = self.target[1] - Beat.speed * self.time 
        self.time_in_field = 0
        self.time_in_field_calc = (6*HEIGHT/7 - HEIGHT/5)/Beat.speed
        #Beat.speed = (self.target[1] - self.y) / self.time
        self.y_check = 0
        
    def getDir(self):
        return self.direction
            
    def getPos(self,time):
        #if(self.direction == 0):
        return time*Beat.speed
    def getX(self, time):
        return time*(75/self.time_in_field_calc)
    
    def getSize(self,time):
        """ values are hard coded sadlyf """
        if(self.direction == 0):
            return time*(30-20)/(self.time_in_field_calc)
        else:
            return time*(50-20)/(self.time_in_field_calc)
    def render(self, screen, time):
        if(self.direction == -1):
        
            move_y = self.getPos(time)
            if(self.y + move_y > 128):
                self.time_in_field += 0.1
                move_x = self.getX(self.time_in_field)
                move_s = self.getSize(self.time_in_field)
                self.y_check = self.y + move_y
                self.drawLeft(self.x - move_x, self.y_check, (0, 255, 0), int(self.s + move_s), self.hit, screen)
                
         
        elif (self.direction == 1):
            move_y = self.getPos(time)
            if(self.y + move_y > 128):
                self.time_in_field += 0.1
                move_x = self.getX(self.time_in_field)
                move_s = self.getSize(self.time_in_field)
                self.y_check = self.y + move_y
                self.drawRight(self.x + move_x, self.y_check, (0, 255, 0), int(self.s + move_s), self.hit, screen)
                
        else:
            
            move_y = self.getPos(time)
            if(self.y + move_y > 128):
                self.time_in_field += 0.1
                move_s = self.getSize(self.time_in_field)
                self.y_check = self.y + move_y
                self.drawCircle(self.x, self.y_check, (0, 255, 0), int(self.s + move_s), self.hit, screen)
        #if(self.y_check > 490 and self.y_check < 495):
        #    self.sound_effect.play()
    def isHit(self, direction):
        print(self.y_check)
        # not yet hit #
        if not (self.hit):
            if(self.y_check > 480 and self.y_check < 530 and direction == self.direction):
                self.sound_effect.play()
                self.hit = True
                return 50
            if(self.y_check > 530 and self.y_check < 560 and direction == self.direction):
                self.sound_effect.play()
                self.hit = True
                return 100 
            if(self.y_check > 560 and self.y_check < 580 and direction == self.direction):
                self.sound_effect.play()
                self.hit = True
                return 25
        return 0
       
    def getDir(self):
        return self.direction
     
    def drawLeft(self, x, y, color, size, fill , a_screen):
        if(fill):
            pygame.gfxdraw.filled_polygon(a_screen, [(x - size, y), (x + size, y - size), (x, y), (x + size, y + size)], color)
        pygame.gfxdraw.aapolygon(a_screen,  [(x - size, y), (x + size, y - size), (x, y), (x + size, y + size)], color)
        if(fill):
            pygame.gfxdraw.filled_circle(a_screen, int(x + size/2), int(y), int(size/4), color)
        pygame.gfxdraw.aacircle(a_screen, int(x + size/2), int(y), int(size/4), color)
        if(fill):
            pygame.gfxdraw.filled_circle(a_screen, int(x + size), int(y), int(size/8), color)
        pygame.gfxdraw.aacircle(a_screen, int(x + size), int(y), int(size/8), color)
        
    def drawRight(self, x, y, color, size, fill , a_screen):
        if(fill):
            pygame.gfxdraw.filled_polygon(a_screen, [(x + size, y), (x - size, y - size), (x, y), (x - size, y + size)], color)
        pygame.gfxdraw.aapolygon(a_screen,  [(x + size, y), (x - size, y - size), (x, y), (x - size, y + size)], color)
        if(fill):
            pygame.gfxdraw.filled_circle(a_screen, int(x - size/2), int(y), int(size/4), color)
        pygame.gfxdraw.aacircle(a_screen, int(x - size/2), int(y), int(size/4), color)
        if(fill):
            pygame.gfxdraw.filled_circle(a_screen,  int(x - size), int(y), int(size/8), color)
        pygame.gfxdraw.aacircle(a_screen, int(x - size), int(y), int(size/8), color)
        
    def drawCircle(self, x, y, color, size, fill , a_screen):

        ## pygame.gfxdraw.filled_circle(a_screen, int(x - size/2), int(y - size/2), size, color)
        pygame.gfxdraw.aacircle(a_screen, int(x), int(y), size, color)
        if(fill):
            pygame.gfxdraw.filled_circle(a_screen, int(x), int(y), size, color)
        pygame.gfxdraw.arc(a_screen, int(x), int(y), size * 2, 180, 360, color)
