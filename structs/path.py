from structs.node import Node
from structs.edge import Edge

class Path:
    def __init__(self, startNode: Node):
        self.path = [startNode]
        self.edges = []
        self.weight = 0

        # Time added to set of solutions
        self.time = None

    def __len__(self):
        return len(self.path)

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        x = self.x
        if x >= len(self.path):
            raise StopIteration
        self.x = x + 1
        return self.path[x]

    def __lt__(self, other):
        if not isinstance(other, Path):
            raise Exception("Trying to compare Path with another type")
        return self.weight < other.weight


    def __str__(self):
        ret = ""
        for node in self.path:
            ret += node
        return ret



    def getLastNode(self):
        return self.path[-1]

    def addEdge(self, e: Edge):
        self.path.append(e.end)
        self.edges.append(e)
        self.weight += e.weight