import pygame
import sys 

def main():
    pygame.init()

    pygame.display.set_caption("Fabula Ultima Character Creator")

    info = pygame.display.Info()
    s_width = info.current_w
    s_height = info.current_h
    screen = pygame.display.set_mode((s_width, s_height))

    color = (255,255,255)
    background = (255, 230, 162)
    color_light = (215, 240, 255)
    color_dark = (160, 222, 255)
    screen.fill((background))

    text_font = pygame.font.SysFont("nirmalatext", 32)
    text = text_font.render('quit' , True , color)
    mouse = pygame.mouse.get_pos() 
    if s_width/2 <= mouse[0] <= s_width/2+140 and s_height/2 <= mouse[1] <= s_height/2+40:  
        pygame.draw.rect(screen,color_light,[s_width/2,s_height/2,140,40])  
    else:  
        pygame.draw.rect(screen,color_dark,[s_width/2,s_height/2,140,40])  
        screen.blit(text, (s_width/2+50,s_height/2))  
    while True:  
        for ev in pygame.event.get():     
            if ev.type == pygame.QUIT:  
                pygame.quit()        
            if ev.type == pygame.MOUSEBUTTONDOWN:  
                if s_width/2 <= mouse[0] <= s_width/2+140 and s_height/2 <= mouse[1] <= s_height/2+40:  
                    pygame.quit()
    pygame.display.flip()


if __name__ == "__main__":
    main()