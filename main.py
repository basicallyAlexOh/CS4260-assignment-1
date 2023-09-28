"""
main.py
Entry point for the program
"""

import yaml
from utils.solver import AStarSolver

# RoadTrip
# Creates an AStarSolver object and passes required parameters
# Params: startLoc (string), goalLoc (string), LocFile (string), EdgeFile (string), resultFile (string)
def RoadTrip(startLoc, goalLoc, LocFile, EdgeFile, resultFile):
    solver = AStarSolver(locFilePath=LocFile, edgeFilePath=EdgeFile, startLoc=startLoc, goal=goalLoc, resultFilePath=resultFile)
    solver.solve()

# main
# Opens config.YAML and sets the parameters of the search
# Entry point of the program.
def main():
    with open('config.YAML', 'r') as file:
        config = yaml.safe_load(file)
    locFilePath = config['locationFile']
    edgeFilePath = config['edgeFile']
    start = config['startLoc']
    goal = config['goal']
    resultFilePath = config['resultFile']

    RoadTrip(start, goal, locFilePath, edgeFilePath, resultFilePath)


if __name__ == '__main__':
    main()