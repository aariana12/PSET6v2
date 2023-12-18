from Board import Board

class Player:
    def __init__(self, player_type, workers, board):
        self.player_type = player_type
        self.workers = workers
        self.board = board
        self.valid_workers = {'A', 'B', 'Y', 'Z'}
        self.valid_directions = {'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw'}

    
    def get_worker(self):
        raise NotImplementedError()
    
    def get_move_direction(self, worker):
        raise NotImplementedError()

    def get_build_direction(self):
        raise NotImplementedError()

    def has_moves(self, worker):
        pass
        # TODO

    def height_score(self):
        pass
    def center_score(self):
        pass
    def distance_score(self):
        pass