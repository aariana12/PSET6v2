from players.Player import Player
import random

class HeuristicPlayer(Player):
    def __init__(self, player_type, workers, color, board):
        super().__init__(player_type, workers, color, board)
        self.player_type = "heuristic"
        self.c1 = 3
        self.c2 = 2
        self.c3 = 1


    # def choose_move(self):
    def weliveinsimulation(self, worker, to_direction, all_workers):
        print("worker in simulation: ", worker)
        if worker[0] == "A" or worker[0] == "B":
            pass
            # print("opp in simulation: ", opp_worker)
        curr_x, curr_y = self.board.worker_position(worker[0])
        self.board.cells[curr_x][curr_y]['worker'] = None
        new_dir = self.board.DIRECTIONS[to_direction]
        new_x, new_y = new_dir
        again_x = curr_x + new_x
        again_y = curr_y + new_y
        self.board.cells[again_x][again_y]['worker'] = worker
        height_score2 = self.height_score2(all_workers)
        center_score2 = self.center_score2(all_workers)
        distance_score2 = self.distance_score2(all_workers)
        self.board.cells[again_x][again_y]['worker'] = None
        self.board.cells[curr_x][curr_y]['worker'] = worker
        return height_score2, center_score2, distance_score2
    
    def get_worker(self):
        # print("ALL worker: ", self.workers)
        possible_moves1 = self.valid_directions(self.workers[0])
        possible_moves2 = self.valid_directions(self.workers[1])
        print('POSSIBLE POSITIONS: ', possible_moves1, possible_moves2)
        # possible_moves = self.get_all_possible_moves(self.workers)
        best_score = -float('inf')
        best_moves = []
        for move in possible_moves1:
            height_score, center_score, distance_score = self.weliveinsimulation(self.workers[0], move, self.workers)
        #     # Calculate scores for each move
        #     height_score = self.calculate_height_score(move)
        #     center_score = self.calculate_center_score(move)
        #     distance_score = self.calculate_distance_score(move)

            move_score = self.c1 * height_score + self.c2 * center_score + self.c3 * distance_score
            if move_score > best_score:
                 best_score = move_score
                 best_moves = [move]
            elif move_score == best_score:
                 best_moves.append(move)
        print("best moves??? ", best_moves)
        # return random.choice(best_moves)

    def get_move_direction(self, worker):
        print("heuristic workers: ", self.workers)
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

    def get_build_direction(self, worker, move_direction):
        pass
