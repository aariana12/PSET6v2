# from players.HeuristicPlayer import HeuristicPlayer

class Board:
    """
    class that sets up the board positions and has the lowest level functions that move and manage workers on the board
    """
    DIRECTIONS = {
        'n': (-1, 0),
        'ne': (-1, 1),
        'e': (0, 1),
        'se': (1, 1),
        's': (1, 0),
        'sw': (1, -1),
        'w': (0, -1),
        'nw': (-1, -1)
    }

    def __init__(self):
        self.cells = [[{'height': 0, 'worker': None} for _ in range(5)] for _ in range(5)]

    def display(self):
        """
        method that displays the board setup
        """
        print("+--+--+--+--+--+")
        for i in range(5):
            for j in range(5):
                cell = self.cells[i][j]
                worker = cell['worker']
                height = cell['height']
                if worker is not None:
                    print(f"|{height}{worker[0]}", end="")
                else:
                    print(f"|{height} ", end="")
            print("|")
            print("+--+--+--+--+--+")

    def make_board(self, color):
        """
        method that sets up the positions on the board
        """
        if color == "white":
            self.cells[3][1]['worker'] = ('A', 3, 1)
            self.cells[1][3]['worker'] = ('B', 1, 3)
            return [('A', 3, 1), ('B', 1, 3)]
        else:
            self.cells[1][1]['worker'] = ('Y', 1, 1)
            self.cells[3][3]['worker'] = ('Z', 3, 3)
            return [('Y', 1, 1), ('Z', 3, 3)]  

    def worker_position(self, worker):
        """
        method that returns the worker position from worker name
        """
        for i in range(5):
            for j in range(5):
                cell = self.cells[i][j]
                if cell['worker'] is not None and cell['worker'][0] == worker:
                    return (i, j)
        return None 

    def is_valid_direction(self, worker, direction):
        """
        method that checks if a move direction is valid
        """
        curr_x, curr_y = direction
        worker_pos = self.worker_position(worker)
        work_x, work_y = worker_pos
        new_x, new_y = curr_x + work_x, curr_y + work_y
        print("new xy:", new_x, new_y)
        if (0 <= new_x < 5 and 0 <= new_y < 5):
            if not self.check_occupied_worker((new_x, new_y)):
                height_diff = self.cells[new_x][new_y]['height'] - self.cells[curr_x][curr_y]['height']
                if height_diff <=1:
                    return True
        else:
            return False

    def is_valid_build(self, worker, move_direction, direction):
        """
        method that checks if a build direction is valid
        """
        work_x, work_y = self.worker_position(worker)  # worker pos
        curr_x, curr_y = self.DIRECTIONS[move_direction] # current move
        build_x, build_y = direction # build dir
        new_x, new_y  = curr_x + work_x + build_x, curr_y + work_y + build_y
        if (0 < new_x < 5 and 0 < new_y < 5):
            # temporarily move it 
            self.cells[work_x + curr_x][work_y + curr_y]['worker'] = worker
            self.cells[work_x][work_y]['worker'] = None
            if not self.check_occupied_worker((new_x, new_y)):
                height_diff = self.cells[new_x][new_y]['height'] - self.cells[curr_x][curr_y]['height']
                if height_diff <=1:
                    # move it back
                    self.cells[work_x][work_y]['worker'] = worker
                    self.cells[work_x + curr_x][work_y + curr_y]['worker'] = None
                    return True
        else:
            return False

    def iliketomoveitmoveit(self, worker, to_direction):
        """
        method that moves the piece in a move direction
        """
        curr_x, curr_y = self.worker_position(worker)
        self.cells[curr_x][curr_y]['worker'] = None
        new_dir = self.DIRECTIONS[to_direction]
        new_x, new_y = new_dir
        again_x = curr_x + new_x
        again_y = curr_y + new_y
        self.cells[again_x][again_y]['worker'] = worker
        return (worker[0], again_x, again_y) 

    def bobthebuilder(self, worker, to_build):
        """
        method that builds in a specified build direction
        """
        curr_x, curr_y = self.worker_position(worker)
        build_x, build_y = self.DIRECTIONS[to_build]
        build_n = curr_x + build_x
        build_m = curr_y + build_y
        print(build_n, build_m)
        self.cells[build_n][build_m]['height'] += 1
        curr_pos_b = self.worker_position(worker)
        print("worker in bob? ", curr_pos_b)

    def check_occupied_worker(self, coordinate):
        """
        method that checks if a position is occupied by a worker
        """
        occupied = False
        for worker in ['A', 'B', 'Y', 'Z']:
            if self.worker_position(worker) == coordinate:
                occupied = True
                print("in check: ", self.worker_position(worker), coordinate)
            elif self.worker_position(worker) == None:
                occupied = False
        return occupied

    # def get_valid_move_directions(self, row, col):
    #         valid_directions = []
    #         for direction, (dx, dy) in self.DIRECTIONS.items():
    #             new_row, new_col = row + dx, col + dy
    #             if 0 <= new_row < 5 and 0 <= new_col < 5:  # Check within board boundaries
    #                 target_cell = self.cells[new_row][new_col]
    #                 if target_cell['worker'] is None:  # Check if cell is not occupied by another worker
    #                     # Additional rules can be added here (e.g., height difference constraints)
    #                     valid_directions.append(direction)
    #         return valid_directions
