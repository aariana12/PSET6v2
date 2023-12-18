from Player import Player

class HeuristicPlayer(player):
    def __init__(self, player_type, workers, color, board):
        super().__init__(player_type, workers, color, board)
        self.player_type = "heuristic"

    def get_worker(self):
        pass

    def get_move_direction(self, worker):
        pass

    def get_build_direction(self, worker):
        pass
