import heapq


class Node:
    def __init__(self, state, parent, cost, heuristic):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic


def a_star_search(start, goal, graph):
    heap = []
    heapq.heappush(heap, (0, Node(start, None, 0, 0)))
    visited = set()
    node_counter = 0

    while heap :
        cost, current_node = heapq.heappop(heap)
        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        if current_node.state in visited:
            continue

        visited.add(current_node.state)
        node_counter += 1

        for neighbour, weight in graph[current_node.state].items():
            if neighbour not in visited:
                heuristic = 0
                heapq.heappush(
                    heap,
                    (
                        cost + weight,
                        Node(neighbour, current_node, cost + weight, heuristic),
                    ),
                )

    return None

graph = {
'A': {'B': 1, 'D': 3},
'B': {'A': 1, 'C': 2, 'D': 4},
'C': {'B': 2, 'D': 5, 'E': 2},
'D': {'A': 3, 'B': 4, 'C': 5, 'E': 3},
'E': {'C': 2, 'D': 3}
}
start = 'A'
goal = 'E'
result = a_star_search(start, goal, graph)
print(result)
