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

class Available_Classes():
    def classes_menu(s_width, s_height, screen):
        #buttons that link to .txt classes
        print("1")
        classes = pygame_menu.Menu('Classes',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
        print("2")
        classes.add.button("Arcanist", Available_Classes.arcanist_menu, s_width, s_height, screen)
        classes.mainloop(screen)
        pass

    def arcanist_menu(s_width, s_height, screen):   
        pass

class Available_Items():
    def shop_menu(s_width, s_height, screen):
        #buttons that link to .txt classes
        shop = pygame_menu.Menu('Shop',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
        pass

class Bond_Types():
    def bonds_menu(s_width, s_height, screen):
        #buttons that link to different bonds
        pygame_menu.Menu('Bonds',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
        pass

def quit_menu(running, screen):
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
    running = True
#render
    mainmenu = pygame_menu.Menu('',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
    mainmenu.add.text_input('Name: ', default='Avatar')
    mainmenu.add.button('Classes', Available_Classes.classes_menu, s_width, s_height, screen)
    mainmenu.add.button('Shop', Available_Items.shop_menu, s_width, s_height, screen)
    mainmenu.add.button('Bonds', Bond_Types.bonds_menu, s_width, s_height, screen)
    mainmenu.add.button('Quit', quit_menu, running, screen)
#game loop
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