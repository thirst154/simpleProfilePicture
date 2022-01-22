##Random Github Profile Picture creator
import pygame, random, time

pygame.init()

class picture():
    def __init__(self, size):
        self.width = size[0]
        self.height = size[1]
        self.scale = 100
        self.screen = pygame.display.set_mode([self.width,self.height])

    def create(self):
        for x in range(0,self.width,self.scale):
            for y in range(0,self.height,self.scale):
                rect = pygame.Rect(x, y, self.scale, self.scale)
                pygame.draw.rect(self.screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), rect)

profilePic = picture((500,500))

def Main():
    profilePic.ceates()
    pygame.image.save(profilePic.screen, 'image.png')
    time.sleep(0.1)
    


if __name__ == '__main__':
    Main()
