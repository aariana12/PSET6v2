from Board import Board

class Player:
    def __init__(self, player_type, color, workers, board):
        self.player_type = player_type # ex: human
        self.workers = workers # ex: [A,B]
        self.color = color # ex: white
        self.board = board 
        # self.valid_directions = {'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw'}

    
    def get_worker(self):
        raise NotImplementedError()
    
    def get_move_direction(self, worker):
        raise NotImplementedError()

    def get_build_direction(self, worker):
        raise NotImplementedError()

    def has_moves(self, worker):
        for direction in self.board.DIRECTIONS.values():
            print(worker[0],direction[0])
            selected_dir = (worker[1] + direction[0], worker[0] + direction[1])
            if self.board.is_valid_direction(worker, selected_dir):
                return True
        return False

    def valid_directions(self, worker):
        """
        returns an array of valid moves for that worker
        """
        valid_directions = []
        for direction in self.board.DIRECTIONS.keys():
            row, column = self.board.DIRECTION[direction]
            selected_dir = (worker[1] + row, worker[2] + column)
            if self.board.is_valid_direction(worker, selected_dir):
                valid_directions.append(select_dir)
        return valid_directions


    def valid_builds(self, worker):
        """
        returns an array of valid builds for that worker
        """

    def height_score(self):
        return 202
        pass
        
    def center_score(self):
        return 12
        pass
    def distance_score(self):
        return 12
        pass