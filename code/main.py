from settings import *
from turn_manager import Turn_Manager
from core.message_router import Message_Router
from core.input_manager import Input_Manager
from core.game_object import Game_object

from ui.ui_button import UI_Button
from ui.ui_text import UI_Text
from ui.uicore.ui_canvas import UI_Canvas

from core.grid import Grid
from controller import Controller

from ui.ui_manager import construct_ui_element
from ui.ui_definitions import UI_NEXT_BUTTON


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("the quisling project")

        self.game_objects: [Game_object] = []
        self.input_manager = Input_Manager(self)
        self.grid = Grid()
        self.turn_manager = Turn_Manager()
        self.message_router = Message_Router()
        self.controller = Controller()

        self.message_router.register_callback(pygame.QUIT, self.on_quit)

        ### TEMP BUTTON ###
        self.button_canvas = UI_Canvas(
            pygame.Rect(WINDOW_WIDTH - 220, WINDOW_HEIGHT - 120, 200, 100)
        )
        self.button_canvas.color = (100, 100, 100)
        button = self.button_canvas.add_child(UI_Button)
        button.click_callbacks.append(self.turn_manager.change_player)
        text = button.add_child(UI_Text)
        text.text = "End Turn"
        ### TEMP BUTTON END ###

        # construct_ui_element(UI_NEXT_BUTTON)

    def add_game_object(self, game_object: Game_object) -> None:
        if not issubclass(game_object.__class__, Game_object):
            print("ERROR: Do not add non Game Object derived objects as Game objects")
            return
        self.game_objects.append(game_object)

    def process_input(self):
        self.input_manager.process_input()

    def on_quit(self, eventdata):
        self.running = False

    def on_end_turn(self, eventdata):
        self.turn_manager.change_player()

    def update(self, delta_time):
        for game_object in self.game_objects:
            game_object.update(delta_time)


    def draw(self, delta_time):
        self.display_surface.fill(BG_COLOR)

        for game_object in self.game_objects:
            game_object.draw(delta_time)

        pygame.display.update()

    def initialise_game(self):
        self.running = True
        self.grid.load_tmx(join("graphics", "tmx", "level_test.tmx"))
        # self.grid.load_tmx(join("graphics", "tmx", "grass.tmx"))
        self.turn_manager.get_players()

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
