from settings import *
from level.walls import Walls


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.walls = pygame.sprite.Group()

        self.read_map()
        self.generate_map()

    def read_map(self):
        self.map_data = []
        with open(path.join(path.dirname(__file__), 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def generate_map(self):
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == 'w':
                    self.walls.add(Walls(col, row))

    def wall_collision(self, dx, dy):
        pass

    def draw(self):
        self.display_surface.fill(BG_COLOR)
        for x in range(0, WINDOW_WIDTH, TILESIZE):
            pygame.draw.line(self.display_surface, GRID_COLOR,
                             (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, TILESIZE):
            pygame.draw.line(self.display_surface, GRID_COLOR,
                             (0, y), (WINDOW_WIDTH, y))
        self.walls.draw(self.display_surface)

