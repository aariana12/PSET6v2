from players.HumanPlayer import HumanPlayer
from players.HeuristicPlayer import HeuristicPlayer
from players.HeuristicPlayer import HeuristicPlayer
from players.RandomPlayer import RandomPlayer

class PlayerFactory:
    """
    Player Factory class that manages the players
    """

    def make_player(self, player_type, color, workers, board):
        """
        method that initializes the player type
        """
        if player_type == 'human':
            return HumanPlayer(player_type, workers, color, board)
        elif player_type == 'heuristic':
            return HeuristicPlayer(player_type, workers, color, board)
        elif player_type == 'random':
            return RandomPlayer(player_type, workers, color, board)