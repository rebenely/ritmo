import os, pygame
from entities.beat import Beat

class Song:
    """ A song in ritmo """
    def __init__(self, title, speed, difficulty):
        self.title = title
        self.speed = speed
        #os.chdir('..')
        self.path = 'assets/' + title
        self.ritmo = self.path + '/' + difficulty + '.ritmo'
        pygame.mixer.music.load(self.path + '/music.mp3')
        self.beat_list = []
        pygame.mixer.music.play()
        count = 0
        Beat.SPEED = self.speed
        with open (self.ritmo, "r") as myfile:
            for line in myfile:
                #print(line)
                line = line.replace('\n', '')
                line = line.replace(' ', '')
                contents = line.split(',')
                sound_effect = pygame.mixer.Sound(self.path + '/sfx/' + contents[2])
                self.beat_list.append(Beat(float(contents[0]), float(contents[1]), self.path + '/sfx/' + contents[2]))
                #print(contents)

    def render(self, screen, time):
        for beat in beat_list:
            beat.render()
    def get_beat_list(self):
        return self.beat_list