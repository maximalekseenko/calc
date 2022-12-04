import pygame
from theatre import theatre
from engine import Element



class Element_Button(Element):
    def __init__(self, scene, text:str, click_unicode:str) -> None:
        super().__init__(scene)

        # for snippets
        from .scene_input import Scene_Input
        self.scene:Scene_Input

        # init data
        self.text = text
        self.click_unicode = click_unicode

        # highlight
        self.is_highlighted = False

    
    def On_Update(self):
        self.text_surface = theatre.font.render(self.text, 1, theatre.colors[0])
        self.text_rect = self.text_surface.get_rect(centerx=self.rect.width / 2, centery=self.rect.height / 2)


    def On_Handle(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.is_highlighted = self.rect.collidepoint(*self.scene.Relative(event.pos))

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(*self.scene.Relative(event.pos)):
                self.scene.act.Button_Click(self.click_unicode)


    
    def On_Render(self, target: pygame.Surface) -> None:

        # fill
        if self.is_highlighted:
            self.surface.fill(theatre.colors[3])
        else:
            self.surface.fill(theatre.colors[2])

        # text
        self.surface.blit(self.text_surface, self.text_rect)

        # border
        pygame.draw.rect(self.surface, theatre.colors[1], (0,0,*self.rect.size), 1,)

        # add to parent
        target.blit(self.surface, self.rect)
            