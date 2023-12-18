from players.Player import Player

class HeuristicPlayer(Player):
    def __init__(self, player_type, workers, color, board):
        super().__init__(player_type, workers, color, board)
        self.player_type = "heuristic"
        self.c1 = 3
        self.c2 = 2
        self.c3 = 1


    # def choose_move(self):

    
    def get_worker(self):
        possible_moves = self.board.get_all_possible_moves(self.workers)
        best_score = -float('inf')
        best_moves = []
        for move in possible_moves:
            # Calculate scores for each move
            height_score = self.player.height_score(move)
            center_score = self.player.center_score(move)
            distance_score = self.player.distance_score(move)

            move_score = self.c1 * height_score + self.c2 * center_score + self.c3 * distance_score
            if move_score > best_score:
                best_score = move_score
                best_moves = [move]
            elif move_score == best_score:
                best_moves.append(move)

        # Choose randomly among the best moves if there's a tie
        return random.choice(best_moves)

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
