import pygame
from theatre import theatre
from engine import Scene



class Scene_Output(Scene):

    def __init__(self, act, base: pygame.Surface | pygame.Rect | None = None) -> None:
        super().__init__(act, base)

        # for snippets
        from act_main import Act_Main
        self.act:Act_Main

    
    def On_Update(self):
        self.text_surf = theatre.font.render(self.act.line, 1, theatre.colors[4])
        self.text_rect = self.text_surf.get_rect(midright = self.rect.midright)


    def On_Render(self) -> None:
        self.surface.fill(theatre.colors[0])

        # 
        self.surface.blit(self.text_surf, self.text_rect)