import pygame
import sys 
import pygame_menu

#create a menu screen
#create the level - current avatar w/ buttons to class, items, bond
#create buttons in level w/ more info in indivuals - button to add
#add buttons to naviagte
#allow text features on avatar for bonds


class Available_Classes():
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
        arcanist.add.button("Add", Universal_Buttons.add)
        arcanist.add.button("Back", Universal_Buttons.back)
        arcanist.mainloop(screen)
        pass

    def chimerist_menu(s_width, s_height, screen):  
        chimerist = pygame_menu.Menu('Chimerist',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
        chimerist.add.label('Chimerists gather their power from the souls of monsters and beasts they encounter. ' \
        'By manipulating their inner energy, they can mimic magical abilities of monsters'
        'and greatly understand feral creatures. They rely on their toughness, physical prowess, and magic.', max_char=-1)
        chimerist.add.label('Permanently increase your maximin Mind Points by 5.', max_char=-1)
        chimerist.add.label('You may perform Rituals whose effects fall within the Ritualism discipline.', max_char=-1)
        chimerist.add.label('Consume', max_char=-1)
        chimerist.add.label('After you deal damage to one or more creatures with a spell, '
        'if you have an arcane/dagger/flail weapon equipped, you recover 2 Mind Points.', max_char=-1)
        chimerist.add.label('Feral Speech', max_char=-1)
        chimerist.add.label('You can communicate with beast/monster/plant Species.', max_char=-1)
        chimerist.add.label('Pathogenesis', max_char=-1)
        chimerist.add.label('When you deal damage to one or more creatures with a Chimerist spell,' \
        'each of those creatures that share their Species with the creature you learned it from is now poisoned.', max_char=-1)
        chimerist.add.label('Ritual Chimerism ', max_char=-1)
        chimerist.add.label('You may perform Rituals whose effects fall within the Chimerism discipline. ', max_char=-1)
        chimerist.add.label('Spell Mimic', max_char=-1)
        chimerist.add.label('When you see a beast/monster/plant Species cast a spell, ' \
        'you may immediately choose to learn that spell as a Chimerist spell of your own: '
        'if you do, record the Species of the creature you learned it from.', max_char=-1)
        chimerist.add.button("Add", Universal_Buttons.add)
        chimerist.add.button("Back", Universal_Buttons.back)
        chimerist.mainloop(screen)
        pass

    def darkblade_menu(s_width, s_height, screen):  
        darkblade = pygame_menu.Menu('Arcanist',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
        darkblade.add.label("Darkblades are powerful warriors with a sorrowful past. Due to tragedy, " \
        "they hav an affinity for pain and shadow energy. They can sacrifice their lifeforce to unleash mighty attacks and " \
        "are able to draw resolve, power, and knowledge from their suffering.", max_char=-1)
        darkblade.add.label("Permanently increase you maximun Hit Points by 5.", max_char=-1)
        darkblade.add.label("Gain the ability to equip martial melee weapons and martial armor.", max_char=-1)
        darkblade.add.label("Agony", max_char=-1)
        darkblade.add.label("After you deal damage to one or more creatures, if you have a Bond towards at least one of those creatures, " \
        "you may recover 2 Hit Points and 2 Mind Points.", max_char=-1)
        darkblade.add.label("Dark Blood", max_char=-1)
        darkblade.add.label("As long as you are in Crisis, you have Resistamce to dark damage and poison damage.", max_char=-1)
        darkblade.add.label("Heart of Darkness", max_char=-1)
        darkblade.add.label("Once per scene upon entering Crisis, you may choose a specific creature you can see that you don't have a Bond towards. " \
        "If you do, create a Bond of Hatred towards that creature.", max_char=-1)
        darkblade.add.label("Painful Lesson", max_char=-1)
        darkblade.add.label("After another creature causes you to lose Hit Points, you may immediately perform the Study action " \
        "on that creature for free. You can study the same aspect of a creature only once.", max_char=-1)
        darkblade.add.label("Shadow Strike", max_char=-1)
        darkblade.add.label("You have learned how to channel your vital force into your attacks. You may use an action to perform a Shadow Strike: " \
        "roll your current Might die and lose an amout of Hit Points equal to the number you rolled. If this didn't reduce your health to 0, " \
        "you may perform a free attack with a weapon you have equipped: if this attack hits one or more targets, it deals an extra 1 + " \
        "number you rolled. However, all damage dealt is dark damage type.", max_char=-1)
        darkblade.add.button("Add", Universal_Buttons.add)
        darkblade.add.button("Back", Universal_Buttons.back)
        darkblade.mainloop(screen)

    def elementalist_menu(s_width, s_height, screen):  
        elementalist = pygame_menu.Menu('Elementalist',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
        elementalist.add.label("An Elementalist has learned to channel the souls that flow within the basic elements of creation: " \
        "Air, Earth, Fire and Water. Some of them develop complex spells to contain the powerful energies of nature; others seek its " \
        "protection in harmony and communion.", max_char=-1)
        elementalist.add.label("Permanently increase your maximum Mind Points by 5.", max_char=-1)
        elementalist.add.label("You may perform Rituals whose effects fall within the Ritualism discipline.", max_char=-1)
        elementalist.add.label("Cataclysm", max_char=-1)
        elementalist.add.label("When you cast a spell with a duration of 'Instantaneous', if you have an arcane weapon equipped, you may " \
        "increase the spell's total MP cost by 10 Mind Points. If you do so and the spell deals damage to one or more creatures, " \
        "it will deal 5 extra damage to each creature for every 10 Mind Points by which you increased its total MP cost.", max_char=-1)
        elementalist.add.label("Elemental Magic", max_char=-1)
        elementalist.add.label("Magical Artillery", max_char=-1)
        elementalist.add.label("When you cast an offensive spell, if you have an arcane weapon equipped, " \
        "you gain a bonus of 2 to your Magic Check.", max_char=-1)
        elementalist.add.label("Ritual Elementalism", max_char=-1)
        elementalist.add.label("You may perform Rituals whose effects fall within the Elementalism discipline.", max_char=-1)
        elementalist.add.label("Spellblade", max_char=-1)
        elementalist.add.label("When you cast an offensive spell targeting a single creature, if the spell has a total Mind Point cost of 10 "
        "or lower and you have one or more bow, brawling, dagger, flail, spear or sword weapons equipped, you may choose one of those weapons. " \
        "If you do, your Magic Check for the spell will use the chosen weapon's Accuracy Checkformula.", max_char=-1)
        elementalist.add .button("Add", Universal_Buttons.add)
        elementalist.add.button("Back", Universal_Buttons.back)
        elementalist.mainloop(screen)

    def entropist_menu(s_width, s_height, screen):  
        entropist = pygame_menu.Menu('Entropist',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
        entropist.add.label("High above the stars, where their lights do not shine, lies a bottomless void where life and souls wither and " \
        "transform in unfathomable ways. This realm is a non-reality, an endless expanse of chaos impervious to the laws of time, space, "
        "and probability. Entropists refer to this realm as the Cosmos, the Heavens, or quite simply as Lady Luck: they are among the few " \
        "gifted with the ability to channel its reality-bending energies.", max_char=-1)
        entropist.add.label("Permanently increase your maximum Mind Points by 5.", max_char=-1)
        entropist.add.label("You may perform Rituals whose effects fall within the Ritualism discipline.", max_char=-1)
        entropist.add.label("Absorb Map", max_char=-1)
        entropist.add.label("After you suffer damage, you may immediately recover 2 Mind Points.", max_char=-1)
        entropist.add.label("Entropic Magic", max_char=-1)
        entropist.add.label("Each time you acquire this Skill, learn one Entropist spell.", max_char=-1)
        entropist.add.label("Lucky Seven", max_char=-1)
        entropist.add.label("You have a lucky number; at the beginning of each session, that number is 7. Once per scene after you perform a Check, " \
        "you may replace the value shown on one of the dice you rolled with your lucky number (even if this would give an impossible Result, " \
        "such as a value of 7 on a d6). If you do, the replaced value becomes your new lucky number.", max_char=-1)
        entropist.add.label("Ritual Entropism", max_char=-1)
        entropist.add.label("You may perform Rituals whose effects fall within the Entropism discipline.", max_char=-1)
        entropist.add.label("Stolen Time", max_char=-1)
        entropist.add.label("During a conflict, you may use an action to interfere with the flow of time by spending up to 5 Mind Points. " \
        "For every 5 Mind Points you spend this way, choose one option: one creature you can see suffers slow; or one creature you can see " \
        "recovers from slow; or one creature you can see may immediately perform the Equipment action for free; or choose one ally you can " \
        "see who has yet to take a turn during this round: that ally may take their turn immediately after yours during this round. " \
        "Each option can only be chosen once per use of this Skill.", max_char=-1)
        entropist.add.button("Add", Universal_Buttons.add)
        entropist.add.button("Back", Universal_Buttons.back)
        entropist.mainloop(screen)

    def fury_menu(s_width, s_height, screen):  
        fury = pygame_menu.Menu('Fury',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
        fury.add.label("Furies never know when to quit. In battle and life they are energetic, determined and often restless. " \
        "Whatever ideals or desires drive their actions, they will stop at nothing and risk everything in order to achieve them.", max_char=-1)
        fury.add.label("Permanently increase your maximum Hit Points by 5.", max_char=-1)
        fury.add.label("Gain the ability to equip martial melee weapons and martial armor.", max_char=-1)
        fury.add.label("Adrenaline", max_char=-1)
        fury.add.label("As long as you are in Crisis, you deal 2 extra damage (be it with attacks, spells, Arcana, items or any other " \
        "method).", max_char=-1)
        fury.add.label("Frenzy", max_char=-1)
        fury.add.label("Your Accuracy Checks with brawling, dagger, flail and thrown weapons trigger a critical success if both dice show " \
        "the same number (and the Check is not a fumble).", max_char=-1)
        fury.add.label("Indomitable SPirit", max_char=-1)
        fury.add.label("When you spend one or more Fabula Points, you get an additional benefit — choose one option: you recover 5 Hit Points; "
        "or you recover 5 Mind Points; or you recover from a single status effect of your choice.", max_char=-1)
        fury.add.label("Provoke", max_char=-1)
        fury.add.label("You may use an action and spend 5 Mind Points to perform an Opposed Check against a creature you can see — " \
        "describe how you taunt them! If you succeed, the target suffers enraged and is compelled to focus their attention on you "
        "(their attacks and offensive spells must include you among the targets if possible). This compulsion ends if you fall unconscious "
        "or leave the scene, if the creature is no longer enraged, or if they are successfully provoked by someone else.", max_char=-1)
        fury.add.label("Withstand", max_char=-1)
        fury.add.label("When you perform the Guard action, if you choose not to provide cover to another creature, you recover " \
        "Hit Points equal to 1 x the highest strength among your Bond and choose Might or Willpower: you treat the chosen Attribute as " \
        "being one die size higher (up to a maximum of d12) until the end of your next turn.", max_char=-1)
        fury.add.button("Add", Universal_Buttons.add)
        fury.add.button("Back", Universal_Buttons.back)
        fury.mainloop(screen) 

    def guardian_menu(s_width, s_height, screen):  
        guardian = pygame_menu.Menu('Guardian',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
        guardian.add.label("", max_char=-1)
        guardian.add.button("Add", Universal_Buttons.add)
        guardian.add.button("Back", Universal_Buttons.back)
        guardian.mainloop(screen)

    def classes_menu(s_width, s_height, screen):
        #buttons that link to .txt classes
        classes = pygame_menu.Menu('Classes',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
        classes.add.button("Arcanist", Available_Classes.arcanist_menu, s_width, s_height, screen)
        classes.add.button("Chimerist", Available_Classes.chimerist_menu, s_width, s_height, screen)
        classes.add.button("Darkblade", Available_Classes.darkblade_menu, s_width, s_height, screen)
        classes.add.button("Elementalist", Available_Classes.elementalist_menu, s_width, s_height, screen)
        classes.add.button("Entropist", Available_Classes.entropist_menu, s_width, s_height, screen)
        classes.add.button("Fury", Available_Classes.fury_menu, s_width, s_height, screen)
        classes.add.button("Guardian", Available_Classes.guardian_menu, s_width, s_height, screen)
        classes.mainloop(screen)
        pass

class Available_Items():
    def inventory(value, item):
        item = value
        pass

    def shop_menu(s_width, s_height, screen):
        #buttons that link to .txt classes
        shop = pygame_menu.Menu('Shop',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
        shop.add.dropselect('Items', ['bronze_plate', 'bronze_shield', 'combat_tunic', 'runic_plate',
        'runic_shield', 'sage_robe', 'silk_shirt', "travel_garb"], onchange= Available_Items.inventory)
        shop.add.button("Add", Universal_Buttons.add)
        shop.add.button("Back", Universal_Buttons.back)
        shop.mainloop(screen)
        pass
    
class Bond_Types():
    def admiration():
        pass

    def inferiority():
        pass

    def loyalty():
        pass

    def mistrust():
        pass

    def affection():
        pass

    def hatred():
        pass

    def bonds_menu(s_width, s_height, screen):
        #buttons that link to different bonds
        bond = pygame_menu.Menu('Bonds',s_width,s_height,theme=pygame_menu.themes.THEME_DARK)
        bond.add.button("Admiration", Bond_Types.admiration)
        bond.add.label('You believe you have much to learn from this person and deeply respect them for their efforts and achievements.'
                       ,max_char=-1)
        bond.add.button("Inferiority", Bond_Types.inferiority)
        bond.add.label('You envy this person or feel like you would be powerless against them.'\
                       'Their very presence frustrates you, acting as a reminder of your failures.',max_char=-1)
        bond.add.button("Loyalty", Bond_Types.loyalty)
        bond.add.label('This person has won your trust, or you believe in their ideals. You are ready to endanger'\
                       'yourself to help or protect them.',max_char=-1)
        bond.add.button("Mistrust", Bond_Types.mistrust)
        bond.add.label("You don't believe the words of this person and doubt their intentions.",max_char=-1)
        bond.add.button("Affection", Bond_Types.affection)
        bond.add.label('You have tender feelings for this person, be they a love interest, a dear friend, or a member of your family.'
                       ,max_char=-1)
        bond.add.button("Hatred", Bond_Types.hatred)
        bond.add.label('You can scarcely control yourself in the presence of this person, '
        'and would do anything to see them broken and defeated.',max_char=-1)
        bond.add.button("Add", Universal_Buttons.add)
        bond.add.button("Back", Universal_Buttons.back)
        bond.mainloop(screen)
        pass

class Universal_Buttons():
    def back():
        pygame_menu.events.CLOSE
        pass
    def add():
        pygame_menu.events.BACK

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