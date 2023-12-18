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

    def setup_workers(self, color):
        print("we made it!", color)
        if color == "white":
            self.cells[3][1]['worker'] = ('A', 3, 1)
            self.cells[1][3]['worker'] = ('B', 1, 3)
            return [('A', 3, 1), ('B', 1, 3)]
        else:
            self.cells[1][1]['worker'] = ('Y', 1, 1)
            self.cells[3][3]['worker'] = ('Z', 3, 3)
            return [('Y', 1, 1), ('Z', 3, 3)]  

    def worker_position(self, worker_id):
        for i in range(5):
            for j in range(5):
                cell = self.cells[i][j]
                if cell['worker'] is not None and cell['worker'][0] == worker_id:
                    # Return the position as (row, column)
                    return (i, j)
        return None 

    
    def is_valid_direction(self, worker, direction):
        # direction = self.DIRECTIONS[direction]
        # print("worker rn: ", worker)
        worker_pos = self.worker_position(worker)
        # print("worker rn: ", worker_pos)
        work_x, work_y = worker_pos
        # print (work_x, work_y)
        print("direction rn? ", direction)
        curr_x, curr_y = direction
        # print("direction rn? ", direction)
        if (0 > curr_x > 5 or 0 > curr_y > 5):
            return False
        elif self.cells[curr_x][curr_y]['worker'] is not None:
            return False
        elif self.cells[curr_x][curr_y]['height'] > self.cells[work_x][work_y]['height']:
            return False
        else:
            return True
    #  print("cur position: ", direction)
    #  cur_pos = self.DIRECTIONS[direction]
    #  print("direction valid?", cur_pos)  
    #out of bounds and 
    # if other worker is there
    # get height of curr cell and also of future cell (cannot move to cell thats higher than u)

    def iliketomoveitmoveit(self):
        pass

    def bobthebuilder(self):
        pass
        
    
    # def get_worker_position(self, worker_id):
    #     for i in range(5):
    #         for j in range(5):
    #             cell = self.cells[i][j]
    #             if cell['worker'] is not None and cell['worker'][0] == worker_id:
    #                 # Return the position as (row, column)
    #                 return (i, j)
    #     return None