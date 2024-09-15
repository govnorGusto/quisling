from settings import *
from level.level import Level
from turn_manager import Turn_Manager
from button import Button

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("the quisling project")
        self.current_stage = Level()
        self.running = True

        self.turn_manager = Turn_Manager()
        self.button = Button(WINDOW_WIDTH - 100,
                             WINDOW_HEIGHT - 70, "NEXT")

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.turn_manager.move(event.key)

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

            self.events()
            self.update(dt)
            self.draw(dt)

            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
