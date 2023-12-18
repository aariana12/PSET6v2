from players.Player import Player
import random

class RandomPlayer(Player):
    def __init__(self, player_type, workers, color, board):
        super().__init__(player_type, workers, color, board)
        self.player_type = "random"

    def get_worker(self):
        worker_choice = random.choice(self.workers)
        return worker_choice[0]

    def get_move_direction(self, worker):

        dir =  random.choice(self.valid_directions(worker))
        print("random move", dir)
        return dir

    def get_build_direction(self, worker, moved_direction): # worker replaced by move_direction

        return random.choice(self.valid_builds(worker, moved_direction))
