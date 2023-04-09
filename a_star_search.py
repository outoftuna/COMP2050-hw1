"""
    Enter your details below:

    Name:       Ta Viet Thang
    Student ID: V202100444
    Email:      21thang.tv@vinuni.edu.vn
"""

from typing import Callable, List

from game_engine.util import raise_not_defined
from search_problems import SearchProblem
from frontiers import PriorityQueue

def solve(problem: SearchProblem, heuristic: Callable) -> List[str]:
    """See 2_implementation_notes.md for more details.

    Your search algorithms needs to return a list of actions that reaches the
    goal from the start state in the given problem. The elements of this list
    need to be one or more references to the attributes NORTH, SOUTH, EAST and
    WEST of the class Directions.
    """
    # *** YOUR CODE HERE ***
    # use Priority Queue for A* implementation
    frontier = PriorityQueue()
    visited_nodes = set()
    optimal_solution = []
    # cost to reach a state 
    g_value = dict() 
    # f(x) = g(x) + h(x)
    f_value = dict()
    state_info = dict()
    initial_state = problem.get_initial_state()
    last_state = None
    g_value[initial_state] = 0
    f_value[initial_state] = g_value[initial_state] + heuristic(initial_state, problem)
    frontier.push(initial_state, f_value[initial_state])
    

    # A* implementation
    while not frontier.is_empty():
        state = frontier.pop()
        visited_nodes.add(state)        
        if problem.goal_test(state):
            last_state = state
            break
        for neighbor, action, cost in problem.get_successors(state):
            if neighbor not in visited_nodes:
                g_value[neighbor] = g_value[state] + cost
                if neighbor not in f_value.keys():
                    f_value[neighbor] = g_value[neighbor] + heuristic(neighbor, problem)
                    state_info[neighbor] = [state, action]
                    frontier.push(neighbor, f_value[neighbor])
                elif g_value[neighbor] + heuristic(neighbor, problem) < f_value[neighbor]:
                    f_value[neighbor] = g_value[neighbor] + heuristic(neighbor, problem)
                    frontier.change_priority(neighbor, f_value[neighbor])
                    state_info[neighbor] = [state, action]
    # track the path
    while last_state != initial_state:
        optimal_solution.append(state_info[last_state][1])
        last_state = state_info[last_state][0]
    optimal_solution.reverse()
    return optimal_solution

    
    



    