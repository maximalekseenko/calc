import pygame
from engine import Scene



class Scene_Input(Scene):

    def __init__(self, act, base: pygame.Surface | pygame.Rect | None = None) -> None:
        super().__init__(act, base)

        # for snippets
        from act_main import Act_Main
        self.act:Act_Main


    def On_Render(self) -> None:
        self.surface.fill("#000000")