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
        self.undo_redo = undo_redo
        self.score = score
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

    def display_score(self):
        player = self.players[self.curr_player]
        # score_str = ''
        if self.score:
            height = player.height_score()
            center = player.center_score()
            distance = player.distance_score()
            score_str = f'({height}, {center}, {distance})'
            return score_str
        else:
            return ''
    
    def display_turn_str(self):
        player = self.players[self.curr_player].color
        player_str = ''
        if player == "white":
            player_str = "white (AB)"
        else:
            player_str = "blue (YZ)"
        score_str = self.display_score()
        print(f"Turn: {self.turn_count}, {player_str} {score_str}")

    def undo_redo_command(self):
        if self.undo_redo:
            command = input("undo, redo, or next\n")
            if command == "undo":
                self.undo()
            elif command == "redo":
                self.redo()
            elif command == "next":
                pass
            else:
                print("Invalid action. Please enter undo, redo, or next.")

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
        self.display_turn_str()
        self.undo_redo_command()
        self.turn_count += 1



        curr_player = self.players[self.curr_player]
        selected_worker = curr_player.get_worker()
        selected_direction = curr_player.get_move_direction(selected_worker)
        selected_build = curr_player.get_build_direction(selected_worker, selected_direction)
        
        self.board.iliketomoveitmoveit(selected_worker, selected_direction)
        self.board.bobthebuilder(selected_worker, selected_build)
        self.switch_players()

    def switch_players(self):
        self.curr_player =  1 - self.curr_player

    def has_won(self):
        for player in self.players:
            for worker in player.workers:
                if self.board.grid[worker[0]][worker[1]]['height'] == 3:
                    return f"{player.color} has won"

                if not player.has_moves(worker):
                    return f"{self.players[self.switch(self.curr_player)].color} has won"
                else:
                    return False

    def check_game_state(self):
        if self.turn_count > 1:
            winner = self.has_won()
            if winner:
                print(winner)
                play = input("Play again?\n")
                if play.lower() == "yes":


    def play_again(self):
        """
        re-initialize everything back to what it was originally
        """
        self.board = Board
        self.turn_count = 1
        self.move_history = []
        self.history_index = -1

        # TODO 

        

        


    def undo(self):
        if self.history_index > 0:
            self.history_index -= 1
            self.memento(self.move_history[self.history_index])

    def redo(self):
        if self.history_index < len(self.move_history) - 1:
            self.history_index += 1
            self.memento(self.move_history[self.history_index])

    def save_memento(self):
        self.history = self.history[self.history_index + 1]
        self.history.append((copy.deepcopy(self.board), copy.deepcopy(self.players), self.curr_player, self.turn_count))
        self.history_index += 1

    def memento(self, return_move):
        self.board, self.players, self.curr_player, self.state = return_move







