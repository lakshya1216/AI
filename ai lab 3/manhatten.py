import heapq

def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val == 0:
                continue
            for x in range(3):
                for y in range(3):
                    if goal[x][y] == val:
                        distance += abs(i - x) + abs(j - y)
    return distance

def get_blank_pos(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_neighbors(state):
    neighbors = []
    x, y = get_blank_pos(state)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def a_star_manhattan(start, goal):
    heap = []
    visited = set()
    heapq.heappush(heap, (0, 0, start, []))

    while heap:
        f, g, current, path = heapq.heappop(heap)
        key = str(current)
        if key in visited:
            continue
        visited.add(key)
        if current == goal:
            return path + [current]
        for neighbor in generate_neighbors(current):
            h = manhattan_distance(neighbor, goal)
            heapq.heappush(heap, (g + 1 + h, g + 1, neighbor, path + [current]))
    return None

def print_solution(path):
    for step, state in enumerate(path):
        print(f"Step {step}:")
        for row in state:
            print(" ", row)
        print()

# --- Main ---
start = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

goal = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

print("Solution using Manhattan Distance Heuristic:")
solution = a_star_manhattan(start, goal)
print_solution(solution)
