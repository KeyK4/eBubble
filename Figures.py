import pygame
import random
from Interface import FONT, WHITE


class Figure(pygame.sprite.Sprite):
    class GameOver(Exception):
        pass
    """Класс фигуры, которых может быть много"""
    def __init__(self, screen, task="0+0", answer=0, points=1, image=None):
        super(Figure, self).__init__()
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = random.randint(90, self.screen_rect.right - 90)  # генерируется положение пузыря на экране, такой диапазон выбран
                                                      # для того чтобы пузырь не оказаляся вне экрана
        self.center = float(self.rect.centery)
        self.rect.top = self.screen_rect.top
        self.task = FONT.render(task, 1, WHITE)
        self.task_rect = self.task.get_rect()
        self.answer = answer
        self.points = points


    def output(self):
        """Отрисовка фигуры"""
        self.screen.blit(self.image, self.rect)
        self.task_rect.center = self.rect.center
        self.screen.blit(self.task, self.task_rect)

    def update(self, speed):
        """Обновление позиции фигуры"""
        if self.rect.bottom < self.screen_rect.bottom:
            self.center += speed
        else:
            raise self.GameOver
        self.rect.centery = self.center


class Bubble(Figure):
    """Класс пузыря с примером"""
    COLORS = ["blue", "brown", "green", "kream", "orange", "purple", "red", "rose", "swamp", "yellow"]

    def __init__(self, screen, task="0+0", answer=0, points=1):

        """Инициализация пузыря"""
        color = random.choice(self.COLORS)
        image = pygame.image.load(f'Images/{color}_bubble.png')

        super().__init__(screen, task=task, answer=answer, points=points, image=image)