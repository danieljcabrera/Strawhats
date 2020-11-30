# Functions for menu creation are defined here to avoid clutter in CovidBlaster
import pygame_menu


# Global variables for theme and font
FONT = './assets/font/m5x7.ttf'
THEME = pygame_menu.themes.THEME_DEFAULT
THEME.title_font = FONT
THEME.widget_font = FONT
THEME.title_font_size = 45
THEME.widget_font_size = 45

def create_main_menu(resolution: tuple, choice: tuple) -> pygame_menu.Menu:
    x, y = resolution
    main_menu = pygame_menu.Menu(y, x, 'COVID BLASTER', theme=THEME)
    main_menu.add_button('PLAY', choice[0])
    main_menu.add_button('HIGH SCORES', choice[1])
    main_menu.add_button('SETTINGS', choice[2])
    main_menu.add_button('QUIT', choice[3])
    return main_menu


def create_play_menu(resolution: tuple, choice: tuple) -> pygame_menu.Menu:
    x, y = resolution
    play_menu = pygame_menu.Menu(y, x, 'COVID BLASTER', theme=THEME)
    play_menu.add_selector('COLOR: ', [
                          ('RED', './assets/sprites/CHARACTER_SPRITES/Red/'), 
                          ('GREEN', './assets/sprites/CHARACTER_SPRITES/Green/'),
                          ('BLUE', './assets/sprites/CHARACTER_SPRITES/Blue/'),
                          ('YELLOW', './assets/sprites/CHARACTER_SPRITES/Yellow/'),
                          ('BLACK', './assets/sprites/CHARACTER_SPRITES/Black/')
                          ], onchange=choice[0], onreturn=choice[0])
    
    play_menu.add_text_input('ENTER A NAME: ', default='PLAYER', maxchar=10, onchange=choice[1], onreturn=choice[1])
    play_menu.add_button('START', choice[2])
    play_menu.add_button('BACK', choice[3])
    return play_menu


def create_hs_menu(resolution: tuple, choice: callable) -> pygame_menu.Menu:
    x, y = resolution
    hs_menu = pygame_menu.Menu(y, x, 'HIGH SCORES', theme=THEME)
    for _ in range(10): hs_menu.add_label('')
    hs_menu.add_button('BACK', choice)
    return hs_menu


def create_settings_menu(resolution: tuple, choice: tuple) -> pygame_menu.Menu:
    x, y = resolution
    settings_menu = pygame_menu.Menu(y, x, 'SETTINGS', theme=THEME)
    settings_menu.add_button('CLEAR HIGH SCORES', choice[0])
    settings_menu.add_button('BACK', choice[1])
    return settings_menu


def create_confirmation_menu(resolution: tuple, choice: tuple) -> pygame_menu.Menu:
    x, y = resolution
    confirmation_menu = pygame_menu.Menu(y, x, 'SETTINGS', theme=THEME)
    confirmation_menu.add_label('ARE YOU SURE?')
    confirmation_menu.add_button('YES', choice[0])
    confirmation_menu.add_button('NO', choice[1])
    return confirmation_menu
