import pygame
import Algorithms
import GameLevels
import Menu

data = Algorithms.Data()
pygame.init()
pygame.display.set_caption("eBubble")
screen = pygame.display.set_mode((1280, 720))
programIcon = pygame.image.load('Images/icon.png')
pygame.display.set_icon(programIcon)

def main_menu():
    """Запуск главного меню игры, и цикл перезапуска одного и того же уровня"""
    menu = Menu.MainMenu(screen)
    key = menu.run()
    data.save()
    feed_back = True
    while feed_back:
        #Пока пользователь выбирает перезапуск, запускаем уровень
        feed_back = run(key)
    return 0

def run(key):
    """Запуск выбранного уровня и получение ответа пользователя из игрового меню"""
    level = GameLevels.Level(screen)
    game_over_menu = Menu.GameOverMenu(screen)


    if key == "SIMPLE":
        level.concrete_level_init(Menu.SimpleStrategy())
        game_over_menu.concrete_menu_init(Menu.SimpleStrategy())

    elif key == "MEDIUM":
        level.concrete_level_init(Menu.MediumStrategy())
        game_over_menu.concrete_menu_init(Menu.MediumStrategy())

    else:
        level.concrete_level_init(Menu.HardStrategy())
        game_over_menu.concrete_menu_init(Menu.HardStrategy())

    feed_back, score = level.run()
    if feed_back == "GAME OVER":
        if data.data[key] > score:
            return game_over_menu.lose(score)
        else:
            data.data[key] = score
            data.save()
            return game_over_menu.win(score)
    elif feed_back == "MAIN MENU":
        return False


while True:
    """Запуск главного меню игры и полследующий его перезапуск после выхода в меню из меню окончания игры"""
    main_menu()


