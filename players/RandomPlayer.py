from players.Player import Player
import random

class RandomPlayer(Player):
    """
    Child class of Player that inherit template methods to randomly get worker, move direction, and build direction
    """
    def __init__(self, player_type, workers, color, board):
        super().__init__(player_type, workers, color, board)
        self.player_type = "random"

    def get_worker(self):
        """
        method to randomly get worker
        """
        worker_choice = random.choice(self.workers)
        return worker_choice[0]

    def get_move_direction(self, worker):
        """
        method to randomly get move direction
        """
        return random.choice(self.valid_directions(worker))

    def get_build_direction(self, worker, moved_direction): 
        """
        method to randomly get build direction
        """
        return random.choice(self.valid_builds(worker, moved_direction))
