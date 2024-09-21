import random
from settings import *
from turn_manager import Turn_Manager
from core.message_router import Message_Router
from core.input_manager import Input_Manager
from core.game_object import Game_object
from resolve import Resolve
from audio.audio import *

from ui.ui_manager import *

from core.grid import Grid
from controller import Controller

from ui.ui_manager import construct_ui_element
from ui.ui_definitions import UI_NEXT_BUTTON

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Animies - the quisling project")

        self.message_router = Message_Router()
        self.game_objects: [Game_object] = []
        self.input_manager = Input_Manager(self)
        self.selected_map = ""
        self.game_over = False
        
        self.message_router.register_callback(pygame.QUIT, self.on_quit)
        self.message_router.register_callback("GameOver", self.on_game_over)

    def add_game_object(self, game_object: Game_object) -> None:
        if not issubclass(game_object.__class__, Game_object):
            print("ERROR: Do not add non Game Object derived objects as Game objects")
            return
        self.game_objects.append(game_object)
        
    def delete_game_object(self, game_object):
        self.game_objects.remove(game_object)
        del game_object

    def process_input(self):
        self.input_manager.process_input()

    def on_quit(self, eventdata=0):
        self.running = False

    def on_end_turn(self, eventdata):
        self.turn_manager.change_player()
        
    def on_game_over(self, losing_player_index : int):
        self.game_over = True
        make_game_over_menu(self.on_quit, losing_player_index)

    def update(self, delta_time):
        to_delete = []
        
        for game_object in self.game_objects:
            game_object.update(delta_time)
            if game_object.is_garbage:
                to_delete.append(game_object)

        for game_object in to_delete:
            self.game_objects.remove(game_object)
            del game_object
                
    def draw(self, delta_time):
        self.display_surface.fill(BG_COLOR)

        for game_object in self.game_objects:
            game_object.draw(delta_time)

        pygame.display.update()
        
    def set_random_map(self):
        self.selected_map = random.choice(MAP_PATHS)

    def set_map(self, index : int):
        if index >= len(MAP_PATHS):
            self.selected_map = MAP_PATHS[0]
        self.selected_map = MAP_PATHS[index]

    def initialise_game(self, map_index : int):
        self.level_select_canvas.mark_for_delete()
        self.grid = Grid()
        self.turn_manager = Turn_Manager()
        self.controller = Controller()
        self.audio_player = Audio_player()
        UI_Manager()
        self.set_map(map_index)
        self.grid.load_tmx(self.selected_map)
        self.turn_manager.get_players()
        self.audio_player.play_music()
        self.game_over = False

    def shutdown(self):
        pygame.quit()
        sys.exit()

    def run(self):
        self.running = True
        total_runtime = 0
        
        self.level_select_canvas = make_level_select_screen(LEVEL_NAMES, self.initialise_game)
        
        while self.running:
            delta_time = self.clock.tick(FPS) / 1000

            self.process_input()
            self.update(delta_time)
            self.draw(delta_time)

        self.shutdown()

if __name__ == "__main__":
    game = Game()
    game.run()
