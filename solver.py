
from dataloader import *
from graph import *
from queue import PriorityQueue

class AStarSolver:
    def __init__(self, locFilePath, edgeFilePath, goal):
        self.__dataloader = Dataloader(locFilePath, edgeFilePath)
        self.__graph = Graph(self.__dataloader, goal=goal)
        self.__solutions = []

    def solve(self):
        frontier = PriorityQueue()


