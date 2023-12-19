from Game import Santorini
import sys

import sys

def main():
    argv_params = [['human', 'heuristic', 'random'], ['human', 'heuristic', 'random'], ['on', 'off'], ['on', 'off']]

    parameters = ['human', 'human', False, False]  # Default values for undo_redo and score

    for i in range(1, len(sys.argv)):
        if sys.argv[i] not in argv_params[i-1]:
            sys.exit('Invalid command line argument: ' + sys.argv[i])

        if i == 3 or i == 4:  # Check if the parameter is 'on' or 'off' and convert to boolean
            parameters[i-1] = sys.argv[i].lower() == 'on'
        else:
            parameters[i-1] = sys.argv[i]

    white_type, blue_type, undo_redo, score = parameters


    game = Santorini.getInstance(white_type, blue_type, undo_redo, score)
    game.initialize_board()

    game.make_moves()

if __name__ == "__main__":
    main()
