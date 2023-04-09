"""
    Enter your details below:

    Name:       Ta Viet Thang
    Student ID: V202100444 
    Email:      21thang.tv@vinuni.edu.vn
"""

from typing import List

from game_engine.util import raise_not_defined
from search_problems import SearchProblem
import math

def solve(problem: SearchProblem) -> List[str]:
    """See 2_implementation_notes.md for more details.

    Your search algorithms needs to return a list of actions that reaches the
    goal from the start state in the given problem. The elements of this list
    need to be one or more references to the attributes NORTH, SOUTH, EAST and
    WEST of the class Directions.
    """

    # *** YOUR CODE HERE ***
    def depth_limited_search(problem: SearchProblem, depth):
        """return steps"""
        # 
        visited_nodes = set()
        initial_state = problem.get_initial_state()
        path = []

        def recursive_depth_limited_search(state, action, depth):
            visited_nodes.add(state)
            # if state is goal state
            if problem.goal_test(state):
                path.append([state, action])
                return path

            elif depth == 0:    
                visited_nodes.remove(state)
                return None
            
            path.append([state, action])
            for neighbor, action, cost in problem.get_successors(state):
                if neighbor not in visited_nodes:
                    result = recursive_depth_limited_search(neighbor, action, depth-1)
                    if result is not None:
                        return result

            path.pop()
            visited_nodes.remove(state)
        
        result = recursive_depth_limited_search(initial_state, None, depth)
        if result is not None: 
            return path 
    
    # set max_depth according to your need
    max_depth = 100
    for depth in range(max_depth):
        solution = depth_limited_search(problem, depth)
        # print when no solution is found 
        print(f"Lower-bound: {depth}")
        if solution is not None:
            optimal_actions = [state[1] for state in solution]
            optimal_actions.remove(None)
            return optimal_actions
        