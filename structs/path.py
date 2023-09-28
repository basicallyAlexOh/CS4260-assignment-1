"""
path.py
Classes: Path
Purpose: Defines a path of nodes and edges.
"""

from structs.node import Node
from structs.edge import Edge

class Path:

    # __init__
    # Constructor: creates a path with a single starting node
    # Param: startNode (Node)
    def __init__(self, startNode: Node):
        self.path = [startNode]
        self.edges = []
        self.weight = 0

        # Time added to set of solutions
        self.time = None

    # __len__
    # Implements len(). Gives the length of the path.
    # Returns: int
    def __len__(self):
        return len(self.path)

    # __iter__
    # Defines a starting iterator for the path.
    def __iter__(self):
        self.x = 0
        return self

    # __next__
    # Increments an iterator to make the Path class iterable
    def __next__(self):
        x = self.x
        if x >= len(self.path):
            raise StopIteration
        self.x = x + 1
        return self.path[x]

    # __lt__
    # Allows comparisons of paths
    # Can be called when priority queue has 2 of the same weights and paths must be compared.
    # A path is less than another path if it is lower in weight.
    # Returns: bool
    def __lt__(self, other):
        if not isinstance(other, Path):
            raise Exception("Trying to compare Path with another type")
        return self.weight < other.weight

    # __str__
    # Gives a string with node IDs separated by a character of whitespace
    # Returns: string
    def __str__(self):
        ret = ""
        for node in self.path:
            ret += str(node) + " "
        return ret


    # getLastNode (Public)
    # Retrieves the last node in the path.
    # Returns: Node
    def getLastNode(self):
        return self.path[-1]

    # addEdge (Public)
    # Adds an edge to the path and updates the list of nodes and list of edges.
    # Params: e (Edge)
    def addEdge(self, e: Edge):
        self.path.append(e.end)
        self.edges.append(e)
        self.weight += e.weight