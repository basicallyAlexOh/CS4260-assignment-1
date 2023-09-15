# Dataloader class

import csv
from graph import *

class Dataloader:
    def __init__(self, locFile, edgeFile):
        try:
            self.__locFile = open(locFile, 'r')
            self.__edgeFile = open(edgeFile, 'r')
        except:
            print("File not found...")

        self.nodeList = []
        self.edgeList = []

        self.__readCSV()

    def __readCSV(self):
        with self.__locFile as locCSV:
            reader = csv.reader(locCSV, delimiter=',')
            for row in reader:
                self.nodeList.append(Node(row[0], row[1], row[2]))

        with self.__edgeFile as edgeCSV:
            reader = csv.reader(edgeCSV, delimiter=',')
            for row in reader:
                self.edgeList.append(Edge(row[1], row[2], float(row[3])))







