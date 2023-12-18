from Board import Board
from copy import deepcopy
from players.HumanPlayer import HumanPlayer
# from players.HeuristicPlayer import HeuristicPlayer
# from players.RandomPlayer import RandomPlayer

class Santorini:
    """
    combines all classes to set up the Santorini game
    Singleton design pattern since we are creating one instance of the game that isopen
    to reference
    """
    def __init__(self, white_type, blue_type, undo_redo=False, score=False):
        self.board = Board()
        # pass in the type of player (human, heursitics, random)
        # self.white_type = white_type
        # self.blue_type = blue_type
        self.undo_redo_setting = undo_redo
        self.score_setting = score
        self.players = [self.make_player(white_type, ['A', 'B'], "white"), 
                        self.make_player(blue_type, ['Y', 'Z'], "blue")] # an array of type Player
        self.turn_count = 1
        self.curr_player = 0 # start with white
        self.move_history = [] # save ALL MOVES
        self.history_index = -1 
        # self.undo_history_index = -1
        # self._undo_history = [] # save all UNDOS
        # self._history_index = 0 # start at turn one, used to move thru the history array
        # redo --> moves index back 1 to get the previous history item, returns that item 


    def make_player(self, player_type, color, workers):
        if player_type == 'human':
            return HumanPlayer(player_type, workers, color, self.board)
        elif player_type == 'heuristic':
            return HeuristicPlayer(player_type, workers, color, self.board)
        else:  # player_type == 'random'
            return RandomPlayer(player_type, workers, color, self.board)

    def make_moves(self):
        for player in self.players:
            player.workers = self.board.setup_workers(player.color)
        self.board.display()

    def undo(self):
        if self.history_index > 0:
            self.history_index -= 1
            self.memento(self.move_history[self.history_index])

    def redo(self):
        if self.history_index < len(self.move_history) - 1:
            self.history_index += 1
            self.memento(self.move_history[self.history_index])

    def memento(self, move):
        self.board







