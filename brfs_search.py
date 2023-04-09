"""
    Enter your details below:

    Name:       Ta Viet Thang
    Student ID: V202100444
    Email:      21thang.tv@vinuni.edu.vn
"""

from typing import List

from game_engine.util import raise_not_defined
from search_problems import SearchProblem
from frontiers import Queue

def solve(problem: SearchProblem) -> List[str]:
    """See 2_implementation_notes.md for more details.

    Your search algorithms needs to return a list of actions that reaches the
    goal from the start state in the given problem. The elements of this list
    need to be one or more references to the attributes NORTH, SOUTH, EAST and
    WEST of the class Directions.
    """
    # *** YOUR CODE HERE ***
    # BFS implementation requires Queue data structure
    frontier = Queue()
    visited_nodes = set() # avoid generating a path to the same state more than once
    initial_state = problem.get_initial_state()
    state_info = dict() # a dictionary of states and their corresponding previous state and action: state: [previous_state, action]
    optimal_actions = [] # what we must return
    state_info[initial_state] = [None, None]

    # Perform BFS
    frontier.push(initial_state)
    while not frontier.is_empty():
        state = frontier.pop()

        # if state is goal state:
        if problem.goal_test(state):
            # sequentially check what action led to that state
            previous_state = state_info[state]
            while not(None in previous_state):
                optimal_actions.append(previous_state[1])
                previous_state = state_info[previous_state[0]]

            optimal_actions.reverse()
            return optimal_actions
        
        # if state is not goal, visit its neighbors
        if state not in visited_nodes:
            visited_nodes.add(state)
            for neighbor, action, cost in problem.get_successors(state):
                if neighbor in visited_nodes:
                    continue
                if neighbor not in frontier.contents:
                    frontier.push(neighbor)
                    # save the info of the neighbor
                    state_info[neighbor] =  [state, action]
