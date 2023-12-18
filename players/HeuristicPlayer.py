from Player import Player

class RandomPlayer(player):
    def __init__(self):
        super().__init__(self.player_type, self.workers, self.board,)
        self.player_type = "heuristic"
