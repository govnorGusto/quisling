from settings import *
from core.game_object import Game_object

class Grid(Game_object):
    def __init__(self):
        super().__init__()

        self.map = [[[] for _ in range(int(GRID_HEIGHT))] for _ in range(int(GRID_WIDTH))]
        self.objects_positions = {}


    def add(self, obj, x, y):
        self.map[x][y].append(obj)
        self.objects_positions[obj] = (x, y)

    def remove(self, obj, x, y):
        if obj in self.map[x][y]:
            self.map[x][y].remove(obj)
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
        


