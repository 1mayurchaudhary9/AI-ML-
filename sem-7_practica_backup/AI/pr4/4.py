# 8-Puzzle using Hill Climbing
# Heuristic: Number of Misplaced Tiles

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def heuristic(state):
    """Return number of misplaced tiles."""
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            count += 1

    return count


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


def hill_climbing(initial):
    current = initial
    path = [current]

    while current != GOAL:

        current_h = heuristic(current)

        neighbors = get_neighbors(current)

        # Select the neighbor with minimum heuristic value
        best = min(neighbors, key=heuristic)
        best_h = heuristic(best)

        print("\nCurrent State:")
        display(current)
        print("h(n) =", current_h)

        print("\nBest Next State:")
        display(best)
        print("h(n) =", best_h)

        # Stop if no improvement is possible
        if best_h >= current_h:
            print("\nHill Climbing stopped: No better state found.")
            return path

        current = best

        if current in path:
            print("\nRepeated state encountered.")
            return path

        path.append(current)

    return path


# Initial state
initial_state = (1, 2, 3,
                 4, 0, 6,
                 7, 5, 8)

print("===== 8-PUZZLE USING HILL CLIMBING =====")
print("\nInitial State:")
display(initial_state)
print("Initial h(n) =", heuristic(initial_state))

solution = hill_climbing(initial_state)

print("\n===== FINAL RESULT =====")

if solution[-1] == GOAL:
    print("Goal state reached!")
    print("Number of moves:", len(solution) - 1)

    print("\nSolution Path:")
    for i, state in enumerate(solution):
        print("\nStep", i)
        display(state)
else:
    print("Goal state could not be reached using Hill Climbing.")