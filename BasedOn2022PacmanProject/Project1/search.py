# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def pathToEnd(finalNode):


    path = []  # i diadromi mas
    step = finalNode[2] # to 1o vima

    # to monopati edo vrisketai anopoda, afoy kinoymaste apo to telos pros tin arxi
    while step:
        path.append(step)

        finalNode = finalNode[1]
        step = finalNode[2]

    # epistrefoyme to monopati poy vrikame anestremeno
    path.reverse()

    return path

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    frontier = util.Stack()
    expanded = set()


    stateNode = (problem.getStartState(),None,None,0.0) # ena node apoteleitai apo to current State, to parentState,
                                                       # to action gia na pame apo to parent sto current kai to synoliko kostos mexri to current

    frontier.push(stateNode)

    # vasismeno stis diafaneies
    while not frontier.isEmpty():
        currentNode = frontier.pop()

        if problem.isGoalState(currentNode[0]):
            return pathToEnd(currentNode)


        if currentNode[0] not in expanded:
            expanded.add(currentNode[0])
            successors = problem.getSuccessors(currentNode[0])

            for succ in successors:
                succNode = (succ[0],currentNode,succ[1],succ[2]+currentNode[3])
                frontier.push(succNode)

    return []


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # oloidio me to dfs mono poy anti gia Stack exoyme Queue sto frontier
    frontier = util.Queue()
    expanded = set()


    stateNode = (problem.getStartState(),None,None,0.0) # ena node apoteleitai apo to current State, to parentState,
                                                       # to action gia na pame apo to parent sto current kai to synoliko kostos mexri to current

    frontier.push(stateNode)

    # vasismeno stis diafaneies
    while not frontier.isEmpty():
        currentNode = frontier.pop()

        if problem.isGoalState(currentNode[0]):
            return pathToEnd(currentNode)


        if currentNode[0] not in expanded:
            expanded.add(currentNode[0])
            successors = problem.getSuccessors(currentNode[0])

            for succ in successors:
                succNode = (succ[0],currentNode,succ[1],succ[2]+currentNode[3])
                frontier.push(succNode)

    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #oloidio me to dfs mono poy anti gia Stack exoyme PriorityQueue sto frontier
    frontier = util.PriorityQueue()
    expanded = set()


    stateNode = (problem.getStartState(),None,None,0.0) # ena node apoteleitai apo to current State, to parentState,
                                                       # to action gia na pame apo to parent sto current kai to synoliko kostos mexri to current

    frontier.push(stateNode,stateNode[3])  # vazoyme tin arxiki state me priority 0 gia na vgei proti

    # vasismeno stis diafaneies
    while not frontier.isEmpty():
        currentNode = frontier.pop()

        if problem.isGoalState(currentNode[0]):
            return pathToEnd(currentNode)


        if currentNode[0] not in expanded:
            expanded.add(currentNode[0])
            successors = problem.getSuccessors(currentNode[0])

            for succ in successors:
                succNode = (succ[0],currentNode,succ[1],succ[2]+currentNode[3])
                frontier.push(succNode,succNode[3])

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #oloidio me to dfs mone poy anti gia Stack exoyme PriorityQueue sto frontier
    frontier = util.PriorityQueue()
    expanded = set()


    stateNode = (problem.getStartState(),None,None,0.0) # ena node apoteleitai apo to current State, to parentState,
                                                       # to action gia na pame apo to parent sto current kai to synoliko kostos mexri to current

    frontier.push(stateNode,heuristic(stateNode[0],problem)+stateNode[3])  # vazoyme tin arxiki state me priority 0 gia na vgei proti

    # vasismeno stis diafaneies
    while not frontier.isEmpty():
        currentNode = frontier.pop()

        if problem.isGoalState(currentNode[0]):
            return pathToEnd(currentNode)


        if currentNode[0] not in expanded:
            expanded.add(currentNode[0])
            successors = problem.getSuccessors(currentNode[0])

            for succ in successors:
                succNode = (succ[0],currentNode,succ[1],succ[2]+currentNode[3])
                frontier.push(succNode,heuristic(succNode[0],problem)+succNode[3])

    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
