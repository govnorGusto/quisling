from settings import *
from level.level import Level
from turn_manager import Turn_Manager
from button import Button
from core.message_router import Message_Router
from core.input_manager import Input_Manager
from core.game_object import Game_object
from game_objects.example_game_object import Example_Game_Object
from game_objects.components.example_component import Example_Component

from ui.ui_button import UI_Button
from ui.ui_text import UI_Text
from ui.uicore.ui_canvas import UI_Canvas

from core.grid import Grid


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("the quisling project")

        self.current_stage = Level()

        self.game_objects: [Game_object] = []
        self.input_manager = Input_Manager(self)
        self.grid = Grid()
        self.turn_manager = Turn_Manager()
        self.message_router = Message_Router()

        self.message_router.register_callback(pygame.QUIT, self.on_quit)

        ### TODO: This binding should probably happen inside the turn_manager,
        ###       Leaving as is for now to avoid conflicts in turn_manager.py
        ###       as a change would require the Turn_Manager::change_player function
        ###       to change signature // Herjeman (GUSTAV)
        ###       PS. See clickable_component.py for example
        self.message_router.register_callback(pygame.KEYDOWN, self.on_key_down)

        ### TODO: I don't like keeping this definition in the init.
        ###       I assume we need some scene manager or the like where can keep
        ###       relevant UI definitions for each game state // Herjeman
        self.button_canvas = UI_Canvas(
            pygame.Rect(WINDOW_WIDTH - 220, WINDOW_HEIGHT - 120, 200, 100)
        )
        self.button_canvas.color = (100, 100, 100)
        button = self.button_canvas.add_child(UI_Button)
        button.click_callbacks.append(self.turn_manager.change_player)
        text = button.add_child(UI_Text)
        text.text = "End Turn"

    def add_game_object(self, game_object: Game_object) -> None:
        if not issubclass(game_object.__class__, Game_object):
            print("ERROR: Do not add non Game Object derived objects as Game objects")
            return
        self.game_objects.append(game_object)

    def process_input(self):
        self.input_manager.process_input()

    def on_quit(self, eventdata):
        self.running = False

    def on_key_down(self, eventdata):
        self.turn_manager.move(eventdata.key)

    def on_end_turn(self, eventdata):
        self.turn_manager.change_player()

    def update(self, delta_time):
        for game_object in self.game_objects:
            game_object.update(delta_time)

        self.turn_manager.update(delta_time)

    def draw(self, delta_time):
        self.display_surface.fill(BG_COLOR)

        for game_object in self.game_objects:
            game_object.draw(delta_time)

        self.current_stage.draw()
        self.turn_manager.players.draw(self.display_surface)

        pygame.display.update()

    def initialise_game(self):
        self.running = True

    def shutdown(self):
        pygame.quit()
        sys.exit()

    def run(self):
        self.initialise_game()

        while self.running:
            delta_time = self.clock.tick(FPS) / 1000

            self.process_input()
            self.update(delta_time)
            self.draw(delta_time)

        self.shutdown()


if __name__ == "__main__":
    game = Game()
    game.run()
