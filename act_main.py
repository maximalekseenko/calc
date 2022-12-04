import pygame
from theatre import theatre
from engine import Act



class Act_Main(Act):
    def __init__(self) -> None:
        super().__init__()

        # scenes
        from scene_output.scene_output import Scene_Output
        self.scene_output:Scene_Output = Scene_Output(self, None)
        from scene_input.scene_input import Scene_Input
        self.scene_input:Scene_Input = Scene_Input(self, None)

        # other
        self.is_preview:bool = True
        '''Is currently showing a result of the previous calculation.'''
        self.line:str = "0.8731505"
        '''Current input (if `.is_preview`==`False`) or result (if `.is_preview`==`True`).'''
        self.memory:int = 0
        '''Used to save previous answer.'''


    def On_Update(self):
        # set scenes rects
        self.scene_output.rect = pygame.Rect(
            0,
            0,
            self.surface.get_width(),
            self.surface.get_height() * 1/3)
        self.scene_input.rect = pygame.Rect(
            0,
            self.surface.get_height() * 1/3,
            self.surface.get_width(),
            self.surface.get_height() * 2/3)

        # update scenes
        self.scene_output.Update()
        self.scene_input.Update()


    def On_Open(self) -> None:
        self.scene_output.Open()
        self.scene_input.Open()

        self.Update()


    def On_Handle(self, event: pygame.event.Event) -> None:
        if event.type == pygame.WINDOWRESIZED:
            self.Update()

        elif event.type == pygame.KEYDOWN:
            print(event)
            self.Button_Click(event.unicode)
        
        else:
            self.scene_input.Handle(event)


    def On_Render(self) -> None:
        self.scene_output.Render()
        self.surface.blit(self.scene_output.surface, self.scene_output.rect)

        self.scene_input.Render()
        self.surface.blit(self.scene_input.surface, self.scene_input.rect)


    def Button_Click(self, unicode:str):
            # numbers
            if unicode in ['0','1','2','3','4','5','6','7','8','9','%','*','/','-','+',' ']:
                self.Add_To_Line(unicode)
            elif unicode in ['\x08']:
                self.Remove_From_Line()
            elif unicode in ['=', '\r']:
                self.Resolve_Line()
            elif unicode in ['\x1b']:
                theatre.is_running = False
            elif unicode in ['\x7f']:
                self.line = ""
                self.scene_output.Update()
            elif unicode in ['a']:
                self.line += str(self.memory)
                self.scene_output.Update()
            else: print(unicode)


    def Add_To_Line(self, char:str):

        # clean preview
        if self.is_preview:
            self.line = ""
            self.is_preview = False

        # add char
        self.line += char

        # update output text
        self.scene_output.Update()


    def Remove_From_Line(self):

        # clean preview
        if self.is_preview:
            self.line = ""
            self.is_preview = False

        # remove char
        if len(self.line) > 0:
            self.line = self.line[:-1]

        # update output text
        self.scene_output.Update()


    def Resolve_Line(self):
        self.is_preview = True

        # validate the line
        for char in self.line:
            if char not in ['0','1','2','3','4','5','6','7','8','9','%','*','/','-','+',' ','.']:
                self.line = "&"
                self.scene_output.Update()
                return
        
        # eval the line
        result = None
        try:
            result = eval(self.line)
            self.memory = result
            self.line = str(result)
        except:
            self.line = "&"
            
        self.scene_output.Update()

