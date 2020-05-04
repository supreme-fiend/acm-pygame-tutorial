import pygame
import random

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("CoinCollector")
pygame.mixer.music.load('rustboro.mp3')
pygame.mixer.music.play(-1)


class Coin:
    def __init__(self):
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 500)
        self.collected = False

    def draw(self):
        pygame.draw.circle(win, (255, 255, 0),(self.x, self.y), 5)

class Player:
    def __init__(self):
        self.x = 250
        self.y = 250
        self.velocity = 0.1
        self.numcollected = 0   


    def draw(self):
        pygame.draw.rect(win, (255,0,0), (self.x, self.y, 20, 20))

class ScoreBar:
    def __init__(self, x, width):
        self.x = x
        self.width = width
        self.text = ""

    def updatescore(self, score):
        font = pygame.font.SysFont('Arial', 10)
        self.text = str(score)
        pygame.draw.rect(win,(255,0,0) , (self.x, 5, self.width, 12))
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), 5 + (12 / 2 - text.get_height() / 2)))
    

p = Player()

coins = []

score = ScoreBar(5, 15)

for i in range (5):
    c = Coin()
    coins.append(c)

def refresh():
    win.fill((0, 0, 0))
    p.draw()
    for coin in coins:
        if coin.collected == False:
            coin.draw()

    score.updatescore(p.numcollected)
    pygame.display.update()


run = True

while (run):
    refresh()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            break
        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        p.y -= p.velocity
    if pressed[pygame.K_DOWN]:
        p.y += p.velocity
    if pressed[pygame.K_LEFT]:
        p.x -= p.velocity
    if pressed[pygame.K_RIGHT]:
        p.x += p.velocity
    
    for coin in coins:
        if coin.x >= p.x and coin.x <= (p.x+20) and coin.y >= p.y and coin.y <= p.y + 20:
            p.numcollected += 1
            coin.collected = True
            coins.remove(coin)
