from Board import Board
from abc import ABC, abstractmethod

class Player:
    def __init__(self, player_type, color, workers, board):
        self.player_type = player_type # ex: human
        self.workers = workers # ex: [A,B]
        self.color = color # ex: white
        self.board = board 
        # self.valid_directions = {'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw'}

    @abstractmethod
    def get_worker(self):
        raise NotImplementedError()
    
    @abstractmethod
    def get_move_direction(self, worker):
        raise NotImplementedError()

    @abstractmethod
    def get_build_direction(self, worker, direction):
        raise NotImplementedError()

    def has_moves(self, worker):
        # TODO get position of a worker 
        for direction in self.board.DIRECTIONS.values():
            position = self.board.worker_position(worker)
            # selected_dir = (position[0] + direction[0], position[1] + direction[1])
            selected_dir =(direction[0], direction[1])
            if self.board.is_valid_direction(worker, selected_dir):
                return True
        return False

    def valid_directions(self, worker):
        """
        returns an array of valid moves for that worker
        """
        valid_directions = []
        for direction in self.board.DIRECTIONS.keys():
            selected_dir = self.board.DIRECTIONS[direction]
            worker_pos = self.board.worker_position(worker[0])
            if self.board.is_valid_direction(worker[0], selected_dir):
                valid_directions.append(direction)
        print("valid direction array", valid_directions)
        return valid_directions

    def valid_builds(self, worker, build_direction):
        """
        returns an array of valid builds for that worker
        """
        print("instead valid builds")
        valid_builds = []
        for direction in self.board.DIRECTIONS.keys():
            
            selected_dir = self.board.DIRECTIONS[direction]
            
            # print("valid buids selected dir", selected_dir)
            if self.board.is_valid_direction(worker[0], selected_dir):
                valid_builds.append(direction)
        return valid_builds

    def height_score(self):
        pass
    def center_score(self):
        pass
    def distance_score(self):
        pass