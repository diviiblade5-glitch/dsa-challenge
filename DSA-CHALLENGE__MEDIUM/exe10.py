def path_exists(graph, start, target):
    stack = [start]
    visited = []

    while stack:
        node = stack.pop()

        if node == target:
            return True

        if node not in visited:
            visited.append(node)
            stack.extend(graph.get(node, []))

    return False
print(path_exists(graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': ['F'],
    'F': []
}, start = 'A', target = 'F'))