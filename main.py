from Game import Santorini
import sys

def main():
    argv_params = [['human', 'heuristic', 'random'], ['human', 'heuristic', 'random'], ['on', 'off'], ['on', 'off']]

    parameters = ['human', 'human', 'off', 'off']

    for i in range(1, len(sys.argv)):
        if (sys.argv[i] not in argv_params[i-1]):
           sys.exit('Invalid command line argument: ' + sys.argv[i])

        parameters[i-1] = sys.argv[i]

    white_type = parameters[0]
    blue_type = parameters[1]
    undo_redo = parameters[2]
    score = parameters[3]

    game = Santorini(white_type, blue_type, undo_redo, score)
    # print(game.board)

    game.make_moves()

    # while True:
    #     game.make_moves()


if __name__ == "__main__":
    main()