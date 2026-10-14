# 8-Puzzle using A* Algorithm
# Heuristic: Manhattan Distance

import heapq

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def manhattan_distance(state):
    distance = 0

    for index, tile in enumerate(state):
        if tile == 0:
            continue

        current_row = index // 3
        current_col = index % 3

        goal_index = GOAL.index(tile)
        goal_row = goal_index // 3
        goal_col = goal_index % 3

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


def display(state):
    print("-------------")
    for i in range(0, 9, 3):
        print("|", state[i], "|", state[i + 1], "|", state[i + 2], "|")
        print("-------------")


def get_neighbors(state):
    neighbors = []

    blank = state.index(0)
    row = blank // 3
    col = blank % 3

    moves = []

    if row > 0:
        moves.append(blank - 3)     # Up

    if row < 2:
        moves.append(blank + 3)     # Down

    if col > 0:
        moves.append(blank - 1)     # Left

    if col < 2:
        moves.append(blank + 1)     # Right

    for new_blank in moves:
        new_state = list(state)

        new_state[blank], new_state[new_blank] = \
            new_state[new_blank], new_state[blank]

        neighbors.append(tuple(new_state))

    return neighbors


def a_star(initial):
    # Priority queue contains:
    # (f(n), g(n), state, path)
    h = manhattan_distance(initial)

    priority_queue = [(h, 0, initial, [initial])]

    visited_cost = {initial: 0}

    while priority_queue:

        f, g, current, path = heapq.heappop(priority_queue)

        # Goal test
        if current == GOAL:
            return path

        # Generate successor states
        for neighbor in get_neighbors(current):

            new_g = g + 1

            # Add only if this is a better path
            if neighbor not in visited_cost or \
               new_g < visited_cost[neighbor]:

                visited_cost[neighbor] = new_g

                h = manhattan_distance(neighbor)
                new_f = new_g + h

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None


# Initial state
initial_state = (1, 2, 3,
                 4, 0, 6,
                 7, 5, 8)

print("===== 8-PUZZLE USING A* ALGORITHM =====")

print("\nInitial State:")
display(initial_state)

print("g(n) = 0")
print("h(n) =", manhattan_distance(initial_state))
print("f(n) =", manhattan_distance(initial_state))

solution = a_star(initial_state)

if solution:
    print("\n===== SOLUTION FOUND =====")
    print("Number of moves:", len(solution) - 1)

    print("\nSolution Path:")

    for i, state in enumerate(solution):
        print("\nStep", i)
        display(state)
else:
    print("No solution exists.")