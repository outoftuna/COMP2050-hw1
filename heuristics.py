# heuristics.py
# ----------------
# COMP2050 Artificial Intelligence

""" This class contains heuristics which are used for the search procedures that
    you write in search_strategies.py.

    The first part of the file contains heuristics to be used with the algorithms
    that you will write in search_strategies.py.

    In the second part you will write a heuristic for Q4 to be used with a
    MultiplePositionSearchProblem.
"""

from typing import Tuple

from search_problems import (MultiplePositionSearchProblem,
                             PositionSearchProblem)

Position = Tuple[int, int]
YellowBirds = Tuple[Position]
State = Tuple[Position, YellowBirds]

# -------------------------------------------------------------------------------
# A set of heuristics which are used with a PositionSearchProblem
# You do not need to modify any of these.
# -------------------------------------------------------------------------------


def null_heuristic(pos: Position, problem: PositionSearchProblem) -> int:
    """The null heuristic. It is fast but uninformative. It always returns 0"""

    return 0


def manhattan_heuristic(pos: Position, problem: PositionSearchProblem) -> int:
    """The Manhattan distance heuristic for a PositionSearchProblem."""

    return abs(pos[0] - problem.goal_pos[0]) + abs(pos[1] - problem.goal_pos[1])


def euclidean_heuristic(pos: Position, problem: PositionSearchProblem) -> float:
    """The Euclidean distance heuristic for a PositionSearchProblem"""

    return ((pos[0] - problem.goal_pos[0]) ** 2 + (pos[1] - problem.goal_pos[1]) ** 2) ** 0.5


# Abbreviations
null = null_heuristic
manhattan = manhattan_heuristic
euclidean = euclidean_heuristic

# -------------------------------------------------------------------------------
# You have to implement the following heuristics for Q4 of the homework.
# It is used with a MultiplePositionSearchProblem
# -------------------------------------------------------------------------------

# You can make helper functions here, if you need them


def bird_counting_heuristic(state: State,
                            problem: MultiplePositionSearchProblem) -> float:
    position, yellow_birds = state
    heuristic_value = 0

    heuristic_value = len(yellow_birds)

    return heuristic_value


bch = bird_counting_heuristic


def every_bird_heuristic(state: State,
                         problem: MultiplePositionSearchProblem) -> float:
    position, yellow_birds = state
    heuristic_value = 0

    # this heuristic is the distance to the nearest bird

    yellow_birds = list(yellow_birds)
    current_bird = position
    distance = problem.distance
    
    while len(yellow_birds) > 0:
        distance_dict = dict()
        next_bird = None
        for each_bird in yellow_birds:
            distance_dict[each_bird] = distance[current_bird, each_bird]
        
        for item in distance_dict:
            if distance_dict[item] == min(distance_dict.values()):
                next_bird = item
        heuristic_value += min(distance_dict.values()) 
        current_bird = next_bird
        yellow_birds.remove(current_bird)

    return heuristic_value


every_bird = every_bird_heuristic
