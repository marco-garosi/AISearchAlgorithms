import time
from AStar import AStarSearch
from Problem import Problem
from Graph import Graph
from ResultVisualization import ResultVisualization
from State import State
import random
import math
from datetime import datetime

def get_state(width, height) -> State:
    user_wants_random = None

    while user_wants_random != 'y' and user_wants_random != 'n':
        user_wants_random = input("Random state? (y/n)\n> ")

        if user_wants_random == 'y':
            row = random.randrange(0, height)
            col = random.randrange(0, width)
            return State(row, col)
        elif user_wants_random == 'n':
            row = int(input("Row?\n> "))
            col = int(input("Column?\n> "))
            return State(row, col)

if __name__ == '__main__':
    # Input grid size
    width = int(input("Grid width?\n> "))
    height = int(input("Grid height?\n> "))

    # Get initial state info
    print("\n-- Initial state --")
    initial = get_state(width, height)

    # Get goal state info
    print("\n-- Goal state --")
    goal = get_state(width, height)

    # Get console output info
    user_wants_console_output = None
    while user_wants_console_output != 'y' and user_wants_console_output != 'n':
        user_wants_console_output = input("\nConsole output during search? (y/n)\n> ")

    #####
    # End of input phase
    # Start of computing phase
    #####

    # Set available actions
    actions = ["UP", "DOWN", "LEFT", "RIGHT"]

    # Build problem specs
    problem = Problem(Graph(), initial, goal, actions, width=width, height=height)

    # Prepare output window
    result_visualization = ResultVisualization(problem, update_figure_iteration=math.floor((width * height) / 2))
    result_visualization.start()

    # Make the actual search
    print(str(datetime.now()) + " | Search started...")
    search_result = AStarSearch.search(problem, function=result_visualization.update_search_grid, console_output=user_wants_console_output == 'y')
    print(str(datetime.now()) + " | Search concluded")

    # Compute and display the path found as a solution
    result_visualization.backtrack_display_path(search_result.node)

    input("\n\nPress ENTER to exit...")