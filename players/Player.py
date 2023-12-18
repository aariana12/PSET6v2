from Board import Board
from abc import abstractmethod

class Player:
    """
    Abstract class for heuristic, human, and random player with template methods
    """
    def __init__(self, player_type, color, workers, board):
        self.player_type = player_type # ex: human
        self.workers = workers # ex: [A,B]
        self.color = color # ex: white
        self.board = board
        # self.valid_directions = {'n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw'}

    @abstractmethod
    def get_worker(self):
        """
        abstract method to get worker
        """
        raise NotImplementedError()
    
    @abstractmethod
    
    def get_move_direction(self, worker):
        """
        abstract method to get move direction
        """
        raise NotImplementedError()

    @abstractmethod
    def get_build_direction(self, worker, move_direction):
        """
        abstract method to get build direction
        """
        raise NotImplementedError()

    def has_moves(self, worker):
        """
        boolean function that returns true if player has any moves
        """
        for direction in self.board.DIRECTIONS.values():
            position = self.board.worker_position(worker)
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
            if self.board.is_valid_direction(worker[0], selected_dir):
                valid_builds.append(direction)
        return valid_builds

    def height_score(self, player):
        """
        method to calculate height score
        """
        height = 0
        for worker in player.workers:
            curr = self.board.worker_position(worker[0])
            x, y = curr[0], curr[1]
            final = self.board.cells[curr[0]][curr[1]]['height']
            height = final + height
        return height


    def center_score(self, player):
        """
        method to calculate center score
        """
        score = 0
        for worker in player.workers:
            get_pos = self.board.worker_position(worker[0])
            x, y = get_pos[0], get_pos[1]
            if (x, y) == (2, 2):
                score += 2
            elif 1 <= x <= 3 and 1 <= y <= 3:
                score += 1
            else:
                score += 0
        return score
    

    def distance_score(self, opp_player, player):
        """
        method to calculate distance score
        """
        opp_workers = opp_player.workers
        min_distances = [float('inf')] * len(opp_workers)
        for worker in player.workers:
            for i, opp_worker in enumerate(opp_workers):
                curr = self.board.worker_position(worker[0])
                x, y = curr[0], curr[1]
                curr_opp = self.board.worker_position(opp_worker[0])
                opp_x, opp_y = curr_opp[0], curr_opp[1]
                distance = max(abs(x - opp_x), abs(y - opp_y))
                min_distances[i] = min(min_distances[i], distance)
        return 8 - sum(min_distances)
    
