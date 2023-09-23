
from dataloader import *
from graph import *
from queue import PriorityQueue
from timer import Timer
import sys

class AStarSolver:
    def __init__(self, locFilePath: str, edgeFilePath: str, startLoc: str, goal: str):
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

    def __findMinSolution(self):
        minCost = self.__solutions[0].weight
        id = 0
        for i in range(0, len(self.__solutions)):
            if self.__solutions[i].weight < minCost:
                minCost = self.__solutions[i].weight
                id = i
        return id


    def __visitedNodes(self):
        ret = ""
        for node in self.__discovered:
            if self.__discovered[node]:
                ret += node.id + " "
        return ret

    def __printSummary(self, output=sys.stdout):
        print("Size of Frontier: " + self.__frontier.qsize(), file=output)
        (minCost, maxCost, avgCost) = self.__solutionSummary()
        print("Min Cost: " + minCost + "\nAverage Cost: " + avgCost + "\nMax Cost: " + maxCost, file=output)
        print("Solution ID of Min Cost: " + self.__findMinSolution(), file=output)
        print("Visited Nodes: " + self.__visitedNodes(), file=output)
        print("Times of Solutions: " + (str(path.time) + "; " for path in self.__solutions), file=output)



    def __promptContinue(self):
        response = input("Would you like to continue? [yes/no]")
        if response.lower() == "yes":
            return True
        elif response.lower() == "no":
            self.__printSummary()
            return False
        print("Invalid response... please try again\n")
        return self.__promptContinue()

    def solve(self):
        adj = self.__graph.getAdjList()

        self.__timer.start()

        self.__frontier.put((self.__start.h, Path(self.__start)))
        while not self.__frontier.empty():
            (f, curPath) = self.__frontier.get()
            curNode = curPath.getLastNode()

            if curNode == self.__graph.getGoal():
                self.__timer.pause()
                curPath.time = self.__timer.get()
                self.__solutions.append(curPath)
                print("Solution Found!")
                continueSearch = self.__promptContinue()
                if not continueSearch:
                    break
                self.__timer.start()


            for edge in adj[curNode]:
                (nextNode, w) = (edge.end, edge.weight)
                if nextNode not in curPath:
                    newPath = curPath.addEdge(edge)
                    newf = curPath.weight + nextNode.h
                    self.__frontier.put((newf, newPath))

        self.__timer.pause()

        if len(self.__solutions) == 0:
            print("no solutions found...")

        return self.__solutions
