from players.Player import Player

class HumanPlayer(Player):
    """
    Child class of Player that inherits template methods to get worker, direction, and build from the command line
    """
    def __init__(self, player_type, workers, color, board):
        super().__init__(player_type, workers, color, board)
        self.player_type = "human"

    def get_worker(self):
        """
        method to get worker from command line
        """
        while True:
            selected_worker = input("Select a worker to move\n")
            worker_names = [worker[0] for worker in self.workers]
            if selected_worker not in worker_names:
                print("Not a valid worker")
            elif not self.has_moves(selected_worker):
                print("That worker cannot move")
            else:
                return selected_worker


    def get_move_direction(self, worker):
        """
        method to get move direction from command line
        """
        while True:
            selected_direction = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n")
            direction = self.board.DIRECTIONS[selected_direction]
            if selected_direction not in self.board.DIRECTIONS.keys():
                print("Not a valid direction.")
            elif not self.board.is_valid_direction(worker, direction):
                print(f"This worker is unable to move to {selected_direction}")
            else:
                return selected_direction

    def get_build_direction(self, worker, move_direction):
        """
        method to get build direction from command line
        """
        while True:
            selected_build = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)\n")
            build = self.board.DIRECTIONS[selected_build]
            if selected_build not in self.board.DIRECTIONS.keys():
                print("Not a valid build direction.")
            elif not self.board.is_valid_build(worker, move_direction, build):
                print(f"This worker is unable to build to {selected_build}")
            else:
                return selected_build

