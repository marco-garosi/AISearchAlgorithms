from Graph import Graph
from Node import Node
from State import State

from math import sqrt

class Problem:
    """
    Represent a problem
    """

    def __init__(self, graph: Graph, initial, goal, actions, width=0, height=0):
        self.graph = graph
        self.initial = initial
        self.goal = goal
        self.actions = actions
        self.width = width
        self.height = height

    def is_goal(self, state):
        """Return True if given state is the goal

        Check whether the current state is the set goal
        """
        return self.goal.row == state.row and \
             self.goal.column == state.column

    def expand(self, node: Node):
        """Return given node's successors

        Expand given node. This generates in real time the node's successors, thus building a
        graph in real time. Be aware that there's no given graph: this is computed during execution!
        Generated successors are stored in the node's adjacency list. The list is then returned.
        """
        for action in self.actions:
            new_state = self.result(node.state, action)
            
            if new_state == None:
                continue
            
            new_node = Node([], state=new_state, cost=node.cost + self.action_cost(node.state, action, new_state), parent=node)
            node.adjacent_nodes.append(new_node)

        return node.adjacent_nodes

    def result(self, state, action) -> State:
        """Return the new State

        Computes the new state that can be reached from current state given the action.
        """

        if action == "UP":
            if state.row == 0:
                return None
            else:
                return State(state.row - 1, state.column)
        elif action == "DOWN":
            if state.row == self.height - 1:
                return None
            else:
                return State(state.row + 1, state.column)
        elif action == "LEFT":
            if state.column == 0:
                return None
            else:
                return State(state.row, state.column - 1)
        elif action == "RIGHT":
            if state.column == self.width - 1:
                return None
            else:
                return State(state.row, state.column + 1)

    def h(self, state):
        """
        Return some heuristic function
        """

        return self.h1(state)
        # return self.h2(state)

    def h1(self, state):
        """
        Manhattan distance
        """

        return abs(state.row - self.goal.row) + abs(state.column - self.goal.column)

    def h2(self, state):
        """
        Euclidean distance
        """

        return sqrt(pow(abs(state.row - self.goal.row), 2) + pow(abs(state.column - self.goal.column), 2))

    def f(self, node):
        """
        Return some cost-evaluation function
        """

        return self.f_standard(node)
        # return self.f_weighted(node, weight=1.3)

    def f_standard(self, node):
        """
        f(n) = g(n) + h(n), where g(n) is the cost of node n and h(n) is the heuristic cost of n
        """

        return node.cost + self.h(node.state)

    def f_weighted(self, node, weight=2):
        """
        f(n) = g(n) + W * h(n), where g(n) is the cost of node n and h(n) is the heuristic cost of n
        """

        return node.cost + weight * self.h(node.state)

    def action_cost(self, state, action, new_state):
        """
        Moving to any allowed direction has a constant cost
        """

        return 1
