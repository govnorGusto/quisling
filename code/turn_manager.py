from settings import *
from player import Player
from actions import MoveAction


class Turn_Manager:
    def __init__(self) -> None:
        self.selected_player = 0
        self.player_list = []

        self.displaying_moves = False
        self.current_round = 0

    def get_current_player(self):
        return self.player_list[self.selected_player]
    
    def get_players(self):
        """add list of players"""
        x = 0
        y = 0
        for i in range(PLAYER_AMOUNT):
            p = Player(x, y, i)
            self.player_list.append(p)

    def move(self, key):
        """manage moves for all players"""
        if (
            self.player_list[self.selected_player].number_of_moves
            < self.player_list[self.selected_player].max_moves
        ):
            dx, dy = 0, 0

            if key == pygame.K_LEFT:
                dx = -TILESIZE
                self.player_list[self.selected_player].record_move(-TILESIZE, dy)
            elif key == pygame.K_RIGHT:
                dx = TILESIZE
                self.player_list[self.selected_player].record_move(TILESIZE, dy)
            elif key == pygame.K_UP:
                dy = -TILESIZE
                self.player_list[self.selected_player].record_move(dx, -TILESIZE)
            elif key == pygame.K_DOWN:
                dy = TILESIZE
                self.player_list[self.selected_player].record_move(dx, TILESIZE)

            if dx != 0 or dy != 0:
                MoveAction(self.player_list[self.selected_player], dx, dy)
                self.player_list[self.selected_player].number_of_moves += 1

    def change_player(self):
        """change player and triggers action round"""
        self.player_list[self.selected_player].reset_position()
        if self.selected_player < PLAYER_AMOUNT - 1:
            self.selected_player += 1
        else:
            self.selected_player = 0
            self.displaying_moves = True

    def apply_all_moves(self):
        """make all the players moves at the same time"""
        if self.current_round < max([p.max_moves for p in self.player_list]):
            self.current_round += 1
            for player in self.player_list:
                try:
                    dx, dy = player.recorded_moves[self.current_round]
                    MoveAction(player, dx, dy)
                except:
                    continue
        else:
            for player in self.player_list:
                player.reset_round()
            self.current_round = 0
            self.displaying_moves = False

    def update(self, delta_time):
        if self.displaying_moves:
            self.apply_all_moves()
        
    def get_current_player(self):
        return self.player_list[self.selected_player]
