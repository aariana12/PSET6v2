from players.Player import Player
import random

class RandomPlayer(Player):
    def __init__(self, player_type, workers, color, board):
        super().__init__(player_type, workers, color, board)
        self.player_type = "random"

    def get_worker(self):
        print("random worker", random.choice(self.workers))
        worker_choice = random.choice(self.workers)
        return worker_choice[0]

    def get_move_direction(self, worker):
        # print("random worker", worker)

        dir =  random.choice(self.valid_directions(worker))
        print("random move", dir)
        return dir

    def get_build_direction(self, worker, move_direction): # worker replaced by move_direction
        print("random builds", random.choice(self.valid_builds(worker, move_direction)))
        return random.choice(self.valid_builds(worker, move_direction))
