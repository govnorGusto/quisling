from settings import *
from player import Player


class Turn_Manager:
    def __init__(self) -> None:
        self.selected_player = 0
        self.players = pygame.sprite.Group()
        self.player_list = []
        self.get_players()

        self.displaying_moves = False
        self.current_round = 0

    def get_players(self):
        """add list of players"""
        x = 5
        for i in range(PLAYER_AMOUNT):
            p = Player(x, 10, i)
            self.players.add(p)
            self.player_list.append(p)
            x += 5

    def move(self, key):
        """manage moves for all players"""
        if self.player_list[self.selected_player].number_of_moves \
                < self.player_list[self.selected_player].max_moves:

            self.player_list[self.selected_player].number_of_moves += 1

            if key == pygame.K_LEFT:
                self.player_list[self.selected_player].move(-TILESIZE, 0)
                self.player_list[self.selected_player].record_move(-TILESIZE, 0)
            if key == pygame.K_RIGHT:
                self.player_list[self.selected_player].move(TILESIZE, 0)
                self.player_list[self.selected_player].record_move(TILESIZE, 0)
            if key == pygame.K_UP:
                self.player_list[self.selected_player].move(0, -TILESIZE)
                self.player_list[self.selected_player].record_move(0, -TILESIZE)
            if key == pygame.K_DOWN:
                self.player_list[self.selected_player].move(0, TILESIZE)
                self.player_list[self.selected_player].record_move(0, TILESIZE)

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
                    player.move(*player.recorded_moves[self.current_round])
                except:
                    continue
        else:
            for player in self.player_list:
                player.reset_round()
            self.current_round = 0
            self.displaying_moves = False

    def update(self):
        if self.displaying_moves:
            self.apply_all_moves()
        self.players.update()
