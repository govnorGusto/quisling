from settings import *
from level.level import Level
from turn_manager import Turn_Manager
from button import Button
from core.message_router import Message_Router
from core.input_manager import Input_Manager

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("the quisling project")
        self.current_stage = Level()
        self.running = True
        
        self.message_router = Message_Router()
        self.input_manager = Input_Manager(self)
        self.message_router.register_callback(pygame.QUIT, self.OnQuit)
        self.message_router.register_callback(pygame.KEYDOWN, self.OnKeyDown)

        self.turn_manager = Turn_Manager()
        self.button = Button(WINDOW_WIDTH - 100,
                             WINDOW_HEIGHT - 70, "NEXT")

    def process_input(self):
        self.input_manager.process_input()
        
    def OnQuit(self, eventdata):
        self.running = False
    
    ### TODO: This binding should happen inside the turn_manager, game does arguably not give a shit
    ###       leaving as is for now to avoid conflicts in turn_manager.py // Herjeman (GUSTAV) 
    def OnKeyDown(self, eventdata):
        self.turn_manager.move(eventdata.key)

    def update(self, dt):
        self.turn_manager.update()

    def draw(self, dt):
        self.current_stage.draw()
        self.turn_manager.players.draw(self.display_surface)
        if self.button.draw():
            self.turn_manager.change_player()

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000

            self.process_input()
            self.update(dt)
            self.draw(dt)

            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
