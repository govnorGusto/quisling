from settings import *
from core.game_object import Game_object
from core.tile import Tile
from pytmx.util_pygame import load_pygame


class Cell:
    def __init__(self) -> None:
        self.tile: Tile = None
        self.occupants = []

    def __repr__(self) -> str:
        return f"{[obj for obj in self.occupants]}"


class Grid(Game_object):
    def __init__(self):
        super().__init__()
        self.objects_positions = {}

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

        for x, y, surf in tmx_data.get_layer_by_name("base").tiles():
            self.map[x][y].tile = Tile(x, y, surf, False)
        for x, y, surf in tmx_data.get_layer_by_name("ground").tiles():
            self.map[x][y].tile = Tile(x, y, surf, True)

    def add(self, obj, x, y):
        self.map[x][y].occupants.append(obj)
        self.objects_positions[obj] = (x, y)

    def on_draw(self, delta_time: float):
        surf = pygame.display.get_surface()
        color = (255, 0, 255)
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                surface_to_draw = pygame.image.load(
                    join(
                        "graphics",
                        "isometric tileset",
                        "separated images",
                        "tile_003.png",
                    )
                ).convert()
                surface_to_draw.set_colorkey(BG_COLOR)
                
                surface_to_draw = pygame.transform.scale(surface_to_draw, (self.tile_width * SCALE, self.tile_width * SCALE))
                
                draw_pos = self.grid_to_screen(x, y)
                rect_to_draw = pygame.Rect(draw_pos, (self.tile_width, self.tile_height))
                surf.blit(surface_to_draw, rect_to_draw)
                surf.set_at(draw_pos, color)

    def remove(self, obj, x, y):
        if obj in self.map[x][y].occupants:
            self.map[x][y].occupants.remove(obj)
        if obj in self.objects_positions:
            del self.objects_positions[obj]

    def move(self, obj, dx, dy):
        if obj not in self.objects_positions:
            raise ValueError("Object is not in the grid")

        current_x, current_y = self.objects_positions[obj]

        new_x = current_x + dx
        new_y = current_y + dy

        if self.in_bounds(new_x, new_y):
            self.remove(obj, current_x, current_y)
            self.add(obj, new_x, new_y)

    def in_bounds(self, x, y):
        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            return True
        else:
            print("Invalid move: Out of grid bounds")
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

        x_offset = pygame.Vector2( -cell_width, cell_height)
        y_offset = pygame.Vector2(cell_width, cell_height)
        origin = pygame.Vector2(GRID_X_ORIGIN, GRID_Y_ORIGIN)

        loc = origin + x_offset * grid_x + y_offset * grid_y
        return (loc.x, loc.y)
