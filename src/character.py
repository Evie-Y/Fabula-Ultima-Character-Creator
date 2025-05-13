import pygame
import sys 
import pygame_menu

#create a menu screen
#create the level - current avatar w/ buttons to class, items, bond
#create buttons in level w/ more info in indivuals - button to add
#add buttons to naviagte
#allow text features on avatar for bonds

def draw_text(text, font, text_color, x, y,screen):
    img = font.render(text, False, text_color)
    screen.blit(img, (x, y))

class Menus():
    def classes_menu(s_width, s_height):
        pygame_menu.Menu('Classes',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
        pass

    def shop_menu(s_width, s_height):
        pygame_menu.Menu('Shop',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
        pass

    def bonds_menu(s_width, s_height):
        pygame_menu.Menu('Bonds',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
        pass

    def quit_menu(running):
        running == False
        pass

def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Fabula_Ultima Character Creator")

    info = pygame.display.Info()
    s_width = info.current_w
    s_height = info.current_h
    screen = pygame.display.set_mode((s_width, s_height))
#render
    background = (255, 230, 162)
    color_light = (215, 240, 255)
    color_dark = (160, 222, 255)

    screen.fill((background))
    pygame.draw.rect(screen, color_dark, [590, 315, 80 , 30])
    text_font = pygame.font.SysFont("nirmalatext", 25)
    draw_text("load", text_font, (0,0,0), 605, 312, screen)

    mainmenu = pygame_menu.Menu('',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
    mainmenu.add.text_input('Name: ', default='Avatar')
    mainmenu.add.button('Classes', Menus.classes_menu)
    mainmenu.add.button('Shop', Menus.shop_menu)
    mainmenu.add.button('Bonds', Menus.bonds_menu)
    mainmenu.add.button('Quit', Menus.quit_menu)

#game loop
    running = True
    while running == True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running == False
    
        if mainmenu.is_enabled():
            mainmenu.update(events)
            mainmenu.draw(screen)
        
        pygame.display.update()     
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()