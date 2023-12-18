from players.Player import Player

class HumanPlayer(Player):

    def __init__(self, player_type, workers, board):
        super().__init__(player_type, workers, board)
        self.player_type = "human"

    def get_worker(self):
        while True:
            selected_worker = input("Select a worker to move\n")
            if selected_worker not in self.valid_workers:
                print("Not a valid worker")
            elif selected_worker not in self.workers:
                print("This is not your worker")
            elif not self.has_moves(selected_worker):
                print("There are no possible moves for this worker")
            return selected_worker

    def get_move_direction(self, worker):
        while True:
            selected_direction = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n")
            if selected_direction not in self.valid_directions:
                print("Not a valid direction.")
            elif self.board.is_valid_direction(worker, selected_direction):
                print(f"This worker is unable to move to {select_direction}")
            return selected_direction

    def get_build_direction(self, worker):
        while True:
            selected_build = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)\n")
            if selected_build not in self.valid_directions:
                print("Not a valid build direction.")
            elif not self.board.is_valid_direction(worker, selected_build):
                print(f"This worker is unable to build to {selected_build}")
            return selected_build

