import pygame
import sys 
import pygame_menu

#create a menu screen
#create the level - current avatar w/ buttons to class, items, bond
#create buttons in level w/ more info in indivuals - button to add
#add buttons to naviagte
#allow text features on avatar for bonds

class Universal_Buttons():
    def back():
        pygame_menu.events.BACK
        pass
    def add(added_class):
        with open("avatar", "a") as file:
            file.write((added_class).read())
            pygame_menu.events.BACK
        

class Available_Classes():
    def classes_menu(s_width, s_height, screen):
        #buttons that link to .txt classes
        classes = pygame_menu.Menu('Classes',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
        classes.add.button("Arcanist", Available_Classes.arcanist_menu, s_width, s_height, screen)
        classes.mainloop(screen)
        pass

    def arcanist_menu(s_width, s_height, screen):  
    
        arcanist = pygame_menu.Menu('Arcanist',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
        arcanist.add.label('Arcanists fall into a trance and project their soul into a physical form.' \
        'These forms are manifestations of ancestral entitnites, sometimes seen as deities.',max_char=-1)
        arcanist.add.label('Permanently increase your maximum Mind Points by 5.',max_char=-1)
        arcanist.add.label('Arcane Circle', max_char=-1)
        arcanist.add.label('Willingly dismiss an Arcanum on your turn during a conflict. If that Arcanum is not summoned during the same turn, '
        'and you have an arcane weapon equipped, you may immediately perform a Spell action for free. ', max_char=-1)
        arcanist.add.label('The spell must cost 5 Mind Points or lower.', max_char=-1)
        arcanist.add.label('Arcane Regeneration', max_char=-1)
        arcanist.add.label('When you summon an Arcanum, you immediately recover 5 Hit Points.', max_char=-1)
        arcanist.add.label('Bind and Summon', max_char=-1)
        arcanist.add.label('You can bind Arcana to your soul and summon them later. ' \
        'You can use an action and spend 40 Mind Points to summon an Arcanum you have bound.', max_char=-1)
        arcanist.add.label('Emergency Arcanum', max_char=-1)
        arcanist.add.label('As long as you are in Crisis, the cost for summoning your Arcana is reduced by 5 Mind Points.', max_char=-1)
        arcanist.add.label('Ritual Arcanism', max_char=-1)
        arcanist.add.label('You may perform Rituals of the Arcanism discipline, as long as their effects ' \
        'fall within the domains of one or more Arcana you have bound to.', max_char=-1)
        added_class = input("arcanist.txt")
        arcanist.add.button("Add", Universal_Buttons.add, added_class)
        arcanist.add.button("Back", Universal_Buttons.back)
        arcanist.mainloop(screen)
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