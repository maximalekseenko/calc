import pygame
from engine import Element



class Element_Button(Element):
    def __init__(self, scene, base: pygame.Surface | pygame.Rect | None = None, surface_flags: int = None) -> None:
        super().__init__(scene, base, surface_flags)

    