import pygame
from engine import Theatre


class Theatre(Theatre):
    def __init__(self) -> None:
        super().__init__()

        self.font = pygame.font.Font("./7seg.ttf", 30)
        self.colors = ["#505050", "#909090", "#a0a0a0", "#b0b0b0", "#10b050"]

theatre = Theatre()