import pygame
from engine import Theatre


class Theatre(Theatre):
    def __init__(self) -> None:
        super().__init__()

        self.font_dseg7_30 = pygame.font.Font("./DSEG7.ttf", 30)
        self.font_none_30 = pygame.font.Font(None, 30)

theatre = Theatre()