import yaml
from solver import AStarSolver

def RoadTrip(startLoc, goalLoc, LocFile, EdgeFile, resultFile):
    solver = AStarSolver(locFilePath=LocFile, edgeFilePath=EdgeFile, startLoc=startLoc, goal=goalLoc)
    solver.solve()


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