from settings import *
from core.game_object import Game_object
from core.tile import Tile
from pytmx.util_pygame import load_pygame


class Cell(Game_object):
    def __init__(self) -> None:
        super().__init__()
        self.tile: Tile = None
        self.occupants = []

    def __repr__(self) -> str:
        return f"{[obj for obj in self.occupants]}"

    def draw_cell(self):
        if self.tile:
            img = pygame.transform.scale(
                self.tile.image,
                (self.game.grid.tile_width * SCALE, self.game.grid.tile_width * SCALE),
            )
            img.set_colorkey(BG_COLOR)
            self.game.display_surface.blit(img, self.tile.rect)

    def on_draw(self, delta_time: float):
        pass


class Grid(Game_object):
    def __init__(self):
        super().__init__()
        self.objects_positions = {}
        self.map = []

    def load_tmx(self, tmx_file):
        try:
            tmx_data = load_pygame(tmx_file)
        except:
            print("Failed to load tmx")

        self.width = tmx_data.width
        self.height = tmx_data.height
        self.tile_width = tmx_data.tilewidth
        self.tile_height = tmx_data.tileheight
        self.map = [[Cell() for _ in range(self.height)] for _ in range(self.width)]

        invalid_spawns = []

        print((self.width, self.height))

        for x, y, surf in tmx_data.get_layer_by_name("base").tiles():
            self.map[y][x].tile = Tile(self.grid_to_screen(y, x), surf, False)
            invalid_spawns.append((x, y))

        for x, y, surf in tmx_data.get_layer_by_name("ground").tiles():
            self.map[y][x].tile = Tile(self.grid_to_screen(y, x), surf, True)

        return invalid_spawns

    def add(self, obj, x, y):
        self.map[x][y].occupants.append(obj)
        self.objects_positions[obj] = (x, y)

    def remove(self, obj, x, y):
        if obj in self.map[x][y].occupants:
            self.map[x][y].occupants.remove(obj)
        if obj in self.objects_positions:
            del self.objects_positions[obj]

    def move(self, obj, dx, dy):
        if obj not in self.objects_positions:
            raise ValueError("Object is not in the grid")

        if self.in_bounds(dx, dy):
            current_x, current_y = self.objects_positions[obj]
            self.remove(obj, current_x, current_y)
            self.add(obj, dx, dy)

    def in_bounds(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return True
        else:
            self.game.message_router.broadcast_message("BadMove")
            return False

    def query_objects(self, objects: list) -> dict:
        results = {}
        for obj in objects:
            if obj in self.objects_positions:
                results[obj] = self.objects_positions.get(obj)
            else:
                print("No object found: " + obj)

        if not results:
            print("No results")
            return False
        return results

    def query_positions(self, positions: list):
        results = {}
        for pos in positions:
            if self.map[pos[0]][pos[1]].occupants:
                results[f"{pos}"] = [obj for obj in self.map[pos[0]][pos[1]].occupants]
            else:
                print("No object found at: " + str(pos))

        if not results:
            print("No results")
            return False
        return results

    def grid_to_screen(self, grid_x: int, grid_y: int):
        cell_width = self.tile_width
        cell_height = self.tile_height

        x_offset = pygame.Vector2(cell_width, -cell_height)
        y_offset = pygame.Vector2(cell_width, cell_height)
        origin = pygame.Vector2(GRID_X_ORIGIN, GRID_Y_ORIGIN)

        loc = origin + x_offset * grid_x + y_offset * grid_y
        return (loc.x, loc.y)

    def on_draw(self, delta_time: float):
        self.width
        self.height
        for x in range(self.width - 1, -1, -1):
            for y in range(self.height):
                self.map[x][y].draw_cell()