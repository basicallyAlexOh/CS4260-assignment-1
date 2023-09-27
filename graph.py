
from collections import defaultdict
from math import sin, cos, asin, sqrt, radians
from node import Node
from edge import Edge

from dataloader import Dataloader


class Graph:
    def __init__(self, dataloader: Dataloader, goal=None):
        self.__nodes = []
        self.__adj = defaultdict(list)
        self.__buildGraph(dataloader)
        self.__goal = goal
        if goal != None:
            self.setGoal(goal)


    def __buildGraph(self, dataloader: Dataloader):
        self.__nodes = dataloader.nodeList
        for e in dataloader.edgeList:
            label, u,v,w = e.label, e.start, e.end, e.weight
            self.__adj[u].append(Edge(label,u,v,w))
            self.__adj[v].append(Edge(label,v,u,w))

    def setGoal(self, goalLoc: str):
        found = False
        for node in self.__nodes:
            if goalLoc == node.id:
                self.__goal = node
                self.__computeHeuristic()
                found = True
                break

        if not found:
            raise Exception("Invalid goal...")

    def __computeHeuristic(self):
        for node in self.__nodes:
            node.h = self.computeDistance(node, self.__goal)
        for key in self.__adj:
            for edge in self.__adj[key]:
                edge.start.h = self.computeDistance(edge.start, self.__goal)
                edge.end.h = self.computeDistance(edge.end, self.__goal)
    def getNodes(self):
        return self.__nodes

    def getAdjList(self):
        return self.__adj

    def getGoal(self):
        return self.__goal


    @staticmethod
    def computeDistance(node1: Node, node2: Node):
        # Taken from the following post
        # https://www.geeksforgeeks.org/program-distance-two-points-earth/
        lon1, lat1 = radians(node1.longitude), radians(node1.latitude)
        lon2, lat2 = radians(node2.longitude), radians(node2.latitude)

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

        c = 2 * asin(sqrt(a))

        # Radius of earth in kilometers. Use 3956 for miles
        r = 3956

        # calculate the result
        return (c * r)




