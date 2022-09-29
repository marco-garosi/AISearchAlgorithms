class QueueItem:
    """
    Represent an enqueued node. This makes it possible to store node references
    in the queue while having it sorted by the expected node cost thanks to the
    override of the `__lt__` method.
    """

    def __init__(self, priority, node):
        self.priority = priority
        self.node = node

    def __lt__(self, other):
        """Return True if self.priority < other.priority

        Queue Item = QI
        QI a < QI b <=> priority(a) < priority(b)
        """

        return self.priority < other.priority