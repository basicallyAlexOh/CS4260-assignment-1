# Dataloader class

import csv
from node import Node
from edge import Edge

class Dataloader:
    def __init__(self, locFile: str, edgeFile: str):
        try:
            self.__locFile = open(locFile, 'r')
            self.__edgeFile = open(edgeFile, 'r')
        except:
            raise Exception("File not found...")

        self.nodeList = []
        self.nodeDict = {}
        self.edgeList = []

        self.__readCSV()

    def __readCSV(self):
        with self.__locFile as locCSV:
            reader = csv.reader(locCSV, delimiter=',')
            for row in reader:
                try:
                    lat = float(row[1])
                    lon = float(row[2])
                    self.nodeList.append(Node(row[0], lat, lon))
                    self.nodeDict.update({row[0]: Node(row[0], lat, lon)})
                except:
                    print("Not a valid location")
                    print(row)

        with self.__edgeFile as edgeCSV:
            reader = csv.reader(edgeCSV, delimiter=',')
            for row in reader:
                try:
                    dist = float(row[3])
                    self.edgeList.append(Edge(row[0], self.nodeDict[row[1]], self.nodeDict[row[2]], dist))
                except:
                    print("Not a valid location")
                    print(row)









