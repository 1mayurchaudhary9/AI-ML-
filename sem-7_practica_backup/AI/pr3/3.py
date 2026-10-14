# Depth First Search (DFS) for Water Jug Problem

def dfs_water_jug(capacity1, capacity2, target):
    initial_state = (0, 0)

    stack = [(initial_state, [initial_state])]
    visited = {initial_state}

    while stack:
        (jug1, jug2), path = stack.pop()

        # Check goal state
        if jug1 == target or jug2 == target:
            return path

        next_states = []

        # Fill Jug 1
        next_states.append((capacity1, jug2))

        # Fill Jug 2
        next_states.append((jug1, capacity2))

        # Empty Jug 1
        next_states.append((0, jug2))

        # Empty Jug 2
        next_states.append((jug1, 0))

        # Pour Jug 1 into Jug 2
        transfer = min(jug1, capacity2 - jug2)
        next_states.append((jug1 - transfer, jug2 + transfer))

        # Pour Jug 2 into Jug 1
        transfer = min(jug2, capacity1 - jug1)
        next_states.append((jug1 + transfer, jug2 - transfer))

        # Push unexplored states onto stack
        for state in next_states:
            if state not in visited:
                visited.add(state)
                stack.append((state, path + [state]))

    return None


# Capacities of the jugs
jug1_capacity = 4
jug2_capacity = 3

# Required amount
target = 2

solution = dfs_water_jug(jug1_capacity, jug2_capacity, target)

if solution:
    print("Solution found using DFS:")
    for i, state in enumerate(solution):
        print("Step", i, ":", state)
else:
    print("No solution exists.")