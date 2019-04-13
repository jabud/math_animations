import pygame
import numpy as np


class MovingObj(pygame.sprite.Sprite):

    def __init__(self, screen, img_path):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        try:
            self.imagePuff = pygame.transform.scale(pygame.image.load(img_path), (90, 144))
        except:
            raise UserWarning("Unable to find image")
        self.image = self.imagePuff
        self.imagePuff.set_colorkey((255,255,255))           
        self.rect = self.image.get_rect()
        self.x = self.screen.get_width()*.45
        self.y = self.screen.get_height()*.3
        self.rect.center = (self.x, self.y)

        self.lifespan = 60
        self.speed = 1
        self.count = 0
        self.angle = 0
        self.y_change = 0
        self.x_change = 0
        self.angle_change = 0


    def update(self):
        self.y += self.y_change
        self.x += self.x_change
        self.angle = (self.angle + self.angle_change) % 360
        self.rect.center = self.x, self.y
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.imagePuff, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter


    def pos_still(self):
        self.y_change = 0
        self.x_change = 0

    def ang_still(self):
        self.angle_change = 0

    def turnleft(self):
        self.angle_change = 5

    def turnright(self):
        self.angle_change = -5

    def forward(self):
        self.y_change = np.cos(np.deg2rad(self.angle))*5
        self.x_change = np.sin(np.deg2rad(self.angle))*5

    def backward(self):
        self.y_change = np.cos(np.deg2rad(self.angle))*-5
        self.x_change = np.sin(np.deg2rad(self.angle))*-5


if __name__  == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    pygame.display.set_caption('Moving Object')
    car = MovingObj(screen, 'Calculus/car.png')
    sprites = pygame.sprite.Group()
    sprites.add(car)
    keepGoing = True
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            # event listeners
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car.turnleft()
                elif event.key == pygame.K_RIGHT:
                    car.turnright()
                elif event.key == pygame.K_DOWN:
                    car.backward()
                elif event.key == pygame.K_UP:
                    car.forward()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car.ang_still()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    car.pos_still()
                    
        # sprites.clear(screen, background)
        screen.fill((255, 255, 255))
        sprites.update()
        sprites.draw(screen)
        pygame.display.flip()   
        clock.tick(60)
