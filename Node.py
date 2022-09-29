class Node:
    """
    Represent a node in a graph. Every node maintains its own list of connections
    with other nodes, a.k.a. the adjacency list
    """

    def __init__(self, adjacent_nodes, state=None, cost=0, parent=None):
        self.adjacent_nodes = adjacent_nodes
        self.state = state
        self.cost = cost
        self.parent = parent