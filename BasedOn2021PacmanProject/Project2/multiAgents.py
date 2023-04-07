# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and child states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed child
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        childGameState = currentGameState.getPacmanNextState(action)
        newPos = childGameState.getPacmanPosition()
        newFood = childGameState.getFood()
        newGhostStates = childGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]


        "*** YOUR CODE HERE ***"
        #Plirofories sxetika me tin torini thesi toy pacman

        curFood = currentGameState.getFood()

        walls = currentGameState.getWalls()

        #H megalyteri apo oles tis manhattan distances poy mporoyn na yparksoyn.
        #Tha tin xreiastoyme gia tin anavathmisi toy score sto telos
        maxLen = walls.height - 2 + walls.width - 2

        #arxika exoyme score 0
        totalScore = 0


        if(curFood[newPos[0]][newPos[1]]): # an sti thesi poy tha vrethoyme yparxei food
            totalScore += 10               # score + 10

        ## Tha psaksoyme na vroyme to kontinotero food
        closestFoodDist = float("inf")   #Arxika exoyme closestFoodDist = + infinity
        foodList = newFood.asList()        # I lista me tis sintetagmenes ton food

        ## diatrexoyme oles tis syntetagmenes ton food
        for food in foodList:
            foodDist = manhattanDistance(newPos, food) ##ypologizoyme thn manhatann apostasi kathe food apo to nextPos
            closestFoodDist = min(closestFoodDist, foodDist)  ##kratame tin mikroteri apostasi

        ## Tha psaksoyme na vroyme to kontinotero ghost
        closestGhostDist = float("inf")                 #arxika exoyme closestGhostDist = + infinity
        ghostList = childGameState.getGhostPositions()  #i lista me tis syntetagmenes ton ghost

        #diatrexoyme tis syntetagmenes ton ghost
        for ghost in ghostList:
            ghostDist = manhattanDistance(newPos, ghost) #ypologizoyme thn manhattan apostasi kathe ghost apo to nextPos
            closestGhostDist = min(closestGhostDist, ghostDist) #kratame tin mikroteri apostasi

        #an i apostasi tis nextPos apo to closest ghost einai < 2,simainei pos tha sigroystoyme me ghost
        if closestGhostDist < 2:
            totalScore -= 500  #xanoyme 500 points

        #prosthetoyme sto score analoga me to poso konta eimaste se food kai poso makria apo ghost
        totalScore += (1.0/closestFoodDist+1) + closestGhostDist/maxLen

        return totalScore

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.getNextState(agentIndex, action):
        Returns the child game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        # O Agent 0(dld o pacman) einai o MAX
        def maximizer(state, depth):
            depth += 1

            #Termatikos elegxos
            if((depth == self.depth) or (state.isWin() is True) or (state.isLose() is True)):
                return self.evaluationFunction(state)

            value = float("-inf")  # arxika value = - infinity
            legalActionsList = state.getLegalActions(0) # oles oi epitreptes kiniseis toy Agent 0(aka pacman)

            for action in legalActionsList:
                # sygrinoyme anamesa stis melontikes action toy MIN kai pairnoyme tin megalyteri
                nextState = state.getNextState(0, action)
                value = max(value, minimizer(nextState, depth, 1))

            return value

        # oi ypoloipoi agents(dld ta ghosts) einai oi MIN
        def minimizer(state, depth, agentIndex):

            #Termatikos elegxos
            if ((state.isWin() is True) or (state.isLose() is True)):
                return self.evaluationFunction(state)

            value = float("inf")  # arxika value = infinity
            legalActionsList = state.getLegalActions(agentIndex) #oles oi epitreptes kiniseis toy Agent i!=0 (dld ghost)
            totalAgents = state.getNumAgents()  # oloi oi agents poy yparxoyn

            #an to ghost poy paizei einai to teleytaio,
            if(agentIndex == totalAgents - 1):
                #meta prepei na paiksei o pacman,eksoy kai to maximizer

                for action in legalActionsList:
                    # sygrinoyme anamesa stis melontikes action toy MAX kai pairnoyme tin mikroteri
                    nextState = state.getNextState(agentIndex, action)
                    value = min(value, maximizer(nextState, depth))

            else:  # an den einai to teleytaio,meta tha paiksei to epomeno ghost,eksoy kai o minimizer

                for action in legalActionsList:
                    # sygrinoyme anamesa stis melontikes action ton ypoloipon agent kai pairnoyme tin mikroteri

                    nextState = state.getNextState(agentIndex, action)
                    nextAgent = agentIndex + 1
                    value = min(value, minimizer(nextState, depth, nextAgent))

            return value

        legalActionsList = gameState.getLegalActions(0) # oles oi epitreptes kiniseis toy Agent 0(aka pacman)

        act = Directions.STOP # i arxiki kinisi(an den kseroyme akomi ti na kanoyme as stamatisoyme na skeftoyme)
        value = float("-inf")

        # tha apofasisoyme ti tha kanoyme(aka poia minimax apofasi tha paroyme)
        for action in legalActionsList:
            #Gia kathe dinati kinisi ypologise tin minimax value,i opoia epeidi eimaste sti riza
            #tha ypologizetai me ti xrisi toy minimizer mias kai tha paiksei o MIN

            nextState = gameState.getNextState(0, action)
            temp = minimizer(nextState, 0, 1)

            # kratame tin megalyteri minimax timi
            if temp > value:
                value = temp # i kaliteri timi allazei
                act = action # tha kanoyme tin kinisi poy dinei ayti tin timi

        return act
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        # O Agent 0(dld o pacman) einai o MAX
        def maximizer(state, depth, alpha, beta):
            depth += 1
            #Termatikos elegxos
            if((depth == self.depth) or (state.isWin() is True) or (state.isLose() is True)):
                return self.evaluationFunction(state)

            value = float("-inf")  # arxika value = - infinity
            legalActionsList = state.getLegalActions(0)

            for action in legalActionsList:
                nextState = state.getNextState(0, action)
                value = max(value, minimizer(nextState, depth, 1, alpha, beta))

                # an to value einai megalytero toy beta,epistrefoyme to value(dld kledeyoyme)
                if value > beta:
                    return value

                #enimeronoyme to alpha
                alpha = max(alpha, value)

            return value

        # oi ypoloipoi agents(dld ta ghosts) einai oi MIN
        def minimizer(state, depth, agentIndex, alpha, beta):

            #Termatikos elegxos
            if ((state.isWin() is True) or (state.isLose() is True)):
                return self.evaluationFunction(state)

            value = float("inf")  # arxika value = + infinity
            legalActionsList = state.getLegalActions(agentIndex)
            totalAgents = state.getNumAgents()

            #an to ghost poy paizei einai to teleytaio,
            if(agentIndex == totalAgents - 1):
                #meta prepei na paiksei o pacman,eksoy kai to maximizer

                for action in legalActionsList:

                    nextState = state.getNextState(agentIndex, action)
                    value = min(value, maximizer(nextState, depth, alpha, beta))

                    # an to value einai mikrotero toy alpha,epistrefoyme to value(dld kledeyoyme)
                    if value < alpha:
                        return value

                    # enimeronoyme to beta
                    beta = min(beta, value)

            else:  # an den einai to teleytaio,meta tha paiksei to epomeno ghost,eksoy kai o minimizer

                for action in legalActionsList:
                    # sygrinoyme anamesa stis melontikes action ton ypoloipon agent kai pairnoyme tin mikroteri

                    nextState = state.getNextState(agentIndex, action)
                    nextAgent = agentIndex + 1
                    value = min(value, minimizer(nextState, depth, nextAgent, alpha, beta))

                    # an to value einai mikrotero toy alpha,epistrefoyme to value(dld kledeyoyme)
                    if value < alpha:
                        return value

                    # enimeronoyme to beta
                    beta = min(beta, value)

            return value

        legalActionsList = gameState.getLegalActions(0) # oles oi epitreptes kiniseis toy Agent 0(aka pacman)

        act = Directions.STOP
        value = float("-inf")  # arxika value = - infinity

        alpha = float("-inf")  # arxika alpha = - infinity
        beta = float("inf")  # arxika beta = + infinity

        # tha apofasisoyme ti tha kanoyme(aka poia minimax apofasi tha paroyme)
        for action in legalActionsList:
            nextState = gameState.getNextState(0, action)
            temp = minimizer(nextState, 0, 1, alpha, beta)

            # kratame tin megalyteri minimax timi
            if temp > value:
                value = temp
                act = action # tha kanoyme tin kinisi poy dinei ayti tin timi

            #an value > beta epistrefoyme tin kinisi(dld kladeyoyme)
            if value > beta:
                return act

            #enimeronoyme to alpha
            alpha = max(alpha, value)

        return act
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"

        # O Agent 0(dld o pacman) einai o MAX
        def maximizer(state, depth):
            depth += 1

            #Termatikos elegxos
            if((depth == self.depth) or (state.isWin() is True) or (state.isLose() is True)):
                return self.evaluationFunction(state)

            value = float("-inf")  # arxika value = - infinity
            legalActionsList = state.getLegalActions(0)

            # Paromoia me ta q2 kai q3 apla tora anti gia minimizer exoyme ton expectizer
            for action in legalActionsList:
                nextState = state.getNextState(0, action)
                value = max(value,expectizer(nextState, depth, 1))

            return value

        # Oi ypoloipoi agents(dld ta ghosts) akoloythoyn ton expectizer(dld droyn vasei pithanotiton)
        def expectizer(state, depth, agentIndex):

            #Termatikos elegxos
            if ((state.isWin() is True) or (state.isLose() is True)):
                return self.evaluationFunction(state)

            legalActionsList = state.getLegalActions(agentIndex)

            totalExpValue = 0  #i sinoliki anamenomeni timi
            totalActions = len(legalActionsList) # to plithos ton dinaton kiniseon

            if(totalActions == 0):
                return totalExpValue

            totalAgents = state.getNumAgents()

            #an to ghost poy paizei einai to teleytaio,
            if(agentIndex == totalAgents - 1):
                #meta prepei na paiksei o pacman,eksoy kai to maximizer

                for action in legalActionsList:
                    nextState = state.getNextState(agentIndex, action)
                    totalExpValue += maximizer(nextState, depth)
            else:  # an den einai to teleytaio,meta tha paiksei to epomeno ghost,eksoy kai o expectizer

                for action in legalActionsList:
                    nextState = state.getNextState(agentIndex, action)
                    nextAgentIndex = agentIndex + 1
                    totalExpValue += expectizer(nextState, depth, nextAgentIndex)

            prob = float(totalExpValue)/float(totalActions)

            return prob

        legalActionsList = gameState.getLegalActions(0)

        act = Directions.STOP
        value = float("-inf")

        #Paromoia logiki me ta q2 kai q3,mono poy tora to temp pairnei times apo to expectizer
        for action in legalActionsList:
            nextState = gameState.getNextState(0, action)
            temp = expectizer(nextState, 0, 1)

            if temp > value:
                value = temp
                act = action

        return act

        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"

    curPacmanPos = currentGameState.getPacmanPosition()   # H thesi toy pacman opos kai sto q1

    curFoodPos = currentGameState.getFood()
    foodList = curFoodPos.asList()       # H lista me ola ta diathesima food,opos kai sto q1

    powPalletsPos = currentGameState.getCapsules()   # Ta power pallets toy paixnidioy,den ta lavame ypopsin sto q1

    totalScore = 0  # Ksekiname me score 0

    foodDistList = []  # lista poy krata tis apostaseis toy pacman apo kathe food
    powPalletsDistList = []     # lista poy krata tis apostaseis toy pacman apo kathe power pallets

    ghostStateList = currentGameState.getGhostStates()  # lista me oles tis ghostStates poy yparxoyn

    #diatrexoyme thn lista me ola ta food gia na vroyme tis apostaseis toys apo ton pacman
    for food in foodList:
        foodDist = manhattanDistance(curPacmanPos, food)
        foodDistList.append(foodDist)

    # diatrexoyme thn lista me ola ta power pallets gia na vroyme tis apostaseis toys apo ton pacman
    for pallet in powPalletsPos:
        powPalletDist = manhattanDistance(curPacmanPos, pallet)
        powPalletsDistList.append(powPalletDist)

    #diatrexoyme thn lista me ta ghostStates,gia na doyme tin kanoyn ta ghost se sxesi me ton pacman
    for ghost in ghostStateList:
        ghostPos = ghost.configuration.getPosition()  # i thesi toy ghost
        ghostDist = manhattanDistance(curPacmanPos, ghostPos)  # i apostasi toy apo ton pacman

        if(ghostDist < 2): # an o pacman einai poli konta se kapoio ghost
            ghostScaredTime = ghost.scaredTimer  # eksetazoyme an to ghost einai scared

            if(ghostScaredTime != 0):  # an einai tote kerdizoyme pontoys
                totalScore += 1000.0/(ghostDist + 1)
            else:    # an den einai tote xanoyme pontoys
                totalScore -= 1000.0/(ghostDist + 1)

    if( min(powPalletsDistList+[100.0]) < 5):  #eksetazoyme an vriskomaste konta se kapoio pallet
        totalScore += 500.0/(min(powPalletsDistList)) # an nai,tote kerdizoyme pontoys

    for pallet in powPalletsPos:  # eksetazoyme an eimaste akrivos se kapoio pallet
        if((pallet[0] == curPacmanPos[0]) and (pallet[1] == curPacmanPos[1])): # an nai, tote kerdizoyme pontoys
            totalScore += 600.0

    foodNum = len(foodDistList) # to plithos ton food poy exoyn apomeinei
    closestFoodDist = min(foodDistList + [100.0])

    totalScore += (1.0/closestFoodDist + 1) - foodNum*10.0
    return totalScore

    util.raiseNotDefined()    

# Abbreviation
better = betterEvaluationFunction
