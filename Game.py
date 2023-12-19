from Board import Board
import copy
from copy import deepcopy
from players.Player import Player
from players.PlayerFactory import PlayerFactory
from players.HumanPlayer import HumanPlayer
from players.HeuristicPlayer import HeuristicPlayer
from players.HeuristicPlayer import HeuristicPlayer
from players.RandomPlayer import RandomPlayer



class Santorini:
    """
    Singleton game class that create one instance of the game Santorini
    """
    _instance = None

    # Singleton getInstance method
    @classmethod
    def getInstance(cls, white_type, blue_type, undo_redo=False, score=False):
        if cls._instance is None:
            cls._instance = cls(white_type, blue_type, undo_redo, score)
        return cls._instance


    def __init__(self, white_type, blue_type, undo_redo=False, score=False):
        if self._instance is not None:
            raise Exception("This class is a singleton!")

        self.board = Board()
        self.player_factory = PlayerFactory()
        self.players = [Player(None, None, None, None) for _ in range(2)]
        self.players[0] = self.player_factory.make_player(white_type, ['A', 'B'], "white", self.board)
        self.players[1] = self.player_factory.make_player(blue_type, ['Y', 'Z'], "blue", self.board)

        self.undo_redo = undo_redo
        self.score = score
        # self.players = [self.make_player(white_type, ['A', 'B'], "white"),
                        # self.make_player(blue_type, ['Y', 'Z'], "blue")]
        self.turn_count = 1
        self.curr_player = 0
        self.move_history = []
        self.history_index = -1

    def display_score(self, player):
        """ 
        method that displays the current score
        """
        opp_player = self.players[1 - self.curr_player]
        if self.score:
            height = player.height_score(player)
            center = player.center_score(player)
            distance = player.distance_score(opp_player, player)
            score_str = f'({height}, {center}, {distance})'
            return score_str
        else:
            return ''
    
    def display_turn_str(self):
        """
        method that displays the turn string
        """
        player = self.players[self.curr_player].color
        player_str = ''
        if player == "white":
            player_str = "white (AB)"
        else:
            player_str = "blue (YZ)"
        score_str = self.display_score(self.players[self.curr_player])
        print(f"Turn: {self.turn_count}, {player_str} {score_str}")

    def undo_redo_command(self):
        """
        method that manages the undo redo commands
        """
        while self.undo_redo:
            command = input("undo, redo, or next\n")
            if command == "undo":
                self.undo()
                return True
            elif command == "redo":
                self.redo()
                return True
            elif command == "next":
                return False
            else:
                print("Invalid action. Please enter undo, redo, or next.")

    def initialize_board(self):
        """
        method that initalizes the players on the board
        """
        for player in self.players:
                player.workers = self.board.make_board(player.color)
        self.save_memento()

    # def make_player(self, player_type, color, workers):
    #     """
    #     method that initializes the player type
    #     """
    #     if player_type == 'human':
    #         return HumanPlayer(player_type, workers, color, self.board)
    #     elif player_type == 'heuristic':
    #         return HeuristicPlayer(player_type, workers, color, self.board)
    #     elif player_type == 'random':
    #         return RandomPlayer(player_type, workers, color, self.board)

    def make_moves(self):
        """
        method that displays board, turn, score, and the undo/redo, get worker, get direction, and get build direction prompt. It moves the worker and executes a build. It checks if the player has won and stores the state of the board in an array of deepcopies
        """
        while True:
            self.board.display()
            self.display_turn_str()
            if not self.undo_redo_command():
                curr_player = self.players[self.curr_player]
                selected_worker = curr_player.get_worker()
                selected_direction = curr_player.get_move_direction(selected_worker)
                selected_build = curr_player.get_build_direction(selected_worker, selected_direction)
                self.board.iliketomoveitmoveit(selected_worker, selected_direction)
                self.board.bobthebuilder(selected_worker, selected_build)
                actual_score = self.display_score(curr_player)
                # print(f'{selected_worker[0], selected_direction[0], selected_build[0]} {actual_score}')
                print(f"{selected_worker[0]},{selected_direction[0]},{selected_build[0]} {actual_score}")
                
                # Save memento after the player has completed their turn
                self.save_memento()
                # Increment turn count after the player has completed their turn
                self.turn_count += 1

                # check has won & play again
                self.switch_players()
                if self.check_game_state():
                    self.play_again()
                    self.initialize_board()
                    continue


    def switch_players(self):
        """
        method that switches the current player
        """
        self.curr_player =  1 - self.curr_player

    def has_won(self):
        """
        method that checks if there is a winner 
        """
        winner = False
        for player in self.players:
            for worker in player.workers:
                
                if self.board.cells[worker[1]][worker[2]]['height'] == 3:
                    winner = True
                    return f"{player.color} has won"

                if not player.has_moves(worker[0]):
                    winner = True
                    return f"{self.players[self.switch(self.curr_player)].color} has won"
        return winner

    def check_game_state(self):
        """
        method that checks the game status and prompts play again if there is a winner
        """
        if self.turn_count > 1:
            winner = self.has_won()
            if winner:
                print(winner)
                play = input("Play again?\n")
                if play.lower() == "yes":
                    self.play_again()



    def play_again(self):
        """
        method that re-initialize everything back to what it was originally if player wants to replay again
        """
        # self.board = Board
        # self.turn_count = 1
        # self.move_history = []
        # self.history_index = -1
        self.board = Board()
        for i, player in enumerate(self.players):
            player_type = 'heuristic' if isinstance(player, HeuristicAI) else 'random' if isinstance(player, RandomAI) else 'human'
            self.players[i] = self.make_player(player_type, player.color, ['A', 'B'] if player.color == 'white' else ['Y', 'Z'], self)
        self.curr_player = 0
        self.turn_count = 1


    def undo(self):
        """
        method that undoes the previous move
        """
        if self.history_index > 0:
            self.history_index -= 1
            self.turn_count -= 1
            self.memento(self.move_history[self.history_index])
            # TODO - can't go all the way back to og position

    def redo(self):
        """
        method that redoes the previous move
        """
        if self.history_index < len(self.move_history) - 1:
            self.history_index += 1
            self.turn_count += 1
            self.memento(self.move_history[self.history_index])

    def save_memento(self):
        """
        method that create the originator/memento
        """
        self.move_history = self.move_history[:self.history_index + 1]
        self.move_history.append((copy.deepcopy(self.board), copy.deepcopy(self.players), self.curr_player, self.turn_count))
        self.history_index += 1

    def memento(self, return_move):
        """
        method that loads the state of the board saved by the memento
        """
        self.board, self.players, self.curr_player, self.state = return_move







