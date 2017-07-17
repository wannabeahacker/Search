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

  goal = True
  res = False
  # get the current/start node
  node = problem.getStartState()

  # add current node to the explored node list, if the node is in explored list don't expand this search
  if node in explored:
    result.pop()
    seq.pop()
    return False
  else:
    explored.add(node)

  # is current node a goal? if it is return it as a solution 
  if problem.isGoalState(node):
    print "current place is ", node
    print "explored nodes are ", explored
    goal = True
    return result
  elif len(problem.getSuccessors(node)) == 0:
    # if the current node does not have children there is nothing to explore
    #result.pop()
    goal = False
    return goal
  else:
    # otherwise there is a child to be explored. Get next node to explore the action needed to explore that, and how much it costs
    for next_state,action,cost in problem.getSuccessors(node):
      problem.startState = next_state
      result.push(getDirection(action))
      seq.push(next_state)
      res = depthFirstSearchIter(problem, explored, result, seq)
      if res == True:
        return result
      else:
        #seq.pop()
        #result.pop()
        return res



    


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

  counter = 0
  for i in result:
    result_array.append(i)
    counter += 1

  for j in range(0,len(result_array)-1):
    res_array.append(result_array[len(result_array)-1-j])

  print "sequence is ", seq
  print "result array is", res_array
  return res_array





    
  
  



