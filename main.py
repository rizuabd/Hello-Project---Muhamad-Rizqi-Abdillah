import pygame
import os
player = int

WIDTH, HEIGHT = 720, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TicMath')
FPS = 60

#Assets
background_image = pygame.image.load(os.path.join("Assets", "bg.bmp"))
question_tab = pygame.image.load(os.path.join("Assets", "question.png"))
player_1_tab = pygame.image.load(os.path.join("Assets", "bar.png"))
player_2_tab = pygame.image.load(os.path.join("Assets", "bar.png"))
button_1_img = pygame.image.load(os.path.join("Assets", "1.png"))


#color
white = (255, 255, 255)
grey = (125,125,125)

#button class
class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
#button instance
button_1 = Button(40,724, button_1_img)

def draw_window():
    WIN.fill(white)
    WIN.blit(background_image, (1, 1))  
    WIN.blit(player_1_tab, (40,724))
    WIN.blit(player_2_tab, (400,724))
    WIN.blit(question_tab, (40,524))

    pygame.display.update()
    
def draw_button(self):
    pos = pygame.mouse.get_pos()
    if self.rect.collidepoint(pos):
        if pygame.mouseget_pressed()[0] ==1:
            player1 +=1 
        
    WIN.blit(self.image, (self.rect.x, self.rect.y))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
        #draw_button()
    pygame.quit()

if __name__ == '__main__':
    main()