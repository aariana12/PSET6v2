class Board:
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
        if color == "white":
            self.cells[3][1]['worker'] = ('A', 3, 1)
            self.cells[1][3]['worker'] = ('B', 1, 3)
            return [('A', 3, 1), ('B', 1, 3)]
        else:
            self.cells[1][1]['worker'] = ('Y', 1, 1)
            self.cells[3][3]['worker'] = ('Z', 3, 3)
            return [('Y', 1, 1), ('Z', 3, 3)]  

    def worker_position(self, worker_id):
        """finds the cur worker position"""
        for i in range(5):
            for j in range(5):
                cell = self.cells[i][j]
                if cell['worker'] is not None and cell['worker'][0] == worker_id:
                    # Return the position as (row, column)
                    return (i, j)
        return None 

    
    def is_valid_direction(self, worker, direction):
        curr_x, curr_y = direction
        worker_pos = self.worker_position(worker)
        work_x, work_y = worker_pos
        if (0 > curr_x > 5 or 0 > curr_y > 5):
            # print("1")
            return False
        elif self.cells[curr_x][curr_y]['worker'] is not None:
            # print("2")
            return False
        elif self.cells[curr_x][curr_y]['height'] > self.cells[work_x][work_y]['height']:
            # print("3")
            
            return False
        return True
    #  print("cur position: ", direction)
    #  cur_pos = self.DIRECTIONS[direction]
    #  print("direction valid?", cur_pos)  
    #out of bounds and 
    # if other worker is there
    # get height of curr cell and also of future cell (cannot move to cell thats higher than u)

    def iliketomoveitmoveit(self, worker, to_direction):
        curr_x, curr_y = self.worker_position(worker)
        self.cells[curr_x][curr_y]['worker'] = None
        # print("cur position before move: ", curr_x, curr_y)
        new_dir = self.DIRECTIONS[to_direction]
        new_x, new_y = new_dir
        again_x = curr_x + new_x
        again_y = curr_y + new_y
        # print("new pos after move: ", new_x, new_y)
        # self.cells[curr_x][curr_y]['worker'] = None
        print("Ilike move it:", worker[0])
        self.cells[again_x][again_y]['worker'] = worker
        
        return (worker[0], again_x, again_y) 

        

    def bobthebuilder(self, worker, to_build):
        curr_x, curr_y = self.worker_position(worker)
        # print("curr pos after move: ", curr_x, curr_y)
        build_x, build_y = self.DIRECTIONS[to_build]
        build_n = curr_x + build_x
        build_m = curr_y + build_y

        #TODO should not be able to build where there is a worker 
        self.cells[build_n][build_m]['height'] += 1
        curr_pos_b = self.worker_position(worker)
        print("worker in bob? ", curr_pos_b)
        # print("worker in bobthebuilder: ", self.cells[build_n][build_m]['worker'])
    
    # def is_valid_build
        
    
    # def get_worker_position(self, worker_id):
    #     for i in range(5):
    #         for j in range(5):
    #             cell = self.cells[i][j]
    #             if cell['worker'] is not None and cell['worker'][0] == worker_id:
    #                 # Return the position as (row, column)
    #                 return (i, j)
    #     return None