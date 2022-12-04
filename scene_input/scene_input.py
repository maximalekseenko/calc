import pygame
from engine import Scene



class Scene_Input(Scene):

    def __init__(self, act, base: pygame.Surface | pygame.Rect | None = None) -> None:
        super().__init__(act, base)

        # for snippets
        from act_main import Act_Main
        self.act:Act_Main

        # buttons
        from .element_button import Element_Button
        self.buttons:list[list[Element_Button]] = [
            [Element_Button(self, "AC", '\x7f'),    Element_Button(self, "BCS", '\x08'),Element_Button(self, "%", '%'),     Element_Button(self, "/", '/')],
            [Element_Button(self, "7", '7'),        Element_Button(self, "8", '8'),     Element_Button(self, "9", '9'),     Element_Button(self, "*", '*')],
            [Element_Button(self, "4", '4'),        Element_Button(self, "5", '5'),     Element_Button(self, "6", '6'),     Element_Button(self, "-", '-')],
            [Element_Button(self, "1", '1'),        Element_Button(self, "2", '2'),     Element_Button(self, "3", '3'),     Element_Button(self, "+", '+')],
            [Element_Button(self, "OFF", '\x1b'),   Element_Button(self, "0", '0'),     Element_Button(self, ".", '.'),     Element_Button(self, "=", '=')],
            ]

    
    def On_Update(self):
        if self.surface.get_width() / len(self.buttons[0]) < self.surface.get_height() / len(self.buttons):
            buttonsize = self.surface.get_width() / len(self.buttons[0])
        else:
            buttonsize = self.surface.get_height() / len(self.buttons)

        for y in range(len(self.buttons)):
            for x in range(len(self.buttons[y])):
                self.buttons[y][x].rect = pygame.Rect(
                    x * buttonsize,
                    y * buttonsize,
                    buttonsize,
                    buttonsize)
                self.buttons[y][x].Update()


    def On_Handle(self, event: pygame.event.Event) -> None:
        for buttonrow in self.buttons:
            for button in buttonrow:
                button.Handle(event)


    def On_Render(self) -> None:
        self.surface.fill("#000000")

        for buttonrow in self.buttons:
            for button in buttonrow:
                button.Render(self.surface)
