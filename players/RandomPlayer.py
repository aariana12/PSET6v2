from Player import player
import random

class RandomPlayer(player):
    def __init__(self):
        super().__init__(self.player_type, self.workers, self.board,)
        self.player_type = "random"

        def get_worker(self):
            return random.choice(self.workers)

        def get_move_direction(self, worker):
            return random.choice(self.valid_directions(worker))

        def get_build_direction(self, move_direction):
            return random.choice(self.valid_directions(move_direction))
