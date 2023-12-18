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

    def is_valid_direction(self, worker, direction):
        