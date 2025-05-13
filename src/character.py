import pygame
import sys 

def draw_text(text, font, text_color, x, y,screen):
    img = font.render(text, False, text_color)
    screen.blit(img, (x, y))

def main():
    pygame.init()
    pygame.font.init()

    pygame.display.set_caption("Fabula_Ultima Character Creator")

    info = pygame.display.Info()
    s_width = info.current_w
    s_height = info.current_h
    screen = pygame.display.set_mode((s_width, s_height))

    color = (255,255,255)
    background = (255, 230, 162)
    color_light = (215, 240, 255)
    color_dark = (160, 222, 255)
    running = True
    while running:
        screen.fill((background))
        pygame.draw.rect(screen, color_dark, [590, 315, 80 , 30])
        text_font = pygame.font.SysFont("nirmalatext", 15)
        draw_text=("load", text_font, (0,0,0,), 590, 315, screen)
        pygame.display.flip()
pygame.quit()


if __name__ == "__main__":
    main()