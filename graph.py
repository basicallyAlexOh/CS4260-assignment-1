
from collections import defaultdict
from dataloader import Dataloader

class Node:
    def __init__(self, name: str, long: float, lat: float):
        self.id = name
        self.longitude = long
        self.latitude = lat
        self.h = 0
#         TODO: finish this with calculating the h-values

    def __str__(self):
        return self.id

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


class Edge:
    def __init__(self, start: Node, end: Node, weight: int):
        self.start = start
        self.end = end
        self.weight = weight

class Path:
    def __init__(self, startNode: Node):
        self.path = [startNode]
        self.weight = 0

        # Time added to set of solutions
        self.time = None

    def __str__(self):
        ret = ""
        for node in self.path:
            ret += node
        return ret



    def getLastNode(self):
        return self.path[-1]
    def addEdge(self, e: Edge):
        self.path.append(e.end)
        self.weight += e.weight


class Graph:
    def __init__(self, dataloader: Dataloader, goal=None):
        self.__nodes = []
        self.__adj = defaultdict(list)
        self.__buildGraph(dataloader)
        self.__goal = goal
        if goal != None:
            self.setGoal(goal)


    # Build graph here.
    def __buildGraph(self, dataloader: Dataloader):
        self.__nodes = dataloader.nodeList
        for e in dataloader.edgeList:
            u,v,w = e.start, e.end, e.weight
            self.__adj[u].append(Edge(u,v,w))
            self.__adj[v].append(Edge(v,u,w))

    def setGoal(self, goalLoc: str):
        found = False
        for node in self.__nodes:
            if goalLoc == node.id:
                self.__goal = node
                self.__computeHeuristic()
                found = True

        if not found:
            raise Exception("Invalid goal...")

    def __computeHeuristic(self):
        for node in self.__nodes:
            node.h = self.computeDistance(node, self.__goal)

    def getNodes(self):
        return self.__nodes

    def getAdjList(self):
        return self.__adj

    def getGoal(self):
        return self.__goal


    @staticmethod
    def computeDistance(node1: Node, node2: Node):
        # TODO: fill here with formula
        long1, lat1 = node1.longitude, node1.latitude
        long2, lat2 = node2.longitude, node2.latitude
        return 1.0
