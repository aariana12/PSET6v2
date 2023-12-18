from Board import Board
import copy
from copy import deepcopy
from players.HumanPlayer import HumanPlayer
# from players.HeuristicPlayer import HeuristicPlayer
from players.RandomPlayer import RandomPlayer


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
        self.history_index = 0 # TODO weird behavior - better when -1
        # when 0, undo weird 
       

    def display_score(self, player):
        # player = self.players[self.curr_player]
        opp_player = self.players[1 - self.curr_player]
        # score_str = ''
        if self.score:
            height = player.height_score(player)
            center = player.center_score(player)
            distance = player.distance_score(opp_player, player)
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
        score_str = self.display_score(self.players[self.curr_player])
        print(f"Turn: {self.turn_count}, {player_str} {score_str}")

    def undo_redo_command(self):
        
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
        for player in self.players:
                player.workers = self.board.make_board(player.color)

    def make_player(self, player_type, color, workers):
        if player_type == 'human':
            return HumanPlayer(player_type, workers, color, self.board)
        elif player_type == 'heuristic':
            return HeuristicPlayer(player_type, workers, color, self.board)
        elif player_type == 'random':
            return RandomPlayer(player_type, workers, color, self.board)

    def make_moves(self):
        while True:
            self.board.display()
            self.display_turn_str()
            if not self.undo_redo_command():
                curr_player = self.players[self.curr_player]
                selected_worker = curr_player.get_worker()
                selected_direction = curr_player.get_move_direction(selected_worker)
                selected_build = curr_player.get_build_direction(selected_worker, selected_direction)
                print("selected:", selected_worker, selected_direction, selected_build)

                self.board.iliketomoveitmoveit(selected_worker, selected_direction)
                self.board.bobthebuilder(selected_worker, selected_build)
                actual_score = self.display_score(curr_player)
                print(f'{selected_worker, selected_direction, selected_build} {actual_score}')
                
                # Save memento after the player has completed their turn
                self.save_memento()

                # Increment turn count after the player has completed their turn
                self.turn_count += 1
                self.switch_players()
            curr_player = self.players[self.curr_player]
            selected_worker = curr_player.get_worker()
            selected_direction = curr_player.get_move_direction(selected_worker)
            selected_build = curr_player.get_build_direction(selected_worker, selected_direction)
            
            self.board.iliketomoveitmoveit(selected_worker, selected_direction)
            self.board.bobthebuilder(selected_worker, selected_build)
            actual_score = self.display_score(curr_player)
            formatted_move = ','.join([selected_worker, selected_direction, selected_build])

            print(f"{formatted_move} {actual_score}")

    
            
            
            # print (f'{selected_worker, selected_direction,selected_build} {actual_score}')
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

    # def check_game_state(self):
    #     if self.turn_count > 1:
    #         winner = self.has_won()
    #         if winner:
    #             print(winner)
    #             play = input("Play again?\n")
    #             if play.lower() == "yes":


    # def play_again(self):
    #     """
    #     re-initialize everything back to what it was originally
    #     """
    #     self.board = Board
    #     self.turn_count = 1
    #     self.move_history = []
    #     self.history_index = -1


    def undo(self):
        if self.history_index > 0:
            self.history_index -= 1
            self.turn_count -= 1
            self.memento(self.move_history[self.history_index])
            self.switch_players()
            # TODO - can't go all the way back to og position

    def redo(self):
        if self.history_index < len(self.move_history) - 1:
            self.history_index += 1
            self.turn_count += 1
            self.memento(self.move_history[self.history_index])
            self.switch_players()

    def save_memento(self):
        self.move_history = self.move_history[:self.history_index + 1]
        # Create a memento (Originator)
        self.move_history.append((copy.deepcopy(self.board), copy.deepcopy(self.players), self.curr_player, self.turn_count))
        self.history_index += 1

    def memento(self, return_move):
        self.board, self.players, self.curr_player, self.state = return_move







