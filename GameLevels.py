import pygame
from pygame.locals import *
from pygame.sprite import Group
import random
import sys
import Interface
import Algorithms
from Figures import Bubble


class Level():
    """Родительский класс уровней игры"""

    class Enter(Exception):
        """Класс ошибки для понимания, что пользователь окончил промежуточный ввод"""
        pass

    class Exit(Exception):
        """Класс ошибки для выхода в меню"""
        pass

    def __init__(self, screen):
        """Инициализация уровня игры"""

        self.data = Algorithms.Data()
        self.screen = screen
        self.interface = Interface.Interface(screen)
        self.bubbles = Group()
        self.sound = self.data.data["SOUND"]
        self.boom1 = pygame.mixer.Sound("Sounds/boom.wav")
        self.boom2 = pygame.mixer.Sound("Sounds/boom2.wav")
        self.concrete_level = None


    def concrete_level_init(self, concrete_level):
        self.concrete_level = concrete_level

    def output_fon(self):
        """отрисовка фона"""

        self.screen.blit(self.concrete_level.image, (0, 0))
        self.interface.InеterfaceDraw()

    def output_inter(self):
        """отрисовка интерфейса"""

        self.interface.InеterfaceDraw()



    def event_handler(self):
        """Обработка действий игрока"""

        for event in pygame.event.get():
            if event.type == QUIT:
                self.data.save()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_0 or event.key == K_KP0:
                    self.interface.text += "0"
                if event.key == K_1 or event.key == K_KP1:
                    self.interface.text += "1"
                if event.key == K_2 or event.key == K_KP2:
                    self.interface.text += "2"
                if event.key == K_3 or event.key == K_KP3:
                    self.interface.text += "3"
                if event.key == K_4 or event.key == K_KP4:
                    self.interface.text += "4"
                if event.key == K_5 or event.key == K_KP5:
                    self.interface.text += "5"
                if event.key == K_6 or event.key == K_KP6:
                    self.interface.text += "6"
                if event.key == K_7 or event.key == K_KP7:
                    self.interface.text += "7"
                if event.key == K_8 or event.key == K_KP8:
                    self.interface.text += "8"
                if event.key == K_9 or event.key == K_KP9:
                    self.interface.text += "9"
                if event.key == K_RETURN or event.key == K_KP_ENTER:
                    raise self.Enter
                if event.key == K_BACKSPACE:
                    self.interface.text = self.interface.text[:-1]
                if event.key == K_ESCAPE:
                    raise self.Exit

    def run(self):
        """Инициализация основоного цикла программы"""

        clock = pygame.time.Clock()
        FPS = 60
        control = 110
        last_bubble_rect = True
        run_game = True
        if self.sound:
            pygame.mixer.music.play(-1)


        while run_game:
            """Основной цикл программы"""

            if len(self.bubbles) == 0 or last_bubble_rect.top > control:
                task, answer, points = self.concrete_level.create_task()
                new_bubble = (Bubble(self.screen, task, answer, points))
                self.bubbles.add(new_bubble)
                last_bubble_rect = new_bubble.rect
            try:
                self.event_handler()
            except self.Enter: # Если пользователь окончил ввод
                if self.interface.text != "":
                    for bubble in self.bubbles.sprites():
                        inp = int(self.interface.text)
                        if bubble.answer == inp:
                            self.interface.score += bubble.points
                            self.bubbles.remove(bubble)
                            if bubble.rect.top == last_bubble_rect.top:
                                last_bubble_rect.top = control + 1
                            self.concrete_level.speed += self.concrete_level.multer
                            random.choice((self.boom1, self.boom2)).play()
                    self.interface.text = ""
            except self.Exit: # Если пользователь хочет выйти в главное меню
                pygame.mixer.music.stop()
                return "MAIN MENU", self.interface.score

            self.output_fon()
            for bubble in self.bubbles.sprites():
                try:
                    bubble.update(self.concrete_level.speed)
                except Bubble.GameOver: # Если один из пузырей достиг нижнего края экрана
                    pygame.mixer.music.stop()
                    return "GAME OVER", self.interface.score

                bubble.output()
            self.output_inter()
            pygame.display.flip()
            clock.tick(FPS) # Отрисовка кадров с заданой частотой
