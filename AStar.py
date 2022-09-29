from SearchAlgorithm import SearchAlgorithm
from SearchSolution import SearchSolution
from Node import Node
from queue import PriorityQueue
from QueueItem import QueueItem

class AStarSearch(SearchAlgorithm):

    @staticmethod
    def search(problem, function=None, console_output=False) -> SearchSolution:
        """Return a Node (solution) or None (no solution)

        Explore new states using the A* ("A Star") algorithm.
        """

        node = Node([], problem.initial, 0)
        frontier = PriorityQueue()
        frontier.put(QueueItem(float(problem.f(node)), node))
        reached = {}
        reached[problem.initial] = node

        # Count iterations - it is not necessary in A* per se,
        # but it may come in handy for visualization (e.g., update only n iterations)
        iteration = 0

        # Explore graph
        while not frontier.empty():
            node = frontier.get().node

            if console_output:
                print(str(iteration + 1) + " | Visiting (" + str(node.state.row) + ", " + str(node.state.column) + ") | Cost = " + str(node.cost) + " | f(node) = " + str(problem.f(node)))

            # Update the output grid
            if function is not None:
                function(node, iteration)

            # Check for goal
            if problem.is_goal(node.state):
                if console_output:
                    print("\n> Total iterations: " + str(iteration + 1))

                # Return the solution (goal node). The found path can be followed
                # backwards, since Node(s) have a connection with their parents
                return SearchSolution(node, reached)
            
            # Expand the current node to get its children
            for child in problem.expand(node):
                s = child.state

                # Check if it's reached a new state or a state already reached but with lower cost
                if s not in reached or child.cost < reached[s].cost:
                    reached[s] = child
                    frontier.put(QueueItem(float(problem.f(child)), child))

            iteration = iteration + 1

        return None