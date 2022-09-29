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
    """Return a user- or random-generated input
    
    Prompt the user to input a state or randomly generate one.
    """

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

def get_obstacles(width, height, how_many=1):
    """Return obstacles to place on the map
    """

    return custom_defined_obstacles(width, height)
    # return generate_obstacles(how_many, width, height)

def custom_defined_obstacles(width, height):
    """Return obstacles

    Define some obstacles as wanted
    """

    obstacles = []

    for column in range(1, width):
        obstacles.append(State(math.floor(height / 2), column))

    for row in range(math.floor(height / 2), height):
        obstacles.append(State(row, math.floor(width / 2)))

    obstacles.remove(State(math.floor(height / 2) + math.floor(height / 3), math.floor(width / 2)))

    return obstacles

def generate_obstacles(how_many, width, height):
    """Return randomly generated obstacles

    Generates `how_many` obstacles with a uniform distribution.
    """
    obstacles = []

    for _ in range(min(how_many, width * height)):
        while True:
            row = random.randrange(0, height)
            col = random.randrange(0, width)
            obstacle = State(row, col)

            if obstacle not in obstacles:
                obstacles.append(obstacle)
                break

    return obstacles

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

    # Get obstacles info
    print("\n-- Obstacles --")
    obstacle_count = int(input("How many obstacles? (Any number if using `custom_defined_obstacles`)\n> "))

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
    problem = Problem(Graph(), initial, goal, actions, width=width, height=height, obstacles=get_obstacles(width, height, obstacle_count))

    # Prepare output window
    result_visualization = ResultVisualization(problem, update_figure_iteration=1000, delay=0.0)
    result_visualization.start()

    # Make the actual search
    print("\n" + str(datetime.now()) + " | Search started...")
    search_result = AStarSearch.search(problem, function=result_visualization.update_search_grid, console_output=user_wants_console_output == 'y')
    print(str(datetime.now()) + " | Search concluded")

    # Compute and display the path found as a solution
    if search_result is not None:
        result_visualization.backtrack_display_path(search_result.node)

    result_visualization.stop(wait_for_key=True)