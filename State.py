class State:
    """
    Represent a node's state
    """

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __eq__(self, other):
        """Return True if two states are the same state

        Check whether self and other represent the same state
        """

        return isinstance(other, State) and self.row == other.row and self.column == other.column

    def __hash__(self):
        return hash(str(self.row) + str(self.column))