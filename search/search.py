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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())

    #"*** YOUR CODE HERE ***"
    
    #To return the actions
    actions = [];

    #To alleviate redundant exploration
    visited_Nodes = [];

    # parent_ptrs has key k and value[v,a] -- meaning 'v' node goes to 'k' node with action 'a'
    # Since the path to return consist of actions; we save it in parent_ptrs.   
    parent_ptrs = {};
    stk = util.Stack();
    
    currentState = problem.getStartState();
    stk.push(currentState);
    visited_Nodes.append(currentState);
    print('visited_Nodes: ',visited_Nodes);
    parent_ptrs[currentState] = [];

    #Iterate till we don't hit the goal state 
    while (not problem.isGoalState(currentState)):
        if stk.isEmpty():
            break;
        neighbours = problem.getSuccessors(currentState);
        print(neighbours[0]);
        #Neighbours have triplet format. Please print it to observe it better.
        for nbr,act,cost in neighbours:
            if nbr not in visited_Nodes:
                stk.push(nbr);
                parent_ptrs[nbr] = [currentState,act];

        #Update currentState
        currentState = stk.pop();
        visited_Nodes.append(currentState);
    #In our scenario goal always exist in given graph. -- therefore truthness of while condition is inevitable
    parent = parent_ptrs[currentState];
    while(parent):
        actions.append(parent[1]);
        parent = parent_ptrs[parent[0]];

    actions.reverse();
    return actions;

    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    actions = [];

    #To alleviate redundant exploration
    visited_Nodes = [];

    # parent_ptrs has key k and value[v,a] -- meaning 'v' node goes to 'k' node with action 'a'
    # Since the path to return consist of actions; we save it in parent_ptrs.   
    parent_ptrs = {};
    Q = util.Queue();
    
    currentState = problem.getStartState();
    Q.push(currentState);
    visited_Nodes.append(currentState);
    parent_ptrs[currentState] = [];

    #Iterate till we don't hit the goal state 
    while (not problem.isGoalState(currentState)):
        if Q.isEmpty():
            break;
        #Update currentState
        currentState = Q.pop();
        if problem.isGoalState(currentState): break;
        neighbours = problem.getSuccessors(currentState);
        #Neighbours have triplet format. Please print it to observe it better.
        for nbr,act,cost in neighbours:
            if nbr not in visited_Nodes:
                Q.push(nbr);
                parent_ptrs[nbr] = [currentState,act];
                visited_Nodes.append(nbr);

        
        
    #In our scenario goal always exist in given graph. -- therefore truthness of while condition is inevitable
    parent = parent_ptrs[currentState];
    while(parent):
        actions.append(parent[1]);
        parent = parent_ptrs[parent[0]];

    actions.reverse();
    return actions;
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    actions = [];

    #To alleviate redundant exploration
    visited_Nodes = [];

    # parent_ptrs has key k and value[v,a] -- meaning 'v' node goes to 'k' node with action 'a'
    # Since the path to return consist of actions; we save it in parent_ptrs.   
    parent_ptrs = {};
    pq = util.PriorityQueue();
    
    currentState = problem.getStartState();
    pq.push(currentState,0);
    #visited_Nodes.append(currentState);
    #print('visited_Nodes: ',visited_Nodes);
    parent_ptrs[currentState] = [];

    #Iterate till we don't hit the goal state 
    while (True):
        if pq.isEmpty():
            break;
        #access(not pop) minimum element
        curr_cost,curr_count,currentState = pq.heap[0];
        neighbours = problem.getSuccessors(currentState);
        pq.pop();
        visited_Nodes.append(currentState);

        #Is Goal reached
        if problem.isGoalState(currentState):
            break;

        print(neighbours[0]);
        #Neighbours have triplet format. Please print it to observe it better.
        for nbr,act,cost in neighbours:
            if nbr not in visited_Nodes:
                new_cost = curr_cost + cost;
                pq.update(nbr,new_cost);
                if nbr in parent_ptrs:
                    if parent_ptrs[nbr][2] > new_cost:
                        parent_ptrs[nbr] = [currentState,act,new_cost]; 
                else:
                    parent_ptrs[nbr] = [currentState,act,new_cost];

        #Update currentState
        #currentState = pq.pop();
        #visited_Nodes.append(currentState);    
    #In our scenario goal always exist in given graph. -- therefore truthness of while condition is inevitable
    parent = parent_ptrs[currentState];
    while(parent):
        actions.append(parent[1]);
        parent = parent_ptrs[parent[0]];

    actions.reverse();
    return actions;

    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    actions = [];

    #To alleviate redundant exploration
    visited_Nodes = [];

    # parent_ptrs has key k and value[v,a] -- meaning 'v' node goes to 'k' node with action 'a'
    # Since the path to return consist of actions; we save it in parent_ptrs.   
    parent_ptrs = {};
    #Track cost values; We denote g: cost values and h: heuristic values.
    # for eg: cost_values[a] --  denotes the cost from startnode to node a.
    cost_values = {}; 

    pq = util.PriorityQueue();
    
    currentState = problem.getStartState();
    pq.push(currentState,0);
    cost_values[currentState]=0;
    #visited_Nodes.append(currentState);
    #print('visited_Nodes: ',visited_Nodes);
    parent_ptrs[currentState] = [];

    #Iterate till we don't hit the goal state 
    while (True):
        if pq.isEmpty():
            break;
        #access(not pop) minimum element
        curr_cost,curr_count,currentState = pq.heap[0];
        neighbours = problem.getSuccessors(currentState);
        pq.pop();
        visited_Nodes.append(currentState);

        #Is Goal reached
        if problem.isGoalState(currentState):
            break;

        print(neighbours[0]);
        #Neighbours have triplet format. Please print it to observe it better.
        for nbr,act,cost in neighbours:
            if nbr not in visited_Nodes:
                new_cost = cost_values[currentState] + cost;
                cost_values[nbr] = new_cost;
                # This is cost = g + h ; cost becomes the priority
                appx_cost = new_cost + heuristic(nbr,problem);
                pq.update(nbr,appx_cost);
                if nbr in parent_ptrs:
                    if parent_ptrs[nbr][2] > new_cost:
                        parent_ptrs[nbr] = [currentState,act,new_cost]; 
                else:
                    parent_ptrs[nbr] = [currentState,act,new_cost];

        #Update currentState
        #currentState = pq.pop();
        #visited_Nodes.append(currentState);    
    #In our scenario goal always exist in given graph. -- therefore truthness of while condition is inevitable
    parent = parent_ptrs[currentState];
    while(parent):
        actions.append(parent[1]);
        parent = parent_ptrs[parent[0]];

    actions.reverse();
    return actions;
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
