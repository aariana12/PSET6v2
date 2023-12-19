from players.Player import Player
import random

class HeuristicPlayer(Player):
    def __init__(self, player_type, workers, color, board):
        super().__init__(player_type, workers, color, board)
        self.player_type = "heuristic"
        self.c1 = 3
        self.c2 = 2
        self.c3 = 1
        self.direction = None


    # def choose_move(self):
    def weliveinsimulation(self, worker, to_direction, all_workers):
        # print("worker in simulation: ", worker)
        opp_workers = [None, None]
        if worker[0] == "A" or worker[0] == "B":
            coords = self.board.worker_position('Y')
            coords2 = self.board.worker_position('Z')
            opp_workers[0] = ('Y', coords)
            opp_workers[1] = ('Z', coords2)
            # print("opp in simulation: ", opp_worker)
        else:
            coords = self.board.worker_position('A')
            coords2 = self.board.worker_position('B')
            opp_workers[0] = ('A', coords)
            opp_workers[1] = ('B', coords2)

        curr_x, curr_y = self.board.worker_position(worker[0])
        self.board.cells[curr_x][curr_y]['worker'] = None
        new_dir = self.board.DIRECTIONS[to_direction]
        new_x, new_y = new_dir
        again_x = curr_x + new_x
        again_y = curr_y + new_y
        self.board.cells[again_x][again_y]['worker'] = worker
        height_score2 = self.height_score2(all_workers)
        center_score2 = self.center_score2(all_workers)
        distance_score2 = self.distance_score2(opp_workers, all_workers)
        self.board.cells[again_x][again_y]['worker'] = None
        self.board.cells[curr_x][curr_y]['worker'] = worker
        return height_score2, center_score2, distance_score2
    
    def get_worker(self):
        # print("ALL worker: ", self.workers)
        possible_moves1 = self.valid_directions(self.workers[0])
        possible_moves2 = self.valid_directions(self.workers[1])
        # print('POSSIBLE POSITIONS: ', possible_moves1, possible_moves2)
        # possible_moves = self.get_all_possible_moves(self.workers)
        best_score = -float('inf')
        best_moves = []
        move_score1 = 0
        move_score2 = 0
        for move in possible_moves1:
            height_score, center_score, distance_score = self.weliveinsimulation(self.workers[0], move, self.workers)
            move_score1 = self.c1 * height_score + self.c2 * center_score + self.c3 * distance_score
            if move_score1 > best_score:
                 best_score = move_score1
                #  print("move score: ", move_score, best_moves)
                 best_moves = [move, self.workers[0]]
            elif move_score1 == best_score:
                 best_moves.append([move, self.workers[0]])
        # print("best moves??? ", best_moves, move_score1)

        best_score2 = -float('inf')
        best_moves2 = []
        for move in possible_moves2:
            height_score, center_score, distance_score = self.weliveinsimulation(self.workers[1], move, self.workers)
            move_score2 = self.c1 * height_score + self.c2 * center_score + self.c3 * distance_score
            if move_score2 > best_score2:
                 best_score2 = move_score2
                 best_moves2 = [move, self.workers[1]]
                #  print("move score 2: ", move_score, best_moves2)
            elif move_score2 == best_score2:
                 best_moves2.append([move, self.workers[1]])
        # best_moves2 = random.choice(best_moves)
        # print("best moves 22222??? ", best_moves2, move_score2)

        # print("worker to move?: ", best_moves2)
        all_best = [best_moves, best_moves2]
        # print('ALLLLL BEST POSS: ', all_best)
        best_overall = random.choice(all_best)
        # print("AND THE WINNER ISSSSSS: ", best_overall)
        self.get_move_direction(best_overall[1][0])
        self.direction = best_overall[0]
        # print(self.direction)
        return best_overall[1][0]

    def get_move_direction(self, worker):
        direction = self.direction
        # print("direction from get work: ", direction)
        return direction
        # self.player_type.workers
        # possible_moves = self.board.get_all_possible_moves(self.workers)
        # best_score = -float('inf')
        # best_moves = []
        # for move in possible_moves:
        #     # Calculate scores for each move
        #     height_score = self.calculate_height_score(move)
        #     center_score = self.calculate_center_score(move)
        #     distance_score = self.calculate_distance_score(move)

        #     move_score = self.c1 * height_score + self.c2 * center_score + self.c3 * distance_score
        #     if move_score > best_score:
        #         best_score = move_score
        #         best_moves = [move]
        #     elif move_score == best_score:
        #         best_moves.append(move)

        # # Choose randomly among the best moves if there's a tie
        # return random.choice(best_moves)

    def get_build_direction(self, worker, moved_direction):
        return random.choice(self.valid_builds(worker, moved_direction))
