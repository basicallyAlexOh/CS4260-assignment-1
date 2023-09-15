
from collections import defaultdict


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

class Node:
    def __init__(self, name, long, lat):
        self.id = name
        self.longitude = long
        self.latitude = lat
        self.h = 0
#         TODO: finish this with calculating the h-values
class Graph:
    def __init__(self, dataloader, goal=None):
        self.__nodes = []
        self.__adj = defaultdict(list)
        self.__buildGraph(dataloader)
        self.__goal = goal
        if goal != None:
            self.setGoal(goal)


    # Build graph here.
    def __buildGraph(self, dataloader):
        self.__nodes = dataloader.nodeList
        for e in dataloader.edgeList:
            u,v,w = e.start, e.end, e.weight
            self.__adj[u].append(Edge(u,v,w))
            self.__adj[v].append(Edge(v,u,w))

    def setGoal(self, goalLoc):
        if goalLoc in self.__nodes:
            self.__goal = goalLoc
            self.__computeHeuristic()
        else:
            raise Exception("Invalid goal...")

    def __computeHeuristic(self):
        for node in self.__nodes:
            node.h = self.computeDistance(node, self.__goal)



    @staticmethod
    def computeDistance(node1: Node, node2: Node):
        # TODO: fill here with formula
        long1, lat1 = node1.longitude, node1.latitude
        long2, lat2 = node2.longitude, node2.latitude
        return 1.0





