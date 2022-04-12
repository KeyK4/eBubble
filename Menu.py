import pygame
from pygame.locals import *
import sys
import Algorithms
import random

class MainMenu:
    """Класс главного меню игры"""

    class Button:
        """Класс конопок меню"""

        def __init__(self, screen, button_image):
            """Инициализация атрибутов кнопки"""

            self.screen = screen
            self.image = button_image
            self.screen_rect = screen.get_rect()
            self.rect = button_image.get_rect()
            self.rect.centerx = self.screen_rect.centerx

        def output(self):
            """Функция отрисовки кнопки"""

            self.screen.blit(self.image, self.rect)


    def __init__(self, screen):
        """Инициализация атрибутов главного меню"""

        self.data = Algorithms.Data()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.sound = self.data.data["SOUND"]
        self.background = pygame.image.load("Images/menu_fon.png")
        self.simple_button = self.Button(screen, pygame.image.load("Images/simple_button.png"))
        self.simple_button.rect.centery = self.screen_rect.centery
        self.medium_button = self.Button(screen, pygame.image.load("Images/normal_button.png"))
        self.medium_button.rect.centery = self.simple_button.rect.centery + 100
        self.hard_button = self.Button(screen, pygame.image.load("Images/insane_button.png"))
        self.hard_button.rect.centery = self.medium_button.rect.centery + 100
        if self.sound:
            self.sound_image = pygame.image.load("Images/sound_off_button.png")
        else:
            self.sound_image = pygame.image.load("Images/sound_on_button.png")
        self.sound_rect = self.sound_image.get_rect()
        self.sound_rect.bottomright = self.screen_rect.bottomright
        pygame.mixer.music.load("Sounds/menu.mp3")

    def run(self):
        """Галавный цикл работы главного меню"""

        click =False
        if self.sound:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play(-1)
            pygame.mixer.music.pause()
        while True:
            self.screen.blit(self.background, (0, 0))
            self.simple_button.output()
            self.medium_button.output()
            self.hard_button.output()
            self.screen.blit(self.sound_image, self.sound_rect)

            mx, my = pygame.mouse.get_pos()

            if self.simple_button.rect.collidepoint((mx, my)):
                if click:
                    return "SIMPLE"
            if self.medium_button.rect.collidepoint((mx, my)):
                if click:
                    return "MEDIUM"
            if self.hard_button.rect.collidepoint((mx, my)):
                if click:
                    return "HARD"
            if self.sound_rect.collidepoint((mx, my)):
                if click:
                    if self.sound:
                        self.sound = False
                        self.data.data["SOUND"] = False
                        self.sound_image = pygame.image.load("Images/sound_on_button.png")
                        pygame.mixer.music.pause()
                    else:
                        self.sound = True
                        self.data.data["SOUND"] = True
                        self.sound_image = pygame.image.load("Images/sound_off_button.png")
                        pygame.mixer.music.unpause()
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.data.save()
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.flip()

class GameOverMenu:
    """Класс меню проигрыша"""

    class Button:
        """Класс конопок меню"""

        def __init__(self, screen, button_image, slide):
            """Инициализация атрибутов кнопок в игровом меню"""

            self.screen = screen
            self.image = button_image
            self.screen_rect = screen.get_rect()
            self.rect = button_image.get_rect()
            self.rect.centerx, self.rect.centery = self.screen_rect.centerx + slide, self.screen_rect.centery + 80

        def output(self):
            """Функция вывода кнопки на экран"""

            self.screen.blit(self.image, self.rect)


    def __init__(self, screen):
        """Инициализация арибутов игровоно меню"""

        self.data = Algorithms.Data()
        self.screen = screen
        self.play_button = self.Button(screen, pygame.image.load("Images/play_button.png"), 90)
        self.menu_button = self.Button(screen, pygame.image.load("Images/main_menu_button.png"), -90)
        self.font = pygame.font.Font('Fonts/BIPs.ttf', 30)
        self.concrete_menu = None


    def concrete_menu_init(self, concrete_menu):
        """Сеттер меню выбранного уровня"""

        self.concrete_menu = concrete_menu


    def words(self, num):
        """Функция склонения слова "очко", для корректного вывода на экран"""
        number = str(num)
        if 10 < num < 20:
            return number + " очков"
        elif number[-1] == "1":
            return number + " очко"
        elif number[-1] in "234":
            return number + " очка"
        else:
            return number + " очков"

    def lose(self, points):
        """Функция для вывода меню проигрыша на экран"""

        self.points_str = self.font.render(self.words(points), 1, (77, 64, 54))
        self.points_rect = self.points_str.get_rect()
        self.points_rect.center = self.concrete_menu.background_rect.center
        self.points_rect.centery -= 10
        return self.gameover(self.concrete_menu.back_ground_lose)

    def win(self, points):
        """Функция для вывода меню выигрыша на экран"""
        self.points_str = self.font.render(self.words(points), 1, (77, 64, 54))
        self.points_rect = self.points_str.get_rect()
        self.points_rect.center = self.concrete_menu.background_rect.center
        self.points_rect.centery -= 10
        return self.gameover(self.concrete_menu.back_ground_win)

    def gameover(self, img):
        """Основной цикл обработки событий игрового меню"""

        click = False
        while True:
            self.screen.blit(img, (0, 0))
            self.screen.blit(self.points_str,  self.points_rect)
            self.play_button.output()
            self.menu_button.output()

            mx, my = pygame.mouse.get_pos()

            if self.play_button.rect.collidepoint((mx, my)):
                if click:
                    return True
            if self.menu_button.rect.collidepoint((mx, my)):
                if click:
                    return False

            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.data.save()
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return False
                    if event.key == K_SPACE or event.key == K_RETURN:
                        return True
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.flip()

class SimpleStrategy():
    """Класс стратегии легкого уровня"""
    def __init__(self):
        self.back_ground_lose = pygame.image.load("Images/simple_game_over.png")
        self.back_ground_win = pygame.image.load("Images/simple_new_record.png")
        self.background_rect = self.back_ground_win.get_rect()
        self.image = pygame.image.load("Images/simple_fon.png")
        self.speed = 0.5
        self.multer = 0.05
        self.data = Algorithms.Data()
        if self.data.data["SOUND"]:
            pygame.mixer.music.load("Sounds/simple.mp3")

    def create_task(self):
        """функция для создания примера"""
        operator = random.choice(("+", "-"))
        if operator == "+":
            first = random.randint(1, 30)
            if len(str(first)) > 1:
                second = random.randint(1, 9)
            else:
                second = random.randint(1, 30)
            return f"{first} + {second}", first + second, 1
        else:
            first = random.randint(1, 30)
            if len(str(first)) > 1:
                second = random.randint(1, 9)
                return f"{first} - {second}", first - second, 2
            else:
                second = random.randint(9, 30)
                return f"{second} - {first}", second - first, 2

class MediumStrategy():
    """Класс стратегии среднего уровня"""
    def __init__(self):
        self.back_ground_lose = pygame.image.load("Images/medium_game_over.png")
        self.back_ground_win = pygame.image.load("Images/medium_new_record.png")
        self.background_rect = self.back_ground_win.get_rect()
        self.image = pygame.image.load("Images/medium_fon.png")
        self.speed = 0.3
        self.multer = 0.03
        self.data = Algorithms.Data()
        if self.data.data["SOUND"]:
            pygame.mixer.music.load("Sounds/medium.mp3")

    def create_task(self):
        """функция для создания примера"""
        operator = random.choice(("*", "/"))
        if operator == "*":
            first = random.randint(0, 19)
            if len(str(first)) > 1:
                second = random.randint(0, 9)
            else:
                second = random.randint(0, 19)
            return f"{first} x {second}", first * second, 3
        else:
            first = random.randint(0, 9)
            second = random.randint(1, 9)
            return f"{first * second} / {second}", first, 4

class HardStrategy():
    """Класс стратегии сложного уровня"""
    def __init__(self):
        self.back_ground_lose = pygame.image.load("Images/insane_game_over.png")
        self.back_ground_win = pygame.image.load("Images/insane_new_record.png")
        self.background_rect = self.back_ground_win.get_rect()
        self.image = pygame.image.load("Images/insane_fon.png")
        self.speed = 0.1
        self.multer = 0.01
        self.data = Algorithms.Data()
        if self.data.data["SOUND"]:
            pygame.mixer.music.load("Sounds/insane.mp3")

    def create_task(self):
        """функция для создания примера"""

        operator = random.choice(("+", "-", "*", "/"))
        if operator == "+":
            first = random.randint(100, 999)
            second = random.randint(100, 999)
            return f"{first} + {second}", first + second, 1
        elif operator == "-":
            first = random.randint(10, 999)
            second = random.randint(10, 999)
            if first >= second:
                return f"{first} - {second}", first - second, 2
            else:
                return f"{second} - {first}", second - first, 2
        elif operator == "*":
            first = random.randint(0, 99)
            if len(str(first)) > 1:
                second = random.randint(0, 10)
            else:
                second = random.randint(0, 99)
            return f"{first} x {second}", first * second, 3
        else:
            first = random.randint(0, 99)
            second = random.randint(0, 99)
            return f"{first * second} / {first}", second, 4
