import pygame, sys
from Player import player
from fish import Fish

class Game:
    fishes = []
    delta = 0.0
    max_tps = 100.0
    clock = pygame.time.Clock()
    color = (0,0,200)
    score = 0
    catched = True
    texty = 10

    def gameOver(self):
        for i in range(3):
            self.fishes[i].rect.y = 500
            self.player.rect.y = 400
        self.texty = 150
        self.text = "Game Over score: " + str(self.score)

    def Ticking(self):
        self.delta += self.clock.tick() / 1000.0  # ile czasu zajelo wykonanie kazdej klatki
        while self.delta > 1 / self.max_tps:
            self.delta -= 1 / self.max_tps  # wykonuje sie to max_tps na sekunde
            self.player.Moving()

            self.fishes[0].Move()
            self.fishes[1].Move()
            self.fishes[2].Move()



            self.collision(0)
            self.collision(1)
            self.collision(2)

#jakies niewazne gowno
            if(self.score%10 == 0):
                if(self.score<102):
                    help = self.score/10
                    help = help%10
                if(self.score<102):
                    self.max_tps = self.makeHarder(help)
                if(self.score>99):
                    self.max_tps = 100.0+10*25

            if(pygame.key.get_pressed()[pygame.K_q]):
                self.score += 1

    def makeHarder(self, it):
        return 100.0+it*25

    def collision(self, i):
        while ((self.fishes[i].rect.y > 300 - 45) & (self.fishes[i].rect.y < 300)):

            if (self.player.rect.colliderect(self.fishes[i])):
                print("catched!")
                self.score += 1
                self.fishes[i].newX()
                # if (self.score > 10):
                #     licznik = licznik3 - 100
                # else:
                self.fishes[i].rect.y = 0
            else:
                if (self.fishes[i].rect.y  > 290):
                    self.catched = False
                    print("not catched")
                    self.gameOver()
                break

    def __init__(self):

        pygame.init()
        self.window = pygame.display.set_mode((50 * 3, 300))

        self.czcionka = pygame.font.SysFont("comicsans", 20)
        self.player = player("./res/man.png")
        self.fishes.append(Fish("./res/blackfish.png"))
        self.fishes.append(Fish("./res/blackfish.png"))
        self.fishes.append(Fish("./res/blackfish.png"))

        self.fishes[0].rect.y = -350
        self.fishes[1].rect.y = -440
        self.fishes[2].rect.y = -525

        while True:
            self.window.fill(self.color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            if (pygame.key.get_pressed()[pygame.K_SPACE]):
                a = Game()

            if(self.catched == True):
                self.text = "score" + str(self.score)
            self.text_render = self.czcionka.render(self.text, 1, (250, 250, 250))
            self.window.blit(self.text_render, (10, self.texty))

            self.window.blit(player.getImage(self.player), (self.player.rect.x,self.player.rect.y))
            self.window.blit(Fish.getImage(self.fishes[0]), (self.fishes[0].rect.x,self.fishes[0].rect.y))
            self.window.blit(Fish.getImage(self.fishes[1]), (self.fishes[1].rect.x,self.fishes[1].rect.y))
            self.window.blit(Fish.getImage(self.fishes[2]), (self.fishes[2].rect.x,self.fishes[2].rect.y))

            self.Ticking()
            pygame.display.flip()

g = Game()
