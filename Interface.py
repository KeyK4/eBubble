import pygame

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font('Fonts/BIPs.ttf', 31)
INP_FONT = pygame.font.Font('Fonts/BIPs.ttf', 35)


class Interface:
    """Класс интерфейса игры"""

    def __init__(self, screen):
        """Инициализация атрибутов интерфейса"""

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text = ""
        self.score = 0
        self.background_rect = pygame.Rect(0, 0, 110, 45)
        self.background_rect.centerx = self.screen_rect.centerx
        self.background_rect.centery += 5

    def InеterfaceDraw(self):
        """Функция для вывода интрефейса на экран"""

        pygame.draw.rect(self.screen, WHITE, self.background_rect, border_radius=5)
        TextForPrint = INP_FONT.render(self.text, 1, BLACK)
        text_rect = TextForPrint.get_rect()
        text_rect.center = self.background_rect.center
        text_rect.centery += 4
        self.screen.blit(TextForPrint, text_rect)

        ScoreForOutput = FONT.render(str(self.score), 1, WHITE)
        score_rect = ScoreForOutput.get_rect()
        score_rect.topright = self.screen_rect.topright
        self.screen.blit(ScoreForOutput, score_rect)