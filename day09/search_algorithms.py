import time
from queue import Queue
from stack import Stack

def state_to_string(state):
    #print(get_successors(state))
    #print(goal_test(state))
    row_strings = [" ".join([str(cell) for cell in row]) for row in state]
    return "\n".join(row_strings)


def swap_cells(state, i1, j1, i2, j2):
    """
    Returns a new state with the cells (i1,j1) and (i2,j2) swapped.
    """
    value1 = state[i1][j1]
    value2 = state[i2][j2]

    new_state = []
    for row in range(len(state)):
        new_row = []
        for column in range(len(state[row])):
            if row == i1 and column == j1:
                new_row.append(value2)
            elif row == i2 and column == j2:
                new_row.append(value1)
            else:
                new_row.append(state[row][column])
        new_state.append(tuple(new_row))
    return tuple(new_state)


def get_successors(state):
    """
    This function returns a list of possible successor states resulting
    from applicable actions.
    The result should be a list containing (Action, state) tuples.
    For example [("Up", ((1, 4, 2),(0, 5, 8),(3, 6, 7))),
                 ("Left",((4, 0, 2),(1, 5, 8),(3, 6, 7)))]
    """

    child_states = []

    # YOUR CODE HERE . Hint: Find the "hole" first, then generate each possible
    # successor state by calling the swap_cells method.
    # Exclude actions that are not applicable.

    #find empty space
    empty_space_xcor,empty_space_ycor = find_empty_space(state)

    #print(empty_space_xcor,empty_space_ycor)

    if empty_space_xcor - 1 != -1:
        new_state = swap_cells(state,empty_space_xcor,empty_space_ycor,empty_space_xcor-1,empty_space_ycor)
        child_states.append(('Up',new_state))
    if empty_space_xcor + 1 != len(state):
        new_state = swap_cells(state,empty_space_xcor,empty_space_ycor,empty_space_xcor+1,empty_space_ycor)
        child_states.append(('Down',new_state))
    if empty_space_ycor - 1 != -1:
        new_state = swap_cells(state,empty_space_xcor,empty_space_ycor,empty_space_xcor,empty_space_ycor-1)
        child_states.append(('Left',new_state))
    if empty_space_ycor + 1 != len(state):
        new_state = swap_cells(state,empty_space_xcor,empty_space_ycor,empty_space_xcor,empty_space_ycor+1)
        child_states.append(('Right',new_state))

    return child_states

def find_empty_space(state):
    empty_space_xcor = 0
    empty_space_ycor = 0
    #find xcor and ycor of empty space
    for nested_tuple in state:
        if 0 in nested_tuple:
            for element in nested_tuple:
                if element == 0:
                    break
                empty_space_ycor += 1
            break
        empty_space_xcor += 1
    return empty_space_xcor,empty_space_ycor


def goal_test(state):
    """
    Returns True if the state is a goal state, False otherwise.
    """
    return state == ((0,1,2),(3,4,5),(6,7,8)) or state == ((1,2,3),(4,5,6),(7,8,0))
    #YOUR CODE HERE

def bfs(state):
    """
    Breadth first search.
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.
    """
    parents = {}
    actions = []

    states_expanded = 0
    max_frontier = 0

    #YOUR CODE HERE

    #Hint: You may start with this:
    frontier = Queue()
    frontier.enque(('Start',state))
    seen = set()
    seen.add(state)

    dequed_state = ('Start',state)
    while not goal_test(dequed_state[1]) and not frontier.length() == 0:
        dequed_state = frontier.deque()
        states_expanded += 1
        #print(dequed_state)
        child_states = get_successors(dequed_state[1])
        for child_state in child_states:
            if not child_state[1] in seen:
                seen.add(child_state[1])
                parents[child_state] = dequed_state
                frontier.enque(child_state)
        if frontier.length() > max_frontier:
            max_frontier = frontier.length()

    #if no such solution exists
    if not goal_test(dequed_state) and frontier.length() == 0:
        return None, states_expanded, max_frontier # No solution found

    current_node = dequed_state
    while current_node[0] != 'Start':
        actions.append(current_node[0])
        current_node = parents[current_node]
    actions.reverse()

    #  return solution, states_expanded, max_frontier
    return actions, states_expanded, max_frontier

def dfs(state):
    """
    Breadth first search.
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.
    """
    parents = {}
    actions = []

    states_expanded = 0
    max_frontier = 0
    #YOUR CODE HERE

    #Hint: You may start with this:
    frontier = Stack()
    frontier.push(('Start',state))
    seen = set()
    seen.add(state)

    popped_state = ('Start',state)
    while not goal_test(popped_state[1]) and not frontier.length() == 0:
        popped_state = frontier.pop()
        states_expanded += 1
        #print(popped_state)
        child_states = get_successors(popped_state[1])
        for child_state in child_states:
            if not child_state[1] in seen:
                seen.add(child_state[1])
                parents[child_state] = popped_state
                frontier.push(child_state)
        if frontier.length() > max_frontier:
            max_frontier = frontier.length()

    #if no such solution exists
    if not goal_test(popped_state) and frontier.length() == 0:
        return None, states_expanded, max_frontier # No solution found

    current_node = popped_state
    while current_node[0] != 'Start':
        actions.append(current_node[0])
        current_node = parents[current_node]
    actions.reverse()

    #  return solution, states_expanded, max_frontier

    return actions, states_expanded, max_frontier # No solution found

#Assumes that the puzzle has been solved at the end
def solve_puzzle(state,moves):
    result = 'Starting state: \n' + state_to_string(state) + '\n'
    empty_space_xcor,empty_space_ycor = find_empty_space(state)
    state = state[:]
    for move in moves:
        if move == 'Up':
            state = swap_cells(state,empty_space_xcor,empty_space_ycor,empty_space_xcor-1,empty_space_ycor)
            empty_space_xcor -= 1
        elif move == 'Down':
            state = swap_cells(state,empty_space_xcor,empty_space_ycor,empty_space_xcor+1,empty_space_ycor)
            empty_space_xcor += 1
        elif move == 'Left':
            state = swap_cells(state,empty_space_xcor,empty_space_ycor,empty_space_xcor,empty_space_ycor-1)
            empty_space_ycor -= 1
        elif move == 'Right':
            state = swap_cells(state,empty_space_xcor,empty_space_ycor,empty_space_xcor,empty_space_ycor+1)
            empty_space_ycor += 1
    result += 'Ending state: \n' + state_to_string(state)
    return result

def find_number(state,number):
    xcor = 0
    ycor = 0
    #find xcor and ycor of empty space
    for nested_tuple in state:
        if number in nested_tuple:
            for element in nested_tuple:
                if element == number:
                    break
                ycor += 1
            break
        xcor += 1
    return xcor,ycor

def misplaced_heuristic(state):
    """
    Returns the number of misplaced tiles.
    """
    misplaced_tiles = 0
    solution = (
    (1,2,3),
    (4,5,6),
    (7,8,0)
    )
    for xcor in range(3):
        for ycor in range(3):
            if state[xcor][ycor] != solution[xcor][ycor] and state[xcor][ycor] != 0:
                misplaced_tiles += 1
    return misplaced_tiles

def manhattan_heuristic(state):
    """
    For each misplaced tile, compute the manhattan distance between the current
    position and the goal position. Then sum all distances.
    """
    manhattan_distance = 0
    solution = (
    (1,2,3),
    (4,5,6),
    (7,8,0)
    )
    actual_xcor = 0
    actual_ycor = 0
    for xcor in range(3):
        for ycor in range(3):
            if state[xcor][ycor] != solution[xcor][ycor]:
                actual_xcor,actual_ycor = find_number(state,solution[xcor][ycor])
                manhattan_distance += abs(xcor-actual_xcor) + abs(ycor-actual_ycor)
    return manhattan_distance # replace this


def best_first(state, heuristic = misplaced_heuristic): #also greedy search
    """
    Breadth first search using the heuristic function passed as a parameter.
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.
    """

    # You might want to use these functions to maintain a priority queue
    from heapq import heappush
    from heapq import heappop

    parents = {}
    actions = []

    states_expanded = 0
    max_frontier = 0

    #YOUR CODE HERE
    frontier = [('Start',state)]
    seen = set()
    seen.add(state)

    popped_state = ('Start',state)
    while not goal_test(popped_state[1]) and not len(frontier) == 0:
        popped_state = frontier.pop(-1)
        states_expanded += 1
        child_states = get_successors(popped_state[1])

        # The following line computes the heuristic for a state
        # by calling the heuristic function passed as a parameter.
        # f = heuristic(state)

        #Sort according to the heuristic: create a dictionary with the heuristics, and then sort the child_states
        children_heuristic = {}
        for item in child_states:
            possible_key = heuristic(item[1])
            if possible_key in children_heuristic.keys():
                children_heuristic[possible_key].append(item)
            else:
                children_heuristic[possible_key] = [item]

        child_states_heuristic = []
        for heuristic_value in children_heuristic.keys():
            heappush(child_states_heuristic,heuristic_value)

        while len(child_states_heuristic) != 0:
            heuristic_value = heappop(child_states_heuristic)
            for child_state in children_heuristic[heuristic_value]:
                if not child_state[1] in seen:
                    seen.add(child_state[1])
                    parents[child_state] = popped_state
                    frontier.append(child_state)

        # track max size of the priority queue
        if len(frontier) > max_frontier:
            max_frontier = len(frontier)

    #if no such solution exists
    #print(popped_state)
    if not goal_test(popped_state) and len(frontier) == 0:
        return None, states_expanded, max_frontier # No solution found

    current_node = popped_state
    while current_node[0] != 'Start':
        actions.append(current_node[0])
        current_node = parents[current_node]
    actions.reverse()

    return actions, states_expanded, max_frontier


def astar(state, heuristic = misplaced_heuristic):
    """
    A-star search using the heuristic function passed as a parameter.
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.
    """
    # You might want to use these functions to maintain a priority queue

    from heapq import heappush
    from heapq import heappop

    costs = {}
    costs[state] = 0 #cost of path

    parents = {}

    states_expanded = 0
    max_frontier = 0

    #YOUR CODE HERE
    frontier = [(heuristic(state),state,'Start')]
    seen = set()
    explored = set()
    seen.add((heuristic(state),state,'Start'))
    popped_state = (heuristic(state),state,'Start')

    while len(frontier) != 0:
        popped_state = heappop(frontier)
        #print(goal_test(popped_state))
        explored.add(popped_state[1])
        states_expanded += 1

        # if the popped state was the goal, generate actions and return
        if goal_test(popped_state[1]):
            #print('Done!')
            break

        child_states = get_successors(popped_state[1]) #returns a tuple of (direction,state)
        cost = costs[popped_state[1]] + 1

        for (direction, child_state) in child_states:
            if not child_state in explored:
                if not child_state in seen:
                    new_child_state = (cost + heuristic(child_state), child_state, direction) #tuple of (actual_cost,state,direction)
                    #print(new_child_state)
                    heappush(frontier, new_child_state)
                    parents[new_child_state[1:]] = popped_state[1:]
                    costs[child_state] = cost
                    seen.add(child_state)

        # track max size of the priority queue
        if len(frontier) > max_frontier:
            max_frontier = len(frontier)
            #print(max_frontier)

    current_node = popped_state[1:]
    actions = []
    if len(frontier) != 0:
        while current_node[1] != 'Start':
            #print(current_node[2])
            #break
            actions.append(current_node[1])
            current_node = parents[current_node]
            actions.reverse()

    return actions, states_expanded, max_frontier

def print_result(solution, states_expanded, max_frontier):
    """
    Helper function to format test output.
    """
    if solution is None:
        print("No solution found.")
    else:
        print("Solution has {} actions.".format(len(solution)))
    print("Total states expanded: {}.".format(states_expanded))
    print("Max frontier size: {}.".format(max_frontier))



if __name__ == "__main__":

    #Easy test case
    test_state = ((1, 4, 2),
                  (0, 5, 8),
                  (3, 6, 7))


    '''
    #More difficult test case
    test_state = ((7, 2, 4),
                  (5, 0, 6),
                  (8, 3, 1))

    print(state_to_string(test_state))
    print()
    '''

    print("====BFS====")
    solution, states_expanded, max_frontier = bfs(test_state) #
    print(type(bfs(test_state)))
    start = time.time()
    print_result(solution, states_expanded, max_frontier)
    end = time.time()
    if solution is not None:
        print(solution)
        print(solve_puzzle(test_state,solution))
    print("Total time: {0:.3f}s".format(end-start))
    '''
    print()
    print("====DFS====")
    start = time.time()
    solution, states_expanded, max_frontier = dfs(test_state)
    end = time.time()
    print_result(solution, states_expanded, max_frontier)
    if solution is not None:
        #print(solution)
        print(solve_puzzle(test_state,solution))
        print_result(solution, states_expanded, max_frontier)
    print("Total time: {0:.3f}s".format(end-start))

    print()
    print("====Heuristics====")
    print('Misplaced Heuristic:', misplaced_heuristic(test_state))
    print('Manhattan Heuristic:', manhattan_heuristic(test_state))

    print()
    print("====Greedy Best-First (Misplaced Tiles Heuristic)====")
    start = time.time()
    solution, states_expanded, max_frontier = best_first(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution, states_expanded, max_frontier)
    print("Total time: {0:.3f}s".format(end-start))
    '''
    print()
    print("====A* (Misplaced Tiles Heuristic)====")
    start = time.time()
    solution, states_expanded, max_frontier = astar(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution, states_expanded, max_frontier)
    print("Total time: {0:.3f}s".format(end-start))
