import pygame

class player:
    id = 0
    y = 300-45
    x = 0

    def __init__(self, filename):
        self.id += 1
        self.image = pygame.image.load(filename)
        self.rect = pygame.Rect(self.x, self.y, 40, 20)


    def  getImage(self):
        return self.image

    def Moving(self):
        if (pygame.key.get_pressed()[pygame.K_RIGHT]):
            self.rect.move_ip(2, 0)
        if (pygame.key.get_pressed()[pygame.K_LEFT]):
            self.rect.move_ip(-2, 0)
        self.checkScreen()

#to zmienic
    def checkScreen(self):
        if(self.rect.x>150):
            self.rect.x = -40
        if(self.rect.x<-40):
            self.rect.x = 150