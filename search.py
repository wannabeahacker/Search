# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util
from sets import Set
import sys
sys.setrecursionlimit(1000000)

count = 0

class SearchProblem:

  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def getDirection(stringVal):
  from game import Directions
  s = Directions.SOUTH
  n = Directions.NORTH
  w = Directions.WEST
  e = Directions.EAST

  if stringVal == 'East':
    return e
  if stringVal == 'West':
    return w 
  if stringVal == 'North':
    return n 
  if stringVal == 'South':
    return s

def depthFirstSearchIter(problem, explored, result, seq):
  from game import Directions
  s = Directions.SOUTH
  n = Directions.NORTH
  w = Directions.WEST
  e = Directions.EAST


  node = problem.getStartState()
  goal = False
  print "Is the start a goal?", problem.isGoalState(node)

  seq.push(node)

  if problem.isGoalState(node):
    goal = True
    return goal
  else:
    for next_state,action,cost in problem.getSuccessors(node):
      problem.startState = next_state
      if next_state not in explored:
        print "state being explored is ", next_state
        print "action being taken is ", action
        explored.add(node)
        result.push(getDirection(action))
        #seq.push(next_state)
        res = depthFirstSearchIter(problem, explored, result, seq)
    
        if res:
          return result
        else:
          result.pop()
          seq.pop()
        #print "current stack is ", result
        #result.pop()
      


    


def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:

  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  from game import Directions
  s = Directions.SOUTH
  n = Directions.NORTH
  w = Directions.WEST
  e = Directions.EAST

  frontier = util.Stack()
  result = util.Stack() 
  seq = util.Stack()
  explored= set() # to store all the explored nodes

  test = util.Stack()
  result_array = []
  res_array = []

  depthFirstSearchIter(problem, explored, result, seq)
  #print "result stack is ", result
  counter = 0
  for i in result:
    result_array.append(i)
    counter += 1
  #print "result array is ", result_array
  for j in range(0,len(result_array)):
    res_array.append(result_array[len(result_array)-1-j])

  #print "sequence is ", seq
  #print "result array is", res_array
  return res_array


def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """

  result = util.Queue()
  node = problem.getStartState()

  frontier = util.Queue()
  explored = set()
  path = []
  result = util.Queue()

  frontier.push((node,[])
  print "Is the current node the solution? ", problem.isGoalState(node)
  if problem.isGoalState(node):
    return result
  count = 0

  while len(frontier) > 0:
    count +=  1
    print "Loop ", count
    node = frontier.pop()
    path.append(node)
    if problem.isGoalState(node):
      print "GOAL found!!!"
      print "result is ", result
      return result
    for next_state, action, cost in problem.getSuccessors(node):
      print ">>> " ,frontier
      if next_state not in explored:

        explored.add(node)
        problem.startState = next_state


        new_path = list(path)
        new_path.append(next_state)
        print new_path
        frontier.push(next_state)
        result.push(action)

        

      

  #return "no path "
        

  
      
def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
