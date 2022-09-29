import time
from matplotlib import pyplot as plt
import numpy as np
import DisplayColors as dp
import cv2

class ResultVisualization:
    """
    Handle result visualization with Matplotlib (figure, grid, updates, etc.)
    """

    FIGURE_NAME = "Graph Exploration"

    def __init__(self, problem, update_figure_iteration=1, delay=0.0):
        self.problem = problem
        self.update_figure_iteration = update_figure_iteration
        self.delay = delay
        
    def __del__(self):
        self.stop()

    def start(self):
        """
        Prepare output window
        """

        # Setup output image (grid)
        self.grid = np.zeros([self.problem.height,self.problem.width], dtype=np.uint8)
        self.grid[self.problem.initial.row][self.problem.initial.column] = dp.INITIAL_NODE
        self.grid[self.problem.goal.row][self.problem.goal.column] = dp.GOAL_NODE

        for obstacle in self.problem.obstacles:
            self.grid[obstacle.row][obstacle.column] = dp.OBSTACLE

        # Setup output figure
        cv2.imshow(self.FIGURE_NAME, self.grid)
        cv2.setWindowProperty(self.FIGURE_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.waitKey(1)

    def stop(self, wait_for_key=False):
        """
        Wait for user to close window and close OpenCV Visualization.
        """

        if wait_for_key:
            cv2.waitKey(0)

        cv2.destroyWindow(self.FIGURE_NAME)

    def update_search_grid(self, node, iteration):
        """
        Update the search grid, a.k.a. the output image
        """

        # Leave state and goal node's colors unchanged
        if node.state == self.problem.initial or node.state == self.problem.goal:
            self.update_search_display()
            return

        # Update current node color. Update displayed image only if necessary
        self.grid[node.state.row][node.state.column] = dp.EXPANDED_NODE
        
        if iteration % self.update_figure_iteration == 0:
            self.update_search_display()

        # Sleep, if necessary
        if self.delay > 0:
            time.sleep(self.delay)

    def update_search_display(self, update_canvas=True):
        """
        Update the window, thus making changes in the model (grid) visible
        """

        cv2.imshow(self.FIGURE_NAME, self.grid)
        cv2.waitKey(1)

    def backtrack_display_path(self, node):
        """
        Color the path found as a solution by following it backwards from goal to initial node
        using every node's `parent` property
        """

        # Goal node
        self.grid[node.state.row][node.state.column] = dp.GOAL_NODE

        # Nodes on path
        current_node = node.parent
        while current_node.parent != None and current_node.state != self.problem.initial:
            self.grid[current_node.state.row][current_node.state.column] = dp.PATH_MIDDLE_NODE
            current_node = current_node.parent

        # Initial node
        self.grid[current_node.state.row][current_node.state.column] = dp.INITIAL_NODE

        # Update the window
        self.update_search_display()