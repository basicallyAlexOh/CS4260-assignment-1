from structs.node import Node
class Edge:
    def __init__(self, label: str, start: Node, end: Node, weight: int):
        self.start = start
        self.end = end
        self.weight = weight
        self.label = label


    def __str__(self):
        ret = str(self.start) + " " + str(self.end) + " " + self.label + " " + str(self.weight)
        return ret