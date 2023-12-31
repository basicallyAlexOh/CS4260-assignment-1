"""
solver.py
Classes: AStarSolver
Purpose: Defines how the solver should solve for paths from the start location to the end location.
"""
import copy

from utils.dataloader import *
from structs.graph import Graph
from structs.path import Path
from utils.timer import Timer

from queue import PriorityQueue
import sys


class AStarSolver:

    # static variable to keep track of solution number
    solNumber = 0



    # __init__
    # Constructor - instantiates an object of AStarSolver
    def __init__(self, locFilePath: str, edgeFilePath: str, startLoc: str, goal: str, resultFilePath: str):
        dataloader = Dataloader(locFilePath, edgeFilePath)
        self.__graph = Graph(dataloader, goal=goal)
        self.__start = None

        for node in self.__graph.getNodes():
            if node.id == startLoc:
                self.__start = node
                break

        self.__discovered = {node : False for node in self.__graph.getNodes()}
        self.__solutions = []
        self.__frontier = PriorityQueue()
        self.__timer = Timer()
        self.__resultFile = open(resultFilePath, "w+")



    # solutionSummary (Private)
    # Finds the min, max, and average cost of solutions
    # Return: (min, max, avg)
    def __solutionSummary(self):
        totalSum = 0
        minCost = self.__solutions[0].weight
        maxCost = self.__solutions[0].weight
        for path in self.__solutions:
            totalSum += path.weight
            minCost = min(minCost, path.weight)
            maxCost = max(maxCost, path.weight)
        avgCost = totalSum / len(self.__solutions)
        return minCost, maxCost, avgCost


    # findMinSolution (Private)
    # Finds the ID of the minimum solution
    # Returns: int
    def __findMinSolution(self):
        minCost = self.__solutions[0].weight
        id = 0
        for i in range(0, len(self.__solutions)):
            if self.__solutions[i].weight < minCost:
                minCost = self.__solutions[i].weight
                id = i
        return id

    # visitedNodes (Private)
    # Lists the nodes that have been visited separated by one character of whitespace
    # Returns: string
    def __visitedNodes(self):
        ret = ""
        for node in self.__discovered:
            if self.__discovered[node]:
                ret += node.id + " "
        return ret


    # printSummary (Private)
    # Prints the summary to output
    # Params: output (default = sys.stdout)
    def __printSummary(self, output=sys.stdout):
        print("Size of Frontier: " + str(self.__frontier.qsize()), file=output)
        (minCost, maxCost, avgCost) = self.__solutionSummary()
        print("Min Cost: " + str(minCost) + "\nAverage Cost: " + str(avgCost) + "\nMax Cost: " + str(maxCost), file=output)
        print("Solution ID of Min Cost: " + str(self.__findMinSolution()), file=output)
        print("Visited Nodes: " + self.__visitedNodes(), file=output)

        for path in self.__solutions:
            output.write("\n")
            self.__pathSummary(p=path, output=output)
            print(str(path.time), file=output)


    # pathSummary (Private)
    # Outputs the summary of a single path
    # Params: output (default = sys.stdout)
    def __pathSummary(self, p : Path, output=sys.stdout):
        print("Solution #%d : %s %d" % (self.solNumber, str(p.path[0]), p.path[0].h),file=output)
        self.solNumber += 1
        curG = 0
        for edge in p.edges:
            curG += edge.weight
            print(str(edge) + " " + str(curG) + " " + str(edge.end.h), file=output)


    # promptContinue (Private)
    # Asks user for a response to continue the search or not
    # Returns: bool
    def __promptContinue(self):
        response = input("Would you like to continue? [yes/no]")
        if response.lower() == "yes":
            return True
        elif response.lower() == "no":
            return False
        print("Invalid response... please try again\n")
        return self.__promptContinue()


    # solve (Public)
    # Solves the graph using anytime A* and gives unique paths to the ending location
    # Returns: list of paths
    def solve(self):
        continueSearch = True

        adj = self.__graph.getAdjList()

        self.__timer.start()

        self.__frontier.put((self.__start.h, Path(self.__start)))
        while not self.__frontier.empty():
            (f, curPath) = self.__frontier.get()
            curNode = curPath.getLastNode()

            self.__discovered[curNode] = True

            if curNode == self.__graph.getGoal():
                self.__timer.pause()
                curPath.time = self.__timer.get()
                self.__solutions.append(curPath)
                print("Solution Found!")
                continueSearch = self.__promptContinue()
                if not continueSearch:
                    self.__printSummary()
                    self.solNumber = 0
                    self.__printSummary(output=self.__resultFile)
                    break
                self.__timer.resume()


            for edge in adj[curNode]:
                (nextNode, w) = (edge.end, edge.weight)
                if nextNode not in curPath:
                    newPath = copy.deepcopy(curPath)
                    newPath.addEdge(edge)
                    newf = curPath.weight + nextNode.h
                    self.__frontier.put((newf, newPath))

        print("Search has terminated... ")

        if len(self.__solutions) == 0:
            print("no solutions found...")

        if continueSearch:
            print("Printing Results:")
            self.__printSummary()
            self.solNumber = 0
            self.__printSummary(output=self.__resultFile)



        return self.__solutions
