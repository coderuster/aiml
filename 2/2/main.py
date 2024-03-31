import heapq

class Node:
    def __init__(self, state, parent, cost, heuristic):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic


def a_star_search(start, goal, graph,max_nodes):
    heap = []
    heapq.heappush(heap, (0, Node(start, None, 0, 0)))
    visited = set()
    node_counter = 0

    while heap and node_counter<max_nodes:
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

graph = {'A': {'B': 1, 'C': 4},
'B': {'A': 1, 'C': 2, 'D': 5},
'C': {'A': 4, 'B': 2, 'D': 1},
'D': {'B': 5, 'C': 1}}
start = 'A'
goal = 'D'
max_nodes = 10
result = a_star_search(start, goal, graph, max_nodes)
print(result)
